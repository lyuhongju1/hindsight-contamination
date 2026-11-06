#!/usr/bin/env python3
"""Merge two independent screening passes (pair_selection_rules.md section 5, design v3 section 6).

Inputs: screening/A_chunk*.txt and screening/B_chunk*.txt, lines 'recid|Y|field' (Y lines only; absent = N,
since each screener screened its whole chunk; the full verdict texts are in the agent transcripts).
A baseline is INCLUDED only if both screeners say Y. If they agree on Y but differ on field,
the record is included with field = 'disputed:<a>/<b>' and logged.
Writes screening/included_baselines.csv, screening/merge_log.md.
"""
import csv, glob, os, re
from collections import Counter

D = os.path.dirname(os.path.abspath(__file__))

def load(prefix):
    out = {}
    for f in sorted(glob.glob(os.path.join(D, f"{prefix}_chunk*.txt"))):
        for line in open(f, encoding="utf-8"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3 and re.fullmatch(r"\d+", parts[0]) and parts[1] in ("Y", "N"):
                out[parts[0]] = (parts[1], parts[2])
    return out

A, B = load("A"), load("B")
base = {r["recid"]: r for r in csv.DictReader(open(os.path.join(D, "..", "runs", "baselines.csv"), encoding="utf-8"))}
# every screener screened its whole chunk; files store Y lines, so an absent recid means N
for S in (A, B):
    for k in base:
        S.setdefault(k, ("N", "-"))
both = set(A) & set(B)
agree = sum(A[k][0] == B[k][0] for k in both)
inc, log = [], []
for k in sorted(both):
    if A[k][0] == B[k][0] == "Y":
        f = A[k][1] if A[k][1] == B[k][1] else f"disputed:{A[k][1]}/{B[k][1]}"
        inc.append({**base[k], "field": f})
    elif A[k][0] != B[k][0]:
        log.append(f"- {k}: A={A[k][0]} B={B[k][0]} — {base[k]['title'][:90]}")
with open(os.path.join(D, "included_baselines.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(base[next(iter(base))].keys()) + ["field"]); w.writeheader(); w.writerows(inc)
missing = sorted(set(base) - both)
with open(os.path.join(D, "merge_log.md"), "w", encoding="utf-8") as fh:
    fh.write(f"# Screening merge\n\nRecords screened by both screeners: {len(both)} of {len(base)}; missing from either: {len(missing)}\n\n")
    fh.write(f"I1 agreement: {agree}/{len(both)}. Included (both Y): {len(inc)}. I1 disagreements (excluded): {len(log)}\n\n")
    fh.write("Fields of included records: " + str(dict(Counter(r['field'] for r in inc))) + "\n\n## I1 disagreements\n" + "\n".join(log) + "\n")
print(open(os.path.join(D, "merge_log.md"), encoding="utf-8").read()[:900])
