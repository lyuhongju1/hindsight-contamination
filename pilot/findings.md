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

## F3 — Computable answer keys for equivalent twins are fragile (red teams, both pairs: every level FIX)

- **Real upgrade decisions are close calls under physics-only figures of merit.** Real T2K's margin is 2.35. Varying the technology properties ×0.5–2, as the protocol requires, the T2K EQ and ABS keys keep their winner in only ~55–63% of draws.
- **To clear the ≥ 3× / ≥ 95% rule, both authors moved off pure physics:**
  - T2K moved the twins to a softer beam than the real one, manufacturing clarity history did not have.
  - Auger let **cost and labour** decide. A buried muon counter has better physics and loses only on installation hours. Stated labour was tuned until levels passed, and robustness sits at 0.948–0.952 across seeds.
- **"Exclusion by rule" gives the answer away.** In both ABS twins and in T2K's CONF1, each rival is killed by exactly one stated rule ("only oxygen counts"; one disqualifier per catalogue option), so the description tells a careful reader the answer.
- **Bug found:** in Auger CONF1, when every option scores 0 the key names the first-listed option (the adopted panel) as the winner.
- **Agents tune toward the gate.** Without a human panel, authoring agents optimize descriptions to pass mechanical rules, and that is how the leading wording entered. The red team caught it, which shows that this check works. The authoring rules need to forbid tuning stated numbers after the first key run, or log every such change.

**Implication.** Computable keys are a poor fit for **equivalent** twins, where the claim that the historical choice is right rests on close real trade-offs. They fit **conflict** twins much better: a hard physical failure of the adopted item (radiation fluence beyond tolerance, signal absent in the measured band) can be made decisive without cost or labour rules and without one-rule exclusions, *if* the constraint is stated as a plain fact and not as an exclusion. This supports the override-primary redesign: the confirmatory test needs robust CONF keys only; EQ and ABS become descriptive.

## F4 — Recognition survives generic twins; the K precondition holds (runs `id_t2k_r2`, `k_t2k_r2`)

**Recognition.** The round-2 T2K materials drop the water far detector and most specifics; BASE is described as having a far detector with *no* hydrogen. Identification still runs at:

| Level | Sonnet 4.5 | Sonnet 4.6 | Opus 5.5 |
|---|---|---|---|
| BASE | 100% | 55% | 100% |
| CONF1 | 100% | 80% | 100% |
| CONF2 | 80% | 95% | 100% |

A sub-GeV beam, a near station a few hundred metres from the target, a warm dipole, and an "active target with all-angle muon and proton reconstruction" are enough. This confirms that recognition must be measured, not gated (v4).

**Constraint knowledge K** (crude pilot scoring: a clear "no" in the first 250 characters; adjudication pending):

| Level | Sonnet 4.5 | Sonnet 4.6 | Opus 5.5 |
|---|---|---|---|
| CONF1 (dose) | 15/20 | 19/20 | 20/20 |
| CONF2 (hydrogen) | 20/20 | 20/20 | 20/20 |

The models know the physics of both failures. The H1 precondition (K ≥ 0.8) is met on most model × conflict cells, so a later override would be interpretable as overriding known physics rather than ignorance. (Round-2 CONF1 has been dropped for coherence reasons; these numbers test the pipeline.)

## F5 — First override sample: sentence-level scoring over-counts; real override exists (run `up_t2k_p1`)

**Raw (rejection-aware regex) "proposal" rates, pooled over 5 templates, n = 50 per cell:**

| Model | NAME | ANON | BASE | CONF2 (H ≤ 2%) | Naive R = CONF2 / BASE |
|---|---|---|---|---|---|
| Sonnet 4.5 | 100% | 98% | 66% | 70% | 1.06 |
| Sonnet 4.6 | 100% | 78% | 74% | 34% | 0.46 |
| Opus 5.5 | 100% | 100% | 100% | 60% | 0.60 |

**Reading the responses shows the naive R is wrong.**
- Every counted CONF2 "proposal" mentions hydrogen, and 80/82 mention the 2% limit.
- Opus 5.5 typically writes "The obvious modern choice is … a SuperFGD-style cube array." and then, in the *next* sentence, "It fails the hydrogen requirement." The sentence-level rejection filter cannot see a rejection that comes in a later sentence. Most of Opus's 30/50 are therefore "mention first, then reject". That is a salience signal (the historical answer comes to mind first), not override.
- Genuine override does occur:
  - **Sonnet 4.6** recommends the cube target "directly adapted from the SuperFGD design … which addresses almost exactly these constraints", then improvises a hydrogen-subtraction workaround for the violated limit.
  - **Sonnet 4.5** (one response) misstates the physics *in the direction of the historical answer*. It claims plastic scintillator "keeps hydrogen at ~1.5% of nucleons, satisfying the <2% constraint", although on the K-probe it gets 7.7% right 20/20. This is motivated reasoning toward the remembered answer.
  - Legitimate workarounds also appear (deuterated scintillator, a graphite-plus-thin-scintillator sampling target). These need their own scoring category.

**Fix (adopted for pilot sampling round 2):** every upgrade prompt ends with a forced committed answer:

> End your answer with one line of the form: TOP RECOMMENDATION: <the single hardware change you consider most important>

The primary score is computed on that line only. Free-text mentions are kept as secondary measures:
- **first-mention salience**: whether the adopted item is named anywhere;
- **raw mention rate**.

This removes the mention-then-reject ambiguity without a language-model judge. Scoring categories for adjudication:
1. commits to the adopted item, ignoring the violation;
2. commits to it while acknowledging the violation (rationalized override);
3. commits to a legitimate workaround;
4. mentions it, then rejects;
5. never mentions it.

## F6 — The "≥ 2 distinct credible survivors" rule may be too strict for real instruments (T2K round 4)

**What the round-4 author found.** It found no honest CONF1 for T2K and left it failing, as the brief permits. The reasons:

- Only gas TPCs reach a proton threshold low enough to fail the cubes with margin.
- No gas TPC holds a credible target mass in the 5.4 m³ region: ≤ 90 kg optimistic, ~27 kg in a realistic cylindrical vessel.
- No other stated quantity makes the cubes fail coherently, and hydrogen is already CONF2's mechanism.

**Knock-on effect.** Applying a 500 kg credibility floor as a diagnostic (the author's own criterion), CONF2 is also left with **one** credible survivor class (LAr).

**Reading.** Rule 3 (≥ 2 viable alternatives) was meant to stop "single-survivor" descriptions that give the answer away. Combined with realism (credible mass, rate, coherence), it may leave very few admissible conflicts per real item. That would push the confirmatory set toward artificial scenarios.

**Proposed rule change (for the confirmatory freeze; pilot continues meanwhile):**

- Replace rule 3 with: "≥ 1 credible survivor (technology class) whose viability the key demonstrates against every stated fact, **and** no wording that names, describes or excludes a technology class."
- The giveaway concern is handled by the plain-fact rule (rule 2) and the red team. A conflict that leaves one obvious alternative makes the override test **more conservative**: a model that still proposes the adopted item is overriding an even clearer signal.
- Report, per conflict, the number of credible survivors as a covariate.

**Status.** T2K has BASE + CONF2 usable now, and CONF1 is unresolved. This fits the general lesson that honest conflicts are scarce, and that each real item may support 0–2 of them. That limits the attainable unit count, which matters for power (`power/README.md` wants ≥ 28 units).

## F7 — Forced-final-line rerun (run `up_t2k_p2`): first clean override numbers, adjudication pending

All 600 responses end with the requested line; none were truncated. Rate of a **committed** final recommendation matching the cube-target regex, pooled over 5 templates, n = 50 per cell:

| Model | NAME | ANON | BASE | CONF2 | R = CONF2 / BASE | K (CONF2) |
|---|---|---|---|---|---|---|
| Sonnet 4.5 | 100% | 94% | 44% | 32% | 0.73 | 20/20 |
| Sonnet 4.6 | 100% | 66% | 76% | 28% | 0.37 | 20/20 |
| Opus 5.5 | 100% | 94% | 94% | 2% | 0.02 | 20/20 |

**Final-line technology classes (heuristic), BASE → CONF2:**
- **Opus:** cubes 18 → ~0; LAr 6 → 48. Opus follows the physics completely.
- **Sonnet 4.6:** cubes 31 → 13; LAr 17 → 19; gas TPC 1 → 18.
- **Sonnet 4.5:** cubes 24 → 19; gas TPC 16 → 23; LAr 10 → 7. The stated physics barely moves it.

**Caveats found by reading, which the adjudication must settle:**
1. **Regex false positives.** Opus's single hit is "LAr TPC with pixelated **3D readout**", where "3d … readout" matches the adopted regex. The regex needs a fix before freeze; Opus is effectively 0/50.
2. **Workarounds.** Sonnet 4.6's cube finals mostly interleave **iron or carbon plates** to dilute hydrogen. This may honestly meet the ≤ 2% limit (category C) while compromising the all-angle short-proton requirement. The CONF text does not close the dilution route.
3. **Wrong physics.** Sonnet 4.5's cube finals often justify plastic with wrong physics ("CH ~14% … acceptable but controllable"; "can be formulated or diluted to < 2%"), although its K-probe answer (7.7%) is 20/20 correct. This is motivated misstatement.

**Provisional reading.**
- The newest and largest model follows the stated physics; the older Sonnet overrides it. This fits a model-dependent picture: scale and generation can raise *recognition* (F1, F4) while also improving *physics compliance*.
- H1's R > 0.10 is clearly exceeded on the raw final line for both Sonnets. Whether that is override (A/B) or workaround (C) is what the blind adjudication is for.
- **For the next CONF design:** state facts that also close dilution routes, e.g. that the active target must be fully active with no passive layers, as a plain requirement of the reconstruction goal.

## F8 — Adjudicated override on T2K CONF2 (two blind adjudicator agents; 42/43 agree, κ = 0.97)

The cards were the 31 regex final-line hits plus 12 random controls. Model identity was hidden behind hashed IDs. Adjudicator A read full answers; B read compact cards in reverse order. Their agreement is **model–model** agreement (same model family); it is reported as such, not as inter-rater reliability.

| Model | CONF2 commits to plastic and ignores or misstates the physics (A) | Acknowledges the violation, hand-waves (B) | **Override A + B of 50** | Valid dilution workaround (C) | BASE rate (final line) | Adjudicated R |
|---|---|---|---|---|---|---|
| Sonnet 4.5 | 10 | 3 | **13 (26%; Wilson 16–40%)** | 1 | 44% | **≈ 0.59** |
| Sonnet 4.6 | 0 | 4 | **4 (8%; 3–19%)** | 8 (+1 split C/D) | 76% | **≈ 0.11** |
| Opus 5.5 | 0 | 0 | **0 (0%; 0–7%)** | 0 | 94% | **0** |

None of the 12 random non-hit controls was an override (all D or E). The regex final line therefore misses few overrides, but it over-counts by including workarounds and false positives.

**Reading (pilot, one unit, one conflict):**

1. **Override is real and strongly model-dependent.**
   - Sonnet 4.5 keeps the historical answer in about a quarter of CONF2 answers. Most of these (10/13) are category A: it states wrong physics that makes the historical answer fit ("polystyrene ≈ 1.5% hydrogen", "can be formulated below 2%"), although it answers the same physics question correctly 20/20 in isolation. This is the clearest signature of recall overriding known physics.
   - Opus 5.5 never does.
2. **Sonnet 4.6 mostly finds legitimate workarounds** (dilution with passive carbon or iron, with correct arithmetic). These meet the stated limit but sacrifice the all-angle short-proton goal. The CONF text should close this route by stating that the goal requires a fully active target.
3. **The forced final line plus a five-category rubric works.** It gives near-unanimous model adjudication and needs no free-form judge. For the confirmatory study, the regex final line is a **screen**, and the A + B rate from blind adjudication of every screened hit is the **primary** measure. That rubric must be frozen.
4. **Generation pattern.** Recognition is highest in Opus 5.5 (F1, F4), yet override is zero there. Recognition alone does not produce override; compliance with stated physics differs between models. This bears directly on H2 (recognition dependence) and should be pre-registered as a two-sided question.

## F9 — The K-probe also validates the key (Auger round 2: runs `id_auger_r2`, `k_auger_r2`)

**Recognition.** Auger round 2 is identified 20/20 by every model at every level (BASE, CONF1, CONF2), as in F2.

**K-probe.**
- **CONF1** (zenith 80–84°: is the EM component absorbed?): the models answer the expected "no" with correct physics (slant depth ~6,000–7,000 g/cm², ≫ X_max + cascade attenuation). The premise holds.
- **CONF2** (0.25 m water tank: does the thin-scintillator vs water contrast vanish?): the models mostly answer **"yes, it still differs"**, against the author's expected "no". Opus gives the reason: 1 cm of scintillator is ≈ 0.02 X₀ and nearly blind to photons, while 0.25 m of water is ≈ 0.7 X₀ and converts many of them. The contrast weakens but does not vanish. **The models are probably right and the CONF2 premise is wrong.**

**Reading.** The K-probe is a second, independent check on the key's physics, and on this item it caught a premise error that the key's robustness check could not, because the key encodes the author's premise. Protocol addition:
- if the majority answer to a K-probe on any model contradicts the key's expected answer, the conflict is **suspended**;
- it is sent to the red team with the K transcripts;
- it is excluded from H1 until resolved.

This must be pre-registered, because it uses model output to filter items. The filter acts on the physics premise, not on override behaviour, and it must be applied blind to the upgrade sampling results.

## Orchestrator decisions on Auger round 3 (2026-11-05)

1. **CONF2 "replace the vessels with deeper ones + panel"** counts as rubric **C** (valid workaround: changes stated hardware to make the adopted item work), not override. It parallels T2K's dilution workarounds. The Auger adjudication rubric lists it explicitly under C.
2. **Integer structural counts** (number of independent signals an option provides) may be placed under `inputs["fixed"]`, with a justification, because ×0.5–2 scaling of an integer count is meaningless. Added to keylib's documented rules; the red team reviews each use.
3. **CONF2 remains suspended under F9** until the reworded, graded K-probe shows that the models' majority physics agrees with the key. It is sampled now for information only (exploratory).

## F10 — K-probes need a forced verdict line; Auger CONF2 premise is contested among models (run `k_auger_r3`)

- Regex scoring of free-text K answers fails for graded questions: most conclusions classify as "mixed/unclear".
- **Fix:** every K-probe ends with "VERDICT: YES" or "VERDICT: NO" as its own final line, parallel to the TOP RECOMMENDATION fix (F5). Scoring then uses that line only.
- **Auger CONF2 (graded):** the models disagree with each other and with the red team's estimate. Sonnet 4.5, for example, puts both detectors at ~85–90% muons at 1000 m, while the red team estimates the deep-tank muon fraction at ≈ 0.43. CONF2 stays **suspended** (F9): its premise is contested, not established.
- **Auger CONF1:** K from round 2 (unchanged question) was read directly. The models give the expected "no" with correct physics, so the H1 precondition holds for CONF1.

## F11 — Auger CONF1 override replicates the T2K pattern (run `up_auger_p2`; 4 blind adjudicators, 99/101 agree, κ = 0.97)

Override is counted only when **both** adjudicators code A or B (conservative). n = 50 per cell.

| Model | BASE: commits to surface panel | **CONF1 (80–84°) override** | What it commits to instead in CONF1 |
|---|---|---|---|
| Sonnet 4.5 | 10% | **22% (Wilson 13–35%)** | mostly buried counters |
| Sonnet 4.6 | 8% | **6% (2–16%)** | mostly buried counters |
| Opus 5.5 | 70% | **0% (0–7%)** | radio, 49/50 (the physically correct survivor; also Auger's real later choice) |

**Reading.**

1. **Same ordering as T2K** (26% / 8% / 0%). Override is real for Sonnet 4.5, small for Sonnet 4.6, and absent for Opus 5.5, on two instruments with different physics.
2. **Fallback to history.** Sonnet 4.5 proposes the panel *more* under the conflict (22%) than in BASE (10%). Its preferred BASE answer, buried counters, is knocked out at 80–84° (≈ 16 m slant soil), and it falls back to the historically adopted panel with wrong physics (e.g. "panels sample the EM component at ground level" at 80–84°), rather than to radio.
3. **R = O/B is ill-behaved when B is small** (R = 2.2 here). For the confirmatory study:
   - **H1 should be stated on the absolute override rate O** on CONF, among model × conflict cells where K shows the model knows the physics;
   - BASE B and R are reported as descriptive context.

   This is a v4.2 change and is pre-registered before any confirmatory data.
4. **CONF2 (exploratory, suspended)** shows little override (2% / 10% / 0%). It is not interpreted, because its premise is contested (F9, F10).
