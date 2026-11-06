# notes: p09_nemo3

## Design choices
- Target: 8-in. high-QE PMTs directly coupled to large PS blocks (only counted item).
- Mechanism (CONF1): calorimeter **granularity**. A ~202 mm bulb plus its magnetic shield and wrapping sets a minimum cell pitch of ~210 mm when each cell has its own tube. CONF1 requires that two electron entry points >= 15 cm apart land in different cells (individual electron energies), i.e. cell pitch * sqrt(2) <= 150 mm. BASE has 40 cm, which the adopted module meets (pitch 210-280 mm, diagonal <= 400 mm).
- Rejected mechanisms: magnetic field (stronger tracker field would curl ~1 MeV electrons before the wall in a 50 cm tracker, so it is incoherent; at a few mT an iron shield works); PMT-glass radiopurity (glass mass per m2 of wall is similar for 3-in. and 8-in. tubes, and the light-guide workaround cannot be closed by plain fact); timing (8-in. modules meet ~400 ps; no robust failure).
- Resolution requirement set at 18% FWHM at 1 MeV (present cells: 20%, so the upgrade is useful in BASE) so that a small-PMT survivor passes with cited precision. This is weaker than the real 7-8% goal; deliberate, so that the CONF has an honest survivor.
- Minimal pair: BASE and CONF1 differ only in "40 cm" -> "15 cm" (diff checked).

## Survivors per CONF
- CONF1: 1 (76 mm PMT directly coupled to ~8-11 cm PS cubes, mu-metal shield). 5-in. direct (pitch 138 mm, diagonal 195 mm) fails segmentation; 10-in. fails; present light-guide cells fail resolution and segmentation.

## Fixed inputs
- res_req 18%, t_req 0.6 ns, depth_req 30 mm, field 3 mT, sep 400/150 mm: exact requirements stated in the descriptions.
- diag_factor = sqrt(2): geometric fact (max separation of two points in one square cell).

## unc ranges (all x0.8-1.25, the narrowest allowed)
- PMT bulb diameters (202, 76, 133, 253 mm): manufacturer datasheet dimensions (exact to a few mm).
- 8-in. resolution 7.5 +- 0.2%: arXiv:1707.06823 Table 7.
- 3-in. direct-coupled resolution 14.2%: NEMO-3 3-in. module ~17% FWHM at 1 MeV (NIM A 536 (2005) 79, from memory) / measured direct-coupling gain 1.20 +- 0.02 (arXiv:1707.06823 sec 4.1). DOUBT: the 17% figure is quoted from memory, not re-fetched.

## Post-run change log
- Before first run (not tuned on key output): separations changed 30 -> 40 cm (BASE) and 12 -> 15 cm (CONF1) after realising that a square cell separates two points only if its diagonal (not its side) is below the separation; with 30 cm the adopted module (pitch >= 210 mm, diagonal 297 mm) would have been marginal in BASE, and with 12 cm a 76 mm tube (+shield) would have been marginal.
- First run: BASE PASS, CONF1 PASS. No further changes.

## Doubts
- Workaround: several small cells funnelled through long light guides to 8-in. tubes staggered in depth. Not closed by a plain fact; it would add light-guide loss (x1.2 in resolution) and still needs one tube per cell, so the tube packing remains at >= 210 mm pitch per layer and needs >= 3 layers. Judged not credible, but a red team may raise it.
- An 8-in. tube reading several cells in common loses individual-cell energies, so it fails the stated requirement.
- Resolution of the 3-in. survivor is derived (two cited factors), not measured directly in this geometry. Smaller cubes should give better light collection than the NEMO-3 blocks, so the estimate is conservative.
- adoption_status "built and operated" is from memory (SuperNEMO Demonstrator), not re-fetched.
