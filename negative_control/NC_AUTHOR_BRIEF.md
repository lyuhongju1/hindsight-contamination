# NC author brief

You build ONE negative-control twin, NC_CONF, for a confirmatory unit of the hindsight-contamination study.

**Read first:**
- `negative_control/NC_DESIGN.md`;
- `materials/AUTHOR_BRIEF.md` (all rules, lessons and clarification C1);
- the unit's `materials/<pair>/` files: `descriptions/CONF1.txt`, `keys/key.py`, `notes.md`, `dossier.md`, `RUBRIC.md`;
- `pilot/harness/keylib.py`.

**Task.**
1. **Identify alt(u):** the documented non-adopted alternative that is the sound survivor of the unit's CONF1. Name it in `notes.md`.
2. **Write `negative_control/<pair>/NC_CONF.txt`:** CONF1.txt plus ONE minimal additional edit (one sentence or one set of numbers), such that:
   - alt(u) robustly fails a stated PHYSICAL requirement;
   - the adopted item still fails as in CONF1;
   - at least one credible THIRD option passes every stated fact.

   Same rules as the main study: physics only; plain facts naming no technology; no questions or candidate lists; no logistics, schedule or cost; coherence; and close workarounds with plain facts where possible. **No text may match the pair's adopted or identity regex in `materials/scoring_regex.json`**, and alt(u)'s own name must not appear either.
3. **Write `negative_control/<pair>/keys/nc_key.py`** using keylib. Treat alt(u) as the "adopted" option whose failure is checked, with the third option as survivor. Also check that the historical item still fails. Run it with `python -I` and save `nc_key_output.txt`.
4. **Write `negative_control/<pair>/nc_kprobe.json`**, in the format `{"NC_CONF": {"question": "... End your answer with one line: VERDICT: YES or VERDICT: NO.", "expected": "NO"}}`. The question tests alt(u)'s failure mechanism neutrally, with no instrument context.
5. **Write `negative_control/<pair>/notes.md`** with: alt(u); the mechanism; survivors; fixed inputs; doubts; and a DIFF line showing CONF1 → NC_CONF.

If no honest NC_CONF exists, write the reasons in `notes.md` and stop (NC-zero). Write only under `negative_control/<pair>/`. If a tool is denied, stop and report it.
