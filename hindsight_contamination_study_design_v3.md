# Measuring Hindsight Contamination in AI-Assisted Detector Design — v3 (solo operation)

*2026-11-05. v3 = v2 plus the changes below. Where they conflict, v3 governs. v2 sections not mentioned here (the recognizability ladder §2, estimands §3, statistical model and inference rules §9.2–9.5, threats §12) carry over unchanged.*

**What changed.** No people are recruited. Every role v2 gave to humans (twin authors, expert panel, daters, research assistant, adjudicators, blinded analyst) is now done by Claude.

**Why that is a problem.** Claude (Opus 5.5) is also one of the models under study. Without countermeasures, the paper would test Claude models on materials Claude wrote and dated, with keys Claude set. A referee would rightly treat that as circular.

**The design principle of v3.** Replace *trusted human judgement* with *checks that do not require trusting the operator*. Each such check is one of:

- a computation anyone can rerun;
- an empirical gate measured on the study models themselves;
- a mechanical rule over public metadata;
- a cross-vendor control that would expose authoring bias.

Where a judgement cannot be replaced, it is logged with its evidence, made by a separately instructed agent, and disclosed as a limitation.

---

## 1. Who does what

| v2 role (human) | v3 replacement | What makes it checkable without trusting Claude |
|---|---|---|
| Twin authors (≥ 2 physicists, blind) | Claude **twin-author agents**, each started fresh with only a role brief and the baseline's public specifications (§3) | Identification gate on every study model (v2 §5); computable keys (§2); author-model crossing (§4) |
| Expert answer-key panel (5 per field) | **Computable answer keys**: each twin states quantities and a figure of merit, and a published script decides the answer (§2) | Anyone can rerun the script; the answer must survive parameter perturbation |
| Expert recognizability (block C) | Dropped | Identification is measured on the study models instead (v2 §5) |
| Two independent daters | Two **dating agents**, each started fresh, plus **mechanical verification** of every cited date and quote (§5) | Dates come from the arXiv, INSPIRE and CDS APIs; quotes are string-matched in the fetched source |
| Research assistant (pair search) | Claude runs the frozen script; **two screening agents** apply I1–I6 independently, and items where they disagree are excluded (§6) | Deterministic search frame and seeded draw; every inclusion decision is logged with a quote |
| Judge validation (human labels) | **The primary scoring needs no judge** (§7) | Regex on real technology names; catalog format with invented tokens for abstract twins |
| Human adjudication | Two **adjudication agents**, blind to condition (labels hashed), with agreement reported (§7) | Disclosed as model adjudication; the regex stays primary |
| Blinded human analyst | Analysis script written on simulated data, then **frozen with a hash before sampling**; Claude runs it without discretion | Hash-chained, timestamped commits |
| IRB | Not needed (no human participants) | — |

**What still requires the PI** (actions only Hong Joo can take):

1. Provide API keys and a budget: Anthropic, plus one multi-vendor gateway key (§4).
2. Approve each outward-facing action: public repository pushes, the Zenodo deposit, and the journal submission.
3. Serve as the accountable author: read and sign off the Stage 1 and Stage 2 manuscripts. AI cannot be an author under journal policies, and its role must be disclosed (§9).
4. Optionally, provide GPU access, if the causal injection arm is wanted (§8).

---

## 2. Computable answer keys (replace the expert panel)

Each twin is written around **one decision with a quantitative figure of merit**. The twin text states every number the decision needs. A key script (`keys/<pair>_<item>.py`) computes the answer from those numbers.

**Examples of decision types** (the key script implements the equation; parameter values come with citations):

| Decision | Figure of merit | Example conflict lever |
|---|---|---|
| Photosensor for a low-energy scintillation TPC | Accidental n-fold coincidence rate from summed dark counts, compared with the required background at threshold | Photosensor area and temperature such that the summed SiPM dark-count rate breaks the requirement |
| Photosensor under radiation | Dark-count rate after fluence Φ (damage ∝ Φ) vs single-photon threshold | High neutron fluence |
| Quantum-noise reduction in an interferometer | Fractional sensitivity gain in the target band, given stated quantum and thermal noise budgets | Thermal noise dominating by ≥ 3× across the band |
| Tracker technology | Occupancy, material budget and radiation tolerance against stated rates | Rate or fluence beyond one option's stated tolerance |
| Veto or active shield | Residual background against requirement, given stated neutron yields and capture properties | Fiducial geometry or source spectrum changed |

**Rules (all pre-registered):**

1. **Margin.** The keyed answer must win by a stated margin of **≥ 3×** on the figure of merit at the nominal parameters.
2. **Robustness.** The answer must stay the same when **every input parameter is varied independently by a factor of 2**. This is checked automatically by a grid or Monte Carlo over the parameters. Twins that fail are revised or dropped. This is the substitute for expert agreement: the answer does not depend on fine judgement.
3. **Citations.** Every parameter value is either stated in the twin itself (and so part of the problem) or cited to a textbook, review or datasheet. Citations are mechanically checked to exist.
4. **Equivalent twins.** The historical choice must win under the twin's parameters by the same rules.
5. **Conflict twins.** The historical choice must **lose** by the same margin.
6. **Red team.** A fresh **red-team agent** receives the twin text alone, with no key, and is told to argue for a different answer *using only the stated physics*. Every argument it produces is either answered by a revision to the twin or the script, or the twin is dropped. The red-team transcripts are released.

**Cost of this choice, to be disclosed.** Only decisions that can be quantified enter. Items whose historical adoption hinged on cost, schedule, politics or tacit expertise are excluded, and the paper says so. This narrows scope, but it makes "the physics says X" a checkable statement rather than an opinion. That arguably makes the study more rigorous than v2's panel.

**Constraint-knowledge probe K** (v2 §4.5): kept, and fully automated.

---

## 3. Agent separation protocol

Every role in §1 runs as a **fresh agent** with a written role brief. It gets read access only to the files the brief lists, and writes only to its role folder.

**Rules:**

- No role agent sees the hypotheses, the power analysis, or any study-model output, except the gate agents, which see only the outputs their gate needs.
- The orchestrator (the main Claude session) runs gates and scripts but **does not edit role outputs**. A twin that fails a gate goes back to a new author agent with the gate report attached.
- Every brief, transcript and output is archived under `agents/<role>/<run-id>/` and released.

**Disclosure.** The separation stops information about *this project* from flowing between roles: hypotheses, model outputs, keys. It does **not** make the roles independent in what they know, because every agent has the same weights and pretraining. Two dating agents can share the same false memory. That is why §5 makes dating mechanical, and why §4 brings in a second model family.

---

## 4. Author-model crossing (the main countermeasure against self-evaluation)

**Idea.** Write two complete twin sets from identical briefs:

- one authored by Claude agents;
- one authored by a non-Anthropic frontier model, called through the API with the same briefs and the same gates.

Then test **both** model families on **both** sets.

- **Authoring-bias test.** Model the author family × tested family interaction on the identification rate and on IR.
  - If Claude-authored twins are easier for Claude models to see through, or carry cues toward history, the interaction shows it.
  - Pre-registered gate: if the interaction on IR exceeds 0.5 logit, primary results are reported **per author set**, and the cross-authored cells (Claude models tested on the other author's twins and vice versa) become the primary cells.
- **Cost.** One extra authoring run plus doubled twin sampling. Most of that cost is the twin cells, roughly +60% of the per-model budget.
- **Requirement.** One API gateway key that reaches at least one non-Anthropic frontier model. A gateway such as OpenRouter also serves open-weight models, which covers Arm 2a without a GPU.

**Without a second vendor,** this check is impossible. The paper must then present itself as a *single-family self-test* and drop "frontier models" from every claim. That is a large loss, and is the main reason to get the second key.

---

## 5. Mechanical dating (replaces human daters)

For each item:

1. Two fresh dating agents each search independently and return the earliest adoption commitment as a structured record: document ID, URL, the claimed date, and a **verbatim quote** showing that the collaboration proposes the item for this program.
2. A **verifier script**, not an agent:
   - fetches each cited document;
   - checks that the quote appears in it (normalized string match);
   - takes the date from metadata APIs (arXiv submission date, INSPIRE earliest date, CDS record date), never from the agent.
3. The class is computed from the verified dates by v2's rule.
4. If the two agents' verified dates fall in **different classes**, or either record fails verification, the item is **indeterminate** and leaves the primary stratum.

**What remains judgement:** whether a quote constitutes a "commitment". That judgement is applied by both agents against the frozen definition in `pair_selection_rules.md` §1, and the quotes are released so readers can disagree.

---

## 6. Pair selection without a research assistant

The `search/inspire_search.py` frame and the seeded draw are unchanged. The hand-filled CSV columns are now filled by **two screening agents** working independently from the documents. Each criterion decision carries a quote, and pairs on which the agents disagree are excluded.

**Known bias, disclosed.** The screening agents are Claude and may recognize famous upgrades. The protections are:

- the frame is mechanical, so the agents decide only eligibility, never which eligible pair is drawn;
- every decision comes with evidence;
- §4 catches the downstream consequences.

The pilot pool remains excluded from the confirmatory set.

---

## 7. Scoring without a validated judge

| Level | Task format | Primary scoring |
|---|---|---|
| NAME, ANON, EQ, CONF | **Open** (v2 templates) | Frozen regex on real technology names, as in the companion study |
| ABS | **Catalog**: the prompt describes 4–6 candidate component families by invented names and properties, and the model proposes and justifies upgrades | Regex on the invented names (unique tokens) |
| All levels, secondary | Catalog format | Regex on catalog tokens. This lets the ABS level be compared with the others in a common format |

- **No language-model judge is used for any primary or confirmatory quantity.**
- **Adjudication.** Two blind adjudication agents read 10 random responses per headline cell. Labels are hashed, and the agents never see the condition. Their agreement with the regex is reported as *model adjudication*, not human validation.
- **Effect on power.** Adding the catalog format increases the number of cells. The power analysis (`power/`) is rerun on the final design before freeze.

---

## 8. Arms under solo operation

| Arm | Status | Note |
|---|---|---|
| 1. Twin ladder (frontier) | **Core** | As v2, plus §§2–7 above |
| 2a. Natural exposure (open-data models) | **Core if the gateway serves an open-data model**; corpus counts via public infini-gram / OLMoTrace APIs | Checkpoint analysis needs intermediate checkpoints served somewhere. If none are, 2a reduces to a cross-item description |
| 2b. Causal injection | **Optional; needs a GPU**. This machine has none (Intel integrated graphics) | Without it the claim ladder tops out at rung 3, and the word "memory" is not used (v2 §1.1) |
| 3. Prospective registry | **Core**, run solo | Claude checks status with dated web sources; deposits need PI approval |

---

## 9. Disclosure and authorship

- **Methods section, "Conduct of the study".** It states that every material, key, date, screening decision, script and analysis was produced by Claude agents under the protocol in §3. The PI designed the research question, approved the protocol, and is accountable for the paper.
- **Release.** All agent briefs and transcripts are released.
- **Referee-facing argument.** "Do not trust the operator" is the right standard for a paper about models trusting their own knowledge. Every quantity that matters can be recomputed (keys, dates), was measured empirically (identification), or was controlled across vendors (authoring). What cannot be is listed as a limitation.
- **Journal policy.** Check the target journal's AI-use policy before Stage 1. Some venues restrict AI-generated text or analysis, which affects the choice of venue.

---

## 10. What is lost relative to v2, honestly

1. **No human judgement anywhere.** Keys are limited to quantifiable decisions (§2), which narrows the item set and may bias it toward decisions that physics settles cleanly.
2. **Expert–history agreement and human recognizability** are gone.
3. **Roles are not independent in knowledge** (§3). Agreement between Claude agents is weak evidence, and the paper never reports it as if it were inter-rater reliability.
4. **The self-evaluation risk** is controlled only if the second vendor is available (§4).
5. **There is no causal arm without a GPU** (§8).

---

## 11. Operating plan

The step-by-step state of the project is kept in `RUNBOOK.md`, so that any future Claude session can resume where the last one stopped.
