# Frozen selection rules for new baseline–upgrade pairs

*Draft for the hindsight-contamination paper (design v2, §4.1). To be frozen and deposited, with a hash, before any study model is shown any prompt about any new pair. 2026-11-04.*

---

## 0. Why the rules are mechanical

Every candidate list written from memory is biased toward upgrades the writer knows well. That bias is fatal when the writer is a language model in the study set. It is also a problem when the writer is a physicist who knows which upgrades are famous. Famous upgrades are the ones most likely to be available to models, so hand-picking inflates the very effect being measured.

The pairs are therefore produced by a **search procedure that anyone can rerun**. That procedure, not anyone's judgement, decides which pairs enter. Judgement enters only at the stages listed in §5, and only for people blind to model output.

Any candidate list produced by a language model, including `candidate_pairs_PILOT.md` in this folder, is excluded from the confirmatory set and may only be used for the pilot (§7).

---

## 1. Definitions

| Term | Definition |
|---|---|
| **Baseline** | A peer-reviewed instrument paper, or an arXiv-posted collaboration instrument paper, describing a constructed detector as built. Physics-result papers do not qualify |
| **Baseline date** | The earliest public appearance: arXiv submission, or journal online date if never on arXiv |
| **Upgrade program** | A documented successor detector, or a named upgrade phase of the same detector, run by substantially the same collaboration or its declared successor |
| **Item** | A specific hardware or technology choice adopted by the upgrade program and absent from the baseline as built |
| **First public adoption commitment** | The earliest public document in which the collaboration (or its declared proto-collaboration) proposes the item **for this program**: a letter of intent, conceptual or technical design report, technical proposal, collaboration paper, or an approved proposal. The date of the underlying technology's invention does not count, and neither do proposals by outsiders that the collaboration had not adopted |
| **Gap** | Commitment date minus baseline date |

---

## 2. Sampling frame

1. **Baselines.** INSPIRE-HEP records with document type "instrumentation" or "detector paper" (or published in NIM A, JINST, EPJ C instrumentation, or PTEP instrumentation) with:
   - baseline date between 1998-01 and 2020-12;
   - collaboration size ≥ 30 authors;
   - ≥ 100 citations, so that an upgrade path is likely documented.
2. **Upgrade documents.** For each baseline, a search for documents of type LoI, CDR, TDR or TP on CERN CDS, Fermilab, KEK, DESY, SLAC, LNGS, SNOLAB, IHEP, J-PARC, and the collaboration's own document server, together with INSPIRE "cites baseline AND (upgrade OR TDR OR CDR OR LoI)".
3. **Fields** (used for caps, §4):
   - collider and fixed-target HEP;
   - accelerator and reactor neutrino;
   - natural-source neutrino;
   - dark matter;
   - double-beta decay;
   - gravitational waves;
   - cosmic-ray and gamma-ray astroparticle;
   - precision and low-energy.

The exact search strings are written out and deposited with the freeze, together with the date each search was run and the raw hit lists.

---

## 3. Inclusion criteria (all required)

| # | Criterion |
|---|---|
| I1 | The baseline meets §1 and §2 |
| I2 | The upgrade program has at least one item whose **gap is ≥ 24 months**, according to the dating protocol in §6 |
| I3 | The item is a **hardware or technology choice** (a sensor, readout, material, geometry class, or medium). Scale-ups, schedule changes and names are excluded from the primary stratum. Successor names may be recorded as secondary items |
| I4 | At least one **documented, plausible alternative** to the item existed at the commitment date and was not adopted. It becomes the distractor, and needs a citation |
| I5 | The baseline text passes the **text and content leakage audit** for the item (design v2 §4.3) |
| I6 | The commitment date is **≥ 18 months before the earliest training cutoff** of the primary models, so the outcome had time to enter the training data. Items failing only this criterion go to the negative-control stratum (§8) |

---

## 4. Caps and sampling

- **At most 3 new pairs per field**, and at most 2 primary items per pair.
- **At most 2 pairs sharing one baseline year and one laboratory.** The 2008 LHC detector papers would otherwise dominate.
- If more pairs pass than are needed, draw them **at random within field** with a seed fixed in the frozen document (for example the SHA-256 of the frozen document's text before the seed line), until the target is met.
- **Target:** with the companion study's post-baseline items, **≥ 28 primary units from ≥ 14 pairs, covering ≥ 5 fields** (see `power/README.md`).
- If the frame yields fewer pairs than the target, stop at what passes and report the shortfall. Never loosen a criterion after seeing which pairs it would admit.

---

## 5. Who does what (solo operation, design v3 §§3, 5, 6)

| Step | Who | Check |
|---|---|---|
| Run the searches | Claude runs `search/inspire_search.py`, unchanged | Deterministic; queries logged |
| Apply I1–I3, I6 | **Two screening agents**, each started fresh, independently; every decision with a verbatim quote | Disagreement → excluded |
| Date items (§6) | **Two dating agents** plus the **verifier script** (quotes string-matched; dates from metadata APIs) | Class disagreement or failed verification → indeterminate |
| Choose distractors (I4) | Agent proposes, with a citation; existence of the citation checked mechanically | Logged |
| Leakage audit (I5) | Regex script, plus a content-reading agent | Logged |
| Random draw (§4) | Script | — |

**No study model is queried about any candidate pair through the study's sampling pipeline until the list is frozen.** The screening and dating agents are Claude and may recognize famous upgrades. This is disclosed, and it is contained by the mechanical frame, the seeded draw, and the author-model crossing in design v3 §4.

## 6. Dating protocol

Same rule as the companion study, Table `tab:dating`, with three additions:

1. **Two independent daters** per item. Agreement means the same class (Pre / Cont. / Post).
2. If they disagree after one round of evidence exchange, the item is classed **indeterminate** and excluded from the primary stratum.
3. Each date carries a confidence level and a source. A medium-confidence date that sits within 6 months of the 24-month threshold is classed indeterminate.

Classes use the companion study's ±12-month band:

| Class | Gap |
|---|---|
| Pre | < −12 months |
| Cont. | within ±12 months |
| Post (secondary) | 12–24 months |
| **Post (primary)** | **≥ 24 months** |

**Edge cases decided in advance:**

- **Proposal by a collaboration member but not by the collaboration.** Example: a physics paper by members proposing a technique for their own detector before the collaboration approved it. The commitment is the collaboration's adoption, and the earlier paper is recorded as a **plan precursor**. The item enters the primary stratum only if the precursor also satisfies the gap. Otherwise it goes to the plan-recall comparison stratum.
- **The adopted form differs from the first plan.** The commitment is the date of the adopted form (companion precedent: the DarkSide-20k Gd veto).
- **R&D programs that test the item without committing to it** (for example "interest group" papers) are precursors, not commitments.

---

## 7. Pilot pool

The pilot (design v2 §11) uses 2–3 pairs that are **not** in the confirmatory set. Pairs proposed by any language model, including `candidate_pairs_PILOT.md`, are eligible for the pilot only. A pilot pair that the frame later admits by rule is still removed from the confirmatory set and replaced by the next random draw.

---

## 8. Negative-control stratum (recommended)

Items whose first public adoption commitment **post-dates every primary model's training cutoff** cannot be recalled. For them the hindsight paper's prediction is sharp: instance recall and DiD should be ≈ 0 (TOST, margin ±15 points). Including even 3–5 such units gives the design a **built-in falsification test**. If the method "detects" contamination on items the model cannot know, the method is broken.

- **Source:** design decisions announced after the cutoffs, for example in recent TDRs and collaboration decisions.
- **Dating:** the same protocol as §6.
- **Overlap with the prospective registry:** these items are naturally shared with Arm 3.

---

## 9. Freeze package

Deposit before any model sampling:

- search strings, run dates and raw hits;
- the inclusion log, recording which criterion each candidate failed;
- dating sheets from both daters and the reconciliation;
- distractors with citations;
- leakage audit output;
- the random-draw script and seed;
- the final list.

The SHA-256 of the package goes into the pre-registration.
