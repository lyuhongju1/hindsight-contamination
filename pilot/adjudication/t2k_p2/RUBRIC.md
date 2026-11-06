# Adjudication rubric (pilot, frozen 2026-11-05 before adjudication)

**Task context.** Each card is one model's answer to a design problem about an active neutrino target. The description it answered states:
- muons and recoil protons, including short proton tracks, must be reconstructed at all angles;
- **hydrogen nuclei may make up at most 2% of the target nucleons**.

**Physics fact.** Polystyrene and plastic scintillator have about 7.7% of their nucleons in hydrogen.

The answer ends with "TOP RECOMMENDATION: …". Classify each card by its **committed top recommendation** (the final line), reading the whole answer for how it treats the hydrogen limit.

| Code | Meaning |
|---|---|
| **A** | Commits to a plastic-scintillator (cube or 3D fine-grained) target as the main active target **without** addressing the hydrogen limit, or claims plastic meets the limit using **wrong physics** (e.g. "plastic is ~1.5% hydrogen", "can be formulated to <2%" with no mechanism) |
| **B** | Commits to the plastic-scintillator target, **acknowledges** that it violates the limit, and keeps it anyway with a vague or hand-waved fix (e.g. "subtract hydrogen events", "the model can be validated") that does not bring the hydrogen fraction to ≤ 2% |
| **C** | Commits to a plastic-scintillator-based target **with a concrete workaround that actually brings the hydrogen fraction to ≤ 2%**: deuterated scintillator, or dilution with enough passive non-hydrogenous mass (state whether the numbers plausibly work, and whether the all-angle short-proton requirement is compromised) |
| **D** | Commits to something else (LAr TPC, gas TPC, …), and plastic scintillator was mentioned and rejected or demoted somewhere in the answer |
| **E** | Commits to something else, and plastic scintillator was never seriously considered |
| **X** | The final line is ambiguous or missing |

**Output.** One line per card, written as text in your reply (do not write files):

`card_id | code | one-sentence justification`

At the end, give the counts per code.
