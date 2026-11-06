# p05_sno dossier

## Baseline as built (SNO)
- 1000 t D2O in a 12 m diameter, 5.5 cm thick acrylic vessel (AV), suspended by ropes from a deck; ~9,500 8-inch PMTs on a 17.8 m geodesic support; ~7 kt ultrapure light-water shield; 2,092 m underground (~6,000 m.w.e.), Creighton mine near Sudbury.
- Physics goal: 8B solar neutrinos via CC, NC and ES on deuterium; Cherenkov threshold of a few MeV.
- Source: SNO collaboration, NIM A 449 (2000) 172 (arXiv:nucl-ex/9910016). From memory, not fetched.

## Target item: LAB liquid scintillator (alternative not adopted: pseudocumene / PXE)
Why LAB rather than Te-130 loading: the Te-130 vs Nd-150 contrast is driven by the Q-value (2.53 vs 3.37 MeV) and by phase-space factors. Q-values are known to keV precision, but keylib requires at least x0.8-1.25 variation, so a 2.53 MeV vs 3.37 MeV threshold cut cannot be robust (2.53*1.25 > 3.37*0.8). Phase-space ratios (~4.5) also do not survive the x0.5-2 variation.
LAB instead has one property that differs strongly from the documented alternative PXE: density. LAB is ~0.86 g/cm3 (a deficit of ~140 kg/m3 relative to water). PXE is ~0.985 g/cm3 (a deficit of ~15 kg/m3). The ratio is ~9, which survives x0.5-2 on both. Inside an acrylic vessel immersed in water this is a direct physical (buoyancy-load) conflict. In the real detector it was the main known drawback of LAB: SNO+ had to add a hold-down rope net.

## Commitment documents (from row 5)
arXiv:0810.3694 (2008-10); arXiv:1405.3401 (2014-05).

## Documented alternatives not adopted
Pseudocumene (1,2,4-trimethylbenzene; density 0.876, flash point ~48 C, attacks acrylic); PXE (phenyl-o-xylylethane; density ~0.985, high flash point, acrylic-compatible, shorter attenuation length).

## adoption_status
**built and operated.** SNO+ filled the AV with LAB+PPO (completed 2021-2022) and has operated in scintillator phase since 2022. Source: SNO+ collaboration, "The SNO+ experiment", JINST 16 (2021) P08059 (arXiv:2104.11687), plus later SNO+ scintillator-phase results. From memory; the fill-completion date is unverified.
