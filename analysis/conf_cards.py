#!/usr/bin/env python3
"""Confirmatory screen + blind adjudication cards (PREREGISTRATION §5). Written before any confirmatory data was read.

  python -I analysis/conf_cards.py

For each pair:
- every CONF1 response whose TOP RECOMMENDATION line matches the frozen 'adopted' regex (screen hit),
- plus 10 random non-hits per CONF1 x model (seed below),
- and, exploratory, the same for BASE (coded P/N/X per the rubric addendum).
Cards carry a hashed id, the level, the final line and the relevant sentences; the model is hidden.
Writes data/conf_upgrade/adjudication/<pair>/{cards.json, KEY_do_not_open.json} and data/conf_upgrade/screen.json.
"""
import hashlib, json, os, random, re
from collections import defaultdict
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.join(H, "data", "conf_upgrade")
R = json.load(open(os.path.join(H, "materials", "scoring_regex.json"), encoding="utf-8"))
SEED = 20261106
KEYWORDS = {  # constraint vocabulary per pair, fixed before data (selects 'relevant sentences' only)
 "p01_xenon1t": r"methane|\bch4\b|ch3t|tritium|getter|calibrat|distill|column",
 "p02_gerda": r"radon|\brn\b|222|progeny|214\s?bi|214\s?po|210\s?po|surface|shroud|encapsul|emanat",
 "p03_advirgo": r"\b8\s?m\b|metre|meter|loss|ppm|linewidth|bandwidth|filter|epr|entangl|cavity|detun",
 "p05_sno": r"buoyan|density|densit|load|hold[\s-]?down|rope|acrylic|float|kg/m",
 "p09_nemo3": r"\bcells?\b|15\s?cm|segment|granular|separat|pitch|light\s?guide|diagonal",
 "p10_borexino": r"deuter|inverse\s+beta|\bibd\b|threshold|elastic|reconstruct|neutral[\s-]current|charged[\s-]current",
}
def final_line(t):
    m = re.findall(r"TOP\s+RECOMMENDATION\s*:\s*\**\s*(.+)", t or "", re.I)
    return m[-1].strip().strip("*").strip() if m else None
def sentences(t, pair):
    pat = "|".join(x for x in (R[pair]["adopted"], R[pair]["distractor"], KEYWORDS[pair]) if x)
    out = []
    for s in re.split(r"(?<=[.!?])\s+|\n+", t or ""):
        s = s.strip()
        if 15 < len(s) < 600 and re.search(pat, s, re.I) and s not in out: out.append(s)
    return out[:25]

def merged(RUN):
    """Main run, with cells resampled at 32k (data/conf_upgrade_resample) replacing the originals (PREREGISTRATION §7)."""
    plan = {r["cid"]: r for r in json.load(open(os.path.join(RUN, "plan.json")))["requests"]}
    rows = [json.loads(l) for l in open(os.path.join(RUN, "raw.jsonl"), encoding="utf-8")]
    rs = os.path.join(os.path.dirname(RUN), "conf_upgrade_resample")
    if os.path.exists(os.path.join(rs, "raw.jsonl")):
        rplan = {r["cid"]: r for r in json.load(open(os.path.join(rs, "plan.json")))["requests"]}
        cells = {(r["pair"], r["level"], r["model"]) for r in rplan.values()}
        rows = [r for r in rows if (r["pair"], r["level"], plan[r["custom_id"]]["model"]) not in cells]
        rows += [json.loads(l) for l in open(os.path.join(rs, "raw.jsonl"), encoding="utf-8")]; plan.update(rplan)
    return rows, plan
rows, plan = merged(RUN)
screen = defaultdict(lambda: {"n": 0, "no_final": 0, "hits": 0, "truncated": 0})
groups = defaultdict(lambda: {"hit": [], "non": []})
for r in rows:
    m = plan[r["custom_id"]]["model"]; pair, lvl = r["pair"], r["level"]
    k = f"{pair}|{lvl}|{m}"; s = screen[k]; s["n"] += 1; s["truncated"] += r.get("stop_reason") == "max_tokens"
    fl = final_line(r["response"])
    if fl is None: s["no_final"] += 1; continue
    hit = bool(re.search(R[pair]["adopted"], fl, re.I)); s["hits"] += hit
    if lvl in ("CONF1", "BASE"): groups[(pair, lvl, m)]["hit" if hit else "non"].append((r, fl, hit))
json.dump(screen, open(os.path.join(RUN, "screen.json"), "w"), indent=1)
rng = random.Random(SEED); per_pair = defaultdict(lambda: ([], {}))
for (pair, lvl, m), g in sorted(groups.items()):
    non = sorted(g["non"], key=lambda x: x[0]["custom_id"]); pick = g["hit"] + rng.sample(non, min(10, len(non)))
    cards, key = per_pair[pair]
    for r, fl, hit in pick:
        cid = hashlib.sha256(("card|" + r["custom_id"]).encode()).hexdigest()[:10]
        cards.append({"card": cid, "level": lvl, "final_line": fl, "relevant_sentences": sentences(r["response"], pair)})
        key[cid] = {"custom_id": r["custom_id"], "model": m, "template": r["template"], "level": lvl, "regex_final_hit": hit}
for pair, (cards, key) in per_pair.items():
    d = os.path.join(RUN, "adjudication", pair); os.makedirs(d, exist_ok=True)
    random.Random(SEED + 1).shuffle(cards)
    json.dump(cards, open(os.path.join(d, "cards.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(key, open(os.path.join(d, "KEY_do_not_open.json"), "w", encoding="utf-8"), indent=1)
    print(pair, len(cards), "cards")
