# Red team r1: p08_cosine (2026-11-06). Verdict: BASE FIX, CONF1 FIX; kprobe OK (minor)

## Blind answers
- **BASE:** in-house purified-powder growth is favoured and sound.
- **CONF1:** at 3,600 m the adopted item "probably fails". The exposure time is not stated, so a fast process (≤4 weeks) would pass.

## FIX list
1. **State the exposure in BASE and CONF1** (identical sentence): "Purifying the powder and growing, annealing, machining and encapsulating each crystal takes about five months at the site where it is done."
   - If aqueous purification can strip ³H, word it as counting from the final drying step, and match the kprobe.
   - At R0=83 and F=17: 30 d gives 0.075 mBq/kg (pass); 150 d gives 0.37 mBq/kg (fail).
2. **Production rate:** widen R0 to ×0.3–1.5 (Activia/Mei estimates of ~26–36 /kg/d), or cite why the ANAIS measured value is preferred. Rerun.
3. **Coherence, both levels:** 0.1 mBq/kg ³H is about **0.85 dru** in 1–6 keV (not 0.2–0.3), which already exceeds the 0.5 dru goal. Raise the goal to ~1.5 dru (or drop the numeric goal) and correct notes.md. Do not tighten the ³H limit, which would kill the survivors.
4. **Close the workarounds with plain facts (both levels):**
   - "The home institute has no underground or heavily shielded space." (Closes shielded storage between steps.)
   - "The collaboration's chemistry, crystal-growth and machining work can only be done at its home institute." (Closes relocating the in-house grower to a low site or the portal.)
   - Without this, a relocated in-house grower is the adopted METHOD plus a valid workaround (code C), not a rejection.
5. **notes.md:**
   - Alpha Spectra is a marginal survivor (nominal ³H 0.066 mBq/kg; ²¹⁰Pb at ×2 breaks the limit); RMD/Astro-Grade is the real survivor.
   - Air shipping of vendor powder is not modelled.
   - Cite or qualify "no chemistry step removes tritium".

## OK
- physics only;
- minimal pair (30 m vs 3,600 m only);
- every option checked against K, ²¹⁰Pb and ³H;
- no booleans;
- kprobe neutral, expected NO.

**Identifiability:** moderately high (COSINE-like).
