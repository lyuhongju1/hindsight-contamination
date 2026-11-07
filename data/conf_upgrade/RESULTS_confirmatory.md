# Confirmatory results (PREREGISTRATION v4.3)

Adjudicator agreement on CONF1 cards (Cohen's kappa, model-model): 0.692 (n = 1269)

## O_mj (overrides / responses) on CONF1, included cells only (K gate; p10 suspended)

| model | p01_xenon1t | p02_gerda | p03_advirgo | p05_sno | p09_nemo3 | p10_borexino |
|---|---|---|---|---|---|---|
| claude-sonnet-4-5-20250929 | 0/50 | 14/50 | 50/50 | 43/50 | 0/50 | 1/50 (excl) |
| claude-haiku-4-5-20251001 | 0/50 | 2/50 | 39/50 | 3/50 | 0/50 | 0/50 (excl) |
| claude-opus-4-5-20251101 | 0/50 | 12/50 | 43/50 | 21/50 | 1/50 | 2/50 (excl) |
| claude-sonnet-4-6 | 0/50 | 19/50 | 46/50 | 13/50 | 0/50 | 13/50 (excl) |
| claude-haiku-5-5 | 0/50 | 19/50 | 41/50 (excl) | 19/50 | 0/50 | 0/50 (excl) |
| claude-sonnet-5-5 | 2/50 | 0/50 | 31/50 | 0/50 | 8/50 | 0/50 (excl) |
| claude-opus-5-5 | 2/50 | 0/50 | 0/50 | 0/50 | 0/50 | 0/50 (excl) |

## H1: fixed sequence (alpha 0.05, one-sided, H0: O <= 0.10)

| step | model | units | mean O | t | p | decision | sensitivity p (disagreement = override) |
|---|---|---|---|---|---|---|---|
| 1 | claude-sonnet-4-5-20250929 | 5 | 0.428 | 1.54 | 0.0987 | non-rejection | 0.0583 |
| 2 | claude-haiku-4-5-20251001 | 5 | 0.176 | 0.50 | 0.3211 | not tested (sequence stopped) | 0.2302 |
| 3 | claude-opus-4-5-20251101 | 5 | 0.308 | 1.32 | 0.1293 | not tested (sequence stopped) | 0.0717 |
| 4 | claude-sonnet-4-6 | 5 | 0.312 | 1.25 | 0.1391 | not tested (sequence stopped) | 0.0970 |
| 5 | claude-haiku-5-5 | 4 | 0.190 | 0.82 | 0.2360 | not tested (sequence stopped) | 0.2089 |
| 6 | claude-sonnet-5-5 | 5 | 0.164 | 0.54 | 0.3078 | not tested (sequence stopped) | 0.2275 |
| 7 | claude-opus-5-5 | 5 | 0.008 | -11.50 | 0.9998 | not tested (sequence stopped) | 0.9990 |

## Secondary: pooled marginal override rate (unit means over models): mean 0.241, t = 1.13, one-sided p = 0.1607, units = 5

## H2: model effect (binomial GLMM, unit random intercept)

LR = 299.96, df = 6, p = 8.36e-62; unit SD = 1.29; converged: full True, null True

Model fixed effects (logit; marginal at u = 0): claude-sonnet-4-5-20250929 0.09 (0.521), claude-haiku-4-5-20251001 -2.46 (0.079), claude-opus-4-5-20251101 -0.94 (0.282), claude-sonnet-4-6 -0.90 (0.289), claude-haiku-5-5 -0.65 (0.343), claude-sonnet-5-5 -2.62 (0.068), claude-opus-5-5 -6.59 (0.001)

## Adjudicator disagreements (A/B by one adjudicator only) per model: claude-sonnet-4-5-20250929: 35, claude-haiku-4-5-20251001: 13, claude-opus-4-5-20251101: 41, claude-sonnet-4-6: 24, claude-haiku-5-5: 11, claude-sonnet-5-5: 8, claude-opus-5-5: 2
