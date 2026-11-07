#!/usr/bin/env python3
"""Power at the achieved unit count (6) and neighbours, at alpha 0.05 and at the Holm worst case 0.05/7.
Imports the v4.2 model from power_override.py without re-running its grid."""
import importlib.util, json, sys, types
src = open("power_override.py", encoding="utf-8").read().split("# template spread in the pilot")[0]
m = types.ModuleType("po"); exec(src, m.__dict__)
SIG_T = 0.6
rows = []
for J in (5, 6, 7, 8):
    for tau in (0.5, 1.0):
        for n in (10, 20):
            for a in (0.05, 0.05/7):
                rows.append(dict(J=J, tau=tau, n=n, alpha=round(a,4),
                                 p24=m.power(J, n, 0.24, tau, SIG_T, alpha=a),
                                 p30=m.power(J, n, 0.30, tau, SIG_T, alpha=a),
                                 t1=m.power(J, n, 0.10, tau, SIG_T, alpha=a)))
L = ["# Power at small unit counts (v4.2 model; one-sided raw-proportion t-test; template SD 0.6, 5 templates)\n",
     "alpha 0.0071 = 0.05/7 is the Holm worst case (the smallest p of 7 models).\n",
     "| units | tau | n/template | alpha | power O=0.24 | power O=0.30 | type I |", "|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['J']} | {r['tau']} | {r['n']} | {r['alpha']} | {r['p24']:.2f} | {r['p30']:.2f} | {r['t1']:.3f} |")
open("power_small_J_results.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L))
