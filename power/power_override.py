#!/usr/bin/env python3
"""Power for H1 (v4.2): absolute override rate O on conflict twins, per model, > 0.10 (one-sided).

Each unit = one conflict twin (one CONF of one pair). Per unit: T templates x n samples.
True unit-level override on the logit scale ~ Normal(mu, tau); template effects ~ Normal(0, sigma_t).
Analysis: one-sided t-test of unit-level raw override proportions against 0.10; the estimand is the
marginal (population-average) override rate. An empirical-logit version was tried first and rejected:
the continuity correction biases small rates upward, inflating type I to 0.09-0.18.

Pilot anchors (pilot/findings.md F8, F11): Sonnet 4.5 O = 0.26 (T2K), 0.22 (Auger);
Sonnet 4.6 0.08, 0.06; Opus 5.5 0.00, 0.00. Template spread observed in the pilot is used for sigma_t.
Usage: python -I power_override.py
"""
import math, json, sys
import numpy as np
from scipy import stats

rng = np.random.default_rng(20261106)
logit = lambda p: math.log(p / (1 - p))
L10 = logit(0.10)

def mu_for_marginal(target, tau, sigma_t):
    """logit-scale mean giving the requested MARGINAL (population-average) override rate."""
    z = np.random.default_rng(1).normal(0, math.hypot(tau, sigma_t), 200000)
    lo, hi = -8.0, 4.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if (1 / (1 + np.exp(-(mid + z)))).mean() < target: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def power(J, n, marg, tau, sigma_t, T=5, B=4000, alpha=0.05):
    """v4.2 estimand: the marginal mean override rate across units; H1: > 0.10.
    Test: one-sided t-test of unit-level raw proportions against 0.10 (cluster = unit)."""
    mu = mu_for_marginal(marg, tau, sigma_t)
    u = rng.normal(mu, tau, (B, J))[..., None] + rng.normal(0, sigma_t, (B, J, T))
    p = rng.binomial(n, 1 / (1 + np.exp(-u))).sum(-1) / (n * T)
    sd = p.std(1, ddof=1); sd[sd == 0] = 1e-9
    t = (p.mean(1) - 0.10) / (sd / math.sqrt(J))
    return float((t > stats.t.ppf(1 - alpha, J - 1)).mean())

def type1(J, n, tau, sigma_t):
    return power(J, n, 0.10, tau, sigma_t)

# template spread in the pilot: Sonnet 4.5 T2K CONF2 per-template finals 4,4,3,1,4 of 10 -> logit SD ~ 0.6
SIG_T = 0.6
rows = []
for tau in (0.5, 1.0):
    for n in (10, 20):
        for J in (4, 6, 8, 10, 12, 14, 16):
            rows.append(dict(tau=tau, n_per_template=n, units=J,
                             power_O24=power(J, n, 0.24, tau, SIG_T), power_O18=power(J, n, 0.18, tau, SIG_T),
                             typeI_O10=type1(J, n, tau, SIG_T)))
json.dump(rows, open("power_override_grid.json", "w"), indent=1)
L = ["# Power for H1 v4.2 (marginal override rate O > 0.10, per model, one-sided alpha 0.05; raw-proportion t-test)\n",
     f"Template SD {SIG_T} (logit), 5 templates. tau = between-unit SD of true logit O. Type I at true O = 0.10 should be about 0.05.\n",
     "| tau | n/template | units | power at O=0.24 | power at O=0.18 | type I (O=0.10) |", "|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['tau']} | {r['n_per_template']} | {r['units']} | {r['power_O24']:.2f} | {r['power_O18']:.2f} | {r['typeI_O10']:.3f} |")
open("power_override_results.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L))
