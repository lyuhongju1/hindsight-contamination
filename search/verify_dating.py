#!/usr/bin/env python3
"""Mechanical verifier for dating claims (design v3 section 5; pair_selection_rules.md section 6).

A dating claim is a JSON object (for multi-version arXiv papers, cite the FIRST version containing the
quote as arXiv:<id>v<N>; the verifier then dates that version and checks the quote is absent in v<N-1>):
  {"item": "<pair_id>/<item>", "dater": "D1", "doc": "arXiv:1901.03750" | "inspire:1713643",
   "quote": "<verbatim sentence committing the collaboration to the item for this program>",
   "baseline_date": "YYYY-MM-DD"}
The verifier never trusts the agent's date. It:
  1. resolves the document's first public date from metadata (arXiv API published date, or INSPIRE
     earliest_date);
  2. downloads the full text (arXiv PDF, or the first arXiv eprint of the INSPIRE record) and checks the
     quote is present after normalisation (case, whitespace, hyphenation, ligatures). If not present
     exactly, it accepts only if a contiguous run of >= 12 words of the quote is present AND >= 85% of the
     quote's words appear in order within one 400-word window (logged as 'fuzzy').
  3. computes the gap in months to the baseline and the class (Pre < -12, Cont. +-12, Post 12-24,
     Post-primary >= 24 months).

Usage: python -I verify_dating.py claims.json out.json
Downloads are cached under search/verify_cache/ as data only (parsed with pypdf, never executed).
"""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import date
from io import BytesIO

HERE = os.path.dirname(os.path.abspath(__file__)); CACHE = os.path.join(HERE, "verify_cache"); os.makedirs(CACHE, exist_ok=True)
UA = {"User-Agent": "hindsight-dating-verifier/1.0 (research script)"}

def get(url, binary=False):
    key = re.sub(r"[^A-Za-z0-9]+", "_", url)[-150:]; p = os.path.join(CACHE, key)
    if os.path.exists(p): return open(p, "rb").read()
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r: data = r.read(); break
        except urllib.error.HTTPError as e:
            if attempt == 3 or e.code not in (429, 500, 502, 503): raise
            time.sleep(30 * (attempt + 1))
        except Exception:
            if attempt == 3: raise
            time.sleep(5 * (attempt + 1))
    open(p, "wb").write(data); time.sleep(3)  # arXiv asks for >= 3 s between requests
    return data

def arxiv_meta(aid):
    """First public date of an arXiv eprint, via INSPIRE's arXiv lookup (avoids arXiv API rate limits)."""
    d = json.loads(get(f"https://inspirehep.net/api/arxiv/{aid}?fields=earliest_date,preprint_date").decode())
    md = d["metadata"]
    return md.get("preprint_date") or md.get("earliest_date")

def inspire_meta(recid):
    d = json.loads(get(f"https://inspirehep.net/api/literature/{recid}?fields=earliest_date,arxiv_eprints").decode())
    md = d["metadata"]; ax = [e["value"] for e in md.get("arxiv_eprints", [])]
    return md.get("earliest_date"), (ax[0] if ax else None)

def version_date(aid, v):
    """Submission date of version v of an arXiv eprint, from the abs page's submission history."""
    import html
    page = get(f"https://arxiv.org/abs/{aid}v{v}").decode("utf-8", "replace")
    m = re.search(rf"\[v{v}\]</strong>\s*([A-Za-z]{{3}}, \d{{1,2}} [A-Za-z]{{3}} \d{{4}})", page)
    if not m: return None
    from datetime import datetime
    return datetime.strptime(m.group(1), "%a, %d %b %Y").date().isoformat()

def pdf_text(aid):
    from pypdf import PdfReader
    raw = get(f"https://arxiv.org/pdf/{aid}", binary=True)
    if not raw[:5].startswith(b"%PDF"): raise ValueError("arXiv did not return a PDF")
    return " ".join((pg.extract_text() or "") for pg in PdfReader(BytesIO(raw)).pages)

def norm(s):
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("‐", "-").replace("‑", "-")
    s = re.sub(r"-\s*\n\s*", "", s)              # de-hyphenate line breaks
    s = re.sub(r"[^a-z0-9%.]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def quote_found(quote, text):
    q, t = norm(quote), norm(text)
    if q and q in t: return "exact"
    qw, tw = q.split(), t.split()
    if len(qw) < 12: return None
    runs = any(" ".join(qw[i:i + 12]) in t for i in range(len(qw) - 11))
    if not runs: return None
    # in-order coverage inside a 400-word window anchored at the first 12-word run
    for i in range(len(qw) - 11):
        k = t.find(" ".join(qw[i:i + 12]))
        if k >= 0:
            start = max(0, len(t[:k].split()) - 200); win = tw[start:start + 400]; j = hit = 0
            for w in qw:
                while j < len(win) and win[j] != w: j += 1
                if j < len(win): hit += 1; j += 1
            return "fuzzy" if hit / len(qw) >= 0.85 else None
    return None

def _d(x):
    x = x.strip()[:10]
    return date.fromisoformat(x + "-01-01" if len(x) == 4 else x + "-01" if len(x) == 7 else x)

def months(a, b):
    a, b = _d(a), _d(b)
    return (a.year - b.year) * 12 + (a.month - b.month)

def classify(gap):
    return "Pre" if gap < -12 else "Cont" if gap <= 12 else "Post" if gap < 24 else "Post-primary"

def verify(c):
    out = dict(c); doc = c["doc"]
    try:
        vm = re.fullmatch(r"(?i)arxiv:(.+?)v(\d+)", doc)
        if vm:  # explicit version: date = that version's submission date; quote must be in vN and not in v(N-1)
            base_id, v = vm.group(1), int(vm.group(2))
            out["meta_date"] = version_date(base_id, v); aid = f"{base_id}v{v}"
            if v > 1 and quote_found(c["quote"], pdf_text(f"{base_id}v{v-1}")):
                out.update(status="FAIL", reason=f"quote already present in v{v-1}: cite the first version containing it"); return out
        elif doc.lower().startswith("arxiv:"):
            aid = doc.split(":", 1)[1]; out["meta_date"] = arxiv_meta(aid)
        elif doc.lower().startswith("inspire:"):
            out["meta_date"], aid = inspire_meta(doc.split(":", 1)[1])
        else:
            out.update(status="FAIL", reason="doc must be arXiv:<id> or inspire:<recid>"); return out
        if not out.get("meta_date"): out.update(status="FAIL", reason="no metadata date"); return out
        if not aid: out.update(status="FAIL", reason="no arXiv full text to check the quote against"); return out
        out["quote_match"] = quote_found(c["quote"], pdf_text(aid))
        if not out["quote_match"]: out.update(status="FAIL", reason="quote not found in document text"); return out
        out["gap_months"] = months(out["meta_date"], c["baseline_date"]); out["class"] = classify(out["gap_months"])
        out["status"] = "VERIFIED"
    except Exception as e:
        out.update(status="FAIL", reason=f"error: {type(e).__name__}: {str(e)[:120]}")
    return out

if __name__ == "__main__":
    claims = json.load(open(sys.argv[1], encoding="utf-8"))
    res = [verify(c) for c in claims]
    json.dump(res, open(sys.argv[2], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    for r in res: print(f"{r['item']:40s} {r.get('dater',''):3s} {r['status']:9s} {r.get('meta_date','-')} {r.get('class','-'):12s} {r.get('quote_match') or r.get('reason','')}")
