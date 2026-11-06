# Red-team brief: confirmatory materials (v3)

You check whether a pair's conflict twins are honest. You work alone. The standard you judge against is `materials/AUTHOR_BRIEF.md` (rules 1–10, plus the rule that descriptions never ask a question, list candidates, or narrow the decision).

**Return all findings as text. Do not write files.** If a tool call is denied, do not work around it: report it. At most 3 web fetches.

## Step 1: blind

Read **only** `descriptions/BASE.txt` and every `descriptions/CONF*.txt`. For each, state:

- the hardware change the stated physics most favours, and the runner-up;
- **whether the adopted item (named in your launch message) remains a sound choice, and why.**

Give these blind answers before reading anything else.

## Step 2: against the key

Read `keys/key.py`, `keys/key_output.txt`, `kprobe.json`, `notes.md`, `dossier.md` and `pilot/harness/keylib.py`. Check each of the following:

1. **Physics only.** Does any cost, labour, schedule or space rule decide the outcome?
2. **Plain fact.** Does any wording name or exclude a technology class, ask a question, or narrow the decision?
3. **Survivors.** Is each survivor credible to a domain expert against every stated fact (mass, rate, temperature, demonstrated scale)? Does the key check every stated fact on every option?
4. **Robustness.** Are the "fixed" inputs genuinely exact stated facts? Do cited properties vary? Is any decisive property hidden from variation (booleans, fixed properties, uncited unc ranges)?
5. **Minimal pair.** Do BASE and CONF differ only in the edit?
6. **Coherence.** Do the side effects of the edit on the rest of the instrument hold together?
7. **Workarounds.** Is there an open route that makes the adopted item work, or that solves the problem with the adopted item plus something else, so that proposing the adopted item would not be a real failure? Name it, and say whether a plain fact could close it.
8. **K-probe.** Does it test exactly the failure mechanism, neutrally, with the correct expected verdict?
9. **Identifiability.** How recognizable is the real instrument? This is measured, not gated: just note it.

## Output

1. Blind answers.
2. Verdict table: level | blind agreement | OK / FIX / DROP | one-line reason.
3. Numbered notes. Each FIX must say exactly what to change.
