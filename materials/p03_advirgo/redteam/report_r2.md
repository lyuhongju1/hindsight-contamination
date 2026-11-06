# Red team r2: p03_advirgo (2026-11-06). Verdict: CONF1 FIX; BASE OK; kprobe OK

## Blind answers
- **BASE:** a detuned filter cavity (~400 m) is favoured; EPR is the runner-up. The adopted item is sound.
- **CONF1:** EPR/conditional squeezing (~4 dB flat) is favoured. The adopted item is unsound at 8 m (loss per unit length), assuming the broadband optimum.

## FIX list (all required)
1. **Decisive.** An 8 m cavity narrowband-tuned (γ≈250–300 Hz, |Δ|≈1.2–1.5γ) rotates the squeeze angle correctly at exactly 20 and 800 Hz.
   - It gives ~6 dB at both points (10–20 ppm). Between 45 and 400 Hz it is 5–11 dB worse than vacuum.
   - This literally meets the two-point requirement.
   - **Fix:** in NAME/ANON/BASE/CONF1, change the requirement to "lower total quantum noise by at least 3 dB at every frequency from 20 Hz to 800 Hz".
   - **Red-team check of the new wording:**
     - 8 m at the 10 ppm floor: best 0.41 dB minimum, so it FAILS.
     - 400 m at 60 ppm: 5.85 dB, so it PASSES.
     - EPR: 4.39 dB flat, so it PASSES.
     - Fixed-angle squeezing: FAILS.
2. **Key.**
   - Evaluate `meets()` on a frequency grid (~25 log-spaced points, 20–800 Hz).
   - Replace the scalar Kwee shortcut in `fd_improvement` with a sideband model that optimises γ, Δ and the injection angle against the band minimum.
3. **Wording.** Make the loss floor a project fact: "The lowest-loss high-reflectivity mirrors available to this project have 5 ppm loss per reflection (absorption plus scatter)." As a world claim, it is ~2× pessimistic. Even at a 2 ppm floor, the band version at 8 m still fails.
4. **notes.md stale text:**
   - eta = 0.85;
   - "arm tubes carry only the main beams";
   - the FIX 4 log value of eps should be ≈0.96 at 12.5 ppm (0.77 is the value at 10 ppm).
5. **Optional:**
   - widen the EPR mismatch unc to [0.5, 3] or cite Brown et al. PRD 96 062003 (2017); do not state the arm linewidth;
   - "main interferometer topology **and its operating point**" (closes detuned signal recycling);
   - add variational readout to the key as a failing option.

## Checks passed
- physics only;
- minimal pair (400 m → 8 m);
- coherence;
- r1 FIX 1–7 done;
- kprobe neutral with expected NO;
- folded, in-arm and WGM routes closed.

**Identifiability:** class high; exact instrument moderate.
