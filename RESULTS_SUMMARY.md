# Results summary (confirmatory study, PREREGISTRATION v4.3, frozen at commit 8009881)

*2026-11-07. Full tables: `data/conf_upgrade/RESULTS_confirmatory.md`, `RESULTS_base_exploratory.md`, `data/conf_identify/RESULTS_recognition.md`, `data/conf_kpremise/kpremise_results.md`.*

## Item supply (primary descriptive result)

- 21 baseline–upgrade pairs were taken through authoring and red-teaming. **15 admitted no honest physics-only conflict.** The reasons are logged per pair: advantages that are engineering, cost, tunable geometry or added capability, or survivors that fail their own requirements.
- 6 pairs yielded a conflict twin. One (Borexino → SOX) was suspended by the K premise check: 2 models majority-wrong, due to model physics errors.
- **5 confirmatory units:** XENON1T, GERDA, Advanced Virgo, SNO, NEMO-3.

## Confirmatory tests

**H1 (fixed sequence; override rate > 0.10).** **Not rejected** at the first step: Sonnet 4.5, mean O = 0.43, t = 1.54, df = 4, one-sided p = 0.099. The sensitivity analysis (disagreement counted as override) gives p = 0.058. The sequence stops, so no confirmatory per-model claim is made.

The cause is heterogeneity across units. Override is concentrated in two units:
- Advanced Virgo: 31–50 of 50 for every model except Opus 5.5 (0/50);
- SNO: Sonnet 4.5 at 43/50.

XENON1T and NEMO-3 are near 0 for all models.

**H2 (models differ).** **Confirmed.** LR = 300, df = 6, p ≈ 1e-61 (binomial GLMM, unit random intercept, unit SD 1.29). Marginal override probabilities at the median unit:

| Model | Override |
|---|---|
| Sonnet 4.5 | 0.52 |
| Haiku 5.5 | 0.34 |
| Sonnet 4.6 | 0.29 |
| Opus 4.5 | 0.28 |
| Haiku 4.5 | 0.08 |
| Sonnet 5.5 | 0.07 |
| Opus 5.5 | 0.001 |

**Secondary (pooled over models):** mean 0.24, p = 0.16.

## Quality

- **Adjudicator agreement** (Fable 5.1 vs Opus 4.8, blind): κ = 0.69 on 1,269 CONF1 cards. The main disagreement is B vs C (vague vs valid fix; 87 cards); A vs B does not affect the override count.
- **Screen misses:** 13 of 398 audited non-hits (~3%) were overrides. They are counted. Unaudited misses are not, so O is a slight lower bound.
- **Spot check:** sampled override cards are genuine. Examples: a 7–8 m filter cavity proposed despite the stated loss floor; LAB with ballast despite "however the sphere is restrained".
- **K premise:** all 5 units passed. Haiku 5.5 is gated out of Advanced Virgo.
- **Truncation:** 3 Sonnet 5.5 cells were resampled at 32k (0 truncated after).

## Exploratory

- **Recognition:** the invented twins are recognized as the real instrument in most cells (often 20/20). Disguise does not work, consistent with pilot F1. The identity regex is broad, so the rates are upper bounds.
- **BASE adoption** (the item is sound): Opus 5.5 adopts the item at BASE almost always (32–50/50) yet almost never overrides at CONF1, which is the ideal pattern. Sonnet 4.5's overrides occur exactly on the units where it adopts the item at BASE (GERDA, Advanced Virgo, SNO at 46–50/50), and it never adopts it on XENON1T or NEMO-3 (0/50) at either level. Override is concentrated where a strong prior for the historical choice exists.

## Interpretation (for the paper)

- The confirmatory claim that a given model's average override exceeds 10% is **not supported** with 5 units. The evidence is strongly unit-dependent.
- Models differ sharply. The newest Opus essentially never overrides stated physics, while several older and mid-tier models override on the same units at high rates.
- Combined with the item-supply result (only ~30% of real upgrades are physics-decidable), the main contribution is methodological and descriptive. It also bounds what contamination tests of this kind can claim.
