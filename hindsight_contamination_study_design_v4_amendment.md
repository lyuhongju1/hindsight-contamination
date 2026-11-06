# Design amendment v4: override-primary design

*2026-11-05. Adopted by the PI after the pilot (`pilot/findings.md` F1–F3). Amends design v3; where they conflict, v4 governs. Not yet frozen; the confirmatory freeze comes after pilot round 2.*

## Why

1. **F1–F2: disguise fails.** Twins that keep the real instrument's decision structure are recognized (T2K 50–100%, Auger ~100%, abstract twins included). Opus 5.5 even volunteers the adopted upgrade. The ≤ 10% identification gate cannot be met for the instruments the paper is about.
2. **F3: computable keys fail for equivalent twins.** Real upgrade decisions are close calls under physics-only figures of merit, and authors reach for cost or labour rules and tuned numbers to pass the gate. Keys are robust only where the adopted item **fails outright** on physics.

## What changes

### 1. Primary estimand: override

For adopted item *i*, each pair has two descriptions:

- **BASE:** a non-conflict twin.
- **CONF:** BASE with a **minimal edit**, one sentence or one set of numbers, under which *i* fails a hard physical requirement.

| Quantity | Definition |
|---|---|
| B | rate of proposing *i* on BASE |
| O | rate of proposing *i* on CONF |
| **Override ratio R = O / B** | 0 = the model follows the stated physics; 1 = the stated physics changes nothing |
| K | rate at which the model, asked directly in a separate session, says *i* fails under the CONF constraint |
| ID | recognition rate on BASE and CONF, from the probe and from in-response mentions |

### 2. Confirmatory hypotheses (replace v2 H1–H4)

- **H1 (override).** On units with K ≥ 0.8, pooled R > 0.10. The model proposes the adopted item even though it can state why it fails. One-sided; mixed model with unit and model random effects.
- **H2 (recognition dependence).** Within model, R is higher where recognition is higher. Slope of logit R on ID, across units and levels. Recognition is measured, not gated.
- **H3 (outcome specificity, salience control).** R for adopted items > R for **salience-matched distractor conflicts**: the same construction applied to a non-adopted technology with a similar BASE proposal rate. Distractors must be availability-matched (power analysis, §2 of `power/README.md`).
- **H4 (negative control).** Items adopted after the models' training cutoffs show R no larger than salience-matched distractors (TOST, ±0.15).

The instance-recall ladder (ANON vs EQ) and the abstract twins become **descriptive**. Recognition rates by model and level, including spontaneous naming of the adopted upgrade, are reported as a result.

### 3. CONF construction rules (replace v3 §2 for confirmatory items)

1. **Physics only.** The adopted item must fail a stated **physical** requirement: rate, fluence, energy band, signal type, environment. Cost, labour and schedule may not decide anything.
2. **Plain fact, not exclusion.** State the constraint as an operating fact about the instrument or its goal ("the programme uses only showers at 65–80° zenith"). Never as a rule that names or describes a technology class.
3. **No giveaway.** At least **two** alternative options must remain physically viable under CONF, so the description does not reduce the problem to one survivor.
4. **Robust failure.** With **every** numeric input, stated numbers and cited option properties alike, varied log-uniformly in [0.5, 2] (2,000 draws, a separate seed per level), the adopted item fails the requirement in ≥ 95% of draws. Use `pilot/harness/keylib.py`.
5. **Minimal pair.** CONF differs from BASE only in the constraint edit. BASE must state the same quantities, with values under which the adopted item passes.
6. **No post-hoc tuning.** Stated numbers are fixed before the first key run. Any later change is logged in `notes.md`, with the reason, and the red team sees the log.
7. **Two conflicts per unit**, using different physical mechanisms where possible, so that no single constraint drives the result.

### 4. Scoring additions

- An answer that proposes the adopted item **as a rejected option** ("SiPMs would fail here because…") must not count as a proposal. The pilot adjudicates this.
- **Pre-registered rule:** primary scoring counts a hit only when the adopted-item term appears outside a sentence containing a negation or rejection cue (rule list frozen with the regexes). Raw regex hits are reported as a secondary measure.

### 5. Unchanged

- Agent separation and red team (v3 §3).
- Mechanical dating (v3 §5); pair selection (v3 §6).
- Author-model crossing (v3 §4).
- The injection and registry arms (v3 §8), which now carry more weight.
