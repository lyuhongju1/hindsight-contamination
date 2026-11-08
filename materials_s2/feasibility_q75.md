# Feasibility q75: NA49 -> NA61/SHINE (arXiv:0709.1867)

## Item F1: helium-filled beam pipe through the TPC sensitive volumes

- Delta electrons, He vs open gas: the rate per cm is proportional to z_beam^2 x (Z/A)rho. He has (Z/A)rho ~8e-5 g/cm3 and Ar/CO2 ~8e-4, so He is about 10x lower for every beam species and energy. He always wins, so no route.
- Delta electrons, He vs vacuum: for Pb at 158A GeV with T0 ~50 MeV, 2.5 m of He gives ~0.4 deltas per ion. The end windows of an evacuated pipe must hold 1 atm (~150-200 um mylar, ~0.3 per ion per window), against ~25 um for He windows. He and vacuum differ by a factor of ~1-3, which does not survive x0.5-2. No route.
- Multiple scattering in the pipe wall (low-momentum tracking): ~125 um mylar is ~4e-4 X0, giving theta0 ~2 mrad at 100 MeV/c. 1 m of Ar is ~9e-3 X0, giving ~13 mrad. The wall is negligible next to the TPC gas itself, and the thicker wall of a vacuum pipe makes vacuum worse than He. No route.
- Secondary interactions: He column plus windows ~6e-4 lambda_I, against 2.5 m of Ar ~4e-3 lambda_I. He beats open gas, and vacuum beats He only within a factor of ~2. Not robust. No route.
- TPC field distortion from the pipe: fixed by field-shaping strips and the pipe's potential, which are settings of the item (C1). No route.
- He diffusing into the TPC gas: fixed by the gas-flow and purge rate, a setting. No route.
- Dead volume around the beam (a stated need to measure beam or fragment tracks along the axis, with light-ion or proton beams where open gas survives): the pipe diameter, length and removability are settings of the item. Beam Z is already measured by the stated upstream beam counters. Contrived, not a robust physical failure. No route.
- Verdict F1: NO WINDOW.

## Item F2: Projectile Spectator Detector (Pb/scintillator modular hadron calorimeter) replacing the VCAL

- Radiation dose: Pb at 158A GeV deposits ~33 TeV per ion. At ~1e4 ions/s (TPC-rate-limited) for ~1e6 s of spill a year, that is ~5e4 J/yr. Averaged over the ~0.4 t central module this is ~100 Gy/yr. The shower core gets ~1-10 kGy/yr, against a polystyrene damage onset of ~10-100 kGy. Both numbers are uncertain by about 10x, so the failure is not robust under x0.5-2. Raising the intensity breaks rule 7, because the TPC rate limit caps it. Settings within the item also defeat it: a rad-hard scintillator or fibre grade, replaceable central modules, transverse position. No route.
- Energy resolution for centrality at 13A-158A GeV: PSD sigma/E ~56%/sqrt(E) (sigma, NA61 PSD prototype values, from memory). Quartz-fibre ZDC sigma/E ~200-250%/sqrt(E) (sigma, ALICE/CMS ZDC class, from memory). For 7 spectators at 13A GeV: PSD sigma ~5 GeV, under 1 nucleon (13 GeV); quartz sigma ~24 GeV, over 1 nucleon. The resolution requirement makes quartz fail and the PSD pass, the opposite of what is needed. No route.
- Transverse granularity for the reaction plane: the PSD is modular (~10-20 cm cells), and quartz can be segmented equally. The old VCAL fails here, not the PSD. No route.
- Non-compensation: the PSD's ~4:1 Pb:scintillator ratio gives e/h ~1. Quartz Cherenkov has e/h >> 1, making fluctuations and linearity worse. This penalises quartz, not the PSD. No route.
- Speed and pile-up: both are ns-scale at <=1e5/s. No separation. No route.
- Keep or refurbish the VCAL: it lacks the stated granularity for the reaction plane and the resolution for spectator counting. VCAL fails, the PSD passes. No route.
- Verdict F2: NO WINDOW. The only mechanism where the PSD fails (dose) is not robust and is defeated by settings within the item. The only survivor that has dose margin (quartz) fails the resolution that centrality selection at 13A GeV needs.
