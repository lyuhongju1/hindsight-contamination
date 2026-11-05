# Measuring Hindsight Contamination in AI-Assisted Detector Design

*Study design for a future follow-up to the availability study ("When Is Agreement with History Evidence in AI-Assisted Detector Design?"). Draft, not pre-registered.*

---

## 1. The question

The availability study showed **that** language models propose many historically adopted detector upgrades without help. It could not show **why**. There are three candidate explanations:

1. **Recall of the outcome.** The model learned what the collaboration adopted and is repeating it.
2. **Recall of the plan.** The model read the older literature where the upgrade was already proposed (13 of 26 items predate their baselines).
3. **Reasoning.** The adopted technology is the sound engineering answer, and the model would reach it from the physics alone.

Only (1) is hindsight contamination in the strict sense. This study aims to separate (1) from (3), and where possible (1) from (2).

**Core question:** For each answer-key item, how much of the model's proposal rate is explained by exposure to the historical outcome, as opposed to the physics of the problem?

---

## 2. Definitions

For an item *i* and a model *m*:

| Quantity | Definition |
|---|---|
| **Availability** A(i, m) | Proposal rate given a description of the real instrument (as in the companion study) |
| **Reasoning rate** R(i, m) | Proposal rate given a matched synthetic instrument with no literature, where experts agree the same upgrade is correct |
| **Recall component** C(i, m) = A − R | The part of availability that the physics alone does not explain |
| **Override rate** O(i, m) | Rate at which the model proposes the historical choice for a synthetic instrument whose constraints make that choice wrong |
| **Exposure** E(i, m) | Measured presence of the item, and its pairing with the instrument, in the model's training data (open-data models only) |

Hindsight contamination is supported for an item when C is large and positive, O is non-zero, and proposal rates track E.

---

## 3. Design overview

Four arms, ordered from most to least feasible. Arms 1 and 2 form a complete study on their own. Arms 3 and 4 are extensions.

| Arm | Separates | Models | Cost | Time to result |
|---|---|---|---|---|
| 1. Synthetic twins | Recall vs reasoning | Any (frontier + open) | Low | Weeks |
| 2. Training-data exposure | Exposure → proposal | Open-data models only | Low–moderate | Weeks |
| 3. Temporal contrast | Outcome vs plan | Time-locked or date-truncated models | High | Months |
| 4. Prospective registration | Eliminates contamination entirely | Frontier | Low | Years |

---

## 4. Arm 1: Synthetic twin instruments

**Idea.** If a model proposes SiPMs for a real liquid-argon dark-matter detector **and** for an invented one with the same physics but no literature, the proposal is reasoning. If it proposes them only for the real one, the difference is recall.

### 4.1 Constructing twins

For each baseline instrument, write two synthetic variants.

- **Equivalent twin.** It changes surface features that do not change the correct upgrade, such as invented names, location, mass, and geometry details within a range that experts agree leaves the optimal choice unchanged. The correct answer is the same as history.
- **Conflict twin.** It changes one physical constraint so that the historical choice becomes wrong or clearly inferior. For example, it imposes an operating condition under which the adopted photosensor performs poorly while the alternative does not. The correct answer differs from history.

Twins are written by physicists who are not told which models will be tested, and are then reviewed by a separate panel (section 4.2).

### 4.2 Validating twins

Each twin must pass three checks before sampling:

1. **Expert answer key.** At least three independent domain experts, blind to the historical outcome where possible, rank candidate upgrades for the twin. The twin enters the study only if the experts agree on the correct answer (equivalent twins: matches history; conflict twins: differs from history).
2. **Non-identifiability.** Each model under test is asked directly, "Which real experiment is this?" A twin is retained only if identification stays below a pre-set threshold (for example, 10 percent). This directly addresses the companion study's finding that condition D was not anonymous on Sonnet 4.6.
3. **Leakage audit.** The same regex audit as the companion study confirms that the twin text contains no answer-key term.

### 4.3 Conditions

For each instrument: real description (as condition D in the companion study), equivalent twin, and conflict twin. Optionally add the full baseline paper for the real instrument to connect to the companion study's anchoring result.

### 4.4 What each outcome would mean

| Real | Equivalent twin | Conflict twin | Interpretation |
|---|---|---|---|
| High | High | Low | Reasoning. The model follows the physics |
| High | Low | Low | Recall triggered by recognition |
| High | High | High | Recall overriding physics (strongest contamination signal) |
| High | Low | High | Incoherent. Check the twin's validity |

The **conflict twin is the key innovation**. An equivalent twin alone cannot distinguish "the model reasoned correctly" from "the model has a generic habit of proposing this technology". A model that keeps proposing the historical choice when the physics argues against it is showing recall, not reasoning.

---

## 5. Arm 2: Training-data exposure (open-data models)

**Idea.** For models whose training data is public, measure directly whether each item appeared in training, and test whether exposure predicts proposals.

### 5.1 Models

Open models with released training corpora and, ideally, intermediate checkpoints and data order. Candidates at the time of writing include the OLMo family (Dolma corpora) and Pythia (the Pile). Verify current availability and choose the largest models that are practical to serve, since the companion study found weak availability in mid-sized open models.

### 5.2 Measuring exposure

For each item, use corpus search tools (for example infini-gram, WIMBD, or OLMoTrace) to count:

- documents mentioning the technology at all (generic frequency);
- documents mentioning the technology together with the instrument or its successor (paired frequency);
- the dates of those documents, where recoverable, classified against the dating table (pre-baseline, contemporaneous, post-baseline).

String matching undercounts paraphrases, so report counts as lower bounds and validate a sample by hand.

### 5.3 Analyses

1. **Cross-item regression.** Proposal rate against log paired frequency, controlling for log generic frequency. Contamination predicts that paired frequency explains proposals beyond generic frequency.
2. **Checkpoint analysis (strongest design).** Where checkpoints and data order are public, locate when documents pairing an item with its instrument enter training, and test whether the proposal rate rises after that point. This comes closest to a causal estimate available without retraining.
3. **Plan vs outcome.** Split paired documents by date. If proposals track exposure to post-baseline documents more than to pre-baseline ones, that separates explanation (1) from explanation (2).

### 5.4 Limitations

Open-data models are weaker than frontier models, so floor effects may hide the signal. Results transfer to frontier models only by analogy. Report them as mechanism evidence, not as frontier estimates.

---

## 6. Arm 3: Temporal contrast (extension)

**Idea.** Compare models whose training data ends before an upgrade was publicly committed with models whose training data ends after.

All current frontier models postdate every item in the companion study, so this requires one of:

- **Time-locked models** trained only on text before fixed dates (for example the Ranke-4B family), if their cutoffs and domain coverage fit the items;
- **Date-truncated training.** Train or continue-train small models on a physics corpus (for example arXiv) truncated at year Y and at year Y + k, around an item's commitment date. This is expensive and gives weak models, but it is the cleanest test of explanation (1) against (2);
- **Natural experiment.** Track upgrades announced after current models' training cutoffs and compare model versions released before and after the announcement. This merges with Arm 4.

---

## 7. Arm 4: Prospective registration (long-term)

**Idea.** Ask models to propose upgrades for decisions that have not been made, lock the answers publicly, and score them when the decision is made. No contamination is possible because the answer does not yet exist.

### 7.1 Procedure

1. Identify pending design decisions in current programs (candidate areas: next-generation dark-matter and neutrinoless double-beta-decay detectors, future neutrino far-detector modules, collider upgrade phases, and next-generation gravitational-wave observatories). Verify each decision's status at registration time.
2. For each decision, freeze the question, the candidate options, and the scoring rule.
3. Sample every model under the same protocol, then deposit responses with a timestamp and hash (for example a commit to a public repository plus a Zenodo deposit).
4. Re-sample newer model versions periodically, to see whether predictions shift as the decision approaches and discussion enters the literature. This is itself a contamination measurement.
5. Score each decision when the collaboration commits publicly, using the same dating rule as the companion study.

### 7.2 Notes

Results arrive over years, so this is best run as a standing registry rather than a single paper. The base rate matters: score against the options experts considered plausible at registration, not against a single answer.

---

## 8. Protocol rules carried over from the companion study

These are lessons from the availability study, to be applied from the start:

- **Date every item first.** Classify each answer-key item against its baseline before sampling, not after.
- **Pre-register everything,** including the robustness criteria and the analyses, with dated amendments for any change.
- **Use at least three matched templates per cell** with identical wording across conditions, since mid-range rates moved about 20 points with wording.
- **Record stop reasons and reasoning settings** for every sample, set output caps generously, and check truncation before scoring.
- **Fix reasoning mode per model** and report where it cannot be disabled.
- **Report noise baselines.** Compare across-template variation to binomial sampling variation.
- **Treat related items as one unit** in headline numbers.
- **Apply leakage exclusions consistently,** at the level of content as well as exact terms.
- **N = 50 per cell** with Wilson intervals, and Newcombe intervals for differences.

---

## 9. Scoring

- **Primary:** frozen regular expressions, as in the companion study, for comparability.
- **Secondary:** a concept-level judge, validated against human labels before use (the companion study ran one but did not validate it, so validation would be a first step here).
- **Adjudication:** manual review of a random sample per headline cell, reporting agreement and error direction.

---

## 10. Hypotheses (to be refined before pre-registration)

- **H1.** For items the companion study found saturated, the reasoning rate R is high (most are sound engineering answers), so the recall component C is small.
- **H2.** For paper-triggered and successor-name items, C is large: rates fall sharply on equivalent twins.
- **H3.** Override rates on conflict twins are non-zero for at least some saturated items, showing that recall can win over physics.
- **H4.** In open-data models, paired frequency predicts proposal rate beyond generic frequency.
- **H5.** Recall components are larger on larger and newer models, consistent with the companion study's generation and scale trends.

---

## 11. Threats to validity

| Threat | Mitigation |
|---|---|
| Twins remain identifiable | Identification check per model, with exclusion threshold |
| Twin changes the correct answer unintentionally | Independent expert answer keys; require agreement |
| Expert answer keys biased by knowing history | Blind experts where possible; report expert–history agreement |
| Generic technology habits mimic reasoning | Conflict twins separate habit from reasoning |
| Corpus string matching misses paraphrase | Report as lower bounds; hand-validate a sample |
| Open models too weak to show signal | Use largest available; interpret as mechanism evidence |
| Prospective decisions take years | Run as a standing registry; publish registration separately |

---

## 12. Deliverables

1. A validated set of equivalent and conflict twins with expert answer keys, released openly.
2. Per-item, per-model estimates of A, R, C, and O.
3. Exposure counts and checkpoint analyses for open-data models.
4. A public prospective-prediction registry (if Arm 4 is pursued).
5. All prompts, responses, scoring code, and pre-registration documents, as in the companion study.

---

## 13. Suggested scope for a first paper

**Arms 1 and 2 only,** on the companion study's ten instruments. Together they answer the core question (how much is recall versus reasoning) with one causal-leaning design (twins) and one exposure-based design (corpus and checkpoints), at a cost comparable to the companion study. Arms 3 and 4 can follow as separate work.
