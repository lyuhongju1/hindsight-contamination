#!/usr/bin/env python3
"""Frozen, rerunnable search for baseline-upgrade pairs (pair_selection_rules.md, sections 2-4, 9).

Run by the research assistant, NOT by the PI and NOT by any study model. The script only collects
and logs; the inclusion criteria I1-I6 that need judgement are applied by people, by hand, in the
CSV columns this script leaves empty.

Subcommands
  baselines   Query INSPIRE for candidate baseline instrument papers (sampling frame, section 2.1).
  upgrades    For each baseline in a CSV, find citing upgrade documents (LoI/CDR/TDR/TP; section 2.2).
  draw        Random draw within field, after inclusion has been decided by hand (section 4).

Every query is logged with its exact string, the UTC time, the number of hits, and the raw JSON
responses, so the freeze package (section 9) can include them.

Examples
  python -I inspire_search.py baselines --out runs/
  python -I inspire_search.py upgrades --baselines runs/baselines.csv --out runs/
  python -I inspire_search.py draw --included included.csv --frozen ../pair_selection_rules.md \
         --per-field 3 --target-pairs 14 --out runs/

Only the Python standard library is used.
"""
import argparse, csv, hashlib, json, os, random, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone

API = "https://inspirehep.net/api/literature"
FIELDS = ("control_number,titles,earliest_date,collaborations,citation_count,author_count,"
          "arxiv_eprints,publication_info,document_type,inspire_categories,report_numbers")
UA = "hindsight-pair-search/1.0 (research script)"

# ---- Frozen query strings (section 2). Edit ONLY before the freeze; the freeze hashes this file.
BASELINE_QUERIES = {
    "nima":  'j "Nucl.Instrum.Meth.A" and de 1998->2020 and ac 30+ and topcite 100+',
    "jinst": 'j JINST and de 1998->2020 and ac 30+ and topcite 100+',
    "epjc_instr": 'j "Eur.Phys.J.C" and inspire_categories.term:Instrumentation and de 1998->2020 and ac 30+ and topcite 100+',
    "ptep_instr": 'j PTEP and inspire_categories.term:Instrumentation and de 1998->2020 and ac 30+ and topcite 100+',
    "arxiv_insdet": 'arxiv_eprints.categories:physics.ins-det and de 1998->2020 and ac 30+ and topcite 100+',
}
UPGRADE_TERMS = ('(t upgrade or t "technical design report" or t "conceptual design report" or '
                 't "letter of intent" or t "technical proposal" or t "design report" or t "phase-2" '
                 'or t "phase ii" or rn LHCC or rn TDR or rn CDR)')


def log_dir(out):
    d = os.path.join(out, "raw"); os.makedirs(d, exist_ok=True); return d


def fetch(q, out, tag, size=250, max_pages=40):
    """Run one INSPIRE query with pagination; save raw pages; return (hits, total)."""
    hits, page, total = [], 1, None
    while page <= max_pages:
        url = API + "?" + urllib.parse.urlencode({"q": q, "size": size, "page": page, "fields": FIELDS, "sort": "mostrecent"})
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, timeout=60) as r: data = json.load(r); break
            except Exception as e:  # rate limit or transient error
                if attempt == 4: raise
                time.sleep(5 * (attempt + 1))
        with open(os.path.join(log_dir(out), f"{tag}_p{page}.json"), "w", encoding="utf-8") as f: json.dump(data, f)
        total = data["hits"]["total"]; batch = data["hits"]["hits"]; hits += batch
        if len(hits) >= total or not batch: break
        page += 1; time.sleep(0.5)  # INSPIRE asks for <= 15 requests per 5 s
    with open(os.path.join(out, "query_log.tsv"), "a", encoding="utf-8") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()}\t{tag}\t{total}\t{len(hits)}\t{q}\n")
    return hits, total


def row(h):
    m = h["metadata"]
    pub = (m.get("publication_info") or [{}])[0]
    return {
        "recid": m.get("control_number"),
        "title": (m.get("titles") or [{}])[0].get("title", ""),
        "earliest_date": m.get("earliest_date", ""),
        "collaboration": "; ".join(c.get("value", "") for c in m.get("collaborations", [])),
        "citations": m.get("citation_count", ""),
        "authors": m.get("author_count", ""),
        "arxiv": "; ".join(e.get("value", "") for e in m.get("arxiv_eprints", [])),
        "journal": f'{pub.get("journal_title", "")} {pub.get("journal_volume", "")} {pub.get("artid", pub.get("page_start", ""))} ({pub.get("year", "")})'.strip(),
        "report_numbers": "; ".join(r.get("value", "") for r in m.get("report_numbers", [])),
        "doc_type": "; ".join(m.get("document_type", [])),
        "categories": "; ".join(c.get("term", "") for c in m.get("inspire_categories", [])),
    }


def cmd_baselines(a):
    os.makedirs(a.out, exist_ok=True)
    seen = {}
    for tag, q in BASELINE_QUERIES.items():
        hits, total = fetch(q, a.out, f"baselines_{tag}")
        print(f"{tag}: {total} hits", file=sys.stderr)
        for h in hits:
            r = row(h); r["source_query"] = tag
            if r["recid"] in seen: seen[r["recid"]]["source_query"] += f"; {tag}"
            else: seen[r["recid"]] = r
    cols = list(next(iter(seen.values())).keys()) + [
        # filled by hand (section 3): is it an instrument paper describing a built detector? field?
        "I1_instrument_paper(Y/N)", "field", "notes"]
    path = os.path.join(a.out, "baselines.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for r in sorted(seen.values(), key=lambda r: r["earliest_date"]): w.writerow(r)
    print(f"wrote {len(seen)} unique baselines to {path}", file=sys.stderr)


def cmd_upgrades(a):
    os.makedirs(a.out, exist_ok=True)
    with open(a.baselines, encoding="utf-8") as f: base = list(csv.DictReader(f))
    if a.only_included:
        base = [b for b in base if b.get("I1_instrument_paper(Y/N)", "").strip().upper() == "Y"]
    out_rows = []
    for b in base:
        q = f'refersto:recid:{b["recid"]} and {UPGRADE_TERMS}'
        hits, total = fetch(q, a.out, f"upgrades_{b['recid']}")
        for h in hits:
            r = row(h)
            out_rows.append({"baseline_recid": b["recid"], "baseline_title": b["title"], "baseline_date": b["earliest_date"],
                             **{f"doc_{k}": v for k, v in r.items()},
                             # filled by hand (sections 3 and 6)
                             "item": "", "is_adoption_commitment(Y/N)": "", "commitment_date": "", "gap_months": "",
                             "I3_hardware_choice(Y/N)": "", "I4_distractor_with_citation": "", "I6_before_cutoff(Y/N)": "",
                             "dater": "", "confidence": "", "notes": ""})
        time.sleep(0.5)
    path = os.path.join(a.out, "upgrade_documents.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()) if out_rows else ["baseline_recid"]); w.writeheader(); w.writerows(out_rows)
    print(f"wrote {len(out_rows)} candidate upgrade documents for {len(base)} baselines to {path}", file=sys.stderr)


def cmd_draw(a):
    """Random draw within field (section 4). Input CSV: one row per pair that passed I1-I6 by hand,
    with columns pair_id, field, n_primary_units. Seed = SHA-256 of the frozen rules document."""
    seed_hex = hashlib.sha256(open(a.frozen, "rb").read()).hexdigest()
    rng = random.Random(int(seed_hex, 16))
    with open(a.included, encoding="utf-8") as f: pairs = list(csv.DictReader(f))
    by_field = {}
    for p in sorted(pairs, key=lambda p: p["pair_id"]): by_field.setdefault(p["field"], []).append(p)
    for fld in by_field: rng.shuffle(by_field[fld])
    chosen, rounds = [], 0
    # round-robin over fields in sorted order, respecting the per-field cap, until the target is met
    while len(chosen) < a.target_pairs and rounds < a.per_field:
        for fld in sorted(by_field):
            if rounds < len(by_field[fld]) and len(chosen) < a.target_pairs: chosen.append(by_field[fld][rounds])
        rounds += 1
    os.makedirs(a.out, exist_ok=True)
    path = os.path.join(a.out, "drawn_pairs.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(pairs[0].keys()) + ["draw_order"]); w.writeheader()
        for i, p in enumerate(chosen): w.writerow({**p, "draw_order": i + 1})
    units = sum(int(p.get("n_primary_units", 0) or 0) for p in chosen)
    with open(os.path.join(a.out, "draw_log.txt"), "w", encoding="utf-8") as f:
        f.write(f"time {datetime.now(timezone.utc).isoformat()}\nseed sha256({a.frozen}) = {seed_hex}\n"
                f"eligible pairs {len(pairs)}; fields {sorted(by_field)}\nchosen {len(chosen)} pairs, {units} primary units\n"
                f"shortfall vs target pairs: {max(0, a.target_pairs - len(chosen))}\n")
    print(f"drew {len(chosen)} pairs ({units} units); see {path}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    b = sp.add_parser("baselines"); b.add_argument("--out", required=True)
    u = sp.add_parser("upgrades"); u.add_argument("--baselines", required=True); u.add_argument("--out", required=True)
    u.add_argument("--only-included", action="store_true", help="only baselines marked Y in the I1 column")
    d = sp.add_parser("draw"); d.add_argument("--included", required=True); d.add_argument("--frozen", required=True)
    d.add_argument("--per-field", type=int, default=3); d.add_argument("--target-pairs", type=int, default=14)
    d.add_argument("--out", required=True)
    sp.add_parser("selftest", help="check that each frozen query parses and returns hits (prints counts only)")
    a = ap.parse_args()
    if a.cmd == "selftest":
        for tag, q in BASELINE_QUERIES.items():
            url = API + "?" + urllib.parse.urlencode({"q": q, "size": 1, "fields": "control_number"})
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                print(f"{tag}: {json.load(r)['hits']['total']} hits")
            time.sleep(0.5)
        return
    {"baselines": cmd_baselines, "upgrades": cmd_upgrades, "draw": cmd_draw}[a.cmd](a)


if __name__ == "__main__":
    main()
