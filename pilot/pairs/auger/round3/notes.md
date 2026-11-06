# Notes: pair auger, round 3

The round-3 files are copies of round 2 with the round-2 red-team fixes applied (round2/redteam/report.md). Round 2 is unchanged.

## Instrument (identical in BASE, CONF1, CONF2 except the conflict edit)
- Teral Plain Array: 1,350 stations on a 0.7 km triangular grid, about 570 km2.
- Each station is a one-piece vessel, 11 m2 floor, water depth 1.3 m, filled to within 5 cm of its lid, with two PMTs.
- Fluorescence detectors (FD) operate 12% of the time.
- Goal: composition above 10^19 eV with full-time exposure. Muonic and EM components measured separately for every shower. Muon-number resolution of 30% or better.
- Zenith band 0-35 deg.
- The adopted item (thin ~1 cm, ~4 m2 scintillator on each station) passes in BASE.

## Conflict mechanisms
- CONF1, zenith band changed to 80-84 deg.
  - The EM cascade is absorbed before ground above ~65 deg (arXiv:2305.10104), so the panel and the two-volume tank see no EM contrast.
  - The chambers and the buried counter obtain EM as the water signal minus their muon count, so they also need EM at ground. They fail for the same reason. The buried counter would additionally sit under ~16 m of slant soil (2.3 m x sec 82 deg).
  - Trace electronics and WCD-only analysis give one mixed signal, so they cannot measure two components (line 7). FD fails the full-time requirement.
  - Survivor: radio, which measures the EM component in the air, combined with the water muon signal.
- CONF2, water depth 1.3 m changed to 0.25 m (~0.7 X0 of water, X0 = 36 cm).
  - The tank becomes thin itself. Its muon fraction falls to ~0.17-0.25, close to the panel's ~0.10-0.20, so the 2x2 inversion is too weak for 30% (round-2 red team). The key encodes this as the cited 1.2 m depth at which the contrast is demonstrated (PDR sec 2.3.4). The red team's estimate of the true threshold, ~0.5-0.7 m, is also above 0.25 m.
  - The two-volume tank and the chambers (which need ~170 g/cm2 of water shielding) fail.
  - Deepening in place fails because the vessel is filled to within 5 cm of its lid (line 2): 1.2 - 0.25 m of extra water does not fit.
  - Survivors: the buried counter (own soil shielding) and replace-vessel-plus-panel.
  - Replacement cannot be excluded by a physical fact that is identical in all three files without contradicting BASE's 1.3 m vessels, so it is admitted. Scoring must decide whether "new deeper vessels + panel" counts as proposing the adopted item.

## Key encoding (keys/key.py)
- Zenith is encoded as sec(theta) (slant/vertical depth) and energies in eV.
- Options with no zenith limit omit the key.
- There is no argmax: `viable()` lists the options that pass explicit checks. The round-1 tie bug cannot recur.
- Every stated fact is checked for every option:
  - zenith band
  - water depth / headroom
  - number of independent channels
  - resolution
  - energy
  - spacing
  - duty
- No booleans. No `unc` ranges (no dossier source states a precision).
- Radio upper zenith limit omitted. The ~85 deg in arXiv:2305.10104 is the selection range of that analysis, not a detection limit. The radio footprint grows with zenith, so efficiency does not fall above 85 deg for the reasons that fail the other options. The round-2 red team agreed. If 85 deg were coded as a limit, it would fail about 37% of draws against the 84 deg band edge for a reason that is not physical.

## Fixed inputs (inputs["fixed"], not varied)
- spacing_km 0.7: grid geometry stated in line 1.
- water_depth_m 1.3 / 0.25 and headroom_m 0.05: vessel geometry stated in line 2.
- duty_req 1.0: "full-time exposure" (line 6).
- e_min_eV 1e19: energy selection (line 6).
- sec_zen_min / sec_zen_max: band edges (line 8).
- res_req 0.30: stated requirement (line 9).
- channels_req 2: line 7 requires two components measured separately.
- channels per option: a structural count of independent signals (one mixed water signal for trace electronics, two for every other option). It is an integer property of the design, not a measured quantity, so multiplicative variation is meaningless. Red team to review.
- Varied: station count, area, floor, PMTs, FD duty, and all cited option properties.

## Post-run changes to stated numbers (all logged)
- Round 2: grid 1.4 to 0.7 km (area 2,300 to 570 km2), BASE/CONF2 band 0-55 to 0-35 deg, CONF1 band 70-84 to 80-84 deg. These were knife-edge fixes, authorised by the coordinator and judged honest by the red team.
- Round 3 (text, no numbers): line 2 adds "one-piece vessel ... within 5 cm of its lid", and line 7 reworded. Both are identical in all three files.

## Status
- BASE PASS, CONF1 PASS (n_survivors 1), CONF2 PASS (n_survivors 2). See keys/key_output.txt.
- No forbidden-pattern matches.

## Doubts
- Radio max spacing (3 km) and res (0.09) are round-1 author estimates.
- The trace-electronics resolution of 0.22 is a placeholder. The option is excluded by its channel count, not its resolution.
- CONF1 coherence: the 80-84 deg band keeps ~2% of exposure, ~5-10 events per year above 10^19 eV on 570 km2.
- Identifiability is high (measured, not gated). The CONF1 survivor is the real AugerPrime radio upgrade.
