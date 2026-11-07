# Negative control NC1: design (pre-registration addendum, draft)

*2026-11-07. Written after the main confirmatory results (which it does not alter) and before any NC material or sample exists. It becomes binding when frozen by a public commit adding `negative_control/NC_FREEZE_MANIFEST.md`, before any NC sampling. It is a separate follow-up, labelled as such in the paper.*

## Question

When stated physics defeats a choice, do models abandon a **non-historical** choice more readily than the **historically adopted** one?

- If yes: the main-study overrides reflect hindsight (history pulls models back to the adopted item).
- If no: they reflect general stickiness to an attractive, plausible fix, whichever item it is.

## Construction (reuses the frozen main materials)

For each confirmatory unit u (p01, p02, p03, p05, p09):

- **NC_BASE(u) = the main CONF1(u)**, already sampled (50 responses per model).
  - In CONF1 the adopted item fails, and the documented non-adopted alternative **alt(u)** is a sound survivor.
  - This makes alt(u) the natural recommendation, with no historical support.
- **NC_CONF(u) = CONF1(u) plus one minimal additional edit** (one sentence or one set of numbers) under which:
  - alt(u) also robustly fails a stated physical requirement (keylib, ×0.5–2);
  - the adopted item still fails (the CONF1 edit is kept);
  - **at least one third option survives**.
- All AUTHOR_BRIEF rules 1–10, the lessons and clarification C1 apply. A red team checks each NC_CONF. If no honest NC_CONF exists, the unit is NC-zero and is reported.
- **K-probe for each NC_CONF:** the 7 models, n = 20. The suspension rule is as in the main study (≥ 2 models majority-wrong).

## Measures

- **B_alt(m, u):** share of model m's main CONF1 responses whose TOP RECOMMENDATION is alt(u). Coded by the two blind adjudicators with a new NC_BASE rubric code set: ALT / OTHER / X.
- **O_alt(m, u):** share of NC_CONF responses that commit to alt(u) as the main recommendation without a valid fix (codes A/B on an NC rubric that defines alt(u) as the target, with C, D, E and X as in the main study). Both adjudicators must agree.
- **Comparison quantities** (main study, unchanged): B_adopted(m, u) is the BASE adoption rate; O_adopted(m, u) is the CONF1 override rate.

## Pre-specified analysis

**Primary NC test (one-sided, α = 0.05).** Persistence ratio, historical vs non-historical:
- Binomial GLMM on the override responses, pooling the main CONF1 (target = adopted item) and NC_CONF (target = alt):
  `override ~ historical + logit(B_target) + model + (1 | unit)`.
- B_target is the cell's BASE-level choice rate of the target: B_adopted from main BASE, B_alt from main CONF1. It is clipped to [0.02, 0.98].
- **H_NC:** the coefficient of `historical` is > 0, by a Wald test.

**Secondary:**
- per-model descriptive pairs (O/B for adopted vs alt);
- a leave-one-unit-out sign check.

**Inclusion:** units with an honest NC_CONF that passes the K premise; per model, cells where that model is K-correct on both CONF1 and NC_CONF.

## Sampling

NC_CONF only: 5 templates × n = 10 × 7 models per unit (same settings as the main study), plus NC_BASE adjudication of the existing main CONF1 responses for the ALT code.

## Limits stated in advance

- alt(u) differs from the adopted item in intrinsic attractiveness. The B_target covariate adjusts for that only partly.
- With ≤ 5 units the NC test has limited power. A null result is reported as inconclusive, not as evidence against hindsight.
