#!/usr/bin/env python3
"""Exploratory analyses (post-freeze; labelled exploratory in the paper).   python -I analysis/exploratory.py
E1 knowledge-override dissociation; E2 recall traces in override responses; E3 recognition vs override;
E4 GLMM version of H1 (per model); E5 per-template override; E6 leave-one-unit-out H2."""
import json, math, os, re
from collections import defaultdict
import numpy as np
from scipy import stats, optimize

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.join(H, "data", "conf_upgrade")
ORDER = ["claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001", "claude-opus-4-5-20251101", "claude-sonnet-4-6",
         "claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"]
UNITS = ["p01_xenon1t", "p02_gerda", "p03_advirgo", "p05_sno", "p09_nemo3"]
SHORT = {m: m.replace("claude-", "").split("-2025")[0] for m in ORDER}
R = json.load(open(os.path.join(H, "materials", "scoring_regex.json"), encoding="utf-8"))
gate = json.load(open(os.path.join(H, "data", "conf_kpremise", "kpremise_gate.json")))

# responses, with the 32k resample replacing its cells
plan = {r["cid"]: r for r in json.load(open(os.path.join(RUN, "plan.json")))["requests"]}
rows = [json.loads(l) for l in open(os.path.join(RUN, "raw.jsonl"), encoding="utf-8")]
rs = os.path.join(H, "data", "conf_upgrade_resample")
rplan = {r["cid"]: r for r in json.load(open(os.path.join(rs, "plan.json")))["requests"]}
cells = {(r["pair"], r["level"], r["model"]) for r in rplan.values()}
rows = [r for r in rows if (r["pair"], r["level"], plan[r["custom_id"]]["model"]) not in cells]
rows += [json.loads(l) for l in open(os.path.join(rs, "raw.jsonl"), encoding="utf-8")]
plan.update(rplan)


def labels(p, w):
    f = os.path.join(RUN, "adjudication", p, f"labels_{w}.txt")
    return {l.split("|")[0]: l.split("|")[1] for l in open(f, encoding="utf-8") if "|" in l}


ovr = {}
for p in UNITS:
    key = json.load(open(os.path.join(RUN, "adjudication", p, "KEY_do_not_open.json")))
    A, B = labels(p, "A"), labels(p, "B")
    for c, k in key.items():
        if k["level"] == "CONF1":
            ovr[k["custom_id"]] = (A[c] in "AB" and B[c] in "AB")

conf = [r for r in rows if r["level"] == "CONF1" and r["pair"] in UNITS]
cnt = defaultdict(lambda: [0, 0])
for r in conf:
    m = plan[r["custom_id"]]["model"]
    cnt[(r["pair"], m)][1] += 1
    cnt[(r["pair"], m)][0] += ovr.get(r["custom_id"], False)
O = {k: v[0] / v[1] for k, v in cnt.items()}
L = ["# Exploratory analyses (post-freeze)\n"]

# E1: knowledge-override dissociation
kp = {r["cid"]: r for r in json.load(open(os.path.join(H, "data", "conf_kpremise", "plan.json")))["requests"]}
kc = defaultdict(lambda: [0, 0])
for l in open(os.path.join(H, "data", "conf_kpremise", "raw.jsonl"), encoding="utf-8"):
    r = json.loads(l)
    m = kp[r["custom_id"]]["model"]
    v = re.findall(r"VERDICT:\s*\**\s*(YES|NO)\b", r["response"] or "", re.I)
    kc[(r["pair"], m)][1] += 1
    kc[(r["pair"], m)][0] += bool(v) and v[-1].upper() == "NO"
L += ["## E1. Knows the physics, overrides anyway\n",
      "Cell: K correct /20 ; override /50. Cells with K >= 15/20 AND override >= 10/50 are marked (D).\n",
      "| unit | " + " | ".join(SHORT[m] for m in ORDER) + " |", "|---|" + "---|" * len(ORDER)]
dis = 0
for p in UNITS:
    cs = []
    for m in ORDER:
        k, o = kc[(p, m)][0], cnt[(p, m)][0]
        star = k >= 15 and o >= 10
        dis += star
        cs.append(f"{k}/20 ; {o}/50" + (" (D)" if star else ""))
    L.append(f"| {p} | " + " | ".join(cs) + " |")
L.append(f"\n{dis} of {len(UNITS) * len(ORDER)} model x unit cells show strong dissociation (K >= 15/20 correct, override >= 10/50).\n")

# E2: recall traces (identity regex on the full response)
tr = defaultdict(lambda: [0, 0])
nt = defaultdict(lambda: [0, 0])
for r in conf:
    d = tr if ovr.get(r["custom_id"]) else nt
    d[r["pair"]][1] += 1
    d[r["pair"]][0] += bool(re.search(R[r["pair"]]["identity"], r["response"] or "", re.I))
L += ["## E2. Recall traces: CONF1 responses naming the real programme (identity regex, full text)\n",
      "| unit | override responses | non-override responses |", "|---|---|---|"]
for p in UNITS:
    L.append(f"| {p} | {tr[p][0]}/{tr[p][1]} | {nt[p][0]}/{nt[p][1]} |")

# E3: recognition vs override
rec = json.load(open(os.path.join(H, "data", "conf_identify", "recognition.json")))
xs, ys = [], []
for p in UNITS:
    for m in ORDER:
        v = rec.get(f"{p}|CONF1|{m}")
        if v:
            xs.append(v[0] / v[1]); ys.append(O[(p, m)])
rho, pr = stats.spearmanr(xs, ys)
L += [f"\n## E3. Recognition (CONF1 identification rate) vs override, {len(xs)} model x unit cells: Spearman rho = {rho:.2f}, two-sided p = {pr:.3f}\n"]

# GLMM helper (unit random intercept, Gauss-Hermite)
gx, gw = np.polynomial.hermite.hermgauss(30)


def make_nll(cells, design):
    def nll(th):
        s = math.exp(th[0]); b = th[1:]; tot = 0.0
        for j in sorted({c[0] for c in cells}):
            u = math.sqrt(2) * s * gx; ll = np.zeros_like(u)
            for jj, mi, k, N in cells:
                if jj != j:
                    continue
                eta = design(b, mi) + u
                ll += k * eta - N * np.logaddexp(0, eta) + math.lgamma(N + 1) - math.lgamma(k + 1) - math.lgamma(N - k + 1)
            mx = ll.max(); tot += mx + math.log((gw * np.exp(ll - mx)).sum() / math.sqrt(math.pi))
        return -tot
    return nll


def fit(cells, nb, design):
    nll = make_nll(cells, design)
    f = optimize.minimize(nll, np.r_[0.0, np.full(nb, -2.0)], method="Nelder-Mead",
                          options={"maxiter": 40000, "maxfev": 40000, "xatol": 1e-6, "fatol": 1e-8})
    return f, nll


def incl(p, m):
    g = gate[f"{p}/CONF1"]
    return g["status"] == "PASS" and g["model_majority_correct"][m]


def marg(b, s):
    return float((gw * (1 / (1 + np.exp(-(b + math.sqrt(2) * s * gx))))).sum() / math.sqrt(math.pi))


# E4: GLMM version of H1
L += ["## E4. GLMM version of H1 (per model; unit random intercept)\n",
      "| model | units | marginal O (GLMM) | LR vs marginal 0.10 | one-sided p |", "|---|---|---|---|---|"]
for m in ORDER:
    cs = [(UNITS.index(p), 0, cnt[(p, m)][0], cnt[(p, m)][1]) for p in UNITS if incl(p, m)]
    f, nll = fit(cs, 1, lambda b, mi: b[0])
    s = math.exp(f.x[0]); mo = marg(f.x[1], s)

    def nll0(ls):
        l0 = min(float(ls[0]), math.log(10.0)); ss = math.exp(l0)
        b0 = optimize.brentq(lambda b: marg(b, ss) - 0.10, -400, 400)
        return nll(np.r_[l0, b0])
    f0 = optimize.minimize(nll0, [f.x[0]], method="Nelder-Mead")
    lr = max(0.0, 2 * (f0.fun - f.fun))
    z = math.sqrt(lr) * (1 if mo > 0.10 else -1)
    L.append(f"| {SHORT[m]} | {len(cs)} | {mo:.3f} | {lr:.2f} | {stats.norm.sf(z):.4f} |")

# E5: per-template override
tt = defaultdict(lambda: [0, 0])
for r in conf:
    m = plan[r["custom_id"]]["model"]
    if incl(r["pair"], m):
        tt[r["template"]][1] += 1; tt[r["template"]][0] += ovr.get(r["custom_id"], False)
L += ["\n## E5. Override by template (included cells pooled)\n", "| template | override |", "|---|---|"]
L += [f"| {t} | {v[0]}/{v[1]} ({v[0] / v[1]:.3f}) |" for t, v in sorted(tt.items())]

# E6: leave-one-unit-out H2
L += ["\n## E6. Leave-one-unit-out H2 (LR test of model effect)\n", "| left out | LR | df | p |", "|---|---|---|---|"]
for drop in UNITS:
    cs = [(UNITS.index(p), ORDER.index(m), cnt[(p, m)][0], cnt[(p, m)][1]) for p in UNITS for m in ORDER if p != drop and incl(p, m)]
    mods = sorted({c[1] for c in cs}); idx = {mi: i for i, mi in enumerate(mods)}
    f1, _ = fit(cs, len(mods), lambda b, mi: b[idx[mi]])
    f0, _ = fit(cs, 1, lambda b, mi: b[0])
    lr = 2 * (f0.fun - f1.fun)
    L.append(f"| {drop} | {lr:.1f} | {len(mods) - 1} | {stats.chi2.sf(lr, len(mods) - 1):.2g} |")

open(os.path.join(RUN, "RESULTS_exploratory.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("\n".join(L).encode("ascii", "replace").decode())
