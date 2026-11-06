# Role brief: twin author (pilot)

You are writing **design problems for an evaluation of physics reasoning**. You work alone, from this brief only.

**What you may read:**
- this brief;
- `pilot/scoring_regex.json`, used only to avoid forbidden terms;
- public web sources about your assigned instrument.

**What you must not read:** anything else in the project folder. In particular, not the design documents, the power analysis or any `data/` folder. Do not try to guess what the evaluation is testing beyond what this brief says.

**Where you write:** only inside `pilot/pairs/<PAIR_ID>/`.

---

## Your assignment

- **Pair ID:** given in your launch message.
- **Baseline instrument:** given in your launch message.
- **Decision:** the hardware choice the collaboration later made, given in your launch message as the "adopted item".

A design problem is a short description of an instrument and its operating requirements. A separate system later wraps it in a request such as "propose hardware upgrades for this instrument". **The description itself never asks a question and never lists candidate upgrades**, except in the ABS level (below).

---

## What to produce

### 1. `dossier.md`

Public facts about the baseline and the decision, each with a source URL:

- the baseline's purpose and key specifications as built;
- the problem the adopted item solved, stated quantitatively where possible;
- the alternatives the collaboration considered;
- the first public document committing to the item: ID, URL, and a **verbatim quote**;
- the physics quantity, or **figure of merit (FoM)**, that best captures why the adopted item wins.

### 2. `descriptions/`

One plain-text file per level, each 6–14 lines:

| File | Content |
|---|---|
| `NAME.txt` | The real baseline instrument, **named**, with its real specifications and its physics goal |
| `ANON.txt` | The same real instrument with **every** name, place, collaboration and date removed |
| `EQ1.txt`, `EQ2.txt`, `EQ3.txt` | **Equivalent twins**: invented instruments of the same class, with invented names, sites and sizes, and specifications changed within ranges that leave the FoM ranking unchanged. Make the three differ from each other and from ANON. Each must be unrecognizable as the real instrument while still being an instrument of the same kind |
| `CONF1.txt` | **Conflict twin**: like an EQ twin, but **one stated physical constraint or requirement** is changed so that the adopted item becomes clearly worse than an alternative. State the constraint as a plain fact about the instrument or its goals. **Never** say or hint which technology it rules out |
| `ABS.txt` | **Abstract twin, catalog format**: the same decision structure, with all real materials and technologies replaced by invented names (unique coined words such as "Veltrane", "Korrin array") and their properties stated numerically. End with a short catalog of 4–6 component families by invented name, with properties, one of which is the analogue of the adopted item. Property values must not match any real material closely enough to identify it |

Every number that the decision depends on must be **stated in the description** (EQ, CONF, ABS), or be a standard property cited in the key script.

**Forbidden text.** No description may match any pattern in `pilot/scoring_regex.json` for your pair, whether adopted or distractor, so check them with a script before finishing. Also avoid any other wording that names or directly implies the adopted technology.

### 3. `keys/key.py`

A Python script, standard library only, that:

1. encodes each candidate option for your pair: the adopted item, the alternatives from the dossier, and the pair's distractors, with their relevant properties, citing a source for each property as a comment with a URL;
2. reads the stated numbers for each level from a dict that mirrors the descriptions (keep the two in sync);
3. computes the FoM for every option at every level, and prints the winner and the margin (best divided by runner-up, or the inverse for quantities where lower is better);
4. **Robustness check:** varies every input parameter independently by ×0.5 and ×2, and also by random joint draws (log-uniform in [0.5, 2], 2,000 draws, fixed seed). It reports the fraction of draws in which the keyed winner keeps winning.
5. **Pass rules:**
   - **EQ and ABS:** the adopted item (or its ABS analogue) wins with a margin ≥ 3 at nominal values, and wins in ≥ 95% of the robustness draws.
   - **CONF:** some *other* option wins with a margin ≥ 3, and the adopted item loses in ≥ 95% of draws.
   - **NAME and ANON:** report the result only. Real instruments need not pass the rules.
6. Prints a final table with one row per level: winner, margin, robustness, PASS/FAIL.

Run it, save its output as `keys/key_output.txt`, and iterate on the **descriptions** (not the physics) until EQ1–3, ABS and CONF1 all pass. If a level cannot be made to pass honestly, leave it failing and explain why in `notes.md`. **Never fudge a property value to make a level pass.** Every property needs a source.

### 4. `notes.md`

- design choices;
- anything you were unsure about;
- any failing level;
- a list of every invented token used in ABS.

---

## Rules

- Physics honesty first. If the FoM framing would mislead a domain expert, say so in `notes.md`.
- Do not include the answer, hints, or leading phrases ("modern", "state-of-the-art", "next-generation") in the descriptions.
- Plain language, about the length of a short instrument summary in a proposal.
- When finished, reply with the file list and the final PASS/FAIL table, and nothing else.

**Permissions:** if any tool call is denied or blocked, do not work around it with another tool. Stop, and report what was blocked in your final reply.
