# Measuring Hindsight Contamination in AI-Assisted Detector Design — v2

*Revised study design for a **standalone paper on hindsight contamination**, 2026-11-04. Supersedes v1 (`hindsight_contamination_study_design.md`, kept unchanged in this folder). Draft, not pre-registered.*

*The companion paper measured availability and was criticized for claiming hindsight it had not measured. This paper's job is to measure hindsight directly. Section 14a applies the companion study's referee report to this design in advance.*

*Companion study: "When Is Agreement with History Evidence? Measuring the Availability of Adopted Upgrades in Language Models for Particle Detector Design" (V3 manuscript in `Downloads\APS Open RR\`; data at `github.com/lyuhongju1/LLM_contamination`).*

v2 keeps v1's core idea, synthetic twins plus training-data exposure. It changes the design wherever the companion study, its referee report, or its revision showed that a v1 step would not hold up. Section 14 maps each change to the lesson behind it.

---

## 1. The question

The companion study measured **availability**: how often a bare model proposes each historically adopted upgrade. It did not measure **provenance**. A high proposal rate is compatible with four mechanisms, not three as v1 assumed:

| # | Mechanism | What the model is drawing on |
|---|---|---|
| M1 | **Outcome recall (instance)** | It knows what *this* collaboration adopted |
| M2 | **Plan recall (instance)** | It read this program's pre-baseline LoI or design report (13 of 26 items predate their baselines) |
| M3 | **Class-level recall / salience** | It knows what *instruments of this kind* tend to adopt, or what the literature talks about most, without recognizing the instance |
| M4 | **Reasoning** | It derives the choice from the stated physics |

v1 treated a high rate on an equivalent twin as evidence of reasoning (M4). That inference fails because a twin removes the instance but not the class. A twin liquid-argon TPC still sits in a literature where liquid-argon TPCs moved to SiPMs. The companion study's distractor result shows that M3 is real: SiPMs were proposed for the xenon dark-matter TPCs in 96 percent of samples, although those programs did not adopt them.

**Hindsight contamination in the strict sense is M1.** This study aims to:

- separate instance-level recall (M1 + M2) from everything else, using twins;
- separate class-level salience (M3) from reasoning (M4), using conflict twins, abstract twins and distractor controls;
- separate outcome (M1) from plan (M2), using dated exposure in open-data models and a controlled injection experiment.

**Core question.** For each answer-key item and each model, what share of the proposal rate depends on the model recognizing the instrument, and, of the part that does not, how much survives when the physics argues against the historical choice?

### 1.1 What the paper is allowed to claim

The companion paper's referee objected that its title said "hindsight contamination" and its abstract said "the memorized future", while the paper had measured only availability (point 5). This paper fixes in advance which claim each result licenses. The title and abstract use the highest rung that the confirmatory tests support, and no higher.

| Rung | Claim | Required evidence |
|---|---|---|
| 0 | The adopted answer is **available** | Already shown by the companion study; not a result here |
| 1 | Availability **depends on recognizing** the instrument | IR > 0, and the slope on identification > 0 (H4) |
| 2 | The dependence is **specific to what was adopted** | DiD > 0 against distractors, on post-baseline units (H1) |
| 3 | Recall **overrides stated physics** | O > 10% where K ≥ 80% (H3) |
| 4 | Outcome exposure **causes** proposals | Arm 2b dose–response, with outcome > plan |

Rungs 1–3 are observational evidence from frontier models; rung 4 is causal but comes from a small open model. The phrase "hindsight contamination" is used for a frontier model only if rung 2 holds on it, and the word "memory" is used only together with rung 4. If the tests fail, the paper reports that hindsight contamination was **not** detected, with equivalence bounds. That is itself publishable, since it would mean agreement with history reflects the backbone's design ability.

---

## 2. The recognizability ladder (core design element)

Every pair is presented at several levels that hold the design problem fixed and progressively remove access to history. All levels use **identical templates**; only the instrument description changes.

| Level | Code | Content | History accessible via |
|---|---|---|---|
| 0 | **NAME** | Real description, experiment named | M1–M4 |
| 1 | **ANON** | Real description, no names (like the companion study's condition D) | M1–M4, if recognized |
| 2 | **TWIN-EQ** | Invented instrument from the same class. Surface and instance features (names, site, mass, geometry within expert-approved ranges) are perturbed, and the correct upgrade is unchanged. **3 per pair** | M3, M4 |
| 3 | **TWIN-ABS** | Abstract twin: the decision structure is kept, but materials and technologies are described only by invented names with stated properties, so that no real class is recognizable (where constructible) | M4 mainly |
| C | **TWIN-CONF** | Conflict twin: one physical constraint is changed so that the historical choice becomes wrong or clearly inferior, and the experts' answer differs from history. **1–2 per targeted item** | Tests M3 against M4 |

Predictions:

- **Pure reasoning (M4):** flat rates across levels 0–3, and low on CONF.
- **Instance recall (M1/M2):** a drop between ANON and TWIN-EQ that tracks identification rate.
- **Class salience (M3):** high through TWIN-EQ, a drop at TWIN-ABS, and high on CONF.
- **Contamination by outcome specifically:** the ANON → TWIN-EQ drop is larger for adopted items than for matched distractors (section 4).

The ladder converts v1's single contrast into a dose–response. Recognizability can be measured at every level (section 5), so the analysis can test whether proposal rate tracks identification within an item while the physics is held fixed.

### 2.1 Example constructions (illustrative only; the expert panel decides)

- **DarkSide-50 → SiPM, conflict.** A cryogenic noble-liquid TPC in a high-neutron-fluence environment over a long exposure, where SiPM radiation damage (dark-count growth) is disqualifying and PMTs are not affected.
- **aLIGO → frequency-dependent squeezing, conflict.** An interferometer whose target band is thermal-noise-limited at every frequency, so quantum-noise reduction buys nothing and the filter cavity is pure cost.
- **Abstract version of the photosensor choice.** "Medium X scintillates at λ = … nm at T = … K; sensor family P has properties …; sensor family Q has properties …". The property values are deliberately chosen not to match any real medium.

---

## 3. Estimands

For item *i*, model *m*, and level *L*, p_L(i, m) is the proposal rate pooled over templates.

| Quantity | Definition | Reads as |
|---|---|---|
| **Instance-recall component** | IR = p_ANON − p_TWIN-EQ | What recognizing the instrument adds |
| **Name component** | NR = p_NAME − p_ANON | What an explicit name adds beyond recognizable description |
| **Abstraction drop** | AD = p_TWIN-EQ − p_TWIN-ABS | Class-level knowledge beyond stated physics |
| **Override rate** | O = rate of proposing the historical choice on TWIN-CONF | Salience or recall that defeats physics |
| **Constraint knowledge** | K = rate at which the model, asked directly, says the historical choice fails under the conflict constraint | Whether override is ignorance or override |
| **Outcome-specific contamination (primary)** | DiD = IR(adopted) − IR(matched distractor) | Recognition benefit specific to what was *adopted* |
| **Identification rate** | ID_L = rate of naming the real baseline or successor at level L (section 5) | Covariate and gate |

**Why the DiD is primary.** Recognition can raise the rate of anything associated with an instrument, including roads not taken. Distractors were never adopted, so outcome recall cannot raise them. Recognition effects common to both cancel in the difference. The companion study's 20 frozen, leakage-audited distractors (two per pair) are reused here, so they are fixed before any new data.

**Override is interpretable only together with K.** If the model *knows* the historical choice fails under the stated constraint (high K) and proposes it anyway (high O), that is salience or recall overriding stated physics. If K is low, the model lacks the physics, and O says nothing about contamination.

---

## 4. Arm 1: Synthetic twins and the ladder

### 4.1 Item set

Hindsight is about knowing what happened *after* the baseline. The companion paper's referee pointed out that its items were not dated, and that many were not "future" at all (point 1). Its own dating table later found only 8 of 26 items to be post-baseline, from 5 pairs. A paper about hindsight therefore builds its item set the other way round: dating comes first, and the post-baseline items are the primary stratum.

- **Primary stratum: post-baseline units.** The first public adoption commitment is ≥ 2 years after the baseline's first arXiv submission.
  - Source 1: the companion study's 8 post-baseline items.
  - Source 2: **new pairs**, enough to reach **≥ 28 post-baseline units from ≥ 14 pairs** (power analysis, §9.3), chosen across fields.
  - Freeze the selection rules (field coverage, commitment gap, a constructible conflict constraint, and dating sources) **before** querying any model on new pairs.
  - Date each new item with the companion study's rule and an independent re-check, before sampling. Items whose dates are uncertain go into an "indeterminate" class and are left out of the primary stratum.
- **Comparison stratum: pre-baseline units.** These are the companion study's 13 pre-baseline items. For them, outcome and plan cannot be told apart, so they serve as the plan-recall comparison: H1's DiD should be **larger** on post-baseline units than on pre-baseline ones if outcome knowledge matters beyond the documented plan.
- **Contemporaneous items** are reported but enter no confirmatory test.
- **Units.** Related items count as one unit in every headline number, for example the two SiPM items, and squeezing with its filter cavity (referee point 4). Inference counts pairs as well as units, since items from one pair are not independent.
- **Reporting.** Show the full distribution over every unit in every cell. Exemplar tables are labelled as selected, and the headline numbers never come from them (point 4).

### 4.2 Roles and blinding

The companion study's condition D was written by the author, simultaneously with the answer keys, and not blind. v2 separates the roles:

| Role | Who | Blind to |
|---|---|---|
| Twin authors (≥ 2 physicists) | Not the PI | Which models are tested; any model output |
| Expert key panel (5 per field) | Different people from the authors | Which twins are real-derived vs fillers; history where possible |
| Analyst | PI | Condition labels until the analysis script is frozen (section 9.4) |

**Twin development rule.** During construction, twins may be iterated against the **identification probe only**. Nobody looks at upgrade proposals on any twin until the full set is frozen and deposited.

### 4.3 Validating twins (all three gates are pre-registered)

1. **Expert answer key.** Each panelist first writes an open-ended top-3 upgrade list for the twin, then rates a candidate list that includes the historical choice, the keyed alternative, and the pair's distractors. Panelists see real-derived twins mixed with filler problems.
   - Inclusion: ≥ 4 of 5 panelists rate the keyed answer as the best or a co-best option.
   - Conflict twins additionally need ≥ 4 of 5 rating the historical choice as wrong or clearly inferior.
   - Report Fleiss' κ, and report expert–history agreement on ANON as a measure of how much the experts themselves are anchored on history.
2. **Non-identifiability** (section 5). A twin enters only if ID ≤ 10% on **every** model in the primary set. Per-model inclusion is a secondary analysis.
3. **Leakage audit, two layers.**
   - Text: the frozen regex audit, as in the companion study.
   - Content: an independent reader checks whether the description implies the answer without naming it. The companion study's text-only audit missed the GERDA argon and VeloPix content leakage.
   - Twins failing either layer are revised before freeze, never after sampling.

### 4.4 Conditions per pair

Per pair: NAME, ANON, 3 × TWIN-EQ, TWIN-ABS where constructible, and 1–2 TWIN-CONF per targeted item. This gives about 8 descriptions. Every description is crossed with every template.

- **The full baseline paper is excluded from the primary design.** The companion study showed that the paper both triggers and *anchors* (10 of 52 A−D cells were significantly negative). Including it would contaminate every ladder contrast with anchoring.
- **Optional secondary arm:** the paper condition on NAME only, for linkage to the atlas.

### 4.5 Constraint-knowledge probe

For each conflict twin, a short probe with N = 20 per model: "Under [constraint], would [historical technology] be a good choice? Explain."

The probe is scored for whether the model identifies the failure mode. It runs in a **separate session** from the upgrade prompts, so it cannot prime them.

---

## 5. Measuring recognizability

The companion study found that a unique instrument has no anonymous description: Sonnet 4.6 named LEGEND in 95% of samples from six words. Identification is therefore measured, not assumed.

- **Direct probe**, run before sampling: "Does this describe a real experiment? If so, which?" N = 20 per description per model. This gives ID_L and is used for the gate.
- **In-response mentions:** scored with the frozen successor and baseline patterns on the main responses.
- **Secondary only.** Subsetting main responses on whether they name the instrument conditions on a post-treatment variable, so it is labelled exploratory, as the companion study did in revision.
- **Primary use of ID:** a covariate in the dose–response analysis (section 9). The prediction for instance recall is that within an item, p rises with ID across levels 0–2.

---

## 6. Arm 2: Training-data exposure (open-data models)

### 6.1 Arm 2a: Natural exposure

Models: the largest open-data models with released corpora, intermediate checkpoints and data order. Candidates include the OLMo family with infini-gram and OLMoTrace; verify current releases at registration.

**Go/no-go gate (pre-registered).** The companion study found weak availability on open-weight models: Qwen2.5-72B kept generic defaults but not named items. Before committing, pilot the open model on ANON for all pairs.

- **Go** if ≥ 6 items reach ≥ 30%.
- **No-go:** Arm 2a is reported as a floor result, and resources move to 2b.

Exposure counts per item:

- generic frequency of the technology;
- paired frequency of the technology with the instrument or successor;
- each paired document classified by date against the dating table (pre-baseline, contemporaneous, post-baseline).

Counts are lower bounds. A random sample of 50 matched documents per item is checked by hand.

Analyses:

1. **Checkpoint analysis (primary for 2a).** Locate the training step at which paired documents enter, and test for a rise in p_ANON (and in IR) after that step against p_TWIN-EQ. Run the twins on the open model too, so that the ladder and exposure measure the same thing.
2. **Cross-item regression (secondary).** With roughly 30 items this is underpowered. Report it as descriptive with intervals and do not test it as a hypothesis.
3. **Plan vs outcome.** Proposal rates against pre-baseline vs post-baseline paired exposure.

### 6.2 Arm 2b: Controlled injection (new; replaces v1's date-truncated training)

**Idea.** Natural exposure is observational. Controlled exposure is causal. Continue pretraining an open checkpoint on a background corpus into which synthetic documents about **fictional** instruments have been inserted.

Design:

- 12–20 fictional instruments, each a fictional baseline plus a fictional upgrade path.
- **Dose:** 0, 1, 10, or 100 paraphrased documents per instrument.
- **Document type:**
  - *plan* documents ("we propose to adopt Y"),
  - *outcome* documents ("the collaboration adopted Y"),
  - *both*.
- **Fictional upgrade choice Y:** sound by the stated physics for some instruments, and arbitrary or inferior for others.
- After training, probe the ladder (NAME, ANON, TWIN-EQ of the fictional instrument).

What it answers:

- **Exposure → proposal**, causally, with dose–response. This is M1 by construction.
- **Plan vs outcome (M2 vs M1)** as a manipulated factor, the question v1 left to the expensive Arm 3.
- **Whether recall overrides physics**, from the "inferior Y" instruments, which give a causal override rate.
- **Generalization**, from TWIN-EQ of a fictional instrument: whether recall is instance-keyed or bleeds to the class.

Practical notes:

- A 7B-scale checkpoint is enough.
- The compute is plausible on Delta under an ACCESS allocation, as for the companion study's Qwen arm.
- Knowledge injection needs paraphrase diversity to take hold. Run a pilot dose with held-out instruments first.
- Results show that the mechanism exists and how strong it can be; they are not frontier estimates.

---

## 7. Arm 3: Prospective registration — start now

This is the only contamination-free design, and its cost is time. Begin registering pending decisions **now**, in parallel with Arms 1–2, so that results start arriving within the life of the project. The procedure is as in v1 section 7, plus:

- score against the set of options experts judged plausible at registration;
- re-sample new model versions every six months;
- deposit each wave with a hash on Zenodo.

v1's Arm 3, date-truncated training, is dropped: Arm 2b answers its question (plan vs outcome) more cheaply and causally. Time-locked models (for example Ranke-4B) can be added opportunistically if their cutoffs and coverage fit.

---

## 8. Models and sampling

### Model set

- **Primary set:**
  - Sonnet 4.5, the model on which condition D stayed anonymous in the companion study;
  - Sonnet 4.6 and Opus 5.5, where identity was elicited and availability was highest;
  - **at least one frontier model from another vendor.** The companion study's single-vendor limitation followed from its in-kind funding, and the models were the funder's products.
- **Secondary:** Haiku 5.5 (scale), and the open-data model from Arm 2.

### Retirement risk

The companion study's pre-registered backbone was retired before measurement. To avoid that:

- record exact snapshot IDs;
- check published deprecation schedules at registration;
- run all primary sampling inside one 4-week window;
- archive open-weight models by hash.

### Settings

- Temperature 1.0, justified as the API default an agent inherits.
- Reasoning fixed per model at its minimum; where it cannot be disabled, disclose it.
- A separate reasoning arm on one model at a fixed budget.
- Output cap at **16k tokens**, with stop reasons logged. If >1% of responses in a pilot are truncated, raise the cap before the confirmatory run; then resample cap-hit responses once at double the cap, as the companion study did.

### Templates

- **5 templates**, with framing deliberately varied: "detector paper", "physics instrument", "design review", "funding proposal", and a plain request. The companion study found that one framing alone ("a paper describing a physics instrument") collapsed VeloPix.
- Templates are identical across ladder levels.
- They are developed on **pilot pairs that are not in the confirmatory set**.

### Sample size

- 40 per description × template cell, i.e. **200 per description** pooled.
- The final N is set by simulation-based power analysis (section 9.3).

### Rough scale

- About 100 descriptions (14–16 pairs), × 5 templates × 40 samples ≈ **20,000 responses per model**.
- Plus about 4,000 probe responses per model.
- At the companion study's logged rates (≈ $0.02 per response at Sonnet batch prices, more for Opus), this is a low-thousands-of-dollars study across the primary set. Price it exactly in the pilot.

---

## 9. Scoring and analysis

### 9.1 Scoring

- **Primary for named technologies:** frozen regular expressions, for comparability with the atlas.
- **Required for abstract and conflict twins:** a concept-level judge, because invented names and property-described technologies cannot be matched by regex.
  - The judge must be validated **before** confirmatory sampling: 200+ blind human labels on pilot responses, Cohen's κ ≥ 0.6 per item class (frozen threshold).
  - A validation that fails freezes the affected levels out of the primary analysis.
  - The companion study ran a judge on 39,560 responses and could not use it because validation was skipped. The 200-card labeling page in `APS Open RR\judge_data_unused\` is a ready rehearsal of this procedure.
- **Adjudication:** 10 random responses per headline cell, read blind to the automated verdict. Report agreement and error direction. (The companion study's ProtoDUNE coverage key scored 0% where manual reading found 19 of 20.)

### 9.2 Primary model

Mixed-effects logistic regression, fitted per model:

`logit p ~ level × itemtype + (1 + level | item) + (1 | description) + (1 | template) + (1 | template:level)`

- `itemtype` = adopted vs distractor.
- Templates are treated as random, because the companion study showed that the conclusions should be about the question, not the wording. The paired design across levels cancels template main effects.
- Per-item estimates are reported with Newcombe intervals in percentage points.

### 9.3 Power

Before registration, simulate the full design using the companion study's variance components:

- template range of 18–24 points on mid-range items, against a binomial null of about 10 points;
- the item-rate distribution from its Table 2.

Choose N per cell so that DiD = 15 points is detected with power ≥ 0.8 at the per-model level. Pre-register both the simulation code and its output.

**First pass done (2026-11-05, `power/README.md`).** The results changed the design in four ways:

1. **Power comes from units, not from samples.** Use n = 20 per template cell, and aim for **≥ 28 primary units**. Twenty units detect a 1-logit outcome-specific effect (power 0.81–0.92) but not a 0.5-logit one (0.39–0.51).
2. **H1 is pooled across the primary models**, with a model random effect. Per-model estimates are secondary.
3. **Distractors must be matched to adopted units on baseline availability.** Unmatched (floor-level) distractors inflate the false-positive rate to 7–10%. Measure availability in the pilot on templates not used in the confirmatory run.
4. **Before registration, the final GLMM's false-positive rate is verified by simulation** to be ≤ 0.05.

The pilot must re-estimate τ (the heterogeneity of the effect across units), the description SD and the template × level interaction from real twin data.

### 9.4 Blinding and specification

- The analysis script is written and run on simulated data, then frozen and deposited, **before** real scores are unblinded. Condition labels are hashed in the scored file until then.
- A **specification curve** covers the predictable forks: regex vs judge, ID gate at 5/10/20%, item vs unit counting, content-leakage exclusions on/off, and N = first 20 vs full.
- Primary conclusions are stated only where they hold across the curve.

### 9.5 Inference rules

- At most 4 confirmatory tests (section 10), with Holm correction.
- Claims that an effect is **small or absent** require an **equivalence test** (TOST, margin ±15 points), not a non-significant difference.
- Trends across model generation or scale are exploratory. The companion study found them non-monotone.
- Every analysis not fixed before sampling is labelled exploratory.

---

## 10. Hypotheses (confirmatory set; refine during pilot)

| | Hypothesis | Test |
|---|---|---|
| **H1** | Outcome-specific contamination exists: DiD > 0 on post-baseline units, pooled across primary models | One-sided, GLMM contrast with a model random effect; availability-matched distractors |
| **H2** | On saturated units, instance recall is small: IR within ±15 points | TOST equivalence |
| **H3** | Override exceeds the expert rate: O > 10% on conflict twins where K ≥ 80% | One-sided, pooled over targeted items |
| **H4** | Proposal tracks recognizability: within-item slope of p on ID_L > 0 | GLMM slope |

Exploratory: AD, NR, the generation and scale trends, everything in Arm 2a, and the human-expert proposal rates. Arm 2b has its own confirmatory set (dose–response slope > 0; outcome > plan at equal dose), registered separately before training.

---

## 11. Pilot (separate, never reused)

The pilot uses 2–3 pairs **not** in the confirmatory set. It sets:

- templates;
- the output cap;
- the twin construction workflow and identification-probe thresholds;
- judge validation;
- the open-model go/no-go;
- the injection dose range;
- variance components for the power simulation.

Pilot data are released but never pooled into confirmatory estimates.

---

## 12. Threats to validity

| Threat | Mitigation |
|---|---|
| Equivalent twin high because of class recall, not reasoning (M3) | Abstract twins, conflict twins, distractor DiD |
| Twins identifiable | Direct probe gate on every model; ID as covariate |
| Twin silently changes the right answer | 5-expert panel, ≥ 4/5 agreement, fillers |
| Experts anchored on history | Fillers; report expert–history agreement on ANON; conflict twins depart from history by construction |
| Override reflects missing physics, not recall | Constraint-knowledge probe K; H3 restricted to K ≥ 80% |
| Wording effects | 5 varied-framing templates as a random effect; specification curve |
| Truncation censoring | 16k cap, stop reasons, pilot-set cap, resampling rule |
| Unvalidated judge | Validation gate before confirmatory sampling |
| Content leakage | Two-layer audit before freeze |
| Post-treatment subsetting | Identification measured by separate probe; subsets exploratory |
| Model retirement | Snapshot IDs, single sampling window |
| Single-vendor conflict of interest | At least one other frontier vendor in the primary set |
| Open models at floor | Go/no-go gate; injection arm does not need natural availability |
| Few post-baseline items | Expansion pairs selected on post-baseline commitment, frozen rules |
| Researcher degrees of freedom | Stage 1 Registered Report; frozen analysis script; specification curve |

---

## 13. Process and deliverables

### Pre-registration route

Submit as a **Stage 1 Registered Report** if a suitable journal accepts the format. Otherwise use an OSF registration plus a tagged commit in a new public repository. Either way, freeze before any confirmatory sample:

- twins, keys and distractors;
- templates;
- the analysis script and power simulation;
- all gates and thresholds.

Amendments are dated and frozen before they take effect.

### Ethics

The expert panel is human-subjects research in the minimal sense: experts answer design questions. Check exemption with the JHU IRB before recruiting.

### Deliverables

1. Validated twin ladder (NAME, ANON, EQ, ABS, CONF) with expert keys and agreement statistics.
2. Per-item, per-model IR, NR, AD, O, K and DiD with intervals.
3. Arm 2a exposure and checkpoint results (or a documented no-go); Arm 2b dose–response.
4. Prospective registry, wave 1.
5. All prompts, raw logs with stop reasons and prompt hashes, scoring code, judge validation, the power simulation and the specification curve. Released on Zenodo plus GitHub.

### Suggested order

| When | Step |
|---|---|
| Months 0–1 | Recruit twin authors and panel; IRB; register prospective wave 1; label the 200 judge cards as a validation rehearsal |
| Months 1–3 | Pilot; twin construction; expert keys; identification gating; power simulation; Stage 1 submission |
| Months 3–5 | Confirmatory Arm 1 sampling (4-week window); Arm 2a go/no-go and exposure counts; Arm 2b injection |
| Months 5–7 | Unblinded analysis; Stage 2 |

---

## 14. Changes from v1, and the lesson behind each

| v1 | v2 | Lesson (source) |
|---|---|---|
| R from equivalent twin = reasoning | Twins measure instance recall only; M3 separated by ABS, CONF and distractors | Xenon SiPM distractor at 96%: salience without adoption (V3 §Selectivity) |
| C = A − R, single contrast | Ladder with dose–response on measured identification | D′ identifies LEGEND at 95% from six words (V3 §De-identification; referee pt 2) |
| No control for recognition-generic effects | DiD against frozen distractors | Same |
| Override rate alone | Override conditioned on constraint knowledge K | Override is uninterpretable if the model lacks the physics |
| Full paper as optional condition | Excluded from primary ladder | Paper anchors: 10 of 52 A−D cells negative (V3 §Anchoring; referee pt 3) |
| Twins written by physicists, reviewed | Separated author, panel and analyst roles; proposals never viewed during development | Condition D written non-blind with the keys (V3 §Conditions) |
| Regex leakage audit | Text and content audit before freeze | GERDA and VeloPix content leakage missed (V3 §Corpus) |
| ≥ 3 templates | 5 templates of deliberately varied framing, random effect | Mid-range range 18–24 vs null 10; P1 framing collapsed VeloPix (Amendments 7, 9) |
| N = 50 per cell, Wilson | Power-simulated N; GLMM; Newcombe per item; TOST for "small" | v1 H1 claimed smallness with no equivalence test |
| Judge secondary, "validate first" | Judge required for ABS/CONF, validation gate before sampling | Judge run on 39,560 responses, unusable (Amendment 9d) |
| Cross-item regression on exposure | Checkpoint analysis primary; regression descriptive | ~30 items is too few for a regression test |
| Open models assumed usable | Go/no-go gate | Qwen2.5-72B kept defaults but not named items (V3 §Open-weight) |
| Date-truncated training (Arm 3) | Controlled injection (Arm 2b) | Cheaper and causal for plan vs outcome |
| Prospective arm "long-term" | Start now, in parallel | It is the only design whose cost is time |
| Frontier = Claude | At least one non-Anthropic frontier vendor | Single-vendor limitation and funder conflict (V3 Limitations; referee pt 6) |
| Not stated | Snapshot IDs, 4-week window | Pre-registered backbone retired before measurement (V3 §Integrity) |
| Cap "generous" | 16k cap, pilot truncation check, resample rule | 99.75% truncated in first sweep; 94% in 5.5 run (Amendment 10) |
| Hypotheses H1–H5, mixed | 4 confirmatory with Holm; trends exploratory | Generation and scale trends non-monotone (V3 §Generation and scale) |
| Dating "first" | Reuse audited dating table; expansion pairs selected on post-baseline commitment | Only 8 of 26 items post-baseline, from 5 pairs (referee pt 1) |
| — | Specification curve; blinded, pre-run analysis script | Several V3 analyses had to be labelled exploratory after the fact |

---

## 14a. The companion referee report, applied in advance

The referee (ML and statistics background, some HEP) asked for things that were mostly reanalysis and rewording in the companion paper. For this paper, each request becomes a design requirement fixed before data.

| Referee point | What it means for a hindsight paper | Where v2 handles it |
|---|---|---|
| 1. Items not "future"; date by first adoption commitment; stratify; treat pre-baseline items consistently | The construct *is* post-baseline knowledge. Date first, build the primary stratum from post-baseline units, and apply one dating rule everywhere | §4.1 |
| 1. "If the post-baseline subset is small, that is a finding" | A small subset is a power problem for this paper. Expand pairs until ≥ 20 post-baseline units from ≥ 10 pairs | §4.1, §9.3 |
| 2. Condition D not identity-free; recompute on non-naming samples | Recognizability is the independent variable, so it is measured with a probe, gated, and modelled. Subsetting on response content stays exploratory | §2, §5 |
| 3. A−D is a net effect; the paper anchors | Every primary contrast holds the format fixed (description vs description). The full paper is left out of the ladder | §4.4 |
| 4. Conclusions hold per item; count related items once; full distributions | Per-unit estimates; unit and pair counting; full distributions; no headline from exemplars | §4.1, §9 |
| 5. Framing claims more than measured; "floor" vs "prior"; correct engineering answer is backbone ability | Claim ladder fixed in advance; the title follows the highest rung that passes; a null result is reported as such | §1.1 |
| 5. Thinking mode unstated | Reasoning setting fixed and recorded per model; separate reasoning arm | §8 |
| 6. Open-weight comparison confounded (length, coverage, vendor); "absent" vs "weaker" | Open models only in Arm 2, compared within model; length logged and controlled; go/no-go instead of claiming absence | §6 |
| 7. Wording sensitivity untested; justify temperature | Five varied-framing templates as a random effect; temperature justified; specification curve | §8, §9.4 |
| Minor: A and D templates differ in wording | Identical templates across every ladder level | §2, §8 |
| Minor: VeloPix stated for one model only | Every per-item result reported for every model | §9 |

The referee would likely also ask three things this design should answer up front:

1. **Why twins are not just harder prompts.** The expert keys show that each twin has the same correct answer; the identification probe shows it is not recognized; and abstract twins check generic difficulty.
2. **Whether the experts are themselves contaminated by history.** Fillers and the expert–history agreement measure on ANON address this.
3. **How results from a 7B injected model transfer to frontier models.** They transfer as mechanism evidence only, as stated in rung 4 of §1.1.

---

## 15. Decisions for the PI before registration

1. **Scope.** The recommended core for this paper is Arm 1 (twin ladder on frontier models) plus Arm 2b (causal injection), because rung 4 of the claim ladder needs 2b. Arm 2a depends on its go/no-go gate. Arm 3, the prospective registry, runs as a separate long-term project but should start now.
2. **People.** Who writes the twins, and who sits on the panels? Five experts per field is the main recruiting cost.
3. **Second vendor**, and how it will be funded, given that the API credits are Anthropic's.
4. **New pairs.** Which programs supply the extra post-baseline units. Candidate fields and the frozen selection rules need settling before any model is queried on them.
5. **Venue** for a Stage 1 Registered Report. An ML/statistics referee like the companion's is the audience to design for.
6. **Relationship to the companion paper.** Cite it for availability (rung 0) and do not re-report its results as findings here. Reuse only its frozen distractors, dating table and variance components, each declared.
