# Pre-registration: Recalled history overriding stated physics in AI detector design

**Status: DRAFT v4.2** (2026-11-06). It becomes binding when tagged `prereg-v4.2-frozen` in the public repository `github.com/lyuhongju1/hindsight-contamination`. That tag is created after the item set and materials are complete and **before any confirmatory sample is drawn**. After the freeze, changes are made only by dated amendments committed before they take effect.

**Route.** Public pre-registration with a timestamped git tag, not a journal Registered Report (PI decision 2026-11-06, for minimal PI involvement). A Zenodo snapshot may be added at the freeze.

**Basis.** Design v2 → v3 (solo operation) → v4/v4.1 amendments; the pilot (`pilot/PILOT_SUMMARY.md`, findings F1–F11). This document consolidates and supersedes them for the confirmatory study.

---

## 1. Question

When a language model is asked to design an upgrade for an instrument whose history it may know, does it propose the **historically adopted** technology even when the description states physics under which that technology fails, and when the same model, asked directly, knows that it fails? We call this **override**: recalled history overriding stated physics.

**What the study measures, and what it does not.** It measures override behaviour. It does not measure training-data provenance, and it makes no causal claim about memorization (no injection arm; v3 §8). Recognition of the real instrument is **measured, not gated** (pilot F1, F2, F4).

---

## 2. Units, items and materials

### 2.1 Pairs

- **Count:** target **14** baseline–upgrade pairs; minimum **10**.
- **Selection:** by the frozen mechanical procedure in `pair_selection_rules.md` (INSPIRE frame, criteria I1–I6, field caps, seeded draw), with screening and dating by agents plus scripts (v3 §§5–6).
- **Excluded:** the two pilot pairs (T2K ND280, Auger).

### 2.2 Unit

One **conflict twin** (CONF) of a pair whose adopted item **a**:

- passes the matched **BASE** twin;
- fails a stated physical requirement in CONF.

Up to two CONFs per pair, each from a different mechanism.

### 2.3 Construction rules (all must hold; checked by `pilot/harness/keylib.py` v4.1 and a red team)

1. **Physics only.** No cost, labour or schedule may decide anything.
2. **Plain fact, never exclusion wording.**
3. **≥ 1 credible survivor**, coded against every stated fact. The survivor count is recorded as a covariate.
4. **Robust failure of a.** Every cited property is varied ×0.5–2 (2,000 draws, per-level seed); a fails in ≥ 95% of draws.
   - Exact stated facts and integer structural counts may be held fixed, with a justification.
   - Tighter ranges for a property only with a cited precision, and never narrower than ×0.8–1.25.
   - All quantities on linear scales; no booleans.
5. **Minimal pair.** CONF differs from BASE only in the conflict edit.
6. **No post-run tuning without a logged reason**, reviewed by the red team.
7. **Scenario coherence**, with every side effect of the edit checked.
8. **Close workaround routes that defeat a stated requirement**, where possible, by plain facts.
9. **Red-team verdict OK** on BASE and CONF. Every FIX is resolved before the freeze.

### 2.4 K premise check (pilot F9, F10)

Each CONF has a constraint-knowledge question (**K-probe**), stated without instrument context and ending with a forced `VERDICT: YES/NO` line.

- It is run on every confirmatory model before the freeze, **without any upgrade sampling on the confirmatory items**.
- A CONF is **suspended** (excluded from confirmatory tests) if, on ≥ 2 models, the majority verdict contradicts the key's expected answer. Suspended CONFs are reported.

### 2.5 Other descriptions per pair

- **ANON** (real instrument, unnamed) and **NAME** (real, named), both descriptive.
- Pilot pairs and abstract or equivalent twins are not part of the confirmatory set.

---

## 3. Models

**Confirmatory set (7 Anthropic models), with snapshot IDs recorded at the freeze:**

| Generation | Models |
|---|---|
| 4.5 | Haiku 4.5, Sonnet 4.5, Opus 4.5 |
| — | Sonnet 4.6 |
| 5.5 | Haiku 5.5, Sonnet 5.5, Opus 5.5 |

**Non-Anthropic models.** If the PI provides a gateway key before the freeze, ≥ 1 non-Anthropic frontier model is added to the confirmatory set. Otherwise the paper states that it is a single-vendor study.

**Settings:**

- temperature 1.0;
- minimum reasoning each model allows (low-effort adaptive where it cannot be disabled; disclosed);
- 16k output cap;
- stop reasons logged;
- all sampling for one model within one 4-week window.

---

## 4. Elicitation

**Upgrade task.**
- 5 frozen templates (`pilot/templates.json`, `upgrade_final`), each ending with: `TOP RECOMMENDATION: <the single hardware change you consider most important>`.
- **n = 10 per template**, so 50 responses per description per model.
- Descriptions sampled: BASE, every CONF, ANON, NAME.

**Probes.**
- Identification probe: n = 20 per description per model.
- K-probe: n = 20 per CONF per model.
- Each probe runs in a separate session.

---

## 5. Scoring

1. **Screen.** A frozen per-pair regex for **a**, applied to the TOP RECOMMENDATION line.
2. **Adjudication.** Every screened hit, plus 10 random non-hits per CONF × model, is adjudicated blind by **two independent adjudicator agents**.
   - Model identity is hidden by hashed IDs.
   - Compact cards: final line plus relevant sentences.
   - A per-pair rubric is instantiated from the frozen template (codes A–E, X; see `pilot/adjudication/*/RUBRIC.md`) and frozen before sampling.
   - **A rubric category C (valid workaround) is defined per CONF before sampling** (pilot F8, F11).
3. **Override.** A response counts as override **only if both adjudicators code A or B**. Disagreements are reported, and a sensitivity analysis counts them as override.
4. **Agreement.** Model–model κ is reported as such, **not** as human inter-rater reliability.
5. **Identification:** frozen identity regex (names of the baseline or successor). **K:** the VERDICT line.

---

## 6. Hypotheses and tests

**Unit of analysis:** CONF unit. **O_mj** = override proportion for model *m* on unit *j* (out of 50).

### H1 (confirmatory, per model)

The marginal override rate across units exceeds 0.10.

- **Test:** one-sided t-test of unit-level O_mj against 0.10, cluster = unit. A binomial GLMM with a unit random effect is fitted as a sensitivity analysis.
- **Inclusion:** only units whose CONF passed the K premise check, and, per model, only units where that model's K majority verdict is correct. This ensures the model knows the physics it overrides.
- **Multiplicity:** Holm correction across the confirmatory models, α = 0.05.
- **Power** (`power/power_override_results.md`): 12 units gives 0.92–1.00 at O = 0.24 and 0.57–0.92 at O = 0.18; the test is conservative (type I ≤ 0.035).

### H2 (confirmatory)

Override rates differ across models.

- **Test:** likelihood-ratio test of the model fixed effect in a binomial GLMM, with a unit random effect, on all included model × unit cells.

### Exploratory (reported as such)

- the relationship between recognition and override (two-sided; pilot F8);
- scale and generation trends;
- BASE rates and R = O/B (descriptive only, because R is ill-behaved when B is small; pilot F11);
- K-gated versus ungated override;
- per-template variation;
- the fallback-to-history pattern (F11);
- qualitative analysis of category-A misstatements.

---

## 7. Stopping and exclusion rules

**Item supply.**
- If fewer than 10 units pass §2.3–2.4 before the freeze, the study proceeds with the units available.
- H1 is reported with the achieved power and is labelled underpowered if fewer than 8 units remain.

**Sampling quality.**
- Responses lacking a TOP RECOMMENDATION line are treated as X: they are excluded from the numerator and reported.
- If more than 1% of a cell is truncated at the cap, the cell is resampled once at double the cap.

**No other exclusions.**

---

## 8. Materials and openness

The following are released in the repository and frozen at the tag:

- the pair-selection logs;
- dating and verification output;
- all descriptions, keys and key outputs;
- red-team reports;
- K-probes;
- templates, regexes and rubrics;
- harness code;
- every agent brief.

Raw responses, adjudication cards and labels are released after collection.

**Conduct disclosure** (v3 §9): every material, key, date, screening decision, adjudication and analysis was produced by Claude agents under this protocol. The PI designed the question, approved the protocol and is accountable for the paper.
