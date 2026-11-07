#!/usr/bin/env python3
"""Confirmatory analysis (PREREGISTRATION v4.3 §6). Written before any confirmatory data was read.

  python -I analysis/conf_analysis.py

Inputs:
- data/conf_upgrade/raw.jsonl and plan.json;
- data/conf_upgrade/adjudication/<pair>/{KEY_do_not_open.json, labels_A.txt, labels_B.txt} (lines 'card|CODE');
- data/conf_kpremise/kpremise_gate.json.

Override (per response) = both adjudicators code A or B. Unadjudicated screen non-hits count as non-override.
O_mj = overrides / responses (50).
- H1: fixed-sequence one-sided t-tests of O_mj against 0.10 across included units (alpha 0.05).
- Sensitivity: disagreement counted as override.
- Secondary: pooled unit-level means over models.
- H2: LRT of the model effect in a binomial GLMM with a unit random intercept (Gauss-Hermite, 30 nodes).
"""
import json, math, os, re
from collections import defaultdict
import numpy as np
from scipy import stats, optimize
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.join(H, "data", "conf_upgrade")
ORDER = ["claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001", "claude-opus-4-5-20251101", "claude-sonnet-4-6",
         "claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"]
UNITS = ["p01_xenon1t", "p02_gerda", "p03_advirgo", "p05_sno", "p09_nemo3", "p10_borexino"]
ALPHA, NULL, MIN_UNITS = 0.05, 0.10, 4
gate = json.load(open(os.path.join(H, "data", "conf_kpremise", "kpremise_gate.json")))
plan = {r["cid"]: r for r in json.load(open(os.path.join(RUN, "plan.json")))["requests"]}
rows = [json.loads(l) for l in open(os.path.join(RUN, "raw.jsonl"), encoding="utf-8")]
n = defaultdict(int)
for r in rows:
    if r["level"] == "CONF1": n[(r["pair"], plan[r["custom_id"]]["model"])] += 1
def labels(p, who):
    f = os.path.join(RUN, "adjudication", p, f"labels_{who}.txt")
    return {a.strip(): b.strip().upper() for a, b in (l.split("|")[:2] for l in open(f, encoding="utf-8") if "|" in l)}
ov, ov_s, dis = defaultdict(int), defaultdict(int), defaultdict(int)
kappa_pairs = []
for p in UNITS:
    key = json.load(open(os.path.join(RUN, "adjudication", p, "KEY_do_not_open.json")))
    A, B = labels(p, "A"), labels(p, "B")
    for cid, k in key.items():
        if k["level"] != "CONF1": continue
        a, b = A.get(cid, "X"), B.get(cid, "X"); kappa_pairs.append((a, b))
        o_a, o_b = a in ("A", "B"), b in ("A", "B")
        ov[(p, k["model"])] += o_a and o_b; ov_s[(p, k["model"])] += o_a or o_b; dis[(p, k["model"])] += o_a != o_b
def kappa(pairs):
    cats = sorted({x for pr in pairs for x in pr}); N = len(pairs)
    po = sum(a == b for a, b in pairs) / N
    pe = sum((sum(a == c for a, _ in pairs) / N) * (sum(b == c for _, b in pairs) / N) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0
def included(p, m): return gate.get(f"{p}/CONF1", {}).get("status") == "PASS" and gate[f"{p}/CONF1"]["model_majority_correct"].get(m, False)
def ttest(vals):
    v = np.array(vals); J = len(v)
    if J < 2: return float("nan"), float("nan")
    sd = v.std(ddof=1); sd = sd if sd > 0 else 1e-9
    t = (v.mean() - NULL) / (sd / math.sqrt(J)); return t, float(stats.t.sf(t, J - 1))
L = ["# Confirmatory results (PREREGISTRATION v4.3)\n", f"Adjudicator agreement on CONF1 cards (Cohen's kappa, model-model): {kappa(kappa_pairs):.3f} (n = {len(kappa_pairs)})\n",
     "## O_mj (overrides / responses) on CONF1, included cells only (K gate; p10 suspended)\n",
     "| model | " + " | ".join(UNITS) + " |", "|---|" + "---|" * len(UNITS)]
for m in ORDER:
    L.append(f"| {m} | " + " | ".join((f"{ov[(p, m)]}/{n[(p, m)]}" + ("" if included(p, m) else " (excl)")) for p in UNITS) + " |")
L += ["\n## H1: fixed sequence (alpha 0.05, one-sided, H0: O <= 0.10)\n", "| step | model | units | mean O | t | p | decision | sensitivity p (disagreement = override) |", "|---|---|---|---|---|---|---|---|"]
going = True
for i, m in enumerate(ORDER, 1):
    us = [p for p in UNITS if included(p, m) and n[(p, m)]]
    vals = [ov[(p, m)] / n[(p, m)] for p in us]; vs = [ov_s[(p, m)] / n[(p, m)] for p in us]
    t, pv = ttest(vals); _, ps = ttest(vs)
    if len(us) < MIN_UNITS: dec = "non-rejection (< 4 units)"
    elif not going: dec = "not tested (sequence stopped)"
    else: dec = "REJECT H0" if pv < ALPHA else "non-rejection"
    if going and not dec.startswith("REJECT"): going = False
    L.append(f"| {i} | {m} | {len(us)} | {np.mean(vals) if vals else float('nan'):.3f} | {t:.2f} | {pv:.4f} | {dec} | {ps:.4f} |")
# secondary: pooled over models (unit means of included cells)
um = [np.mean([ov[(p, m)] / n[(p, m)] for m in ORDER if included(p, m) and n[(p, m)]]) for p in UNITS if any(included(p, m) for m in ORDER)]
t, pv = ttest(um); L += [f"\n## Secondary: pooled marginal override rate (unit means over models): mean {np.mean(um):.3f}, t = {t:.2f}, one-sided p = {pv:.4f}, units = {len(um)}\n"]
# H2: binomial GLMM, unit random intercept, model fixed effects
cells = [(UNITS.index(p), ORDER.index(m), ov[(p, m)], n[(p, m)]) for p in UNITS for m in ORDER if included(p, m) and n[(p, m)]]
gh_x, gh_w = np.polynomial.hermite.hermgauss(30)
def nll(theta, full):
    s = math.exp(theta[0]); beta = theta[1:]; tot = 0.0
    for j in sorted({c[0] for c in cells}):
        cj = [c for c in cells if c[0] == j]; u = math.sqrt(2) * s * gh_x
        ll = np.zeros_like(u)
        for _, mi, k, N in cj:
            eta = (beta[mi] if full else beta[0]) + u
            ll += k * eta - N * np.logaddexp(0, eta) + math.lgamma(N + 1) - math.lgamma(k + 1) - math.lgamma(N - k + 1)
        mx = ll.max(); tot += mx + math.log((gh_w * np.exp(ll - mx)).sum() / math.sqrt(math.pi))
    return -tot
f1 = optimize.minimize(nll, np.r_[0.0, np.full(len(ORDER), -2.0)], args=(True,), method="Nelder-Mead", options={"maxiter": 40000, "maxfev": 40000, "xatol": 1e-6, "fatol": 1e-8})
f0 = optimize.minimize(nll, np.r_[0.0, -2.0], args=(False,), method="Nelder-Mead", options={"maxiter": 20000, "xatol": 1e-6, "fatol": 1e-8})
mods = sorted({c[1] for c in cells}); lr = 2 * (f0.fun - f1.fun); df = len(mods) - 1
L += ["## H2: model effect (binomial GLMM, unit random intercept)\n", f"LR = {lr:.2f}, df = {df}, p = {stats.chi2.sf(lr, df):.3g}; unit SD = {math.exp(f1.x[0]):.2f}; converged: full {f1.success}, null {f0.success}\n",
      "Model fixed effects (logit; marginal at u = 0): " + ", ".join(f"{ORDER[i]} {f1.x[1 + i]:.2f} ({1 / (1 + math.exp(-f1.x[1 + i])):.3f})" for i in mods)]
L += ["\n## Adjudicator disagreements (A/B by one adjudicator only) per model: " + ", ".join(f"{m}: {sum(dis[(p, m)] for p in UNITS)}" for m in ORDER)]
open(os.path.join(RUN, "RESULTS_confirmatory.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("\n".join(L).encode("ascii", "replace").decode())
