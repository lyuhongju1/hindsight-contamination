# notes: s2_q78_phenix (PROVISIONAL; second dater running)

## Outcome: NO ROBUST WINDOW (lesson 5). kprobe.json = {}. No descriptions written.

The formal keylib check of the planned CONF1 (sigma_E/E <= 4% at 2 GeV) passes only at the edge
(adopted_fails = 0.954 against a 0.95 threshold), and only because the W/SciFi **constant term**
(3.5%, measured on one prototype) is held within x0.8-1.25. That constant term is mainly a
uniformity and calibration matter, which counts as a setting within the item (lesson 4, C1). The
same prototype gives 3.0% or 3.5% depending on the position correction used. If it is halved, or
set to a routine 1%, the adopted item fails in only 59% or 51% of draws. The stochastic terms alone do
not separate the options robustly: under the stated lateral-containment fact, the best W/SciFi
configuration reaches about 5.7%/sqrt(E), against PbWO4's 3.6%/sqrt(E). That ratio of about 1.6 is
right at the x0.8-1.25 floor, so this is not an honest robust conflict.

This corrects the feasibility note (materials_s2/feasibility_q77_q78.md, q78). It claimed that dilution
within compact W/SciFi only reaches about 8-10%/sqrt(E). In the coded sampling model, replacing
W/binder with fibres (scale s) and using finer fibres (down to 0.25 mm) reaches about
5.7%/sqrt(E) while keeping the Moliere radius at or below 2.5 cm (best: s = 0.7, d = 0.25 mm,
R_M about 2.26 cm, X0 about 0.99 cm).

## Key output (keys/key_output.txt)
```
nominal best W/SciFi config (scale, fibre mm), sigma/E at 2 GeV, RM cm, X0 cm: ((0.7, 0.25), 0.0532, 2.263, 0.993)
nominal PbWO4 sigma/E at 2 GeV: 0.0285
BASE      adopted_passes_nominal=True PASS
CONF1     adopted_fails_nominal=True viable_nominal=['PbWO4_APD'] (n_survivors=1) adopted_fails=0.954 >=1_viable=1.000 PASS
CONF1_c/2 adopted_fails_nominal=True viable_nominal=['PbWO4_APD'] (n_survivors=1) adopted_fails=0.590 >=1_viable=1.000 FAIL
CONF1_c1  adopted_fails_nominal=True viable_nominal=['PbWO4_APD'] (n_survivors=1) adopted_fails=0.506 >=1_viable=1.000 FAIL
```

## Mechanism attempted
- BASE: sigma/E <= 12% at 2 GeV (W/SciFi nominal is about 10%, so it passes).
- CONF1: sigma/E <= 4% at 2 GeV (physics motivation intended: pi0/eta peak width for photon physics).
- Facts in both levels (fixed): radial gap 32 cm including readout; at least 18 X0; 90% lateral containment
  within 2.5 cm (that is, Moliere radius <= 2.5 cm, the tightest value PbWO4 survives at x1.25); B = 1.4 T;
  100 ns crossings; 20 Gy dose.
- Item settings coded: W(+binder) volume scale s in {1.0 ... 0.3}, fibre diameter d in {0.25 ... 1.0} mm;
  stochastic term scaled as sqrt(d / f_mip), with f_mip from PDG dE/dx and volume fractions, calibrated to
  the measured prototype; X0 and R_M from volume-weighted mixtures.
- Survivor PbWO4 + APD: passes every fact (16 cm + 5 cm readout <= 32 cm; R_M 1.96 cm; APD to 4 T; 10 ns
  decay; dose tolerance far above 20 Gy; stabilisation to +-0.1 C adds 0.2% to the constant term).
  It has 2.85% at 2 GeV nominal and is viable in 100% of draws. PbSc, PbGl and LAr fail on depth and/or R_M.

## Resolution figures (all sigma)
- sPHENIX 2D projective EMCal prototype (Fermilab T-1044, 2018), IEEE TNS 68 (2021) 173, arXiv:2003.13685:
  3.5(0.1)% (+) 13.3(0.2)%/sqrt(E) (hodoscope position correction); 3.0(0.1)% (+) 15.4(0.3)%/sqrt(E)
  (cluster correction). [fetched]
- sPHENIX 1D-projective prototype, IEEE TNS 65 (2018) 2901, arXiv:1704.01461: 2.8% (+) 15.5%/sqrt(E). [fetched]
- PHOS (ALICE PbWO4 + APD, -25 C): D.V. Aleksandrov et al., NIM A550 (2005) 169, doi:10.1016/j.nima.2005.03.174
  (record fetched; its abstract gives no numbers). Values used from the paper body, NOT verified this session:
  a = 1.30%·GeV (noise), b = 3.58%, c = 1.12%.
- CMS ECAL: 2.8%/sqrt(E) (+) 12%/E (+) 0.3%, JINST 3 (2008) S08004 (not fetched).
- PHENIX PbSc 8.1%/sqrt(E) (+) 2.1%; PbGl 5.9%/sqrt(E) (+) 0.8%: L. Aphecetche et al., NIM A499 (2003) 521 (not fetched).
- PDG: X0(PbWO4) 0.89 cm, R_M 1.96 cm; X0(W) 0.35 cm, R_M(W) 0.93 cm.

## unc ranges used (x0.8-1.25)
- wsf b and c (fit errors in arXiv:2003.13685), wsf X0_nom, PbWO4 X0/RM/b (PDG; PHOS fit), PDG material constants.

## adoption_status
- built and operated: the W/SciFi EMCal was built for sPHENIX and has operated since the 2023-2024 runs.

## Doubts
- The coded dilution model (Fabjan sqrt(d/f) scaling, nominal fibre volume fraction 0.2) is approximate.
  Its optimism toward the item is deliberate, because the item must be defeated in every configuration.
- A tighter lateral fact cannot help: R_M <= 2.5 cm is already at the limit set by PbWO4 x1.25.

## Post-run change log
- 2026-11-08: stated facts moved from varied "stated" to "fixed" (they are exact stated facts). The
  sensitivity runs on the constant term were added. The verdict was set to no robust window.
