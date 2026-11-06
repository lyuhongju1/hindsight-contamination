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

## Fixed inputs (keylib v4.1, inputs["fixed"], not varied)
- zen_min_deg = 0 (stored as 0.0001) in BASE and CONF2, 70 in CONF1: the lower limit of the zenith band is set by definition in description line 8. It is a selection cut, not a measured property.
- zen_max_deg = 55 in BASE and CONF2, 84 in CONF1: the upper limit of the same band, also a definitional selection cut from line 8.
- water_depth_m = 1.3 in BASE and CONF1, 0.25 in CONF2: the tank geometry is stated as fact in line 2. It is the instrument's own construction, not a cited technology property.
- duty_req = 1.0: line 6 says "full-time exposure", which by definition is a fraction of 1 of the time.
- Everything else stays varied: spacing, energy, resolution requirement, FD duty, counts and areas, and all option properties (including each option's zenith limits and depth threshold).

## v4.1 rerun (2026-11-05), diagnosis of the remaining FAILs
- CONF1 has >=1 viable in 0.241 of draws. Radio's cited zen_min (70) is varied against the fixed 70, which is a coin flip. Radio's e_min_log10 and its spacing limit are also varied.
- CONF2 has >=1 viable in 0.084 of draws. For the buried counter, three checks fail often under the draws:
  - e_min_log10 = 17.5 against the stated 19.0. This is an encoding flaw: a log10 energy scaled by x0.5-2 is not physical. Encoding the energy linearly (10^17.5 eV against 10^19 eV) would make the check robust.
  - max_spacing_km = 1.5 against 1.4: near-equal values, so a coin flip.
  - zen_max 65 against 55.
- Following the coordinator's instruction, I made no changes to the encoding or the property values in this revision. These are left for a decision.

## Post-run changes (keylib v4.1 + unc revision, 2026-11-05; coordinator-authorised)
Stated numbers were changed after the first run. Each change is logged here with its reason.
1. Grid spacing 1.4 km -> 0.7 km, in BASE, CONF1 and CONF2.
   - Reason: knife-edge against the per-station options' cited 1.5 km (the grid for which their resolutions are quoted).
   - Coherence side effect: the area changes from 2,300 km2 to 570 km2 (1,350 x 0.866 x 0.7^2), in all three files. 0.7 km is chosen to avoid the real 0.75 km infill value.
2. BASE/CONF2 zenith band 0-55 -> 0-35 deg.
   - Reason: knife-edge against the cited ~65 deg limit, once the zenith is encoded on the physical scale (sec theta).
3. CONF1 zenith band 70-84 -> 80-84 deg (this is the CONF edit itself).
   - Reason: knife-edge, radio "fully efficient from ~70 deg" against a band starting at 70.
4. kprobe CONF1 angle changed from 75 to 82 deg to match the new band.

## Re-encoding (no cited value changed)
- Zenith is now encoded as sec(theta), the air-mass factor: atmospheric slant depth divided by vertical depth. This is the linear physical variable behind EM absorption and radio footprint size.
- Energies are encoded in eV, not log10.
- Options with no lower or upper zenith limit omit that key. This avoids a 1.0-against-1.0 coin flip.
- No `unc` ranges were used. No source in the dossier states a precision for the decisive properties.

## Fixed inputs (supersedes the earlier list)
- spacing_km 0.7: grid geometry stated in line 1 (a definition of the instrument).
- water_depth_m 1.3 / 0.25: the tank geometry stated in line 2.
- duty_req 1.0: "full-time exposure" means a fraction of 1 by definition.
- e_min_eV 1e19: the energy selection stated in line 6.
- sec_zen_min, sec_zen_max: the band edges stated in line 8 (selection cuts).
- res_req 0.30: the requirement stated in line 9. It is a stated threshold, not a measured quantity.
- Still varied: station count, area, floor, number of PMTs, FD duty, and every option property.

## Doubts added
- Radio has no upper zenith limit in the key. The 85 deg in arXiv:2305.10104 is an analysis selection, not a detection limit, and the footprint grows with zenith. This is my reading and needs red-team review. With a cited 85 deg limit, the 84 deg band edge would be a knife-edge again.
- The buried counter's 65 deg limit was set in round 1 as "vertical analysis". It is not an EM-absorption limit for a shielded counter. I kept it unchanged.
- Each CONF has one survivor (n_survivors = 1): a covariate, now allowed by keylib v4.1.
