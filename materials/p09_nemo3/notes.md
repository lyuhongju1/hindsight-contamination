# notes: p09_nemo3

## Design choices
- Target: 8-in. high-QE PMTs directly coupled to large PS blocks (only counted item).
- Mechanism (CONF1): calorimeter **granularity**. A ~202 mm bulb plus its magnetic shield and wrapping sets a minimum cell pitch of ~210 mm when each cell has its own tube. CONF1 requires that two electron entry points >= 15 cm apart land in different cells (individual electron energies), i.e. cell pitch * sqrt(2) < 150 mm. BASE has 40 cm, which the adopted module meets (pitch 210-280 mm, diagonal <= 400 mm).
- Rejected mechanisms: magnetic field (stronger tracker field would curl ~1 MeV electrons before the wall in a 50 cm tracker, so it is incoherent; at a few mT an iron shield works); PMT-glass radiopurity (glass mass per m2 of wall is similar for 3-in. and 8-in. tubes, and the light-guide workaround cannot be closed by plain fact); timing (8-in. modules meet ~400 ps; no robust failure).
- Resolution requirement set at 18% FWHM at 1 MeV (present cells: 20%, so the upgrade is useful in BASE) so that a small-PMT survivor passes with cited precision. This is weaker than the real 7-8% goal; deliberate, so that the CONF has an honest survivor.
- Minimal pair: BASE and CONF1 differ only in "40 cm" -> "15 cm" (diff checked).

## Survivors per CONF
- CONF1: 1 (76 mm PMT directly coupled to ~8-11 cm PS cubes, mu-metal shield). 5-in. direct (pitch 138 mm, diagonal 195 mm) fails segmentation; 10-in. fails; present light-guide cells fail resolution and segmentation.

## Fixed inputs
- res_req 18%, t_req 0.6 ns, depth_req 30 mm, field 3 mT, sep 400/150 mm: exact requirements stated in the descriptions.
- diag_factor = sqrt(2): geometric fact (max separation of two points in one square cell).

## unc ranges (x0.8-1.25 where a precision is cited; others default x0.5-2)
- PMT bulb diameters (202, 76, 133, 253 mm): manufacturer datasheet dimensions (exact to a few mm).
- 8-in. resolution 7.5 +- 0.2%: arXiv:1707.06823 Table 7.
- (superseded in r1, see below) 3-in. direct-coupled resolution 14.2% = NEMO-3 figure / 1.20.
- r1: 3-in. survivor resolution uses the default x0.5-2 range (derived scaling, no cited precision); nominal 8.0% FWHM, so the range is 4.0-16.0%, all below 18%.

## Survivor resolution derivation (r1, option (i))
Photostatistics-dominated scaling: FWHM proportional to 1/sqrt(N_pe), with N_pe proportional to (photocathode coverage of the cell face) x (QE). Both modules are directly coupled, so the light-guide factor does not enter.
- Reference: C256 block (256 x 256 mm face) directly coupled to an 8-in. R5912-MOD, 7.5 +- 0.2% **FWHM** at 1 MeV (arXiv:1707.06823 Table 7, R5912-MOD AI; re-fetched 2026-11-06). The paper's resolution symbol is FWHM (its summary contrasts NEMO-3's 14-17% FWHM with ~7% for SuperNEMO), so it is not sigma.
- Coverage factor: 8-in. bulb 202 mm on a 256 mm face: pi*101^2/256^2 = 0.489. 3-in. bulb 76 mm on an 80 mm face: pi*38^2/80^2 = 0.709. Ratio 1.450. (Bulb diameters: datasheet values; using effective photocathode diameters, ~70 mm and ~190 mm, gives ratio 1.39 and 8.15%, no material change.)
- QE factor: R5912-MOD 41% at 400 nm (arXiv:1707.06823 Table 6). The 3-in. tube is taken at the standard 25%, the average QE of the NEMO-3 3-in. and 5-in. tubes (arXiv:1707.06823 sec 4.2.1). This is conservative, since the same section says ~40% peak-QE 3-in. tubes exist. Ratio 25/41 = 0.610.
- N_pe ratio = 1.450 x 0.610 = 0.884. Resolution = 7.5% / sqrt(0.884) = **7.98%, so 8.0% FWHM** (sigma 3.4%).
- Cross-check from the other side: NEMO-3 3-in. block, NIM A 536 (2005) 79 (physics/0402115), Table 11: sigma/E = 7.3 +- 0.1% at 1 MeV = 17.2% FWHM, through a light guide. Removing the guide (/1.20, arXiv:1707.06823 sec 4.1, measured on a NEMO-3 block with a 5-in. tube) gives 14.3%. The coverage goes from a 76 mm tube on a ~200 mm face (0.113) to 0.709 (x6.3), giving 14.3/sqrt(6.3) = 5.7%. The two routes bracket 5.7-8.0%. The key takes the conservative 8.0%.
- Robustness: even at x2 (16.0%) the survivor is below the unchanged 18% requirement. The 18% requirement and the separations are unchanged.
- The 5-in. non-survivor was rescaled the same way (133 mm on ~138 mm, coverage 0.729, giving 7.9%) for consistency. It fails on segmentation regardless.

## Shape independence and strictness of the CONF1 failure (r1)
- The failure does not depend on cell shape. Any cell holding a directly coupled 202 mm tube has a largest dimension >= 202 mm > 150 mm, so two points 150 mm apart fit inside it for every shape (square, hexagonal, round). The square-cell sqrt(2) factor in the key only adds margin.
- The criterion is strict: two points at least X apart must be in different cells, so the cell's maximum internal distance must be < X (a cell diameter exactly equal to X would hold both points). key.py uses `<`.

## Post-run change log
- Before first run (not tuned on key output): separations changed 30 -> 40 cm (BASE) and 12 -> 15 cm (CONF1) after realising that a square cell separates two points only if its diagonal (not its side) is below the separation; with 30 cm the adopted module (pitch >= 210 mm, diagonal 297 mm) would have been marginal in BASE, and with 12 cm a 76 mm tube (+shield) would have been marginal.
- First run: BASE PASS, CONF1 PASS. No further changes.

## post-run changes (r1 fixes)
Source: redteam/report_r1.md (2026-11-06). None of these changes was tuned on key output. The 18% requirement and the 400/150 mm separations are unchanged.
1. BASE.txt and CONF1.txt, line 2: "About 40 kg" -> "About 9 kg" (identical edit). Reason: coherence. 45 mg/cm2 x 21 m2 = 9.45 kg. NAME/ANON are unchanged: they describe the real detector (~10 kg) and do not carry the invented sentence.
2. key.py, survivor res_fwhm_pct 14.2 -> 8.0 and unc entry removed (default x0.5-2). Reason: the /1.20 direct-coupling factor applied to a NEMO-3 figure does not transfer, and the survivor previously passed only through the x0.8-1.25 floor. The value is re-derived per option (i); see "Survivor resolution derivation". Note: the r1 instruction described the 7.5 +- 0.2% as sigma. The re-fetched paper shows it is FWHM. Read as sigma (17.7% FWHM) it would scale to ~18.8% FWHM and the survivor would fail, so this point is load-bearing.
3. NEMO-3 citation: the memory figure "~17% FWHM" is replaced by NIM A 536 (2005) 79, Table 11, sigma/E = 7.3 +- 0.1% at 1 MeV (17.2% FWHM), as verified by the red team. It is now used only as a cross-check.
4. key.py, 5-in. non-survivor res 11.7 -> 7.9. Reason: consistency with the same derivation. It fails on segmentation either way.
5. key.py, segmentation test `<=` -> `<`. Reason: a strict criterion (FIX 3). Added a shape-independence note (FIX 3).
6. BASE.txt and CONF1.txt (identical, optional FIX 4, neutral, no technology named): line 4 appends "; the track curvature determines only the sign of the charge." (closes the tracker-energy route by plain fact). Line 10 appends ", whose energies are measured separately".
7. Rerun: BASE PASS. CONF1 PASS: adopted_fails 1.000, survivor viable 1.000. gates.py: GATES PASSED.

## Doubts
- Workaround: several small cells funnelled through long light guides to 8-in. tubes staggered in depth. Not closed by a plain fact; it would add light-guide loss (x1.2 in resolution) and still needs one tube per cell, so the tube packing remains at >= 210 mm pitch per layer and needs >= 3 layers. Judged not credible, but a red team may raise it.
- An 8-in. tube reading several cells in common loses individual-cell energies, so it fails the stated requirement.
- Resolution of the 3-in. survivor is derived (r1: coverage and QE scaling from the 8-in. measurement), not measured directly in this geometry. The scaling ignores non-photostatistical terms (non-uniformity, the effect of block depth on light collection), and these are covered by the x2 range: 16% < 18%.
- Study decision r1: 8-in. tubes reading small cells through light guides is coded C (adopted tube plus valid workaround).
- adoption_status "built and operated" is from memory (SuperNEMO Demonstrator), not re-fetched.

## Post-run changes (r2, 2026-11-06, applied by the orchestrator from red-team r2, which was non-blocking)

- **Survivor resolution nominal 8.0 -> 8.5 % FWHM.**
  - The r1 derivation used EJ-204 PVT data, projected-disc coverage and 25 % QE. It was optimistic on geometry: the 8-in. photocathode is hemispherical (about 1.6x the projected disc), and light collection in a wrapped block saturates (collection ~ A_pc/(A_pc+(1-R)A_wall), R~0.96).
  - Corrected: polystyrene factor x1.04 (Table 4); a 3-in. high-QE tube at ~38 % (sec 4.2.1).
  - Credible range 8-11 % FWHM. The max under x2 is 17 %, still < 18 %.
  - **Doubt:** the gate fails if the nominal exceeds ~9.5 %. With a 25 %-QE 3-in. tube a realistic figure is ~10-11 %, so the survivor relies on a high-QE 3-in. tube, which is cited as available.
- **The r1 cross-check (5.7 %) is withdrawn.** It ignored light-collection saturation; with saturation it gives ~9 %.
- **kprobe:** "directly behind the cell" -> "directly coupled to the back face of the cell, with no light guide" (shuts out the depth-staggering reading).
- **Exploratory note:** at 18 % BASE gives little physical reason to prefer the adopted item over small direct-coupled cells. Expect low BASE elicitation; this is recorded, not gated.
- Correction to r1: the /1.20 light-guide factor was measured on a NEMO-3 block with a 5-in. R6594 (sec 4.1.2), as these notes already said.
