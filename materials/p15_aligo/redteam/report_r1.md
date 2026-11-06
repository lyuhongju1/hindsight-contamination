# Red team r1 (confirmation): p15_aligo (2026-11-06). Verdict: NO HONEST CONFLICT (agrees with author)

The common pattern: DC readout couples every common noise through the offset x0. The separate-reference readout couples it through L_eff≈7e-13 m/rad or ε·x0, which is 10–100× smaller. A conflict would need a noise that exists only in the reference path and that no servo or design choice can remove.

**Routes examined (all fail):**
- **Reference-phase noise:** a fast piezo servo defeats it. Sensing noise reaches only the shot level, so it is not robust.
- **Requirement band:** removes the motivation for the adopted item; nothing fails.
- **No squeezing:** the same.
- **Scattered light:** the adopted item loses only if f_ref is more than ~100× f_AS. Fringe wrapping needs motion of order λ, which is impossible under BASE. Making the reference path worse requires exclusion wording, or an edit that hurts DC readout more.
- **Dark-port contrast:** points the wrong way (it favours the adopted item).
- **Reference RIN:** a recycling-cavity pickoff gives a ~100× advantage. Forbidding that pickoff would be an exclusion or space rule.
- **Readout loss budget:** a ~0.3–2% added loss that depends on design. It is a knife-edge disguised exclusion and not robust.
- **Laser frequency noise × path difference:** ~4e-25 m/√Hz, negligible.
- **Radiation pressure, thermal noise and jitter:** negligible or common to both readouts.

**Adoption status:** approved not built. Sources: arXiv:2508.08423 lists BHD as a planned O5 upgrade; LIGO-T2200032-v5 is the "Final design for the O5 BHD system". No descoping was found. Reference for the couplings: arXiv:1506.07308.

**BASE fixes (only if BASE is ever reused):**
- delete the offset noise-coupling clause (a hint);
- state the filter cavity as built;
- drop "including all optics beyond the antisymmetric port" and "in quadrature with the signal".

## Outcome
p15_aligo is a **zero-unit pair** (author plus red-team confirmation, per A2). Replacement: **p16_besiii**.
