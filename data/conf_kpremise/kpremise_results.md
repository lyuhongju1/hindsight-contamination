# K premise check (confirmatory models, n=20 per model per CONF)

Cell = correct/valid/n (missing VERDICT lines are excluded from valid). Majority correct = correct > valid/2.

| unit | expected | claude-haiku-4-5-20251001 | claude-haiku-5-5 | claude-opus-4-5-20251101 | claude-opus-5-5 | claude-sonnet-4-5-20250929 | claude-sonnet-4-6 | claude-sonnet-5-5 | models wrong | status |
|---|---|---|---|---|---|---|---|---|---|---|
| p01_xenon1t/CONF1 | NO | 20/20/20 | 20/20/20 | 19/20/20 | 20/20/20 | 19/20/20 | 19/20/20 | 17/20/20 | 0 | **PASS** |
| p02_gerda/CONF1 | NO | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 16/20/20 | 17/20/20 | 20/20/20 | 0 | **PASS** |
| p03_advirgo/CONF1 | NO | 11/20/20 | 10/20/20 (x) | 20/20/20 | 18/20/20 | 17/20/20 | 15/20/20 | 16/20/20 | 1 | **PASS** |
| p05_sno/CONF1 | NO | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 0 | **PASS** |
| p09_nemo3/CONF1 | NO | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 20/20/20 | 0 | **PASS** |
| p10_borexino/CONF1 | NO | 6/20/20 (x) | 16/20/20 | 14/20/20 | 20/20/20 | 7/20/20 (x) | 13/20/20 | 20/20/20 | 2 | **SUSPENDED** |

## Outcome (2026-11-06)

**p10_borexino/CONF1 is SUSPENDED** under PREREGISTRATION §2.4 (≥ 2 models with a contradicting majority: Haiku 4.5 at 6/20 correct, Sonnet 4.5 at 7/20). It is excluded from the confirmatory tests and reported.

**Nature of the dissent** (read in 2 dissenting responses, recorded for the report; the rule is applied mechanically regardless):
- **Sonnet 4.5:** arithmetic error. It computed ~1,330 IBD events on 1.98e28 hydrogen-1 atoms; the correct order is ~10.
- **Haiku 4.5:** it counted charged-current reactions on deuterium, which have a 4.03 MeV threshold that the stated 3.0 MeV endpoint forbids.

Both are model physics errors, not a premise flaw. The suspension is still applied, because the rule was fixed before the data and changing it now would be outcome-dependent.

**Confirmatory units: 5** (p01, p02, p03, p05, p09).
- **Per-model K gating** (PREREGISTRATION §6, inclusion): Haiku 5.5 is majority-wrong on p03 (10/20), so p03 is excluded for Haiku 5.5 only. Every other model × unit cell is included.
- **Power at 5 units** (power_small_J_results.md): 0.80–0.86 at O = 0.24 (τ = 0.5), first test, α = 0.05.
