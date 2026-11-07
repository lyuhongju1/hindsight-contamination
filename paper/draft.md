# Hindsight contamination in AI-assisted detector design: a pre-registered test of whether language models reproduce historically adopted upgrades when stated physics rules them out

**Lyuhong Ju** [affiliation TBD]

*Draft manuscript, 2026-11-07. Study pre-registered as `PREREGISTRATION.md` v4.3 and frozen at commit `8009881` of github.com/lyuhongju1/hindsight-contamination.*

---

## Abstract

Language models are increasingly used to propose upgrades to physics instruments, many of which have documented upgrade histories that the models may recall. We ask whether models reproduce the historically adopted upgrade even when the problem statement includes physics under which that upgrade fails, and when the same model, asked in isolation, answers the relevant physics correctly. We call this *override*. In a public pre-registration, we built *conflict twins*: invented instruments matched to a real baseline in which a minimal, plainly stated physical fact makes the adopted item fail while at least one credible alternative survives. Item selection was mechanical: an INSPIRE-derived frame, two independent dating agents plus a quote verifier, and author and red-team agents working under fixed rules with randomized robustness checks. Of 21 real baseline–upgrade pairs taken through authoring, 15 admitted no honest physics-only conflict; 6 did, and 5 passed a pre-registered constraint-knowledge check. We sampled seven Anthropic models (50 responses per description per model). Two non-study models adjudicated the responses blind (Cohen's κ = 0.69). The first confirmatory test in the pre-registered fixed sequence (Sonnet 4.5, mean override 0.43 against a null of 0.10) was not rejected (one-sided p = 0.099), so no per-model confirmatory claim is made. Models differed strongly (likelihood-ratio test, LR = 300, df = 6). Override was concentrated in two of five units, and the newest Opus model almost never overrode. A pre-specified GLMM sensitivity analysis disagrees with the primary test; we report both. The low yield of physics-decidable upgrades limits how much contamination tests of this kind can show.

---

## 1. Introduction

Large language models are now used as design assistants in experimental physics. They are asked to suggest upgrades, compare technologies and critique proposals. Many real instruments have well-documented upgrade histories: a baseline detector was built, its collaboration later committed to a specific change, and that commitment is described in public documents that are likely to appear in model training data. When a model is asked to improve such an instrument, or something resembling it, two sources of an answer compete. One is reasoning from the stated requirements. The other is recall of what the collaboration actually did.

In ordinary use these two sources usually agree, because the historical choice was usually a reasonable one. That agreement makes it hard to tell whether a model that proposes the historical choice is reasoning or remembering. The two sources can only be separated in problems where they disagree: where the stated physics rules out the historically adopted choice. We call the behaviour of interest **override**: proposing the historically adopted item as the main recommendation when the stated physics makes it fail, while the same model, asked the underlying physics question without instrument context, gets it right. We use "hindsight contamination" as an umbrella term for this behaviour. The term describes a behavioural pattern; it does not, by itself, assert anything about training-data provenance.

This paper reports a pre-registered study of override. It makes three contributions.

1. **A design.** *Conflict twins* are paired with matched *BASE* twins, a constraint-knowledge (K) premise check, and recognition measured rather than gated. The design was developed and stress-tested in a two-instrument pilot (`pilot/PILOT_SUMMARY.md`; `pilot/findings.md`, findings F1–F11).
2. **A confirmatory test** across seven models from one vendor, with a fixed-sequence multiplicity procedure, pre-registered before any confirmatory upgrade sample was drawn.
3. **A materials funnel**, reported as a primary descriptive result. When real upgrade decisions are drawn mechanically from the literature and subjected to strict physics-only construction rules, most of them cannot be turned into an honest conflict. This limits the population on which any test of this kind can be run.

The confirmatory test of the first hypothesis did not reject its null. We report this result as it stands, together with the confirmatory evidence that models differ, and with exploratory analyses that are labelled as such.

---

## 2. Design

### 2.1 Conflict twins and BASE twins

Each study unit is built from a real **baseline–upgrade pair**: a baseline instrument (e.g. XENON1T) and the upgrade programme that followed it (e.g. XENONnT), with one **counted item** *a* that the collaboration committed to as its chosen plan (`search/SELECTED_PAIRS.md`; Amendment A1, addendum 3). For each pair an author agent wrote four descriptions (`materials/AUTHOR_BRIEF.md`):

| Description | Content |
|---|---|
| NAME | The real baseline, named |
| ANON | The real baseline, unnamed |
| BASE | An invented instrument of the same class in which *a* is a physically sound upgrade: it passes every stated requirement |
| CONF1 | BASE with one minimal edit (one sentence or one set of numbers) under which *a* fails a stated physical requirement |

The **unit of analysis** is one CONF (conflict twin). The pre-registration allowed up to two CONFs per pair; each achieved pair has one (CONF1) (`PREREGISTRATION.md` §2.1a).

The construction rules (`PREREGISTRATION.md` §2.3; `materials/AUTHOR_BRIEF.md` rules 1–10) are central to what the study can claim. All of them must hold:

1. **Physics only.** No cost, labour or schedule may decide anything.
2. **Plain fact, never exclusion wording.** Descriptions do not name, describe or rule out any technology class.
3. **At least one credible survivor**, checked against every stated fact. The survivor count is recorded as a covariate.
4. **Robust failure of *a*.** Every cited property is varied over ×0.5–2 in 2,000 random draws with a per-level seed, and *a* must fail in at least 95% of draws. This check is run by the frozen library `pilot/harness/keylib.py` and a per-pair key script (`materials/<pair>/keys/key.py`). Exact stated facts and integer structural counts may be held fixed, with a justification. Ranges may be tightened only with a cited precision, never below ×0.8–1.25. Only linear scales are allowed, with no booleans.
5. **Minimal pair.** CONF differs from BASE only in the conflict edit.
6. **No post-run tuning** of stated numbers without a logged reason.
7. **Scenario coherence**, with every side effect of the edit checked.
8. **Workaround routes closed** by plain facts where possible.
9. **Red-team verdict OK** on BASE and CONF, with every requested fix resolved before the freeze.

Lessons from the first authoring round and Clarification C1 (Section 3.4) refined how rules 1, 7 and 8 were applied. They added no new rule.

Because CONF differs from BASE by a single edit, BASE provides the model's propensity to choose *a* when *a* is sound, and CONF provides its propensity to choose *a* when the stated physics rules it out.

### 2.2 The K premise

An override is only interpretable as "recalled history overriding *known* physics" if the model knows the physics. Each CONF therefore has a **K-probe**: a neutral physics question about the failure mechanism, with no instrument context, that ends with a forced `VERDICT: YES` or `VERDICT: NO` line (`materials/<pair>/kprobe.json`; pilot findings F9, F10). The K-probe has two roles.

- **Premise check.** Before the freeze, each K-probe was run 20 times on each confirmatory model, with no upgrade sampling on the confirmatory items. A CONF is **suspended** if, on two or more models, the majority verdict contradicts the key's expected answer (`PREREGISTRATION.md` §2.4). The pilot showed this check can catch a wrong premise that the robustness check cannot, because the key script encodes the author's own premise (F9).
- **Per-model inclusion.** For H1, a model × unit cell is included only if that model's own K majority verdict is correct (§6).

### 2.3 Recognition is measured, not gated

The original design required that the invented twins not be recognized as the real instrument (an identification gate of at most 10%). The pilot showed this gate cannot be met. Twins of T2K ND280 were identified at 50–100% and twins of Auger at about 100%, including abstract twins, and Opus 5.5 named the real upgrade unprompted (F1, F2, F4). The decision context of a real instrument acts as a fingerprint. The confirmatory design therefore **measures recognition and does not gate on it**: an identification probe (n = 20 per description per model) is run on every description, and recognition enters only as an exploratory covariate. Override on a recognized CONF is the behaviour of interest, not a confound: the model is shown physics under which the remembered choice fails.

### 2.4 Pre-registration

The protocol was publicly pre-registered rather than submitted as a journal Registered Report (PI decision, 2026-11-06; `PREREGISTRATION.md`, "Route"). Version 4.3 is frozen by the public commit that adds `FREEZE_MANIFEST.md`. The manifest holds SHA-256 hashes of the pre-registration, every description, key, K-probe and rubric, the scoring regexes, the templates, the harness and the analysis and power scripts. The commit precedes all confirmatory upgrade and identification sampling. The only confirmatory-model calls made before the freeze were the K premise check (`FREEZE_MANIFEST.md`, preamble). The frozen state is commit `8009881` (`RESULTS_SUMMARY.md`). The pre-registration text also refers to git tags (`prereg-v4.2-frozen`, `prereg-v4.3-frozen` "if permitted") [CHECK: whether either tag was created].

**Hypotheses** (`PREREGISTRATION.md` §6):

- **H1 (confirmatory, per model).** The marginal override rate across units exceeds 0.10. One-sided t-test of the unit-level override proportions O_mj against 0.10, with the unit as the cluster. Multiplicity is controlled by **fixed-sequence testing** at α = 0.05 in this pre-specified order: Sonnet 4.5, Haiku 4.5, Opus 4.5, Sonnet 4.6, Haiku 5.5, Sonnet 5.5, Opus 5.5. Testing stops at the first non-rejection. The order follows the pilot override rates (Sonnet 4.5 22–26%, Sonnet 4.6 6–8%, Opus 5.5 0%) and places unpiloted models by generation. A binomial GLMM with a unit random effect is pre-specified as a sensitivity analysis.
- **H2 (confirmatory).** Override rates differ across models. Likelihood-ratio test of the model fixed effect in a binomial GLMM with a unit random intercept, on all included model × unit cells.
- **Secondary (pre-specified, outside the confirmatory family).** The pooled override rate across all models and units, tested against 0.10.
- **Exploratory (pre-specified as such).** The relation between recognition and override (two-sided), scale and generation trends, BASE rates and R = O/B (descriptive), K-gated versus ungated override, per-template variation, the fallback-to-history pattern, and qualitative analysis of misstatements.

---

## 3. Item selection and the materials funnel

### 3.1 Sampling frame and selection

Pairs were selected by a mechanical procedure frozen before any assessment (`pair_selection_rules.md`, frozen at commit `721e55f`). Its stages were as follows.

1. **Frame.** An INSPIRE search produced 539 baseline records.
2. **I1 screening.** Two independent screening agents agreed on 537 of 539 records. Disagreements were excluded. 83 records were included, 81 after removing the two pilot instruments (T2K ND280, Auger).
3. **Document search.** 2,130 upgrade documents were retrieved for 65 baselines.
4. **Sequential seeded draw (Amendment A1).** The 81 baselines were put in a random order within each field, seeded by the SHA-256 of the frozen rules. Fields were visited round-robin. Within a field, the first baseline in random order that passed criteria I2–I6 was selected, subject to a per-field cap of 3 and a year-and-lab cap of 2.
5. **Dating.** Each assessed baseline was dated by **two independent dating agents** (D1, D2). Each counted item needed both daters' claims **verified** by the script `verify_dating.py`. The script checks the metadata date, checks the verbatim quote against the arXiv text, requires the commitment to come at least 24 months after the baseline (class Post-primary), and requires the commitment date to be on or before 2023-06-30 (the I6 boundary, A1 addendum).

The two daters agreed on eligibility for all 25 baselines assessed in the first three rounds (`search/SELECTED_PAIRS.md`). The verifier caught one dater paraphrase (the XENON1T Gd veto claim). It was corrected mid-stream for PDF-extraction false negatives, after which all claims were re-verified. A fabricated-quote control failed throughout.

Of the first 25 assessed baselines, 14 were eligible and selected, 2 were eligible but not selected (their field was already filled that round), 9 were not eligible, and 2 more were skipped by the lineage rule (A1 addendum 2). Later replacements (Section 3.3) assessed further baselines in queue order: q19 LUX, q23 Super-Kamiokande, q26 ADMX, q27 CUORE-0, q30 IceCube, q34 EXO-200, q37 ANTARES and q38 MAGIC. ADMX, IceCube and ANTARES were not eligible.

### 3.2 Authoring, red-teaming and robustness

For each selected pair, an **author agent** working from `materials/AUTHOR_BRIEF.md` wrote a dossier, the four descriptions, a key script using `keylib`, a K-probe and notes. It was explicitly told that a pair with no honest conflict is an acceptable outcome. A separate **red-team agent** (`materials/REDTEAM_BRIEF.md`) checked every rule and returned OK, FIX or DROP. Every CONF that reached the freeze needed at least one fix round (`RUNBOOK.md`, 2026-11-06). Survivor counts and red-team scoring notes are in `materials/STATUS.md`. Examples of scoring notes: for p02, underground argon plus any radon-progeny measure is a valid workaround (C); for p05, LAB plus a density-raising co-solvent is C. Mechanical gates (`materials/gates.py`, `materials/test_regex.py`) checked that no description matches the pair's adopted-item regex, and that only NAME matches its identity regex.

### 3.3 Replacement and stop rules

When a selected pair was concluded, after author and red-team rounds, to admit no honest physical conflict, it was kept in the report as a **zero-unit pair**. It was then replaced by the next eligible baseline in queue order (Amendment A2). Zero-unit pairs do not count toward the field caps, and their lineages are not re-entered. After 21 pairs had been worked, and the last 7 queue draws had all yielded zero units, item supply was stopped (Amendment A3). Reaching the pre-registered minimum of 10 units would have needed on the order of 15–30 further selections with no assurance of success. Supply stopped at 6 units-bearing pairs, all from the original 14 selected pairs. This happened before any confirmatory sampling.

### 3.4 Clarification C1

During authoring, a feasibility author for p19 (CUPID) rejected a candidate conflict on grounds stricter than those applied to the pairs already cleared. Clarification C1 (`materials/AUTHOR_BRIEF.md`, 2026-11-06) aligned the standard.
- Stated physical facts about the instrument or site (dimensions, retained hardware, available path lengths) are allowed.
- Routine settings *within* the item (servo gains, filters, thresholds, mounting) defeat a conflict.
- A separate added component does not defeat a conflict; "item plus add-on" answers are scored C.

All twelve earlier zero-unit verdicts were audited against C1 and none changed. Only p19 was affected; it received a full new author attempt, which also ended zero-unit (`RUNBOOK.md`, "Standards check"; `materials/STATUS.md`).

### 3.5 The funnel (figure-ready)

**Table 1. Materials funnel.** Sources: `RUNBOOK.md`, `search/SELECTED_PAIRS.md`, `search/AMENDMENT_A1.md`, `materials/STATUS.md`, `data/conf_kpremise/kpremise_results.md`.

| Stage | Count | Note |
|---|---|---|
| INSPIRE frame records | 539 | |
| Included after two-screener I1 screening | 83 (81 non-pilot) | 537/539 screener agreement |
| Baselines assessed for eligibility by two daters | 25 in rounds 1–3, plus 8 in the resumed queue | [CHECK: total of 33 assumes no overlap] |
| Pairs selected and worked through authoring and red team | 21 | 14 original + 7 replacements |
| Zero-unit pairs (no honest physics-only conflict) | 15 | categorized in Table 2 |
| Units-bearing pairs (one CONF1 each) | 6 | p01, p02, p03, p05, p09, p10 |
| Suspended by the K premise check | 1 | p10 Borexino → SOX |
| **Confirmatory units** | **5** | p01, p02, p03, p05, p09 |

**Table 2. The 15 zero-unit pairs, with the reasons recorded.** The categories are our grouping of the logged reasons.

| Category | Pair (item) | Recorded reason |
|---|---|---|
| No physics window: the item is at least as good on every physical criterion, or its drawbacks are cost or engineering | p04 ICARUS (serial ADC per channel) | per-channel synchronous digitisation dominates on physics; its drawbacks are cost, density and power engineering |
| | p06 AGATA (Ethernet readout) | the transport choice is cost/engineering |
| | p12 MiniBooNE (PPO doping) | no physics window (from LoI numbers) |
| | p18 Super-K (Gd sulfate loading) | no physics window: attenuation from Gd3+, and a low loading reaches the H-only regime; salt purification is a secondary ground |
| A routine setting or free geometry of the item defeats the conflict | p15 aLIGO (balanced homodyne readout) | a servo, i.e. a setting |
| | p14 KASCADE (tripole antennas) | a notch filter (a setting); the extra arm is harmless |
| | p17 LUX (Gd-loaded LS outer detector) | threshold setting; loading level |
| | p11 KAGRA (optical levers) | lever geometry and mounting of the item itself are free, so there is no robust window |
| The item is defined more broadly than any defeatable configuration | p07 MEG (radiative decay counter) | placement is part of the item; a thin near-target counter survives every coherent edit |
| The only closure would need a non-physics (logistics) rule | p08 COSINE-100 (in-house NaI growth) | the in-house method reaches the required purity, so the window is empty; the altitude route needs a logistics rule |
| The conflict breaks the instrument class or is not robust | p16 BESIII (MRPC endcap TOF) | the conflict needed a hadron collider, which breaks the class rule; no same-class route is robust |
| | p13 NA62 (small-diameter straws) | the electrostatic window is only 2× and not robust |
| Recorded only as "author/feasibility + batched confirmation" | p19 CUORE-0 → CUPID (Li2MoO4 bolometers) | zero-unit after a full attempt under C1 [CHECK: specific physics reason in `materials/p19_cuore0/`] |
| | p20 EXO-200 → nEXO (VUV SiPMs) | [CHECK: specific reason in `materials/p20_exo200/`] |
| | p21 MAGIC → MAGIC-II (increased-QE PMTs) | [CHECK: specific reason in `materials/p21_magic/`] |

**Table 3. The six units-bearing pairs** (`PREREGISTRATION.md` §2.1a; `materials/STATUS.md`).

| Unit | Baseline → programme | Adopted item *a* | CONF1 mechanism | Credible survivors | adoption_status |
|---|---|---|---|---|---|
| p01 | XENON1T → XENONnT | liquid-phase Xe purification | a tritiated-methane calibration must be removed, and only a heated gas getter removes CH4 | 1 (existing heated-getter gas loop) | built and operated |
| p02 | GERDA Phase II → LEGEND-1000 | underground-sourced argon | radon-progeny surface background dominates; underground argon alone leaves the budget unmet | 1 (encapsulation / shroud) | approved, not built (unverified) |
| p03 | Advanced Virgo → AdV+ | frequency-dependent squeezing via an external filter cavity | an 8 m absolute path limit plus 5 ppm mirror loss make the required cavity linewidth unreachable | 1 (EPR / conditional squeezing) | built and operated (unverified) |
| p05 | SNO → SNO+ | LAB liquid scintillator | buoyancy load limit on a thin acrylic sphere | 2 (PXE; an LAB30/MN70 blend, not counted as LAB) | built and operated |
| p09 | NEMO-3 → SuperNEMO | 8-in. high-QE PMT calorimeter modules | granularity: 15 cm two-electron separation against a cell pitch of at least 210 mm | 1 (76 mm PMTs on small cubes) | built and operated (unverified) |
| p10 | Borexino → SOX (suspended) | 144Ce-144Pr antineutrino source | a fully deuterated scintillator removes inverse beta decay | 2 (51Cr, 37Ar) | cancelled |

The materials log states the pattern behind the yield (`RUNBOOK.md`, materials-stage checkpoint). Upgrades whose advantage is engineering, cost, a tunable geometry or an added capability admit no honest physics-only conflict. Upgrades that trade one physical property for another (radiopurity, buoyancy, granularity, squeezing-loss budget) do. The realized yield was 6 of 21 pairs (about 29%), or 5 of 21 (about 24%) after the K premise check.

---

## 4. Elicitation and scoring

### 4.1 Models and settings

The confirmatory set is seven Anthropic models, with these snapshot IDs recorded at the freeze (`PREREGISTRATION.md` §3):
- `claude-sonnet-4-5-20250929`, `claude-haiku-4-5-20251001`, `claude-opus-4-5-20251101`;
- `claude-sonnet-4-6`;
- `claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5`.

No key for a second vendor was provided before the freeze, so this is a **single-vendor study** (`PREREGISTRATION.md` §3; `RUNBOOK.md`, PI action P2).

Settings:
- temperature 1.0;
- the minimum reasoning each model allows (low-effort adaptive reasoning where it cannot be disabled);
- a 16k output-token cap, with stop reasons logged.

### 4.2 Upgrade task and probes

- **Upgrade task.** Five frozen templates (`pilot/templates.json`) wrap each description: T1_detector, T2_instrument, T3_review, T4_proposal and T5_plain. Each ends with the instruction to give a final line `TOP RECOMMENDATION: <the single hardware change you consider most important>`. The forced final line was introduced after the pilot showed that sentence-level scoring cannot tell "mention, then reject" from a committed proposal (F5). Each description (BASE, CONF1, ANON, NAME) was sampled n = 10 per template, giving 50 responses per description per model.
- **Identification probe.** n = 20 per description per model.
- **K-probe.** n = 20 per CONF per model, run before the freeze.
- **Sessions.** Each probe ran in a separate session.

The harvest was 8,400 upgrade responses and 3,360 identification responses, with no non-success (`RUNBOOK.md`, 2026-11-07). Three Sonnet 5.5 cells exceeded the pre-registered 1% truncation threshold (§7): p03 CONF1 (1/50 truncated), p10 BASE (9/50) and p10 CONF1 (11/50). As pre-specified, they were resampled once at double the cap (32k), with no truncation after resampling, and the resampled responses replace those cells (`data/conf_upgrade_resample`).

### 4.3 Screening

A frozen per-pair regex for the adopted item (`materials/scoring_regex.json`, unit-tested by `materials/test_regex.py`) was applied to the TOP RECOMMENDATION line. It produced 938 hits out of 2,100 CONF1 responses and 1,162 hits out of 2,100 BASE responses. With the pre-specified random non-hits, this gave 2,668 adjudication cards in total (`RUNBOOK.md`, 2026-11-07).

### 4.4 Adjudication

Every screened hit, plus 10 random non-hits per CONF × model cell, was adjudicated blind by **two adjudicators** (`PREREGISTRATION.md` §5). In the implementation (`analysis/adjudicate.py`; `RUNBOOK.md`, 2026-11-07), each adjudicator is a separate model that is not in the confirmatory set, so no model codes its own outputs:
- adjudicator A was `claude-fable-5-1`;
- adjudicator B was `claude-opus-4-8`.

Each card was coded in an independent Batches-API request. The request contained only the frozen per-pair `RUBRIC.md` and one blinded card: the final line plus the relevant sentences, with model identity hidden behind a hashed ID and no template information.

The rubric codes are:
- **A**, commits to *a* and ignores or misstates the stated physics;
- **B**, commits to *a* while acknowledging the violation without a valid fix;
- **C**, a valid workaround, defined per CONF before sampling;
- **D**, mentions *a* and then rejects it;
- **E**, does not mention *a*;
- **X**, no valid final line or not codeable.

A response counts as **override only if both adjudicators code A or B**. A pre-specified sensitivity analysis counts disagreements (A or B from one adjudicator only) as override. Responses lacking a TOP RECOMMENDATION line are coded X and excluded from the numerator (`PREREGISTRATION.md` §7).

**Agreement.** Cohen's κ between the two adjudicators on the 1,269 CONF1 cards was 0.692 (`data/conf_upgrade/RESULTS_confirmatory.md`). This is agreement between two models, not human inter-rater reliability. The main disagreement was B versus C (a vague fix versus a valid one; 87 cards). Disagreements between A and B do not affect the override count (`RESULTS_SUMMARY.md`). The number of cards on which only one adjudicator coded override, per model: Sonnet 4.5 35, Haiku 4.5 13, Opus 4.5 41, Sonnet 4.6 24, Haiku 5.5 11, Sonnet 5.5 8, Opus 5.5 2.

**Screen misses.** Of 398 audited non-hits, 13 (about 3%) were coded as overrides by both adjudicators and are counted (`RESULTS_SUMMARY.md`). [CHECK: the pre-registered audit is 10 non-hits per CONF × model, i.e. 420 for 6 units × 7 models or 350 for 5 units; reconcile with 398.] Unaudited non-hits are not adjudicated, so O is a slight lower bound.

**Identification and K scoring.** Identification is scored by a frozen identity regex (names of the baseline or successor) over the full response; K is scored from the VERDICT line.

---

## 5. Confirmatory results

### 5.1 K premise check

The K premise check ran on 2026-11-06, before the freeze (`data/conf_kpremise/kpremise_results.md`). Four of the six CONFs passed with no model majority-wrong, and p03 passed with one (Haiku 5.5, 10/20 correct). **p10 Borexino CONF1 was suspended**: two models were majority-wrong (Haiku 4.5, 6/20 correct; Sonnet 4.5, 7/20). Reading the dissenting responses suggests model physics errors rather than a flawed premise:
- an arithmetic error by Sonnet 4.5 (about 1,330 inverse-beta-decay events computed on 1.98e28 hydrogen-1 atoms, against a correct order of about 10);
- Haiku 4.5 counting charged-current reactions on deuterium, whose 4.03 MeV threshold is above the stated 3.0 MeV endpoint.

The suspension was applied anyway, because the rule was fixed in advance and overriding it would be outcome-dependent. Per-model K gating removed one further cell: p03 for Haiku 5.5. All other model × unit cells on the five units were included (34 cells).

### 5.2 Override proportions

**Table 4. Override O_mj on CONF1 (both adjudicators A or B, out of 50).** Source: `data/conf_upgrade/RESULTS_confirmatory.md`. "excl" marks cells excluded from confirmatory tests; p10 is shown for completeness only.

| Model | p01 XENON1T | p02 GERDA | p03 Adv. Virgo | p05 SNO | p09 NEMO-3 | Mean O (included) | p10 Borexino (suspended) |
|---|---|---|---|---|---|---|---|
| Sonnet 4.5 | 0/50 | 14/50 | 50/50 | 43/50 | 0/50 | 0.428 | 1/50 |
| Haiku 4.5 | 0/50 | 2/50 | 39/50 | 3/50 | 0/50 | 0.176 | 0/50 |
| Opus 4.5 | 0/50 | 12/50 | 43/50 | 21/50 | 1/50 | 0.308 | 2/50 |
| Sonnet 4.6 | 0/50 | 19/50 | 46/50 | 13/50 | 0/50 | 0.312 | 13/50 |
| Haiku 5.5 | 0/50 | 19/50 | 41/50 (excl) | 19/50 | 0/50 | 0.190 (4 units) | 0/50 |
| Sonnet 5.5 | 2/50 | 0/50 | 31/50 | 0/50 | 8/50 | 0.164 | 0/50 |
| Opus 5.5 | 2/50 | 0/50 | 0/50 | 0/50 | 0/50 | 0.008 | 0/50 |

Override is concentrated in two units. On p03 (Advanced Virgo) it occurs in 31–50 of 50 responses for every model except Opus 5.5 (0/50). On p05 (SNO) it reaches 43/50 for Sonnet 4.5. On p01 (XENON1T) and p09 (NEMO-3) override is at or near zero for every model, with a maximum of 8/50 (Sonnet 5.5 on p09). Spot checks of override cards found genuine cases, for example a 7–8 m filter cavity proposed despite the stated loss floor, and LAB with ballast despite the statement that the sphere is restrained (`RESULTS_SUMMARY.md`).

### 5.3 H1: fixed sequence

**Table 5. H1 fixed-sequence test** (one-sided, H0: O ≤ 0.10, α = 0.05). Source: `data/conf_upgrade/RESULTS_confirmatory.md`.

| Step | Model | Units | Mean O | t | One-sided p | Decision | Sensitivity p (disagreement = override) |
|---|---|---|---|---|---|---|---|
| 1 | Sonnet 4.5 | 5 | 0.428 | 1.54 | 0.0987 | **not rejected** | 0.0583 |
| 2 | Haiku 4.5 | 5 | 0.176 | 0.50 | 0.3211 | not tested (sequence stopped) | 0.2302 |
| 3 | Opus 4.5 | 5 | 0.308 | 1.32 | 0.1293 | not tested | 0.0717 |
| 4 | Sonnet 4.6 | 5 | 0.312 | 1.25 | 0.1391 | not tested | 0.0970 |
| 5 | Haiku 5.5 | 4 | 0.190 | 0.82 | 0.2360 | not tested | 0.2089 |
| 6 | Sonnet 5.5 | 5 | 0.164 | 0.54 | 0.3078 | not tested | 0.2275 |
| 7 | Opus 5.5 | 5 | 0.008 | −11.50 | 0.9998 | not tested | 0.9990 |

At the first step, Sonnet 4.5 had the highest mean override (0.428), but the one-sided t-test across five units (df = 4) gave p = 0.0987. **H1 is not rejected at the first step, the sequence stops, and no confirmatory per-model claim is made.** The p-values for steps 2–7 are descriptive only. The pre-registration specified Holm-adjusted p-values as secondary for models after the first non-rejection [CHECK: Holm-adjusted values not reported in the results file]. The sensitivity analysis that counts disagreements as override also does not reject at step 1 (p = 0.058). Every test in this study carries the pre-registered label **"small unit count"** (fewer than 8 included units). The pre-registered power for the first test at 5 units was 0.80–0.86 at O = 0.24 with between-unit SD τ = 0.5 (`data/conf_kpremise/kpremise_results.md`, citing `power/power_small_J_results.md`). The observed failure to reject comes from between-unit heterogeneity rather than a low mean (Section 5.2): Sonnet 4.5's unit-level rates were 0, 0.28, 1.00, 0.86 and 0.

**Secondary (pre-specified, not confirmatory).** The pooled override rate, computed as unit means over models, was 0.241 (t = 1.13, one-sided p = 0.161, 5 units). It does not exceed 0.10 at α = 0.05.

### 5.4 H2: models differ

The likelihood-ratio test of the model fixed effect in a binomial GLMM with a unit random intercept gave **LR = 299.96, df = 6, p = 8.4 × 10⁻⁶²**, with an estimated unit SD of 1.29 on the logit scale. Both the full and null models converged. **H2 is confirmed.**

**Table 6. GLMM model effects** (logit, and marginal override probability at the median unit, u = 0).

| Model | Logit | P(override) at u = 0 |
|---|---|---|
| Sonnet 4.5 | 0.09 | 0.521 |
| Haiku 5.5 | −0.65 | 0.343 |
| Sonnet 4.6 | −0.90 | 0.289 |
| Opus 4.5 | −0.94 | 0.282 |
| Haiku 4.5 | −2.46 | 0.079 |
| Sonnet 5.5 | −2.62 | 0.068 |
| Opus 5.5 | −6.59 | 0.001 |

The ordering does not follow a simple scale or generation trend. Opus 5.5 almost never overrides (2 of 250 included responses), and Sonnet 5.5 and Haiku 4.5 are low. Haiku 5.5, Sonnet 4.6 and Opus 4.5 are intermediate, and Sonnet 4.5 is highest. The ordering of Sonnet 4.5 > Sonnet 4.6 > Opus 5.5 matches the pilot on separate instruments (26%/22%, 8%/6%, 0%/0%; `pilot/PILOT_SUMMARY.md`).

