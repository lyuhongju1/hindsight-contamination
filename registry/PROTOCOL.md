# Prospective prediction registry: protocol (draft)

*Design v2 §7 (Arm 3). 2026-11-05. This is a standing registry, not a single study. Wave 1 should be registered as soon as the decision list is frozen. `pending_decisions_candidates.md` in this folder, compiled separately, is input to step 1. It does not replace step 1.*

---

## 1. Purpose

Language models are asked about detector design decisions that **have not yet been made**. Their answers are locked publicly and scored when the collaboration commits. Contamination is impossible for answers locked before the decision, so these scores are an uncontaminated measure of the models' design judgement. Comparing them with how well the same models agree with history on past decisions (the main study) is the most direct test of how much of that agreement comes from hindsight.

---

## 2. Selecting decisions (frozen rule)

**Eligible decisions** must meet all of the following:

1. **Hardware or technology choice** for a funded or formally proposed instrument or upgrade, in the fields of `pair_selection_rules.md` §2.3.
2. **At least 2 options listed publicly** by the collaboration or its design documents, with a dated source.
3. **No public commitment yet.** Check the collaboration's most recent public documents within 30 days of registration, and record each check with a date and source.
4. **A decision expected within 1–6 years**, according to a stated schedule or design-report timeline. Decisions with no stated timeline enter as "open-ended" and are analysed separately.
5. **Resolvable:** a commitment would appear in a public document that can be dated with the main study's dating rule.

**Selection procedure:**

- Candidates come from a systematic sweep of the latest design documents (CDR/TDR/LoI/white papers) and roadmap documents (for example, national and international strategy reports) for each field. The sweep and its date are logged.
- **Any model-compiled list is a seed for the sweep, not the frame.** Every decision on it must be re-verified by a person.
- Cap: at most 4 decisions per program and at most 6 per field. If the eligible set exceeds 25, draw at random with the registry's frozen seed.
- The **checker**, who confirms that each decision is still pending and records its options, is a person, not a study model.

---

## 3. What is frozen per decision

| Field | Content |
|---|---|
| ID | R-YYYY-NNN |
| Program and subsystem | e.g. "[program], photosensor for the [subsystem]" |
| Context description | Neutral description of the instrument and constraints, written from public documents. Reviewed by a second person for leading wording |
| Option set | The publicly listed options, verbatim with sources, plus "other" |
| Resolution rule | What counts as the commitment (the main study's dating rule), and how "other", partial, or mixed outcomes are handled |
| Expected decision window | With source |
| Status checks | Dated checks with links |

---

## 4. Elicitation

Two tasks are run for each decision in **separate sessions**:

1. **Open proposal (comparable with the main study).** The context description is wrapped in the main study's five templates: "propose concrete hardware upgrades". The options are not shown. The answer is scored later for whether it contains the eventually adopted option.
2. **Closed forecast.** Context plus the option set:
   - "Which option should the collaboration choose given the stated physics? Give a probability for each option (summing to 1) and a one-paragraph justification."
   - Asked twice, once phrased as **"should choose"** (design judgement) and once as **"will choose"** (forecast). The gap between the two is reported.

**Settings:**

- The same models, reasoning settings, output caps and stop-reason logging as the main study.
- n = 20 per template cell for the open proposal, and n = 20 per phrasing for the closed forecast.
- **Human baseline:** if the expert panel is available, the same closed forecast for a subset of decisions.

---

## 5. Locking

For each wave:

1. Raw JSONL with prompt hashes, model snapshot IDs, timestamps and stop reasons.
2. A manifest with the SHA-256 of every file, and the SHA-256 of the manifest.
3. Deposit:
   - a **Zenodo** version (DOI);
   - a **signed git tag** in the public registry repository;
   - optionally, the manifest hash in an OpenTimestamps proof.
4. **No edits** after deposit. Corrections go into a new wave with a note.

The deposit is public at registration. Publishing predictions could in principle reach the collaborations, but the risk is negligible at this scale; it is disclosed anyway.

---

## 6. Waves

- **Wave 1** comes first. After that there is a new wave every **6 months**, and an extra wave whenever a primary model is superseded by a new release.
- Every wave re-samples **all unresolved decisions** on all current models, and also on the earlier models that are still served.
- This gives two contamination measurements for free:
  - **Before vs after the public decision.** Models released after a decision becomes public form a **positive control**: they should match the outcome better than models released before it. The size of that jump measures hindsight directly, for decisions where the time course is known.
  - **Drift as discussion grows.** Proposal rates are tracked across waves while the decision is pending.

---

## 7. Resolution and scoring

**Resolution:**

- A decision resolves when the commitment is public under the main study's dating rule.
- Two people resolve each decision independently; disagreements are classed as "ambiguous".
- If the program is cancelled, or the decision is deferred indefinitely, the decision is marked **void** and not scored.

**Scores for each model and wave:**

| Score | Definition |
|---|---|
| Open proposal hit rate | Share of responses that include the adopted option |
| Closed forecast | Brier score and log score against the outcome |
| Baselines | (a) uniform over the option set; (b) the expert panel, where available; (c) the option most emphasized in the public documents at registration (salience baseline: the main study found that models track salience) |

**Reporting:** results are cumulative, with intervals. The registry reports **calibration**, not just accuracy. Only decisions locked before resolution count as uncontaminated.

---

## 8. Link to the hindsight paper

The paper reports:

- the registry design;
- Wave 1 registration, with its DOI;
- any decisions that resolve before Stage 2.

The registry's main payoff probably comes after the paper. State this plainly, and do not make any confirmatory hypothesis depend on resolutions within the paper's timeline.

---

## 9. To do before Wave 1

1. Run the sweep in §2. The checker verifies each candidate in `pending_decisions_candidates.md` and in the sweep.
2. Write and review the context descriptions.
3. Create the public registry repository (name to be chosen) and a Zenodo community or record.
4. Freeze this protocol, the decision list, and the prompts. Register on OSF or in the repository.
5. Sample and deposit. The sampling is cheap: about 20 decisions × (5 templates × 20 + 2 × 20) responses × the primary models.
