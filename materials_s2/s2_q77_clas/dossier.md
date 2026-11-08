# Dossier: s2_q77_clas (PROVISIONAL; second dater running)

## Baseline as built: CLAS (Hall B, Jefferson Lab; operated 1997-2012; reference paper 2003)
- CEBAF Large Acceptance Spectrometer: six-sector superconducting toroid (six coils, field mainly azimuthal, ~1-2 T at the coils, field-free on the beam line), drift chambers (3 regions), Cherenkov counters, time-of-flight scintillators, and forward electromagnetic calorimeters (EC). Mecking et al., NIM A503 (2003) 513.
- EC: six triangular modules, one per sector, outside the coils at ~5 m from the target, covering 8-45 deg; lead/scintillator sampling, 39 layers (10 mm scintillator + 2.2 mm Pb), ~16 X0, U/V/W stereo readout with 10 cm strips; ~8 m^2 per module (~50 m^2 total). Resolution sigma/E ~ 0.116/sqrt(E[GeV]) (sigma). Amarian et al., NIM A460 (2001) 239.
- Physics goal: electron and photon detection for electro-production of mesons and baryon resonances at beam energies up to ~6 GeV; electron/pion separation, neutral detection.

## Item targeted
- The single counted item: a pre-shower calorimeter (PCAL) in front of the RETAINED EC: lead/scintillator, 15 layers, ~5-5.5 X0, U/V/W stereo with 4.5 cm strips (finer granularity), to separate the two photons of pi0 up to ~10 GeV/c and complete shower containment for 11 GeV electrons.
- The EC stays; PCAL is an add-on in front of it. The intrinsic resolution of the combined PCAL+EC remains of the sampling type, ~10%/sqrt(E) (sigma) (CLAS12 FTOF/ECAL papers, NIM A959 (2020) 163419 for the PCAL, Asryan et al.).

## Commitment document
- CLAS12 Technical Design Report / conceptual design, arXiv:0810.4718 (2008): upgrade of the forward EC with a pre-shower calorimeter to improve pi0/gamma separation at high momentum.

## Documented alternative(s) not adopted
- Replacing the forward calorimeter with a homogeneous crystal calorimeter (PbWO4), as done in fixed-target JLab experiments for photon-energy precision: PrimEx HyCal (PbWO4 inner part, sigma/E ~ 2.6%/sqrt(E), Gasparian et al.; Larin et al. PRL 106 (2011) 162303) and the CLAS inner calorimeter IC (424 PbWO4 crystals, DVCS run 2005, sigma/E ~ 4.5%/sqrt(E) in situ; NIM A 2010 / Girod et al. PRL 100 (2008) 162002). CMS ECAL PbWO4 stochastic term 2.8%/sqrt(E) (sigma), CMS JINST 3 (2008) S08004.
- Within the sampling class: a fine-sampling (shashlik) rebuild, ~3%/sqrt(E) (KOPIO prototype), not adopted.

## adoption_status
- **built and operated.** PCAL was built for CLAS12 and has operated since 2017-2018 (Burkert et al., NIM A959 (2020) 163419; Asryan et al., NIM A959 (2020) 163425).

## Mechanism (see notes.md)
- BASE: pi0 two-photon separation at ~10 GeV/c and moderate resolution; preshower + retained sampling calorimeter passes.
- CONF1: adds a sigma/E <= 2.5% at 2 GeV photon-energy requirement (narrow two-photon invariant-mass / exclusive missing-mass peak). Sampling term of retained calorimeter dominates; item fails robustly; PbWO4 (depth ~22 X0 = 20 cm, within a stated 30 cm) passes.
