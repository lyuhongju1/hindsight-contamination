# Feasibility q73 STAR (arXiv:0710.0172): H1 HFT MAPS pixels, H2 FGT triple-GEM disks
All figures are order-of-magnitude estimates from standard formulas (Highland, sagitta); no web fetch was made.

## H1: MAPS pixel layers vs hybrid pixels or CCDs
- Pile-up and occupancy at a stated luminosity. RHIC-II Au+Au: about 8e27 x 7 b, or about 50 kHz, gives about 10 min-bias events per 200 us. That is about 50 hits/cm² at r = 2.5 cm, an occupancy of about 1e-3. MAPS pass with large margin. pp at about 2e32 x 50 mb (about 1e7 Hz) gives about 2000 events per 200 us, or about 160 hits/cm². With a search window of about 300 um from the outer layers, that means about 0.4 ghost hits per track, so a rolling-shutter MAPS can fail. This is killed by lesson 1 / C1: integration time is a variant within the MAPS item. ALPIDE-type MAPS integrate in 2-10 us (about 100x less pile-up), and depleted MAPS with in-pixel timestamps (MALTA, TJ-Monopix) reach about 25 ns, the same as hybrids. A conflict therefore cannot defeat every MAPS variant. Not robust.
- Pointing resolution vs material. MAPS at about 0.3-0.4% X0 give a multiple-scattering pointing term of about 16 um at 1 GeV/c and r = 2.5 cm. Hybrids at 1-1.5% X0 give about 30-40 um, about 60 um at x2 material. Any requirement tight enough to stress pixels favours MAPS. This route points the wrong way.
- Radiation dose. The RHIC dose at r = 2.5 cm is about 0.1 Mrad per year. Current MAPS tolerate about 1-3 Mrad and DMAPS about 100 Mrad and 1e15 neq/cm². A dose at which MAPS fail needs LHC-class fluence, which breaks the class rule (same trap as p16). Not viable.
- Readout speed or trigger latency. Fast-timestamp MAPS variants defeat it, as above.
- **H1 verdict: NO WINDOW.** Every physical route where MAPS lose (pile-up, dose) is closed. Pile-up is closed because fast-integration and timestamping MAPS are variants of the item (lesson 1, C1 settings). Dose is closed because the needed dose is not RHIC-class. Material and pointing favour MAPS.

## H2: triple-GEM disks vs silicon-strip disks for W -> e charge sign, 1 < eta < 2
- Position resolution vs charge-sign sagitta. With B = 0.5 T, a transverse lever arm of about 0.4 m and pT = 40 GeV, s = 0.3 B L^2 / (8 pT), about 75 um. The GEM resolution is about 60-100 um σ and silicon strips about 20-30 um σ (pitch/sqrt12). Under x0.5-2, GEMs reach about 35-50 um and silicon about 40-60 um; the ranges overlap, so no requirement threshold separates them robustly. GEM resolution is also a setting (strip pitch, 2D readout, drift gap): fine-pitch GEMs reach about 30-50 um σ. Not robust.
- Number of points and lever arm. The disk count, the z placement, the EEMC shower-max point at z of about 270 cm and the vertex constraint are available to both technologies. These are settings, not discriminators.
- Material and bremsstrahlung. A triple-GEM disk is about 0.5-1% X0; a silicon-strip disk with support and cooling is about 1-2% X0. Electron bremsstrahlung and charge-sign confusion therefore favour GEMs. This route points the wrong way.
- Rate and occupancy. In 500 GeV pp at about 2e32, forward rates are well below GEM limits of about MHz/cm². No conflict.
- Large-area cost was the real driver; it is excluded by rule 1.
- **H2 verdict: NO WINDOW.** The resolution gap (about x3) is smaller than the x0.5-2 robustness band on both properties, and it is tunable within the GEM item. Material favours GEMs.

## Candidate verdict: zero-unit (both items NO WINDOW)
