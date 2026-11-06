# Author brief: confirmatory conflict twins (v3)

You write design problems for an evaluation of physics reasoning. You work alone, from this brief. It condenses `pilot/briefs/author_v2.md` (rules 1–10) and the v4.1 refinements in `hindsight_contamination_study_design_v4_amendment.md`; follow those files where this brief is silent.

**What you may read:**
- this brief;
- `search/SELECTED_PAIRS.md` (your pair's row);
- `materials/scoring_regex.json` (your pair's entry);
- `pilot/harness/keylib.py`;
- `pilot/briefs/author_v2.md`;
- the v4.1 section of the amendment;
- **as worked examples only:** `pilot/pairs/t2k_nd280/round3/` and `pilot/pairs/auger/round3/`.

**What you must not read:** any `data/`, `adjudication/`, power or results file.

**Where you write:** only `materials/<PAIR_ID>/`.

**Permissions:** if a tool call is denied, do not work around it: stop and report it.

**Save each file as soon as it is written. At most 5 web fetches.**

---

## Files to produce in `materials/<PAIR_ID>/`

### 1. `dossier.md`

- The baseline as built: key specifications and physics goal, with sources.
- **The item you target.** If your row lists two counted items, pick the one that admits the cleaner physical conflict and say why.
- The verified commitment document, from your row.
- The documented alternative(s) not adopted.
- `adoption_status` of the item, with a source: one of **built and operated / approved not built / cancelled / unknown**.

### 2. `descriptions/`

| File | Content |
|---|---|
| `NAME.txt` | The real baseline, named |
| `ANON.txt` | The real baseline, unnamed |
| `BASE.txt` | An invented instrument of the same class in which the adopted item is a physically sound upgrade: it **passes** every stated requirement |
| `CONF1.txt` | BASE with a **minimal edit** (one sentence or one set of numbers) under which the adopted item **fails a stated physical requirement** |
| `CONF2.txt` | Optional. A second, physically different mechanism |

### 3. `keys/key.py` and `keys/key_output.txt`

Use `keylib` (`check_base`, `check_conf`). BASE and every CONF must PASS.

**Descriptions never ask a question and never list candidate upgrades.** A separate template wraps each description with the request. End with the instrument's requirements, stated as facts. Do not narrow the decision to one subsystem's configuration: describe the instrument and its goals, and let the reader decide what to change.

### 4. `kprobe.json`

Use exactly this format:

```json
{"CONF1": {"question": "...", "expected": "NO"}, "CONF2": {...}}
```

For each CONF, a neutral physics question about the failure mechanism, with no instrument context, that ends exactly with:

`End your answer with one line: VERDICT: YES or VERDICT: NO.`

Give the expected verdict.

### 5. `notes.md`

- design choices;
- survivors per CONF (the count is a covariate);
- fixed inputs, with a justification for each;
- any unc ranges, with their citations;
- the log of post-run changes;
- doubts.

---

## Rules (all must hold; a red team will check every one)

1. **Physics only.** No cost, labour or schedule decides anything.
2. **Plain fact, never exclusion wording.** Do not name, describe or rule out a technology class in a description.
3. **≥ 1 credible survivor per CONF**, coded against **every** stated fact. It must be credible to a domain expert: real mass, real rates, real temperatures.
4. **Robust failure of the adopted item** with every cited property varied ×0.5–2.
   - Exact stated facts and integer structural counts may go under `inputs["fixed"]`, with a justification.
   - A tighter range is allowed only with a cited precision (never narrower than ×0.8–1.25).
   - Linear scales only; **no booleans**.
5. **Minimal pair.** BASE and CONF differ only in the edit.
6. **No post-run tuning** of stated numbers without a logged reason.
7. **Coherence.** Check every side effect of the edited number on the rest of the instrument. Example from the pilot: a dose high enough to damage plastic implies rates no tracker survives.
8. **Close legitimate workaround routes** where possible by plain facts. Pilot examples: dilution with passive layers; deeper replacement tanks.
9. **No forbidden terms.** No description may match your pair's `adopted` or `identity` pattern (identity is allowed in `NAME.txt` only). Check with a script. Distractor terms are allowed.
10. **No leading words** ("modern", "next-generation", "state-of-the-art"). Avoid copying the real instrument's exact numbers in BASE and CONF. Recognition is measured anyway, so copying gains nothing.

If no honest CONF exists for your pair, say so in `notes.md` and leave it failing. **That is an acceptable outcome.**

**Final reply:** the file list, the `key_output` table, and one line per CONF naming the mechanism and its survivors.

---

## Lessons from round 1 (added 2026-11-06; they apply rules 1, 7 and 8, nothing new)

1. **The item is what the dated quote commits to, and no narrower.** If the quote says "a radiative decay counter", then any placement of such a counter is the item. Your CONF must defeat every reasonable variant of the item, not one configuration of it (p07 MEG failed this).
2. **Never close a workaround with a logistics, site, schedule or organisational rule** (e.g. "this work can only be done at X", "it takes N months"). These are rule-1 violations even when they read as plain facts (p08 COSINE failed this).
3. **"Item plus an add-on that fixes it" is a workaround, scored C, not a rejection.** Close such routes with plain physical facts, or accept that they exist and say so in notes.md.
4. **A servo, filter or design tweak that an expert would add as a matter of course defeats a noise- or rate-based conflict** (p15 aLIGO). Check for one before you build on such a mechanism.
5. **Decide early.** Within your first few calculations, ask whether ANY physical requirement separates the item from its alternative, robustly under ×0.5–2. If the window is empty, say so: a zero-unit outcome is acceptable and honest.
6. **Label every resolution figure as σ or FWHM**, with its source.
