#!/usr/bin/env python3
"""Recognition (measured, not gated): share of identification-probe responses naming the real baseline or successor
(frozen 'identity' regex), per pair x level x model.   python -I analysis/conf_identify.py"""
import json, os, re
from collections import defaultdict
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); RUN = os.path.join(H, "data", "conf_identify")
R = json.load(open(os.path.join(H, "materials", "scoring_regex.json"), encoding="utf-8"))
plan = {r["cid"]: r for r in json.load(open(os.path.join(RUN, "plan.json")))["requests"]}
agg = defaultdict(lambda: [0, 0])
for l in open(os.path.join(RUN, "raw.jsonl"), encoding="utf-8"):
    r = json.loads(l); m = plan[r["custom_id"]]["model"]; k = (r["pair"], r["level"], m)
    agg[k][1] += 1; agg[k][0] += bool(re.search(R[r["pair"]]["identity"], r["response"] or "", re.I))
models = sorted({k[2] for k in agg}); L = ["# Recognition: identification rate (identity regex), n = 20 per cell\n",
     "| pair | level | " + " | ".join(m.replace("claude-", "") for m in models) + " |", "|---|---|" + "---|" * len(models)]
for p in sorted({k[0] for k in agg}):
    for lvl in ("NAME", "ANON", "BASE", "CONF1"):
        L.append(f"| {p} | {lvl} | " + " | ".join(f"{agg[(p, lvl, m)][0]}/{agg[(p, lvl, m)][1]}" for m in models) + " |")
json.dump({"|".join(k): v for k, v in agg.items()}, open(os.path.join(RUN, "recognition.json"), "w"), indent=1)
open(os.path.join(RUN, "RESULTS_recognition.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n"); print("\n".join(L))
