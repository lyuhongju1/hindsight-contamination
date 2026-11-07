#!/usr/bin/env python3
"""K premise check for the NC twin (same rule as PREREGISTRATION §2.4: suspend if >= 2 models are majority-wrong).
  python -I analysis/nc_kpremise.py"""
import json, os, re
from collections import Counter, defaultdict
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D = os.path.join(H, "data", "conf_nc_kpremise")
plan = {r["cid"]: r for r in json.load(open(os.path.join(D, "plan.json")))["requests"]}
exp = json.load(open(os.path.join(H, "negative_control", "p09_nemo3", "nc_kprobe.json"), encoding="utf-8"))["NC_CONF"]["expected"]
c = defaultdict(Counter)
for l in open(os.path.join(D, "raw.jsonl"), encoding="utf-8"):
    r = json.loads(l); v = re.findall(r"VERDICT:\s*\**\s*(YES|NO)\b", r["response"] or "", re.I)
    c[plan[r["custom_id"]]["model"]][v[-1].upper() if v else None] += 1
maj = {m: (cc[exp] > (cc["YES"] + cc["NO"]) / 2) for m, cc in c.items()}
wrong = sum(not v for v in maj.values()); status = "SUSPENDED" if wrong >= 2 else "PASS"
json.dump({"status": status, "expected": exp, "model_majority_correct": maj, "counts": {m: dict(cc) for m, cc in c.items()}},
          open(os.path.join(D, "nc_kpremise_gate.json"), "w"), indent=1, default=str)
print(status, {m: f"{c[m][exp]}/{sum(c[m].values())}" for m in sorted(c)})
