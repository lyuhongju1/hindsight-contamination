#!/usr/bin/env python3
"""K premise check (PREREGISTRATION: suspend a CONF if >= 2 confirmatory models' majority verdict contradicts the expected one).
Parses the final 'VERDICT: YES|NO' line of each K-probe response.   python -I analysis_kpremise.py"""
import json, re, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, "data", "conf_kpremise", "raw.jsonl"), encoding="utf-8")]
plan = {r["cid"]: r for r in json.load(open(os.path.join(HERE, "data", "conf_kpremise", "plan.json")))["requests"]}
exp = {}
for pair in {r["pair"] for r in rows}:
    for lvl, q in json.load(open(os.path.join(HERE, "materials", pair, "kprobe.json"), encoding="utf-8")).items(): exp[(pair, lvl)] = q["expected"]
def verdict(t):
    m = re.findall(r"VERDICT:\s*\**\s*(YES|NO)\b", t or "", re.I)
    return m[-1].upper() if m else None
cnt = collections.defaultdict(collections.Counter)
for r in rows:
    m = plan[r["custom_id"]]["model"]; cnt[(r["pair"], r["level"], m)][verdict(r["response"])] += 1
models = sorted({k[2] for k in cnt}); units = sorted({(k[0], k[1]) for k in cnt})
L = ["# K premise check (confirmatory models, n=20 per model per CONF)\n", "Cell = correct/valid/n (missing VERDICT lines are excluded from valid). Majority correct = correct > valid/2.\n",
     "| unit | expected | " + " | ".join(models) + " | models wrong | status |", "|---|---|" + "---|" * len(models) + "---|---|"]
gate = {}
for u in units:
    e = exp[u]; cells = []; wrong = 0; per = {}
    for m in models:
        c = cnt[(u[0], u[1], m)]; valid = c["YES"] + c["NO"]; ok = c[e]; n = sum(c.values())
        maj = ok > valid / 2 if valid else False; per[m] = maj; wrong += (not maj)
        cells.append(f"{ok}/{valid}/{n}{'' if maj else ' (x)'}")
    st = "SUSPENDED" if wrong >= 2 else "PASS"; gate[f"{u[0]}/{u[1]}"] = {"status": st, "model_majority_correct": per}
    L.append(f"| {u[0]}/{u[1]} | {e} | " + " | ".join(cells) + f" | {wrong} | **{st}** |")
open(os.path.join(HERE, "data", "conf_kpremise", "kpremise_results.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
json.dump(gate, open(os.path.join(HERE, "data", "conf_kpremise", "kpremise_gate.json"), "w"), indent=1)
print("\n".join(L))
