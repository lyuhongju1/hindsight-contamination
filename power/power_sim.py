#!/usr/bin/env python3
"""Simulation-based power analysis for the hindsight-contamination study (design v2, section 9.3).

Step 1 estimates variance components on the logit scale from the companion (APS) study's
five-template data (Sonnet 4.5 and 4.6; templates O, P1-P4; conditions A, D; plus D').
Step 2 simulates the twin-ladder contrast ANON vs TWIN-EQ, for adopted units and paired
distractors, and reports power for:
  H1  outcome-specific DiD > 0          (one-sided t-test across units, alpha 0.05)
  H2  instance recall IR within +-15 pp  (TOST across units, alpha 0.05, true IR = 0)

The analysis in the simulation is a unit-level t-test, which is conservative relative to the
pre-registered GLMM; the GLMM should have at least this power.

Usage: python -I power_sim.py <aps_repo_root> <out_dir>
"""
import json, os, re, sys, math
from collections import defaultdict
import numpy as np
from scipy import stats

ROOT, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
P = lambda *a: os.path.join(ROOT, *a)
MODELS = {'claude-sonnet-4-5-20250929': 'S4.5', 'claude-sonnet-4-6': 'S4.6'}
T5 = ['O', 'P1', 'P2', 'P3', 'P4']

# ---------------------------------------------------------------- step 1: load and count
cells = defaultdict(list)
def load(fn, default_t='O', keep=None):
    best = {}
    for line in open(P('data', fn), encoding='utf-8'):
        r = json.loads(line)
        if r['model'] not in MODELS: continue
        t = r.get('template', default_t)
        if keep and t not in keep: continue
        k = (t, r['pair'], r['condition'], r['model'], r['sample'])
        if k not in best or r.get('max_tokens', 0) > best[k].get('max_tokens', 0): best[k] = r
    for (t, pn, c, m, s), r in best.items(): cells[(t, pn, c, MODELS[m])].append(r['response'])
load('raw_v2.jsonl'); load('raw_dprime.jsonl')
load('raw_paraphrase.jsonl', keep={'P1', 'P2'}); load('raw_amend9_ab.jsonl', keep={'P3', 'P4'})

cfg = json.load(open(P('keys.json'), encoding='utf-8'))
pairs = {p['name']: p for p in cfg['pairs']}
dis = json.load(open(P('distractor_keys.json'), encoding='utf-8'))['distractors']
adopted = []
for pn, p in pairs.items():
    text = open(P(p['paper_txt']), encoding='utf-8', errors='ignore').read()
    for item, spec in p['items'].items():
        if not re.search(spec['regex'], text, re.I): adopted.append((pn, item, spec['regex']))
assert len(adopted) == 26, len(adopted)
distr = [(pn, name, rx) for pn, d in dis.items() for name, rx in d.items()]

def count(t, pn, c, m, rx):
    rs = cells.get((t, pn, c, m), [])
    return sum(re.search(rx, x, re.I) is not None for x in rs), len(rs)

def logit_cc(k, n):  # continuity-corrected logit and its binomial variance
    p = (k + 0.5) / (n + 1)
    return math.log(p / (1 - p)), 1 / ((n + 1) * p * (1 - p))

rows = []
for kind, lst in (('adopted', adopted), ('distractor', distr)):
    for pn, name, rx in lst:
        for m in MODELS.values():
            for c in ('A', 'B', 'D'):
                for t in T5:
                    k, n = count(t, pn, c, m, rx)
                    if n: rows.append(dict(kind=kind, pair=pn, item=name, model=m, cond=c, template=t, k=k, n=n))
            k, n = count('O', pn, 'Dp', m, rx)
            if n: rows.append(dict(kind=kind, pair=pn, item=name, model=m, cond='Dp', template='O', k=k, n=n))
json.dump(rows, open(os.path.join(OUT, 'aps_cell_counts.json'), 'w'), indent=0)

# ---------------------------------------------------------------- step 1b: variance components
idx = {(r['kind'], r['pair'], r['item'], r['model'], r['cond'], r['template']): r for r in rows}
def lg(kind, pn, it, m, c, t):
    r = idx.get((kind, pn, it, m, c, t)); return logit_cc(r['k'], r['n']) if r else None

# (a) template-by-condition interaction: for each item x model, d_t = logit_c1,t - logit_c2,t over
#     the five templates; var_t(d_t) minus mean binomial variance of d_t. Mid-range cells only.
#     A vs D (paper vs description) is the conservative estimate; A vs B (paper held fixed) the
#     optimistic one. Ladder contrasts (description vs description) should lie between them.
def interaction(c1, c2):
    obs, binv = [], []
    for kind, lst in (('adopted', adopted), ('distractor', distr)):
        for pn, it, _ in lst:
            for m in MODELS.values():
                ds, vs, ks, ns = [], [], 0, 0
                for t in T5:
                    a, d = lg(kind, pn, it, m, c1, t), lg(kind, pn, it, m, c2, t)
                    if a and d:
                        ds.append(a[0] - d[0]); vs.append(a[1] + d[1])
                        for c in (c1, c2):
                            r = idx[(kind, pn, it, m, c, t)]; ks += r['k']; ns += r['n']
                if len(ds) == 5 and 0.10 <= ks / ns <= 0.90:
                    obs.append(np.var(ds, ddof=1)); binv.append(np.mean(vs))
    return max(0.0, np.mean(obs) - np.mean(binv)), len(obs)

# (b) description-to-description variance: D vs D' (two descriptions of one instrument, one
#     template). Var across items of (logit_D - logit_D') minus binomial variance minus the
#     template-interaction share. Mid-range only.
dd, dv = [], []
for kind, lst in (('adopted', adopted), ('distractor', distr)):
    for pn, it, _ in lst:
        for m in MODELS.values():
            a, b = lg(kind, pn, it, m, 'D', 'O'), lg(kind, pn, it, m, 'Dp', 'O')
            if a and b:
                ra, rb = idx[(kind, pn, it, m, 'D', 'O')], idx[(kind, pn, it, m, 'Dp', 'O')]
                pool = (ra['k'] + rb['k']) / (ra['n'] + rb['n'])
                if 0.10 <= pool <= 0.90: dd.append(a[0] - b[0]); dv.append(a[1] + b[1])
var_desc_diff = max(0.0, np.var(dd, ddof=1) - np.mean(dv))
var_desc = var_desc_diff / 2  # per description
var_int, n_int = interaction('A', 'D')
var_int_ab, n_int_ab = interaction('A', 'B')

# (c) empirical D rates (pooled over templates) for adopted and distractor items
def pooled(kind, lst, c='D'):
    out = []
    for pn, it, _ in lst:
        for m in MODELS.values():
            ks = sum(idx[(kind, pn, it, m, c, t)]['k'] for t in T5 if (kind, pn, it, m, c, t) in idx)
            ns = sum(idx[(kind, pn, it, m, c, t)]['n'] for t in T5 if (kind, pn, it, m, c, t) in idx)
            if ns: out.append(ks / ns)
    return np.array(out)
pA, pD = pooled('adopted', adopted), pooled('distractor', distr)

comp = dict(var_template_by_condition=var_int, sd_template_by_condition=math.sqrt(var_int),
            n_cells_interaction=n_int, sd_template_by_condition_AB=math.sqrt(var_int_ab), n_cells_interaction_AB=n_int_ab, var_description=var_desc, sd_description=math.sqrt(var_desc),
            n_cells_description=len(dd),
            adopted_D_rates_quantiles=np.quantile(pA, [.1, .25, .5, .75, .9]).round(3).tolist(),
            distractor_D_rates_quantiles=np.quantile(pD, [.1, .25, .5, .75, .9]).round(3).tolist())
json.dump(comp, open(os.path.join(OUT, 'variance_components.json'), 'w'), indent=2)

# ---------------------------------------------------------------- step 2: simulate the ladder
rng = np.random.default_rng(20261105)
expit = lambda x: 1 / (1 + np.exp(-x))
clip = lambda p: np.clip(p, 0.02, 0.98)
LA, LD = np.log(clip(pA) / (1 - clip(pA))), np.log(clip(pD) / (1 - clip(pD)))
s_d = math.sqrt(var_desc)                       # per-description deviation
S_E = {'conservative (A-D)': math.sqrt(var_int / 2), 'optimistic (A-B)': math.sqrt(var_int_ab / 2)}

def sim(U, n, d_out, tau, s_e, n_t=5, n_tw=3, d_rec=0.3, B=2000):
    """Unit-level IR and DiD on the pp scale and on the logit scale."""
    base_a = rng.choice(LA, size=(B, U)); base_d = rng.choice(LD, size=(B, U))
    eff_a = d_rec + d_out + rng.normal(0, tau, (B, U))
    eff_d = d_rec + rng.normal(0, tau, (B, U))
    def contrast(base, eff):
        anon_mu = base[..., None] + rng.normal(0, s_d, (B, U, 1)) + rng.normal(0, s_e, (B, U, n_t))
        twin_mu = (base - eff)[..., None, None] + rng.normal(0, s_d, (B, U, n_tw, 1)) \
                  + rng.normal(0, s_e, (B, U, n_tw, n_t))
        ka = rng.binomial(n, expit(anon_mu)).sum(-1); na = n * n_t
        kt = rng.binomial(n, expit(twin_mu)).sum((-1, -2)); nt = n * n_t * n_tw
        pp = 100 * (ka / na - kt / nt)
        lo = np.log((ka + .5) / (na - ka + .5)) - np.log((kt + .5) / (nt - kt + .5))
        return pp, lo
    pa, la = contrast(base_a, eff_a); pd_, ld = contrast(base_d, eff_d)
    return dict(ir_pp=pa, did_pp=pa - pd_, did_logit=la - ld)

def p_onesided(x):
    U = x.shape[1]; t = x.mean(1) / (x.std(1, ddof=1) / math.sqrt(U))
    return float((t > stats.t.ppf(0.95, U - 1)).mean())

def p_tost(ir, margin=15.0):
    U = ir.shape[1]; m, se = ir.mean(1), ir.std(1, ddof=1) / math.sqrt(U); tc = stats.t.ppf(0.95, U - 1)
    return float(((((m - margin) / se) < -tc) & (((m + margin) / se) > tc)).mean())

TAU = 0.5
results = []
for se_name, s_e in S_E.items():
    for U in (12, 20, 28):
        for n_t, n_tw in ((5, 3), (8, 3), (5, 5), (8, 5)):
            for n in (20, 40):
                for d_out in (0.0, 0.5, 1.0):
                    r = sim(U, n, d_out, TAU, s_e, n_t, n_tw)
                    row = dict(interaction=se_name, units=U, templates=n_t, twins=n_tw, n_per_cell=n, d_out_logit=d_out,
                               power_logit=round(p_onesided(r['did_logit']), 3), power_pp=round(p_onesided(r['did_pp']), 3),
                               responses_per_unit_model=n * n_t * (1 + n_tw))
                    if d_out == 0.0:
                        r0 = sim(U, n, 0.0, TAU, s_e, n_t, n_tw, d_rec=0.0)
                        row['power_H2_TOST'] = round(p_tost(r0['ir_pp']), 3)
                    results.append(row)
json.dump(results, open(os.path.join(OUT, 'power_grid.json'), 'w'), indent=1)

# ---------------------------------------------------------------- report
L = ["# Power simulation results (generated by power_sim.py)\n",
     "## Variance components from the APS five-template data (logit scale, mid-range cells)\n",
     f"- Template x condition interaction SD, A vs D (paper vs description): **{comp['sd_template_by_condition']:.2f}** ({comp['n_cells_interaction']} cells)",
     f"- Template x condition interaction SD, A vs B (paper held fixed): **{comp['sd_template_by_condition_AB']:.2f}** ({comp['n_cells_interaction_AB']} cells)",
     f"- Description-to-description SD (D vs D'): **{comp['sd_description']:.2f}** ({comp['n_cells_description']} cells)",
     f"- Adopted-item D rates, 10/25/50/75/90th pct: {comp['adopted_D_rates_quantiles']}",
     f"- Distractor D rates, same: {comp['distractor_D_rates_quantiles']}\n",
     f"Effect heterogeneity across units tau = {TAU} logit; generic recognition effect 0.3 logit on both adopted and distractor units.\n",
     "## H1 (DiD > 0, one-sided, alpha 0.05)\n",
     "Each cell: power on the **logit** scale, with the pp-scale test in brackets. The d=0 column is the false-positive rate (target 0.05).\n"]
for se_name in S_E:
    L.append(f"### Interaction: {se_name}\n")
    L.append("| units | templates x twins | n/cell | responses per unit per model | d=0 | d=0.5 | d=1.0 |")
    L.append("|---|---|---|---|---|---|---|")
    for U in (12, 20, 28):
        for n_t, n_tw in ((5, 3), (8, 3), (5, 5), (8, 5)):
            for n in (20, 40):
                rs = [r for r in results if r['interaction'] == se_name and r['units'] == U and r['templates'] == n_t
                      and r['twins'] == n_tw and r['n_per_cell'] == n]
                L.append(f"| {U} | {n_t} x {n_tw} | {n} | {rs[0]['responses_per_unit_model']} | " +
                         " | ".join(f"{r['power_logit']:.2f} ({r['power_pp']:.2f})" for r in rs) + " |")
    L.append("")
L.append("## H2 (TOST |IR| < 15 pp, true IR = 0), conservative interaction\n")
L.append("| units | templates x twins | n/cell | power |"); L.append("|---|---|---|---|")
for r in results:
    if r['interaction'].startswith('conservative') and 'power_H2_TOST' in r:
        L.append(f"| {r['units']} | {r['templates']} x {r['twins']} | {r['n_per_cell']} | {r['power_H2_TOST']:.2f} |")
open(os.path.join(OUT, 'power_results.md'), 'w', encoding='utf-8').write("\n".join(L) + "\n")
print("\n".join(L))
