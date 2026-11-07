# p19_cuore0 dossier (PROVISIONAL: eligibility dating still running)

## Baseline as built: CUORE-0
- Single CUORE-style tower at LNGS: 52 natural TeO2 bolometers, 5x5x5 cm, ~750 g each (39 kg TeO2, ~10.8 kg 130Te), NTD-Ge thermistors, operated at ~10-15 mK. Data 2013-2015.
- Physics goal: 0nbb of 130Te, Q = 2527 keV (below the 2615 keV 208Tl line). No particle identification (heat channel only).
- Performance: ~4.9 keV FWHM at 2615 keV (summed calibration); ROI background ~0.058 counts/(keV kg yr), dominated by degraded alphas from surfaces plus 208Tl Compton events. Limit T1/2(0nbb) > 2.7e24 yr (CUORE-0), > 4.0e24 yr combined with Cuoricino.
- Sources: CUORE coll., PRL 115, 102502 (2015); PRC 93, 045503 (2016) (CUORE-0 detector and results papers). From memory; not re-fetched.

## Item targeted
- Li2(100)MoO4 scintillating bolometers (100Mo, Q = 3034 keV), each read with a bolometric light detector (Ge wafer + NTD) for alpha rejection by light yield. The row lists one counted item, so no choice needed.

## Verified commitment document
- CUPID Conceptual Design Report, arXiv:1907.09376 (2019): baseline of ~1500 Li2(100)MoO4 cubic crystals (45 mm side, ~280 g), Ge light detectors with NTD readout, target background ~1e-4 counts/(keV kg yr), ~5 keV FWHM at Q. The CDR treats 2nbb random-coincidence pile-up as a leading background, requiring a resolving time well below 1 ms (light-detector pulse-shape analysis).

## Documented alternatives not adopted (CDR)
- TeO2 (enriched 130Te) with Cherenkov-light readout (needs ~100 eV light signal; requires low-noise, e.g. NTL-amplified or TES, light detectors).
- ZnSe (82Se, Q = 2998 keV), the CUPID-0 demonstrator: ~20 keV FWHM at Q; ROI background (3.5 +1.0 -0.9)e-3 counts/(keV kg yr) (CUPID-0 Phase I, PRL 123, 032501 (2019); from memory).
- CdWO4 (116Cd, Q = 2813 keV).

## adoption_status
- **approved not built** for CUPID (CDR baseline adopted 2019; the Li2MoO4 technology itself was built and operated in the CUPID-Mo demonstrator, 20 crystals, 2019-2020; Armengaud et al., EPJC 80, 44 (2020)). Status of formal approval is from memory; confirm against the dating outcome.

## CONF outcome
- NO ROBUST WINDOW under C1 (see notes.md): pile-up can be stated into a Li2MoO4 failure, but no alternative meets a background requirement strict enough to make that failure robust (ZnSe demonstrated ~3.5e-3 counts/(keV kg yr)).
