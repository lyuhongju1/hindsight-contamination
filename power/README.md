# Power analysis: summary and design consequences

*2026-11-05. Exploratory planning analysis for design v2 §9.3. It is not part of any pre-registration yet. Rerun it on pilot data before freezing.*

## Files

| File | What |
|---|---|
| `power_sim.py` | Estimates variance components from the APS data, then simulates the ladder contrast |
| `diag_typeI.py` | Diagnoses the false-positive rate |
| `power_results.md`, `power_grid.json` | Full power grid |
| `typeI_diagnostic.md` | Diagnostic output |
| `variance_components.json`, `aps_cell_counts.json` | Inputs extracted from the APS data |

Rerun with:

`python -I power_sim.py <APS repo root> .`

The APS repo is `github.com/lyuhongju1/LLM_contamination` (local clone in the old APS session scratchpad). Seed 20261105.

## Inputs taken from the APS study (Sonnet 4.5 and 4.6, five templates)

| Component (logit scale, mid-range cells) | SD |
|---|---|
| Template × condition interaction, paper vs description (A vs D) | 1.12 |
| Template × condition interaction, paper held fixed (A vs B) | 0.69 |
| Description to description (D vs D′, two descriptions of one instrument) | 0.78 |

Baseline rates in condition D:

- adopted items are bimodal, with a median of 63% and a quarter at ≥ 95%;
- distractors are mostly near zero, with a median of 5%.

Assumed, not estimated:

- heterogeneity of the true effect across units, τ = 0.5 logit;
- a generic recognition effect of 0.3 logit on all units.

**τ is the biggest unknown.** Estimate it in the pilot.

## Findings

**1. The number of units decides power. Samples per cell barely matter.** Power for H1 (outcome-specific DiD > 0, per model, one-sided α = 0.05):

| Units | Effect 0.5 logit (≈ 12 pp at mid-range) | Effect 1.0 logit (≈ 23 pp at mid-range) |
|---|---|---|
| 12 | 0.25–0.35 | 0.59–0.76 |
| 20 | 0.39–0.51 | 0.81–0.92 |
| 28 | 0.51–0.65 | 0.92–0.98 |

- Going from 20 to 40 samples per template cell adds about 3–5 points of power.
- Going from 5×3 to 8×5 templates × twins adds about 5–10 points.
- The conservative and optimistic interaction estimates give nearly the same power, because heterogeneity between units dominates the error.
- **Consequence:** use n = 20 per cell and put the money into **units (pairs)**.
- With 20 units the design detects a large outcome-specific effect per model but not a moderate one. A moderate effect needs ≥ 28 units, or pooling across models (point 4).

**2. The naive tests are anticonservative: 7–10% false positives against a nominal 5%.**
- **Cause:** the adopted and distractor units have different baseline distributions. Distractors sit at the floor, where any shift is compressed.
- **Evidence:** drawing both from the same distribution restores 5.0–5.4% (`typeI_diagnostic.md`). Balancing the samples between ladder levels does **not** fix it.
- This is a design flaw in v2 as written, now fixed:
  - **match distractors to adopted units on baseline availability**;
  - make the primary analysis a binomial GLMM, not a t-test on per-unit differences;
  - **verify the false-positive rate of the final analysis by simulation before registration.**
- The percentage-point scale is worse than the logit scale, so the primary estimand stays on the logit scale.

**3. H2 (equivalence, |IR| < 15 pp) is easy.** Power is ≥ 0.87 with 12 units and ≥ 0.99 with 20.

**4. Recommended: make H1 a pooled test across the primary models.** Use a model random effect, with per-model estimates reported as secondary. Three or four models give roughly 3–4 times the information on the shared effect. It also matches the claim the paper wants to make about "frontier models" rather than about one snapshot.

## Budget implication

Per pair, about 8 descriptions × 5 templates × 20 samples ≈ **800 responses per model**. For 14 pairs that is about 11,000 per model, roughly half the v2 estimate. Adopted items and distractors are scored on the same responses.

## Limits of this analysis

- It uses the APS Sonnet 4 models, and the ladder contrasts are proxied by the A/D/D′ contrasts.
- The analysis model is a t-test, not the GLMM.
- Units are treated as independent, although several items share a pair.
- τ is assumed.

The pilot should re-estimate τ, the description SD, and the template × level interaction **from real twin data**, and the simulation should then be rerun with the actual GLMM.
