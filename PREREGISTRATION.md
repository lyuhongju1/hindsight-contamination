# Pre-registration: Recalled history overriding stated physics in AI detector design

**Status: FROZEN v4.3** (2026-11-06). It is frozen by the public commit that adds `FREEZE_MANIFEST.md`, which holds SHA-256 hashes of this file and of every material, rubric, regex, template and script. That commit precedes any confirmatory upgrade or identification sampling. v4.3 changed H1 multiplicity and the item count under Amendment A3, before any confirmatory sampling. A git tag `prereg-v4.3-frozen` is added if permitted. Later changes require dated amendments. It becomes binding when tagged `prereg-v4.2-frozen` in the public repository `github.com/lyuhongju1/hindsight-contamination`. That tag is created after the item set and materials are complete and **before any confirmatory sample is drawn**. After the freeze, changes are made only by dated amendments committed before they take effect.

**Route.** Public pre-registration with a timestamped git tag, not a journal Registered Report (PI decision 2026-11-06, for minimal PI involvement). A Zenodo snapshot may be added at the freeze.

**Basis.** Design v2 → v3 (solo operation) → v4/v4.1 amendments; the pilot (`pilot/PILOT_SUMMARY.md`, findings F1–F11). This document consolidates and supersedes them for the confirmatory study.

---

## 1. Question

When a language model is asked to design an upgrade for an instrument whose history it may know, does it propose the **historically adopted** technology even when the description states physics under which that technology fails, and when the same model, asked directly, knows that it fails? We call this **override**: recalled history overriding stated physics.

**What the study measures, and what it does not.** It measures override behaviour. It does not measure training-data provenance, and it makes no causal claim about memorization (no injection arm; v3 §8). Recognition of the real instrument is **measured, not gated** (pilot F1, F2, F4).

---

## 2. Units, items and materials

### 2.1 Pairs

- **Count:** target 14 and minimum 10 in v4.2. **Achieved: 6 units-bearing pairs** after 21 pairs were worked; supply stopped under Amendment A3 (`search/AMENDMENT_A1.md`). The funnel (21 worked, 15 zero-unit, with reasons) is reported as a primary descriptive result.
- **Selection:** by the frozen mechanical procedure in `pair_selection_rules.md` (INSPIRE frame, criteria I1–I6, field caps, seeded draw), with screening and dating by agents plus scripts (v3 §§5–6).
- **Excluded:** the two pilot pairs (T2K ND280, Auger).

### 2.1a Achieved units (v4.3)

| Unit | Baseline → programme | Adopted item | adoption_status (covariate) |
|---|---|---|---|
| p01 | XENON1T → XENONnT | Liquid-phase Xe purification | built and operated |
| p02 | GERDA Phase II → LEGEND-1000 | Underground-sourced argon | approved, not built (unverified) |
| p03 | Advanced Virgo → AdV+ | Frequency-dependent squeezing via an external filter cavity | built and operated (unverified) |
| p05 | SNO → SNO+ | LAB liquid scintillator | built and operated |
| p09 | NEMO-3 → SuperNEMO | 8-in. high-QE PMT calorimeter modules | built and operated (unverified) |
| p10 | Borexino → SOX | 144Ce-144Pr antineutrino source | cancelled |

Each has one CONF (CONF1). Rubrics: `materials/<pair>/RUBRIC.md`.

**K premise check (run 2026-11-06, `data/conf_kpremise/`):** p10_borexino/CONF1 is **suspended** (2 models majority-wrong; see the results file for the nature of the dissent). **Confirmatory units: 5** (p01, p02, p03, p05, p09). Haiku 5.5 is K-gated out of p03. Power at 5 units for the first fixed-sequence test: 0.80–0.86 at O = 0.24 (τ = 0.5).

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

**Snapshot IDs** (confirmed available via the API model list, 2026-11-06):
- `claude-sonnet-4-5-20250929`
- `claude-haiku-4-5-20251001`
- `claude-opus-4-5-20251101`
- `claude-sonnet-4-6`
- `claude-haiku-5-5`
- `claude-sonnet-5-5`
- `claude-opus-5-5`

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
- **Multiplicity (v4.3): fixed-sequence (hierarchical) testing at α = 0.05.**
  - **Order.** Models are tested in this pre-specified order, and testing stops at the first non-rejection:
    1. Sonnet 4.5
    2. Haiku 4.5
    3. Opus 4.5
    4. Sonnet 4.6
    5. Haiku 5.5
    6. Sonnet 5.5
    7. Opus 5.5
  - **Basis for the order** (fixed before any confirmatory data):
    - the pilot override rates on separate pilot pairs: Sonnet 4.5 22–26%, Sonnet 4.6 6–8%, Opus 5.5 0%;
    - the pilot trend that newer and larger models override less;
    - unpiloted models placed by generation, oldest first, Haiku before Opus within a generation.
  - Family-wise error stays ≤ 0.05.
  - Models after the first non-rejection are reported descriptively, with Holm-adjusted p-values, as secondary.
- **Why v4.3 changed this.** With 6 units, Holm across 7 models leaves the first test at α = 0.05/7, where power is about 0.4 (`power/power_small_J_results.md`). Fixed sequence gives the first model the full α.
- **Power at 6 units, first test, α = 0.05** (`power/power_small_J_results.md`):
  - between-unit SD τ = 0.5: 0.89–0.94 at O = 0.24, and 0.99–1.00 at O = 0.30;
  - τ = 1.0: 0.53–0.55 at O = 0.24;
  - the type I rate is ≤ 0.025 (the test is conservative).
- **Secondary (pre-specified):** the pooled marginal override rate across all models and units against 0.10 (unit-level means over models, t-test across units). This is reported, not part of the confirmatory family.
- **K gating** may drop units for some models. A model left with < 4 included units is reported descriptively, and its position in the sequence counts as a non-rejection.

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
- With 6 units, H1 is run as specified in §6 (v4.3) and reported with the achieved power above. Any model's test with fewer than 8 included units carries the label "small unit count".

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
