# Pilot findings log

## F1 — T2K twins fail the identification gate (2026-11-05, run `id_t2k_v1`)

**Setup.** Identification probe, n = 20 per description per model. The gate (design v2 §4.3) requires ID ≤ 10% on every model.

| Level | Sonnet 4.5 | Sonnet 4.6 | Opus 5.5 | Responses naming the adopted item (SuperFGD), per model 4.5 / 4.6 / Opus |
|---|---|---|---|---|
| EQ1 | 95% | 50% | 100% | 0 / 0 / 19 |
| EQ2 | 100% | 95% | 100% | 4 / 0 / 20 |
| EQ3 | 80% | 85% | 100% | 0 / 0 / 19 |
| CONF1 | 100% | 80% | 100% | 0 / 0 / 5 |
| ABS | 5% | 95% | 100% | 0 / 0 / 20 |

**Reading.** Almost every identification is of the form "this appears invented, but it is clearly modelled on T2K ND280". Counting these as identifications is correct for this study: what matters is whether the instance's history is accessible, not whether the model believes the text describes the real detector. Opus 5.5 also names the outcome. On EQ and ABS it says the twin resembles "the ND280 upgrade, where the P0D was replaced by SuperFGD", and it maps the invented ABS component ("Korrin array") onto SuperFGD.

**Likely cause (to be checked against the red team).** The twins keep the *decision context* of the real instrument, and that context is a fingerprint:

- the upstream section of a dipole near detector being emptied for a new active target;
- the "kinematically complete events / transverse kinematic imbalance" goal;
- a water far detector;
- a sub-GeV off-axis beam;
- planar x/y scintillator bars with gas TPCs.

The same mechanism as the companion study's D′ result applies: a unique instrument has no anonymous description, and v1 twins carry the decision structure that makes it unique.

**Implications for design v3 (to decide after Auger and the red teams):**

1. A 10% gate may be unattainable for twins that keep the decision structure, at least on the strongest models. Options:
   - (a) push twins further from the real context, at the cost of fidelity;
   - (b) treat ID as the continuous covariate of the dose–response (H4), rather than as a hard gate; report results per model;
   - (c) both: a gate at a looser, pre-registered threshold, plus the covariate analysis.
2. The explicit "is this real?" probe invites a search for a match. The in-response mention rate under the upgrade task is a second, probably lower, measure of recognition, and the pilot sampling will provide it.
3. Model dependence is large. Sonnet 4.5 is fooled by ABS and Opus 5.5 is not, consistent with the companion study's finding that recognition grows with scale and generation. The ladder may work on some models and not on others, and that itself is reportable.
4. This is evidence *for* the mechanism the paper is about. The strongest model reconstructs the real instance, and its adopted upgrade, from a disguised description of the decision context.

## F2 — Auger twins are identified on every model at every level (run `id_auger_v1`)

| Level | Identified, per model 4.5 / 4.6 / Opus | Opus names AugerPrime unprompted |
|---|---|---|
| EQ1–3 | 20 / 20 / 20 on each | 20 / 20 / 20 |
| CONF1 | 20 / 20 / 20 | 20 |
| ABS | 20 / 17 / 20 | 20 |

A ground array of water-Cherenkov tanks with fluorescence telescopes *is* Auger: there is no other instrument of its class at that scale. Even ABS, with invented materials, keeps the hybrid-array decision structure. In the identification probe, where no upgrade is asked for, Opus 5.5 volunteers AugerPrime in every twin response.

## Consequence: the identification gate as specified cannot be met on the pilot pairs

Two of two pilot pairs fail the ≤ 10% gate at every disguised level on the strongest model, and one fails it on all models. If the gate is kept as a hard filter, the confirmatory item set would shrink to non-unique instruments, which biases the set toward generic technologies and away from the instruments the paper is about.

**Proposed redesign (recorded 2026-11-05; adopt before the confirmatory freeze):**

1. **Primary estimand → the override test (H3) on conflict twins, with recognition measured, not gated.**
   - A model that recognizes the instrument ("modelled on T2K") but is told physics under which the adopted choice fails, and still proposes the adopted choice, is showing recall overriding physics. Recognition is not a confound for this test; it is the channel the test is about.
   - Compare the override rate for the adopted item with the same-response rate of salient distractors, and condition on constraint knowledge K (design v2 §3).
2. **The instance-recall ladder (ANON vs EQ) is demoted to secondary.** It is analysed as a dose–response of proposal rate on *measured* recognition (H4), across models and levels. Where recognition is near 100% on every level, IR is not identifiable, and the paper says so per pair.
3. **Report recognition itself as a finding.** Recognition rates by model and level, including spontaneous naming of the adopted upgrade, quantify how far disguise fails. This extends the companion study's "no anonymous description" result to deliberately constructed twins and abstract twins.
4. **The causal injection arm (fictional instruments, no recognition possible) and the prospective registry gain weight.** They are the designs that do not depend on disguise.
