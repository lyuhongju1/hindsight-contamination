# Role brief: conflict-twin author (pilot round 2)

You write **design problems for an evaluation of physics reasoning**. You work alone, from this brief.

**What you may read:**
- this brief;
- `pilot/scoring_regex.json` (forbidden terms);
- `pilot/harness/keylib.py`;
- your pair's `dossier.md`, `notes.md` and `redteam/report.md` from round 1. These describe problems found in an earlier attempt, and you must not repeat them.

**What you must not read:** anything else in the project folder.

**Where you write:** only `pilot/pairs/<PAIR_ID>/round2/`.

**Permissions:** if a tool call is denied or blocked, do not work around it. Stop and report it.

**Save each file as soon as it is written.** Do at most 3 web fetches.

---

## What a description is

A description is 6–12 plain lines about an instrument and its requirements. A separate system later wraps it in a request such as "propose hardware upgrades". It never asks a question and never lists candidate upgrades.

## What to produce, in `round2/descriptions/`

| File | Content |
|---|---|
| `BASE.txt` | An invented instrument of the same class as the baseline, with invented names. The adopted item is a physically sound upgrade here: it **passes** every stated requirement. You do not need to show that it is the single best option. |
| `CONF1.txt` | `BASE.txt` with a **minimal edit**: change one sentence or one set of numbers, so that the adopted item **fails a stated physical requirement**. |
| `CONF2.txt` | Same as CONF1, but the failure comes through a **different physical mechanism**. |

### Rules (design v4 §3; all must hold)

1. **Physics only.** The failure is physical: rate, fluence, energy band, signal type, temperature, field, timing. Cost, labour, schedule or space limits may not decide anything.
2. **Plain fact, not exclusion.** State the edit as an operating fact about the instrument or its goal. Never as a rule that names or describes a technology class. Never "no X may be used".
3. **No giveaway.** Under each CONF, at least **two** alternatives remain physically viable. The edit must not leave a single survivor.
4. **Minimal pair.** BASE and each CONF differ only in the edited sentence or numbers. BASE states the same quantity at a value where the adopted item passes.
5. **No forbidden terms.** No description may match any pattern in `pilot/scoring_regex.json` for your pair. Check with a script.
6. **No tuning.** Fix the stated numbers before you first run the key. If you later change any stated number, log the change and the reason in `round2/notes.md`.
7. **No leading words** such as "modern", "next-generation" or "state-of-the-art". Avoid copying the real instrument's exact numbers. Recognition is measured, not gated, so exact copying adds nothing.

---

## Key: `round2/keys/key.py`

The key imports `keylib`:

```python
import sys; sys.path.insert(0, r"<absolute path to pilot\harness>")
```

It must:

1. put every stated number and every cited option property in `inputs`, with a source URL comment for each property;
2. define `fails(inputs)` for the adopted item, and `viable(inputs)`, which returns the passing alternatives;
3. call `check_base("BASE", ...)` and `check_conf("CONF1", ...)` and `check_conf("CONF2", ...)`.

Run it and save the output as `round2/keys/key_output.txt`. **BASE, CONF1 and CONF2 must all PASS.** If a conflict cannot pass honestly, leave it failing and say why. Never adjust a cited property to make a level pass.

## K-probe: `round2/kprobe.json`

For each CONF, write one neutral yes/no question that tests whether a reader knows the physics of the failure, without the instrument context. For example: "Would a silicon photomultiplier remain usable after a 1-MeV-equivalent neutron fluence of 3×10¹² n/cm²? Explain briefly."

Also give the expected correct answer.

Format: `{"CONF1": {"question": "...", "expected": "no"}, "CONF2": {...}}`

## `round2/notes.md`

- design choices;
- the conflict mechanisms and their sources;
- the log of any changes to stated numbers;
- doubts.

When finished, reply only with the file list and the key_output table.

---

## Added after the round-2 red team (2026-11-05)

8. **Every stated fact is a check on every option.** If a description states a temperature, field, rate, dose, size or composition, `viable()` must test every alternative against it. Survivors that contradict a stated fact (for example a cryogenic liquid in a "room temperature" volume) are the main failure seen so far.
9. **No boolean properties.** `keylib` now rejects them. Encode capabilities as numbers with cited thresholds (for example a rate tolerance in Hz/cm², a dose tolerance in Gy).
10. **Coherence of the scenario.** A conflict number must be physically coherent with the rest of the instrument. Example: a dose high enough to damage plastic implies particle rates no tracker could reconstruct, so it cannot be a near-detector constraint. Check the side effects of the edited number on every other system described.
