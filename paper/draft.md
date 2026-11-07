# Hindsight contamination in AI-assisted detector design: a pre-registered test of whether language models reproduce historically adopted upgrades when stated physics rules them out

**Lyuhong Ju** [affiliation TBD]

*Draft manuscript, 2026-11-07. Study pre-registered as `PREREGISTRATION.md` v4.3 and frozen at commit `8009881` of github.com/lyuhongju1/hindsight-contamination.*

---

## Abstract

Language models are increasingly asked to propose upgrades to physics instruments whose upgrade histories they may recall. We ask whether models reproduce the historically adopted upgrade when the problem states physics under which it fails, and when the same model answers that physics correctly in isolation. We call this *override*. In a public pre-registration, we built *conflict twins*: invented instruments matched to a real baseline in which a minimal, plainly stated physical fact makes the adopted item fail while at least one credible alternative survives. Item selection was mechanical: an INSPIRE-derived frame, two independent dating agents plus a quote verifier, and author and red-team agents working under fixed rules with randomized robustness checks. Of 21 real baseline–upgrade pairs taken through authoring, 15 admitted no honest physics-only conflict; 6 did, and 5 passed a pre-registered constraint-knowledge check. We sampled seven Anthropic models (50 responses per description per model). Two non-study models adjudicated the responses blind (Cohen's κ = 0.69). The first confirmatory test in the pre-registered fixed sequence (Sonnet 4.5, mean override 0.43 against a null of 0.10) was not rejected (one-sided p = 0.099), so no per-model confirmatory claim is made. Models differed strongly (likelihood-ratio test, LR = 300, df = 6). Override was concentrated in two of five units, and the newest Opus model almost never overrode. A pre-specified GLMM sensitivity analysis disagrees with the primary test; we report both. The low yield of physics-decidable upgrades limits how much contamination tests of this kind can show.

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

The protocol was publicly pre-registered rather than submitted as a journal Registered Report (PI decision, 2026-11-06; `PREREGISTRATION.md`, "Route"). Version 4.3 is frozen by the public commit that adds `FREEZE_MANIFEST.md`. The manifest holds SHA-256 hashes of the pre-registration, every description, key, K-probe and rubric, the scoring regexes, the templates, the harness and the analysis and power scripts. The commit precedes all confirmatory upgrade and identification sampling. The only confirmatory-model calls made before the freeze were the K premise check (`FREEZE_MANIFEST.md`, preamble). The frozen state is commit `8009881` (`RESULTS_SUMMARY.md`). The pre-registration text also refers to git tags (`prereg-v4.2-frozen`, `prereg-v4.3-frozen` "if permitted") (no git tag was created; pushing tags was outside the project's permitted operations, so the freeze is defined by the manifest commit 8009881).

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
| Baselines assessed for eligibility by two daters | 25 in rounds 1–3, plus 8 in the resumed queue | (33 distinct baselines; the resumed queue entries q19, q23, q26, q27, q30, q34, q37 and q38 were not among the first 25) |
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
| Recorded only as "author/feasibility + batched confirmation" | p19 CUORE-0 → CUPID (Li2MoO4 bolometers) | zero-unit after a full attempt under C1 (no survivor meets a background index strict enough for 2νββ pile-up to robustly defeat Li2MoO4: ZnSe's demonstrated background is 5–20× too high, TeO2 sits below the 208Tl line; other routes favour the item; `materials/p19_cuore0/redteam/report_r1.md`) |
| | p20 EXO-200 → nEXO (VUV SiPMs) | (the only separating route, SiPM dark counts under a few-photon light-only trigger, has no survivor: APDs fail the threshold and VUV PMTs fail the background goal; `materials/p20_exo200/redteam/report_r1.md`) |
| | p21 MAGIC → MAGIC-II (increased-QE PMTs) | (the Cherenkov-weighted QE advantage of GaAsP HPDs is only ~1.3–1.5×, timing differs < 2×, and afterpulsing is defeated by trigger settings; `materials/p21_magic/redteam/report_r1.md`) |

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

**Screen misses.** Of 398 audited non-hits, 13 (about 3%) were coded as overrides by both adjudicators and are counted (`RESULTS_SUMMARY.md`). The audit samples min(10, available non-hits) per CONF × model, so cells with fewer than 10 non-hits contribute fewer; 398 is the realised total over the six sampled pairs (`analysis/conf_cards.py`). Unaudited non-hits are not adjudicated, so O is a slight lower bound.

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

At the first step, Sonnet 4.5 had the highest mean override (0.428), but the one-sided t-test across five units (df = 4) gave p = 0.0987. **H1 is not rejected at the first step, the sequence stops, and no confirmatory per-model claim is made.** The p-values for steps 2–7 are descriptive only. The pre-registration specified Holm-adjusted p-values as secondary for models after the first non-rejection Holm-adjusted p-values (secondary, descriptive): Sonnet 4.5 0.691; Opus 4.5 0.776; Sonnet 4.6 0.776; Haiku 4.5, Haiku 5.5 and Sonnet 5.5 0.944; Opus 5.5 1.000.. The sensitivity analysis that counts disagreements as override also does not reject at step 1 (p = 0.058). Every test in this study carries the pre-registered label **"small unit count"** (fewer than 8 included units). The pre-registered power for the first test at 5 units was 0.80–0.86 at O = 0.24 with between-unit SD τ = 0.5 (`data/conf_kpremise/kpremise_results.md`, citing `power/power_small_J_results.md`). The observed failure to reject comes from between-unit heterogeneity rather than a low mean (Section 5.2): Sonnet 4.5's unit-level rates were 0, 0.28, 1.00, 0.86 and 0.

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

---

## 6. Exploratory results

Everything in this section is exploratory and was computed after the freeze. Where an analysis was pre-specified (as an exploratory question or as a sensitivity analysis), we say so. Otherwise it is post hoc. None of these analyses changes the confirmatory conclusions in Section 5. Sources: `data/conf_upgrade/RESULTS_exploratory.md` (E1–E6), `RESULTS_base_exploratory.md`, `data/conf_identify/RESULTS_recognition.md`, `data/conf_adj_stress/RESULTS_adjudication_stress.md`.

### 6.1 Knowledge–override dissociation (E1; post hoc)

For each model × unit cell we cross-tabulated the K-probe result (correct out of 20) against override (out of 50). We marked a cell as a **strong dissociation** if K ≥ 15/20 and override ≥ 10/50: the model answers the isolated physics question correctly at least three times in four, yet commits to the failing historical item in at least a fifth of design responses. **12 of 35 cells** met this criterion:
- p02 GERDA: Sonnet 4.5, Opus 4.5, Sonnet 4.6, Haiku 5.5;
- p03 Advanced Virgo: Sonnet 4.5, Opus 4.5, Sonnet 4.6, Sonnet 5.5;
- p05 SNO: Sonnet 4.5, Opus 4.5, Sonnet 4.6, Haiku 5.5.

Examples: Sonnet 4.5 on p05 was 20/20 correct on K and overrode in 43/50; Opus 4.5 on p03 was 20/20 and 43/50. The thresholds were chosen after the data, so the count of 12 is descriptive. The pattern matches the pilot, where Sonnet 4.5 misstated physics in the direction of the historical answer while answering the same physics correctly in isolation (F5, F8). We have not yet systematically coded category-A misstatements in the confirmatory data, although that analysis was pre-specified (`PREREGISTRATION.md` §6) (no systematic qualitative analysis of category-A misstatements was performed; this pre-specified exploratory item is listed as not done in Section 11).

### 6.2 GLMM sensitivity analysis for H1 (E4; pre-specified)

The pre-registration specified a binomial GLMM with a unit random intercept as a sensitivity analysis for H1. For each model it was fitted separately, and the marginal override rate was tested against 0.10 by likelihood ratio (one-sided).

**Table 7. GLMM version of H1.**

| Model | Units | Marginal O (GLMM) | LR vs 0.10 | One-sided p |
|---|---|---|---|---|
| Sonnet 4.5 | 5 | 0.159 | 13.91 | 0.0001 |
| Haiku 4.5 | 5 | 0.164 | 2.00 | 0.0786 |
| Opus 4.5 | 5 | 0.238 | 4.20 | 0.0202 |
| Sonnet 4.6 | 5 | 0.166 | 5.28 | 0.0108 |
| Haiku 5.5 | 4 | 0.073 | 42.86 | 1.0000 |
| Sonnet 5.5 | 5 | 0.046 | 0.00 | 0.5000 |
| Opus 5.5 | 5 | 0.009 | 0.37 | 0.7276 |

**This analysis disagrees with the primary test.** For Sonnet 4.5, the first model in the sequence, the GLMM rejects O ≤ 0.10 (p = 0.0001), whereas the pre-registered t-test does not (p = 0.099). If the GLMM had been the primary test, the fixed sequence would have rejected at step 1 and stopped at step 2 (Haiku 4.5, p = 0.079). We report the pre-registered t-test as the confirmatory result, and **H1 remains not supported**. We do not reinterpret the study on the basis of the sensitivity analysis.

Three features of the comparison should be noted.
- **The two tests target different estimands.** The t-test compares the arithmetic mean of unit-level proportions (0.428 for Sonnet 4.5) with 0.10. The GLMM's "marginal O" here is a model-based quantity (0.159 for Sonnet 4.5), far below the arithmetic mean. With rates near 0 on two units and near 1 on others, a logit random-intercept model and a mean of proportions summarize the same data very differently.
- **The t-test is conservative.** The pilot power simulation showed it has type I error at or below 0.025 (`PREREGISTRATION.md` §6). The GLMM's inference with five clusters and strongly bimodal unit effects rests on asymptotic likelihood-ratio approximations, which may be unreliable at this cluster count.
- **One row looks anomalous.** For Haiku 5.5 the LR statistic is large (42.86), but the estimate is below 0.10, so the one-sided p is 1.00 (confirmed: the LR statistic is two-sided in magnitude; the one-sided p uses the sign of the estimate relative to 0.10, so a large LR with an estimate below 0.10 gives p ≈ 1; `analysis/exploratory.py`, E4). The per-model GLMM estimates also differ from the H2 GLMM's marginal probabilities at u = 0 (Table 6; e.g. 0.521 vs 0.159 for Sonnet 4.5), because the H2 model shares the unit effects across all seven models (the marginal O is the population-averaged override probability, integrating the logistic curve over the fitted unit random-intercept distribution by Gauss–Hermite quadrature; `analysis/exploratory.py`).

### 6.3 Templates (E5; pre-specified)

Override pooled over the 34 included cells was similar across the five templates: T1_detector 73/340 (0.215), T2_instrument 77/340 (0.226), T3_review 79/340 (0.232), T4_proposal 85/340 (0.250) and T5_plain 73/340 (0.215). No formal test was run.

### 6.4 Leave-one-unit-out (E6; post hoc)

Refitting the H2 test with each unit left out in turn gave LR between 142.5 (without p03) and 330.3 (without p01), all on df = 6, with p ≤ 3 × 10⁻²⁸. The model effect does not depend on any single unit. It is weakest without p03, the unit with the most override.

### 6.5 Recall traces (E2; post hoc)

We counted CONF1 responses whose full text matched the identity regex, i.e. named the real baseline or successor programme. Counts are pooled over all seven models, including the K-excluded Haiku 5.5 cell on p03.

| Unit | Override responses naming the real programme | Non-override responses naming it |
|---|---|---|
| p01 XENON1T | 2/4 | 91/346 |
| p02 GERDA | 28/66 | 84/284 |
| p03 Adv. Virgo | 55/250 | 7/100 |
| p05 SNO | 40/99 | 83/251 |
| p09 NEMO-3 | 8/9 | 81/341 |

Naming the real programme is more common among override responses than non-override responses on p02, p03, p05 and p09. Many overrides are made without naming it, especially on p03 (55 of 250). The identity regex is broad (Section 6.6), and naming is neither necessary nor sufficient for recall, so these counts are suggestive only.

### 6.6 Recognition (E3; pre-specified, two-sided)

In the identification probe (n = 20 per cell; `data/conf_identify/RESULTS_recognition.md`), the invented BASE and CONF1 twins were recognized as the real instrument in most cells. For p02, p03 and p10, every model identified every description at 20/20, except for the p10 CONF1 cells of Sonnet 4.5 (8/20), Sonnet 4.6 (13/20) and Sonnet 5.5 (16/20). Recognition was lowest for Haiku 4.5 on p01 (BASE 1/20, CONF1 3/20) and p09 (BASE 2/20, CONF1 3/20). Disguise therefore largely failed, as in the pilot (F1, F2, F4). The identity regex is broad, so these rates are upper bounds (`RESULTS_SUMMARY.md`).

Across the 35 model × unit cells, CONF1 recognition and override were not correlated (Spearman ρ = 0.07, two-sided p = 0.673). With recognition near ceiling in most cells, this test has little range to work with. It does not show that recognition is irrelevant. It does show that high recognition is not sufficient for override: Opus 5.5 recognized every CONF1 at 20/20 and overrode in 2 of 250 included responses.

### 6.7 BASE adoption (pre-specified, descriptive)

**Table 8. BASE adoption** (both adjudicators code the response as proposing *a*, out of 50; audited non-hits included). Source: `data/conf_upgrade/RESULTS_base_exploratory.md`.

| Pair | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Sonnet 4.6 | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|---|---|---|---|
| p01 XENON1T | 0 | 0 | 4 | 1 | 0 | 35 | 50 |
| p02 GERDA | 50 | 1 | 50 | 49 | 50 | 44 | 50 |
| p03 Adv. Virgo | 49 | 29 | 50 | 50 | 50 | 48 | 50 |
| p05 SNO | 46 | 2 | 50 | 49 | 46 | 50 | 50 |
| p09 NEMO-3 | 0 | 0 | 0 | 0 | 0 | 10 | 32 |
| p10 Borexino | 1 | 0 | 3 | 20 | 0 | 43 | 47 |

Two descriptive patterns stand out.
- **Opus 5.5 shows the pattern the design treats as ideal.** It adopts the item when it is sound (32–50/50 at BASE) and almost never when stated physics rules it out (0–2/50 at CONF1).
- **Override follows BASE adoption.** Sonnet 4.5 overrides on exactly the units where it adopts the item at BASE (p02, p03, p05; 46–50/50 at BASE). It never adopts the item on p01 or p09, at either level. More generally, among the included cells, none with BASE adoption of 4/50 or below shows CONF1 override above 3/50 (Tables 4 and 8). Override is concentrated where the model already has a strong preference for the historical choice.

This is consistent with override being a *persistence* of a prior preference against stated physics. It cannot separate a preference rooted in recalled history from one rooted in the item's general attractiveness; that question motivates the negative control (Section 7). The pilot found a "fallback to history" pattern, in which Sonnet 4.5 proposed the historical item *more* often under conflict than at BASE (Auger, 22% vs 10%; F11). In the confirmatory data, CONF1 override exceeds BASE adoption in five included cells. Four differ by a single response: Sonnet 4.5 on p03 (50 vs 49), Haiku 4.5 on p02 (2 vs 1) and p05 (3 vs 2), and Opus 4.5 on p09 (1 vs 0). The fifth, Haiku 4.5 on p03 (39/50 override vs 29/50 BASE adoption), is the only sizeable instance. We do not interpret it further. We did not compute R = O/B, which is ill-behaved when B is small (F11). The pre-registered comparison of K-gated with ungated override is not reported separately here (cell-by-cell comparison of Sections 5.2 and 6.7). The only ungated cells on the five units are Haiku 5.5 on p03 (41/50).

### 6.8 Adjudication stress test (post hoc)

To probe the dependence of the override count on the two adjudicators, we re-coded 216 stratified CONF1 cards: per unit, up to 20 cards both adjudicators coded as override, 20 neither did, and 20 split (`data/conf_adj_stress/RESULTS_adjudication_stress.md`). Two additional codings were made:
- **C**, a third adjudicator model (labelled "Opus 5" in the results file (`claude-opus-5`));
- **A2**, adjudicator A with a reworded rubric and a reversed code table.

| Check | Agreement |
|---|---|
| C vs A, override yes/no | 191/216 (0.88) |
| C vs B, override yes/no | 180/216 (0.83) |
| A2 vs A, override yes/no | 206/216 (0.95) |
| C vs A, exact code | 180/216 (0.83) |
| A2 vs A, exact code | 193/216 (0.89) |

By original stratum, C coded override on 67 of 73 "both" cards, 3 of 100 "none" cards and 17 of 43 "split" cards. A2 coded override on 73/73, 4/100 and 21/43. Override calls on which both original adjudicators agreed were mostly reproduced by a third model and by a reworded rubric. The split cards divide roughly evenly. Override is a judgement about whether a stated workaround is valid (Section 4.4), and that boundary is where model adjudicators disagree. All of these are model–model checks.

---

### 6.9 K-gated versus ungated override (pre-specified exploratory)

| Model | K-gated mean O (units) | Ungated mean O, all 6 units incl. suspended p10 | Ungated one-sided p |
|---|---|---|---|
| Sonnet 4.5 | 0.428 (5) | 0.360 | 0.111 |
| Haiku 4.5 | 0.176 (5) | 0.147 | 0.364 |
| Opus 4.5 | 0.308 (5) | 0.263 | 0.143 |
| Sonnet 4.6 | 0.312 (5) | 0.303 | 0.101 |
| Haiku 5.5 | 0.190 (4) | 0.263 | 0.140 |
| Sonnet 5.5 | 0.164 (5) | 0.137 | 0.364 |
| Opus 5.5 | 0.008 (5) | 0.007 | 1.000 |

Gating changes no conclusion. Including the suspended Borexino unit lowers most means, because override there is low except for Sonnet 4.6 (13/50).

## 7. Negative control (follow-up, separately pre-registered)

### 7.1 Rationale and design

The main study shows that some models persist with an item that stated physics rules out. It does not show that the item's *historical* status is what makes them persist. An attractive, plausible fix might be just as sticky whether or not a collaboration ever adopted it. Negative control NC1 (`negative_control/NC_DESIGN.md`) addresses this. It was written on 2026-11-07, **after** the main confirmatory results and before any NC material or sample existed. It is a separate follow-up and does not alter the main results. It becomes binding when frozen by a public commit adding `negative_control/NC_FREEZE_MANIFEST.md`, before any NC sampling (made: commit c6ec5fb, `negative_control/NC_FREEZE_MANIFEST.md`, before any NC_CONF sample).

The question is whether models abandon a **non-historical** choice more readily than the historically adopted one when stated physics defeats each.

For each confirmatory unit u:
- **NC_BASE(u)** is the main CONF1(u), already sampled. In CONF1 the adopted item fails, and the documented non-adopted alternative alt(u) is a sound survivor. This makes alt(u) the natural recommendation, with no historical support.
- **NC_CONF(u)** is CONF1(u) with one more minimal edit, under which:
  - alt(u) also fails robustly (keylib, ×0.5–2);
  - the adopted item still fails;
  - at least one third option survives.

All authoring rules, the lessons and C1 apply, a red team checks each NC_CONF, and each NC_CONF has a K-probe with the same suspension rule as the main study.

**Measures.**
- B_alt(m, u) is the share of main CONF1 responses whose TOP RECOMMENDATION is alt(u), coded ALT / OTHER / X by the two blind adjudicators.
- O_alt(m, u) is the share of NC_CONF responses that commit to alt(u) without a valid fix.
- These are compared with the main study's B_adopted (BASE adoption) and O_adopted (CONF1 override).

**Primary NC test (as designed for several units).** A binomial GLMM on the pooled main-CONF1 and NC_CONF responses, `override ~ historical + logit(B_target) + model + (1 | unit)`, with B_target clipped to [0.02, 0.98], and a one-sided Wald test that the coefficient of `historical` is positive (α = 0.05). A positive coefficient means that, at a matched baseline preference, models persist more with the historical item than with the non-historical one.

### 7.2 Authoring outcome (Amendment NC-A1)

Authoring ended with **4 of 5 units NC-zero** (`negative_control/NC_DESIGN.md`, Amendment NC-A1, 2026-11-07, after authoring and before any NC sampling):

| Unit | NC outcome | Recorded reason |
|---|---|---|
| p01 XENON1T | NC-zero | no third option without the historical item |
| p02 GERDA | NC-zero | the only robust survivor contains underground argon |
| p03 Advanced Virgo | NC-zero | nothing besides EPR and an external cavity rotates the squeezing across the band |
| p05 SNO | NC-zero | no transparent near-water-density fill besides PXE |
| p09 NEMO-3 | NC_CONF authored; red team CLEARED; sampled | separation edited from 15 to 6 cm; alt(u) = 3-inch directly coupled cells; survivors SiPM arrays and 1-inch PMTs |

This mirrors the main funnel. Once both the historical item and its documented alternative are ruled out, real design spaces rarely leave an honest third option.

Because a unit random intercept cannot be estimated from one unit, NC-A1 specifies that, if only p09 qualifies, the primary NC test becomes a within-unit fixed-effects logistic regression on the p09 CONF1 responses (target = the 8-inch item) and the p09 NC_CONF responses (target = alt): `override ~ historical + logit(B_target) + model`, with a one-sided Wald test of `historical` > 0 at α = 0.05. The result will be labelled a single-unit control that cannot generalize across units. B_alt(m) will be coded on all 350 p09 CONF1 responses. Note that p09 is the unit where the main study saw almost no override of the adopted item (Table 4: 0–8/50), so the contrast is between two low rates, and its power will be limited. A null result will be reported as inconclusive, not as evidence against hindsight (`NC_DESIGN.md`, "Limits stated in advance").

### 7.3 Results

**Outcome: inconclusive (floor effect).** The NC twin passed its red team and the K premise (all 7 models majority-correct, 15–20/20), and was frozen (commit c6ec5fb) before sampling. All 350 NC_CONF responses and all 350 NC_BASE responses (the main p09 CONF1 responses) were coded blind by the two adjudicators (`data/conf_nc_cards/RESULTS_nc.md`).

| Model | B_adopted (BASE) | O_adopted (CONF1) | B_alt (NC_BASE) | O_alt (NC_CONF) |
|---|---|---|---|---|
| Sonnet 4.5 | 0/50 | 0/50 | 0/50 | 0/50 |
| Haiku 4.5 | 0/50 | 0/50 | 0/50 | 0/50 |
| Opus 4.5 | 0/50 | 1/50 | 0/50 | 0/50 |
| Sonnet 4.6 | 0/50 | 0/50 | 0/50 | 0/50 |
| Haiku 5.5 | 0/50 | 0/50 | 0/50 | 0/50 |
| Sonnet 5.5 | 10/50 | 8/50 | 2/50 | 1/50 |
| Opus 5.5 | 32/50 | 0/50 | 21/50 | 0/50 |

**Pre-specified test (NC-A1).** `historical` coefficient −0.035 (SE 1.12), z = −0.03, one-sided p = 0.51. There were 700 responses and 10 overrides.

The control cannot discriminate, for two reasons:
- Five of seven models essentially never chose either the historical item or the 3-inch alternative on this unit, so there is no preference whose persistence could be compared.
- p09 is also the unit with the lowest main-study override.

As stated in advance, this null is reported as **inconclusive, not as evidence against hindsight**. The informative finding of the negative-control effort is the authoring outcome (Section 7.2): once the historical item and its documented alternative are both excluded, real design spaces rarely leave an honest third option. A more informative control would need units where models hold a strong prior for a non-historical choice.

---

## 8. Discussion

### 8.1 What the study shows

1. **Override of stated physics by a historically adopted choice occurs, at high rates, in some models on some units.** In 12 of 35 model × unit cells, a model that answered the isolated physics question correctly (at least 15/20) committed to the failing historical item in at least 10 of 50 design responses. On Advanced Virgo, six of seven models overrode in 31–50 of 50 responses. Two of these cells had lower K scores: Haiku 4.5 at 11/20, and Haiku 5.5 at 10/20, which is K-excluded.
2. **Models differ sharply (H2, confirmatory).** The difference does not depend on any single unit (Section 6.4). Opus 5.5 overrode in 2 of 250 included responses while adopting the item at BASE in most responses, which is the pattern the design treats as ideal. The pilot ordering of Sonnet 4.5, Sonnet 4.6 and Opus 5.5 replicated on new instruments.
3. **Override is unit-dependent, and the confirmatory per-model claim fails for that reason.** The pre-registered H1 test for the first model was not rejected (p = 0.099). The pre-specified GLMM sensitivity analysis would have rejected it (p = 0.0001). We follow the pre-registered primary analysis and do **not** claim that any model's average override rate exceeds 10%. The pooled secondary test was also not significant (p = 0.161). With five units, two near 0 and others near 1 for some models, the population-level override rate is poorly determined.
4. **Disguise fails, and recognition does not predict override across cells.** Invented twins were mostly recognized as the real instrument. The most consistent recognizer, Opus 5.5, was the least likely to override. Recognition alone is not sufficient for override.
5. **The funnel is a finding.** Of 21 mechanically selected, verified real upgrade decisions, 15 admitted no honest physics-only conflict under the rules, and the negative control shows the same scarcity one level deeper (4 of 5 units NC-zero). Most real upgrade choices in this frame were decided by engineering, cost, tunable settings or added capability, not by a physical requirement that the alternative fails. Tests of this kind are therefore restricted, by construction, to a minority of real decisions, and that minority is chosen by the item's physics and not by any model behaviour.

### 8.2 What the study does not show

- **No causal claim about memorization.** The study has no injection or training-data arm (`PREREGISTRATION.md` §1). "Hindsight contamination" here names a behavioural pattern: commitment to the historical item against stated physics. Recall traces (Section 6.5) and the BASE-adoption pattern (Section 6.7) are consistent with a role for recalled history. They are equally consistent with a general preference for the item that would persist whether or not it was historical. The negative control is designed to separate these, but on a single unit at most.
- **No per-model confirmatory claim** (H1 not rejected).
- **No claim beyond one vendor.** All seven models are from Anthropic; the planned non-Anthropic model was not added. Model differences may reflect training choices specific to this vendor.
- **No claim about all detector upgrades.** The confirmatory population is "baseline–upgrade pairs whose counted item admits an honest physical conflict" (Amendment A2). That population was 6 of 21 worked pairs.
- **No claim about human-validated coding.** Adjudication was by two models, κ = 0.69 between them, with no human coding.

### 8.3 Interpretation

The data fit a picture in which override is a persistence effect. Models that strongly prefer an item when it is sound tend to keep proposing it when a plainly stated fact rules it out, even though they answer the relevant physics correctly in isolation. Models also differ in how strongly stated requirements override that prior preference. Whether the preference is strong *because* the item is historical cannot be decided from these data. For users of AI design assistants, the practical point is narrower and better supported: on familiar instruments, some current models will recommend the well-known historical upgrade in a substantial fraction of responses even when the stated requirements rule it out, and this varies strongly between models and between instruments.

---

## 9. Limitations

1. **Small unit count.** Five confirmatory units (four for Haiku 5.5), against a pre-registered target of 14 and minimum of 10. Every test carries the pre-registered "small unit count" label. Between-unit heterogeneity is large (GLMM unit SD 1.29 on the logit scale), and the t-test across five units has df = 4.
2. **Disagreement between the primary and sensitivity analyses** (Section 6.2). The conclusion about H1 depends on the choice of test. The primary test was fixed in advance and is the one we report.
3. **Single vendor.** All study models are Anthropic models, and the two adjudicators and the agents that built the materials are also Anthropic models. A shared bias in physics judgement between material builders, adjudicators and study models cannot be excluded.
4. **Model–model adjudication.** κ = 0.69, with disagreements concentrated on whether a stated fix is valid (B vs C, 87 cards). The stress test (Section 6.8) shows the "both agree" override calls are stable, while the split cards are not. No human coding was done. The pilot summary recommended a human spot-check of the conflict keys by the PI (not done: by design the study used no human roles; this is a limitation).
5. **Screen-based lower bound.** Only screened hits and a random sample of non-hits were adjudicated. 13 of 398 audited non-hits were overrides, so O slightly underestimates the true rate.
6. **Materials built by models.** Descriptions, keys, K-probes and rubrics were written by author agents and checked by red-team agents and scripts. The robustness check verifies each key's internal logic, not its premise. The K premise check caught a premise disagreement in the pilot, and it suspended p10 here for what appear to be model errors.
7. **Recognition is near ceiling.** Recognition varies too little to test its role in override, and the identity regex is broad.
8. **Scope restriction by physics decidability.** Results apply to upgrades that trade one physical property for another. They may not transfer to the majority of real upgrade decisions, which turn on engineering and cost.
9. **Adoption status.** Some items were never built (p02 approved but not built, unverified; p10 cancelled). The study measures reproduction of a recorded collaboration choice, whether or not construction followed (A1 addendum 3).
10. **Settings.** Temperature 1.0 with minimal reasoning. Override rates at other reasoning settings were not measured.

---

## 10. Methods details and reproducibility

**Roles of agents and models (conduct disclosure).** As disclosed in the pre-registration (`PREREGISTRATION.md` §8), every material, key, date, screening decision, adjudication and analysis was produced by Claude agents and models under the frozen protocol. The PI designed the question, approved the protocol and is accountable for the paper. Specifically:
- **screening**: two independent screening agents applied criterion I1 to the INSPIRE frame;
- **dating**: two independent dating agents (D1, D2) made dated claims for each assessed baseline, checked by a verifier script;
- **authoring**: author agents wrote dossiers, descriptions, keys, K-probes and notes under `materials/AUTHOR_BRIEF.md`;
- **red-teaming**: red-team agents under `materials/REDTEAM_BRIEF.md` reviewed every BASE and CONF;
- **adjudication**: two models outside the study set, `claude-fable-5-1` and `claude-opus-4-8`, coded each card in an independent request;
- **orchestration and analysis**: an orchestrating Claude session ran the pipeline, logged its decisions in `RUNBOOK.md`, and ran the analysis scripts.

**Pilot.** Before the confirmatory study, a pilot on two excluded instruments (T2K ND280 → SuperFGD 3D-cube target; Auger → AugerPrime surface scintillators) used three models, 4 author and 6 red-team rounds, about 1,900 identification and K responses, about 2,700 upgrade responses and 144 blind adjudication cards (κ = 0.97; `pilot/PILOT_SUMMARY.md`). The pilot produced the design changes adopted before the freeze:
- recognition measured rather than gated (F1, F2, F4);
- a forced final line (F5);
- at least one survivor rather than two (F6);
- adjudication codes including a valid-workaround category (F8, F11);
- the K premise check with a forced verdict (F9, F10);
- H1 stated on the absolute override rate O rather than R (F11).

**Analysis.** H1, H2 and the secondary test follow `PREREGISTRATION.md` §6. The K premise analysis is `analysis_kpremise.py`, and adjudication is `analysis/adjudicate.py`. Confirmatory: `analysis/conf_cards.py` and `analysis/conf_analysis.py` (committed in 2390733 before any confirmatory data were read). Exploratory: `analysis/exploratory.py`, `analysis/conf_identify.py`, `analysis/adjudication_stress.py`. Negative control: `analysis/nc_kpremise.py`, `analysis/nc_pipeline.py`.. The power simulations are `power/power_override.py` and `power/power_small_J.py`.

**Reproducibility statement.** All materials, briefs, logs, regexes, rubrics, templates, harness code and analysis code are in the public repository **github.com/lyuhongju1/hindsight-contamination**.
- The confirmatory protocol (v4.3) is frozen at commit **8009881**. Its `FREEZE_MANIFEST.md` (generated 2026-11-06 21:45:11 EST) lists SHA-256 hashes for 58 files: the pre-registration, the K premise analysis and gate, the author and red-team briefs, the gate script, each unit's rubric, four descriptions, key and K-probe, the scoring regexes and their tests, the harness (`batch.py`, `keylib.py`, `score.py`), the templates, the power scripts, Amendment A1 and the selected-pairs file.
- The pair-selection rules were frozen earlier, at commit `721e55f`.
- Raw responses, adjudication cards and labels are released after collection (`PREREGISTRATION.md` §8) (all raw responses, cards, keys and labels are in the public repository; the commit current at submission will be cited).
- A Zenodo snapshot may be added (not yet created; requires the PI's account).
- The negative control was frozen by a separate manifest, `negative_control/NC_FREEZE_MANIFEST.md` (commit c6ec5fb), before NC sampling.
- Line-ending conversion was disabled in the repository so that hashes are byte-stable (`RUNBOOK.md`, 2026-11-05).

---

## 11. Deviations from the pre-registration

All amendments and implementation notes are listed with their dates and their timing relative to the data. "Confirmatory data" means confirmatory upgrade or identification samples. The K premise check, which used confirmatory models on K-probes only, preceded the freeze by design.

**Table 9. Amendments, clarifications and implementation notes.**

| # | Change | Date | Timing | Source |
|---|---|---|---|---|
| 1 | Pilot-driven redesign, from design v2/v3 to v4/v4.1/v4.2: recognition measured not gated; override-primary H1 on absolute O; ≥ 1 survivor; forced final lines; K premise check | 2026-11-05 to 06 | Before the selection rules were frozen and before any confirmatory data; pilot data only | `pilot/findings.md`; `PREREGISTRATION.md` "Basis" |
| 2 | **Amendment A1**: sequential seeded draw in place of assess-all-then-draw; same seed and caps | 2026-11-06 | Before any eligibility (I2–I6) assessment and before any draw | `search/AMENDMENT_A1.md` |
| 3 | A1 addendum: I6 boundary fixed at commitment ≤ 2023-06-30 | 2026-11-06 | Before any eligibility assessment | same |
| 4 | A1 addendum 2: one baseline per programme lineage (Virgo 2012 and GERDA 2012 skipped) | 2026-11-06 | Before round 2 of selection | same |
| 5 | A1 addendum 3: "adopted" means the collaboration's chosen plan; adoption_status recorded as an exploratory covariate | 2026-11-06 | Before round-3 selection | same |
| 6 | Author-brief lessons 1–6 (application of rules 1, 7, 8) | 2026-11-06 | During materials; before any confirmatory data | `materials/AUTHOR_BRIEF.md` |
| 7 | **Amendment A2**: zero-unit pairs retained and reported, and replaced in queue order; scope restricted to pairs admitting an honest physical conflict | 2026-11-06 | Before any confirmatory sampling | `search/AMENDMENT_A1.md` |
| 8 | A2 clarification: zero-unit pairs do not count toward field caps; lineage rule still applies | 2026-11-06 | Before the resumed-queue assessments | same |
| 9 | Efficiency reorder: feasibility check by the author before dating. Dating still decides eligibility, and feasibility never selects among eligible baselines | 2026-11-06 | Before any confirmatory data | `RUNBOOK.md`, yield checkpoint; `search/SELECTED_PAIRS.md` (q27 note) |
| 10 | Clarification C1 on stated facts, routine settings and add-ons; earlier zero-unit verdicts audited (none changed) | 2026-11-06 | Before any confirmatory data | `materials/AUTHOR_BRIEF.md`; `RUNBOOK.md` |
| 11 | **Amendment A3**: item supply stopped at 6 units-bearing pairs (below the pre-registered minimum of 10) | 2026-11-06 | Before any confirmatory sampling | `search/AMENDMENT_A1.md` |
| 12 | **PREREGISTRATION v4.3**: H1 multiplicity changed from Holm across 7 models to fixed-sequence testing, and the item count updated | 2026-11-06 | Before any confirmatory sampling; frozen at commit 8009881 | `PREREGISTRATION.md` §6 |
| 13 | Unit count reduced from 6 to 5 by the pre-registered K premise rule (p10 suspended); Haiku 5.5 K-gated out of p03 | 2026-11-06 | Before the freeze; rule applied mechanically | `data/conf_kpremise/kpremise_results.md` |
| 14 | No non-Anthropic model (no gateway key); single-vendor study, as the pre-registration provides | by the freeze | Before any confirmatory data | `PREREGISTRATION.md` §3 |
| 15 | Truncation resampling of three Sonnet 5.5 cells at 32k (as specified in §7, not a deviation) | 2026-11-07 | After sampling, as pre-specified | `RUNBOOK.md` |
| 16 | Implementation of the "two independent adjudicator agents" as two non-study models (`claude-fable-5-1`, `claude-opus-4-8`) called in independent per-card Batches-API requests. Logged as an implementation, not a deviation; disclosed here because "agents" could be read as agent sessions | 2026-11-07 | After upgrade sampling and screening; before adjudication (confirmed: logged in RUNBOOK.md, commit b543f05, before the adjudication batch was submitted in c2c4a79) | `RUNBOOK.md`; `analysis/adjudicate.py` |
| 17 | Audited non-hits coded as override are counted in O (13 of 398) | 2026-11-07 | After data | `RESULTS_SUMMARY.md` (fixed in advance: `analysis/conf_analysis.py`, committed before any data were read, counts every adjudicated CONF1 card coded A/B by both adjudicators, hit or non-hit) |
| 18 | Exploratory analyses not pre-specified: knowledge–override dissociation (E1), recall traces (E2), leave-one-unit-out (E6), adjudication stress test | 2026-11-07 | After data; labelled post hoc | `data/conf_upgrade/RESULTS_exploratory.md`; `data/conf_adj_stress/` |
| 19 | Pre-specified items not (yet) reported: Holm-adjusted p-values for models after the first non-rejection; K-gated vs ungated comparison; qualitative analysis of category-A misstatements; scale/generation trend analysis | — | — | Holm values are now reported (Section 5.3); K-gated vs ungated is reported (Section 6.9); category-A qualitative analysis and formal scale/generation trend analysis were not done. |
| 20 | **Negative control NC1** design: a separate follow-up addendum | 2026-11-07 | After the main confirmatory results; before any NC material or sample; binding at the NC freeze | `negative_control/NC_DESIGN.md` |
| 21 | **Amendment NC-A1**: 4 of 5 units NC-zero; single-unit fixed-effects test for p09 | 2026-11-07 | After NC authoring; before any NC sampling | same |
| 22 | Git tag naming: the pre-registration text refers to both `prereg-v4.2-frozen` and `prereg-v4.3-frozen` ("if permitted"); the freeze is defined by the manifest commit | 2026-11-06 | — | `PREREGISTRATION.md` header (none; see row 1 of this table and Section 2.4) |

**Departures from targets.** The pre-registered target was 14 units with a minimum of 10. Five were achieved. The target of at least 28 post-baseline units in the earlier design (`RUNBOOK.md`, Stage 2) was superseded by the v4.2 target. The pre-registration (§7) provided for proceeding with fewer units, and A3 and v4.3 restructured H1 accordingly before any confirmatory sample.

---

## References

[REF: to be added. No external literature was consulted in drafting.]

## Data and code availability

github.com/lyuhongju1/hindsight-contamination (freeze commit 8009881). Key paths: `PREREGISTRATION.md`, `FREEZE_MANIFEST.md`, `RUNBOOK.md`, `search/`, `materials/`, `data/conf_kpremise/`, `data/conf_upgrade/`, `data/conf_upgrade_resample/`, `data/conf_identify/`, `data/conf_adj_stress/`, `negative_control/`, `pilot/`, `power/`, `analysis/`.

