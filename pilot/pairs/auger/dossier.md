# Dossier: auger (Pierre Auger Observatory surface detector -> AugerPrime surface scintillator)

## 1. Baseline as built

- About 1,600 (final count 1,660) autonomous water-Cherenkov stations on a 1,500 m triangular grid covering about 3,000 km2 near Malargue, Argentina. Each station is a rotomolded polyethylene tank with about 12 m3 of purified water, 10 m2 area and 1.2 m water depth, a Tyvek liner, three 9-inch PMTs, solar power, GPS timing and a radio link. Sources: NIM A 798 (2015) 172, https://arxiv.org/abs/1502.01323 ; engineering array, NIM A 523 (2004) 50, https://doi.org/10.1016/j.nima.2003.12.012 ; PDR section 4.1, https://arxiv.org/abs/1604.03637
- Hybrid design: 4 fluorescence sites x 6 telescopes (plus HEAT) overlook the array. They measure Xmax directly, but only on dark, clear nights: duty cycle about 15%. Source: PDR sec. 2.3 and ch. 6 ("Optical observations of Xmax can presently be performed only with a duty cycle of about 15%"), https://arxiv.org/abs/1604.03637
- Physics goal: the energy spectrum, arrival directions and mass composition of cosmic rays above about 10^18.5 eV, including composition in the flux-suppression region above about 4x10^19 eV.

## 2. Problem solved by the adopted item

- The fluorescence detector's 15% duty cycle gives too few Xmax events above 10^19.5 eV. The surface array runs at 100% duty cycle, but a single water volume measures only a mixed signal. The muon content of vertical showers can be estimated only indirectly. PDR sec. 2.3: "the largest boost in performance ... is expected from an improved composition sensitivity of the surface detector array with its 100% duty cycle ... by measuring ... the decomposition between electromagnetic and muonic components at ground level."
- How it works: in the thin scintillator, the ratio of electromagnetic to muonic integrated signal "is more than a factor two higher ... than in a water-Cherenkov detector" (PDR sec. 2.3.4). A 2x2 matrix inversion then gives the muonic signal at each station.
- Performance: the reconstructed resolution of S_mu(800) is about 22% (p) and 14% (Fe) at 10^19.8 eV and 38 deg. The proton-iron merit factor is about 1.5 (Table 3.4: 1.54 for showers with mean energy 10^19.6 eV, QGSJetII-04). PDR sec. 3.5.
- Cost: WBS 1.1 "Scintillator Surface Detector" is US$ 10.30 M with infrastructure and US$ 8.36 M without it, for 1660 stations plus spares. That is about US$ 5.0 k (no infrastructure) to 6.2 k (with infrastructure) per station. Source: PDR Appendix A.1.
- Deployment: two teams of two people, 1.5 h of work at each site, three stations per team per day. The unit is mounted on a light aluminium frame on the tank's lifting lugs. Source: PDR sec. 9.2.
- Scope: the scintillator method is for more vertical showers. For zenith angles above about 65 deg the EM cascade is absorbed before reaching the ground, and the water stations see an almost pure muon signal. Source: arXiv:2305.10104, https://arxiv.org/abs/2305.10104

## 3. Alternatives considered

- Layered (two-volume) water-Cherenkov tank, "LSD": a Tyvek separation is inserted into the existing liner, and the top and bottom layers are read separately. Muon-size resolution is 20% (p) / 16% (Fe) at 10 EeV, and Fisher separation is about 2 or more above 10^19 eV. Letessier-Selvon et al., NIM A 767 (2014) 41, https://arxiv.org/abs/1405.5699 . It was one of the two finalists out of five. The scintillator was chosen as "a more non-invading solution", although its resolution was "not so good as in the case of the layered surface detector". Source: CORDIS AUGER2FUTURE final report, https://cordis.europa.eu/project/id/328826/reporting
- RPCs under each tank, "MARTA": four RPCs of 1.2 x 1.5 m2 (over 7 m2) in a concrete structure under the WCD. The tank provides 170 g/cm2 of shielding. Muon resolution is below 20% up to 1000 m at 10^19 eV. Abreu et al., EPJ C 78 (2018) 333, https://arxiv.org/abs/1712.07685 . It requires the station to sit on a new concrete support.
- Buried scintillator muon counters, AMIGA/UMD: 30 m2 per station, buried 1.3 to 2.3 m deep. Deployment takes about two days per station with a retro-digger and three technicians, and 21 m3 of soil is removed per 10 m2 module (PDR sec. 9.6). Completing 61 stations, of which 7 were already built, costs US$ 1.6 M, or about US$ 30 k per station. These counters were adopted only for the 23.5 km2 infill. PDR: shielded/buried detection "is not feasible for the 1660 surface detectors".
- Radio antennas: an R&D option (AERA) in 2014. Radio was later added array-wide in 2019-2024 for inclined showers above 65 deg, where it is fully efficient from about 70 deg. Its proton-iron merit factor with the WCD is 1.60. Source: arXiv:2305.10104
- Extending the fluorescence duty cycle from about 15% to about 29%: adopted as a complement, not as an alternative (PDR ch. 6).

## 4. First public commitment

- The collaboration took the internal decision in November 2014. Source: SDEU CDR slides, Orsay, 4 Feb 2015, https://atrium.in2p3.fr/nuxeo/nxfile/default/ca67b159-730d-48ae-a472-49eebd0d30ed/blobholder:0/SDE_Upgrade_CDR_04fev15_V4.1.pdf : "The collaboration decided to upgrade the SD with Scintillator detector on top of the tank in November 2014."
- First public paper: R. Engel for the Pierre Auger Collaboration, "Upgrade of the Pierre Auger Observatory (AugerPrime)", PoS(ICRC2015)686, https://pos.sissa.it/236/686 (also in arXiv:1509.03732). Verbatim: "The key element of the upgrade will be the installation of a new detector consisting of a plastic scintillator plane above each of the existing water-Cherenkov detectors (WCD)."
- Full design report: arXiv:1604.03637, dated April 2015. Verbatim: "the upgrade will include new 4 m2 plastic scintillator detectors on top of all 1660 water-Cherenkov detectors".

## 5. Figure of merit

The FoM is composition-tagged exposure under the deployment constraints:

FoM = G x f_cov x MF^2

- MF = Delta ln N_mu / sqrt(sigma_p^2 + sigma_Fe^2 + 2 sigma_det^2) is the per-event proton-iron merit factor of the muon-content estimator. Statistical power for a composition fraction scales as N x MF^2.
- f_cov = min(1, budget/cost, labour/labour-need) is the fraction of the array that can be equipped.
- G is a feasibility gate:
  - the option must give a measurement complementary to the water signal in the required zenith band;
  - it must not open or alter the sealed water volume (continuity with the archived data);
  - it must not require lifting the filled stations.

The scintillator wins because it is the only option that meets all requirements and is cheap and quick enough to equip the full array. Its per-station resolution is comparable to, not better than, the alternatives.
