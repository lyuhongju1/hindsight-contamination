# Dossier: t2k_nd280

## Baseline: ND280 as built
Source: T2K Collaboration, "The T2K Experiment", NIM A 659 (2011) 106, https://arxiv.org/abs/1106.1238

- Purpose: off-axis near detector, 280 m from the J-PARC target. It measures the unoscillated nu_mu spectrum and the nu_e contamination, and constrains flux and cross sections for Super-Kamiokande.
- UA1/NOMAD magnet: 0.2 T dipole, inner volume 7.0 x 3.5 x 3.6 m, yoke 850 t. The SMRD scintillator sits in the yoke gaps.
- P0D: 40 P0Dules of triangular polystyrene bars with water bags, brass and lead. Active size 2103 x 2239 x 2400 mm, 16.1 t with water and 13.3 t without.
- TPCs: three of them, gas Ar:CF4:iC4H10 (95:3:2), bulk Micromegas readout.
- FGDs: each 2300 x 2400 x 365 mm with 1.1 t of target. Bars are 9.61 x 9.61 x 1864.3 mm, oriented perpendicular to the beam. FGD1 has 5,760 bars in 30 layers of 192. FGD2 has 7 XY modules plus six 2.5 cm water layers.
- ECal: lead-scintillator. Readout: WLS fibres and MPPCs throughout.

## Problem solved by the adopted item
- "The existing FGDs consist of plastic scintillator bars aligned in either x or y direction perpendicular to the beam direction, which limits the acceptance to essentially the forward direction." (TDR Sect. 2.1, https://arxiv.org/abs/1901.03750)
- Lepton efficiency "drops considerably for scattering angles with respect to the beam direction larger than ~50 degrees". The high-angle ToF-based selection reaches only about 20% efficiency. (TDR Sect. 6.1)
- Protons below about 450 MeV/c are not reconstructed in the FGD (https://arxiv.org/abs/1610.06367 Sect. 1). This is roughly 50% of the protons (same source, Sect. 3).
- Systematic uncertainty is about 6% now; the T2K-II goal is about 4% (TDR Sect. 1).
- Adopted item, per the TDR:
  - 192 x 192 x 56 cubes of 1 cm^3: 2,064,384 cubes, 58,368 channels, about 2 t.
  - Muon efficiency above 90% at all angles.
  - Proton threshold about 300 MeV/c with three views, against about 500 MeV/c with two views (TDR Sect. 2.1, 6.4.1).

## Alternatives considered
- WAGASCI-like 3D grid with water (2.5 cm cells, 70% H2O / 30% CH by mass). It was the "Reference option for the target detectors" in 2016 (https://indico.cern.ch/event/568177/contributions/2312536/attachments/1367753/2073240/T2K-NDupgrade-CERN-v4.pdf). Its proton threshold is about 450 MeV/c (arXiv:1610.06367).
- Empty WAGASCI (no water): proton threshold 200-250 MeV/c (arXiv:1610.06367; July 2016 task-force talk, https://indico.ipmu.jp/event/94/contributions/2149/attachments/1710/2013/T2K-upgrade-HK-july2016.pdf).
- FGD-like bar target with finer segmentation or horizontal orientation, i.e. two views (CERN 2016 talk above; TDR Sect. 6.5.4, "FGDXY").
- High-pressure gas TPC as a second option: "a high pressure gas TPC, which will be able to achieve a low momentum threshold with 4pi acceptance" (T2K-II proposal, https://arxiv.org/abs/1609.04111 Sect. VI). For proton thresholds of about 10 MeV kinetic energy in 10 atm argon, see https://arxiv.org/abs/2203.06281.
- Options compared at NuINT 2017: "FGD-like / Super-FGD (cubes) / Wagasci-like" (https://indico.triumf.ca/event/6/contributions/2217/attachments/1594/1802/NuINT17-ND280upgrade-Yokoyama-v5.pdf).

## First public commitment
- The concept paper, Blondel et al., arXiv:1707.01785 (6 July 2017), proposed the item but did not commit the collaboration to it.
- Earliest commitment: the ND280 upgrade proposal CERN-SPSC-2018-001 / SPSC-P-357, submitted January 2018. I could not retrieve its text because the CDS page was bot-blocked, so I have no verbatim quote from it.
- First retrievable committing document: T2K ND280 Upgrade TDR, arXiv:1901.03750 (11 Jan 2019), https://arxiv.org/abs/1901.03750. Verbatim abstract: "This goal is achieved by modifying the upstream part of the detector, adding a new highly granular scintillator detector (Super-FGD), two new TPCs (High-Angle TPC) and six TOF planes." Sect. 2.1 also states: "We have chosen a novel design of fine grained fully-active plastic scintillator detector, called SuperFGD".

## Figure of merit
The FoM is the yield of kinematically complete CC events, with both the muon and the leading proton reconstructed:

FoM = V · rho · w_req · eps_mu(angles) · eps_p(angles) · F(p > p_th)

These are the events used for transverse kinematic imbalance, which the TDR (Sect. 6.5) gives as the main gain over an FGD-like target. The plastic-cube target wins for three reasons:
- it keeps full solid-density mass, unlike the gas TPC and the empty grid;
- it has flat high-angle efficiency, unlike planar bars;
- it has the lowest threshold among the dense options.
