# Pre-registration, Study 2: prospective replication on new units

*Status: DRAFT (2026-11-07). Written after the Study 1 results (`RESULTS_SUMMARY.md`) and before any Study 2 unit is selected, authored or sampled. It becomes binding when frozen by a public commit adding `FREEZE_MANIFEST_S2.md`, before any Study 2 upgrade sample. Later changes require dated amendments.*

## 1. Why a Study 2

Study 1 (PREREGISTRATION v4.3) found override rates of up to 50/50 on some units and near 0 on others. Its average-based H1 was not rejected, with 5 units (p = 0.099). Study 2 tests, on **new units only**, hypotheses chosen in light of that heterogeneity:
- the *existence* of override per model (primary);
- the average rate (secondary, GLMM);
- model differences (replication).

Study 1 units, materials and data are excluded from every Study 2 confirmatory test.

## 2. Units

- **Frame and order.** The remaining entries of the frozen assessment queue (`search/assessment_queue.json`, positions 39–81), in queue order, under Amendment A1 and its addenda.
  - **Lineage rule (A1 addendum 2).** No lineage already used in Study 1 is re-entered, including Study 1 zero-unit lineages. This skips q41 CUPID-Mo, q42 LIGO 2003, q44 IceTop, q47 aLIGO, q53 KASCADE-Grande and q64 BES. Duplicate records of one experiment are skipped after the first (BaBar q57/q81, ATLAS q62/q72, COMPASS q61/q70).
- **Eligibility.** Two independent daters plus `verify_dating.py`; both daters must agree on the item (unchanged).
- **Feasibility before authoring.** An author agent runs the lesson-5 feasibility check (AUTHOR_BRIEF, including clarification C1).
  - This may precede the second dater (an efficiency reordering).
  - The selected set is the **first eligible-and-feasible baselines in queue order**; the population is the same as A2/A3: pairs whose counted item admits an honest physics-only conflict.
- **Materials.** Unchanged pipeline: author (AUTHOR_BRIEF rules 1–10, lessons, C1), keylib ×0.5–2, red team until no open FIX, gates.
- **Per-field cap within Study 2:** 3 units.
- **Count.** Target **12** units, minimum 6. Supply stops at 12 or at frame exhaustion. If fewer than 6, Study 2 is reported descriptively.
- **K premise check.** As in Study 1 §2.4: a CONF is suspended if ≥ 2 of the 7 models are majority-wrong. Per-model K gating applies.

## 3. Models, elicitation, scoring

As in Study 1:
- **Models:** the same 7 snapshot IDs.
- **Templates:** the 5 `upgrade_final` templates, n = 10 each (50 per description × model).
- **Levels:** BASE, CONF1, ANON and NAME; identification probes n = 20.
- **Truncation:** the §7 rule.
- **Screen:** the frozen per-pair regex on the TOP RECOMMENDATION line.
- **Adjudication:** blind cards; two non-study adjudicators (`claude-fable-5-1`, `claude-opus-4-8`; `analysis/adjudicate.py`). Every screen hit plus min(10, available) random non-hits per CONF × model.
- **Override** = both adjudicators code A or B.
- **Rubrics:** per pair, frozen before sampling, including pair-specific C cases.

## 4. Hypotheses and tests

The fixed model order for sequential testing, by Study 1 mean O (descending):
1. Sonnet 4.5 (0.428)
2. Sonnet 4.6 (0.312)
3. Opus 4.5 (0.308)
4. Haiku 5.5 (0.190)
5. Haiku 4.5 (0.176)
6. Sonnet 5.5 (0.164)
7. Opus 5.5 (0.008)

### H1-S2 (primary): existence of override, per model

For model m, at least one included unit has O_mj > 0.10.
- **Per-unit test:** one-sided exact binomial test of k_mj of n_mj = 50 against 0.10.
- **Within model:** Holm correction across that model's included units (family-wise α = 0.05 within the model).
- **Across models:** fixed-sequence testing in the order above at α = 0.05. A model is "rejected" if at least one of its units survives Holm. Testing stops at the first model with no surviving unit.
- **Sensitivity (pre-specified):** a template-cluster quasi-binomial version, with the dispersion estimated from the 5 template proportions within the cell and the variance inflated if the dispersion exceeds 1.
- **Reported with each rejection:** the number and identity of a model's significant units, as a share of its included units.

### H2-S2 (secondary confirmatory): average override, per model

The marginal override rate across units exceeds 0.10.
- **Test:** binomial GLMM with a unit random intercept; one-sided likelihood-ratio test against the marginal rate fixed at 0.10 (implementation as `analysis/exploratory.py`, E4).
- **Multiplicity:** fixed sequence in the same order, α = 0.05, as a separate family.
- **Sensitivity:** the Study 1 t-test on unit-level proportions.

### H3-S2 (secondary confirmatory): models differ

LR test of the model effect in the binomial GLMM with a unit random intercept (as Study 1 H2), α = 0.05.

### Exploratory (labelled)

- **Conditional persistence:** override in cells where the model adopts the item at BASE (both adjudicators P) in ≥ 30/50;
- knowledge–override dissociation;
- recognition;
- recall traces;
- templates;
- leave-one-unit-out;
- a pooled Study 1 + Study 2 analysis (never confirmatory).

## 5. Power (pre-specified reasoning)

- **H1-S2** with 50 draws per cell: a cell at 13/50 gives a one-sided binomial p ≈ 0.003, which survives Holm across 12 units (0.05/12 ≈ 0.0042). Study 1 showed per-model maxima of 14–50/50 among units where the model favours the item. Power for H1-S2 is therefore high whenever a model has a single strongly overridden unit, and it is not reduced by heterogeneity across units.
- **H2-S2** is sensitive to between-unit heterogeneity (Study 1 unit SD ≈ 1.3 on the logit scale) and is expected to be underpowered below about 10 units. That is why it is secondary.

## 6. Disclosure

Study 2's hypotheses were chosen after seeing Study 1. Its confirmatory status rests on new units and new samples, fixed before selection. The paper reports both studies, the full funnel and every amendment.
