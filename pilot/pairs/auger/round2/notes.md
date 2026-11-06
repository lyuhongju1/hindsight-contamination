# Notes: pair auger, round 2

## Design choices
- Invented Teral Plain Array: 1,350 stations, 1.4 km grid, 2,300 km2, 11 m2 x 1.3 m water, two PMTs, FD 12% of the time. Numbers shifted from the real Auger values (round-1 identifiability finding).
- No cost, labour, lifting or opening rules anywhere. Every option is checked against every stated fact: zenith band, water depth, resolution, energy, spacing, full-time duty (rule 8). No booleans (rule 9).
- The round-1 tie bug is gone: `viable()` builds a list from explicit checks. There is no argmax and no fallback to the first key.
- No web access. All property values come from the dossier sources or the round-1 key.

## Conflict mechanisms
- CONF1 (zenith 0-55 changed to 70-84 deg): the EM cascade is absorbed before ground above ~65 deg (arXiv:2305.10104). The thin panel's EM/mu contrast disappears. Radio (fully efficient from ~70 deg) remains viable.
- CONF2 (water depth 1.3 m changed to 0.25 m): the panel separates components only because deep water responds very differently to EM particles and muons (PDR sec 2.3.4, shown with a 1.2 m tank). A 0.25 m tank is itself a thin detector, so the 2x2 inversion becomes degenerate. The layered tank and the under-tank chambers (which need ~170 g/cm2 of water shielding) also fail. The buried counter (own soil shielding) remains viable.
- Coherence (rule 10): a 0.25 m tank still triggers on showers. Inclined showers at 70-84 deg on a 1.4 km grid are a standard regime. Neither edit affects the FD or the electronics.

## Failing levels and why
- CONF1 and CONF2 FAIL keylib's ">= 2 viable" test. Each has exactly one honest survivor (radio; buried counter). Nothing in the dossier gives a second physically viable option: FD extension (29%) fails the full-time requirement, and the shielded or layered options fail the stated physics. I did not invent a survivor or adjust any property to force a pass. The coordinator allowed one survivor for the inclined CONF, but keylib enforces two.
- Robustness caveat: keylib varies angles and log10 E by x0.5-2. This is not physical for zenith limits (it can exceed 90 deg), and it makes near-equal thresholds coin flips (radio zen_min 70 vs stated 70). That is why CONF1 shows ">=2_viable 0.052" and CONF2 shows "0.001".

## Number changes log
- None. The stated numbers were fixed before the first run.

## Doubts
- Radio max spacing 3 km and radio res 0.09 are round-1 author estimates, flagged there. A zen_min of 0.0001 stands for 0 deg, because keylib cannot vary zero.
- The panel's depth threshold of 1.2 m is the depth at which the contrast is cited, not a measured minimum. The real minimum is lower, though well above 0.25 m.
- The real AugerPrime Radio Detector is the CONF1 survivor, so CONF1 can be answered by recall (round-1 red team (b)).
