# Red-team report r1, p03_advirgo (returned as text; saved by the orchestrator, 2026-11-06)

**Verdicts:**

| Level | Verdict | Reason |
|---|---|---|
| BASE | OK | Filter cavity passes with a large margin |
| CONF1 | FIX | See items 1–6 |
| kprobe | FIX (minor) | See item 7 |

**FIX items:**
1. State the 8 m limit as absolute (no longer path can exist or be added; folding does not help), to close the infrastructure route.
2. Reword "arm tubes carry only the main beams" as "no auxiliary optics or separate auxiliary beam lines can be installed in the arm tubes". The current wording can be read as excluding EPR (the idler travels in the arms).
3. The EPR survivor is modelled as an ideal filter (thin margin, 0.1–0.6 dB). Add a varied `filter_mismatch_excess` property (~0.02–0.03 vacuum units; Ma et al. 2017), and restore the margin by raising stated efficiency from 85% to 90% in both BASE and CONF1. The 8 m cavity still fails.
4. The short-cavity loss floor is the open route (≤ 5–6.5 ppm). Close it with a plain hardware fact (best attainable loss ~5 ppm per reflection), or give the loss a cited unc range (anchor: Isogai et al. 2013, ~10 ppm per round trip at 2 m). Optionally use the exact loss formula with an under-coupling check.
5. Uncoded non-squeezing routes (speed meter): code them, or close them with "main interferometer topology is unchanged".
6. **Scoring definition:** the adopted item = squeeze rotation by an **external detuned filter cavity**. EPR/conditional squeezing is a distinct alternative; a generic "frequency-dependent squeezing" answer with no mechanism is ambiguous (X).
7. kprobe: use a 10–30 ppm loss range, or tighten the criterion to < 30%.

**Other:**
- Verify the Oelker 2016 cavity length (~2 m, not 16 m).
- Identifiability: class high, exact instrument moderate (AdV+ vs A+).
