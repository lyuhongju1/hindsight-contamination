# Feasibility (lesson 5) for q34 and q38, 2026-11-06

## Candidate A: EXO-200 to nEXO (item: VUV-sensitive SiPM arrays in LXe)

- Dark counts at about 165 K, with a light-only low-energy trigger requirement: SiPM DCR at 163 K is 0.14-0.35 Hz/mm² (14-35 Hz/cm²; arXiv:1903.03663, arXiv:2209.07765). R11410 is about 0.3-1 Hz/cm². So the SiPM is 15-100x worse per area, and about 0.6-1.4 MHz over 4 m². With a k=3 coincidence in a 100 ns window, SiPM accidentals are about 1-5 kHz against about 0.01-0.1 Hz for PMTs. That gap survives ×0.5-2 on DCR (cubic). But the window, k, overvoltage and requiring distinct channels are all settings of the item that eat part of the margin (lesson 4). The survivors fail too. APDs (about 1000 e- noise) cannot trigger on a few photons. VUV PMTs carry about 0.5-1 mBq 226Ra/228Th and about 10 mBq 40K/60Co per tube, roughly 1000x the SiPM per area. A coherent 0νββ description must state a background goal at Q, and the PMTs fail it. Dropping that goal makes the instrument incoherent (rule 7). No survivor passes everything stated.
- Radiopurity per photosensitive area: this kills the PMT, not the SiPM. APDs pass about as well as SiPMs. Wrong direction, no conflict against the item.
- PDE at 175 nm: SiPM 15-25% (up to about 30% claimed), APD effective QE about 1 but with gain noise, R11410 about 30%. The ratios are 1.2-2, which is inside ×0.5-2. Not robust.
- Electronic noise and capacitance per area: SiPM about 30-50 pF/mm². Channel ganging and size are settings of the item. APD capacitance is comparable. No robust separation.
- Correlated avalanches and gain noise: SiPM correlated avalanches are 0.16-0.42 per pulse, giving ENF about 1.2-1.4. APD ENF is about 2 or more at gain 100-200. This favours the item.
- Energy resolution at Q (σ/E about 1% target, from photon statistics plus noise): SiPM is better than APD and comparable to PMT. No requirement makes the SiPM fail while a survivor passes.
- Verdict A: NO WINDOW. The only route that separates the options (DCR with a light-only trigger) has no survivor. The APD fails the threshold, and the PMT fails the background goal a 0νββ description must state. Settings (window, k, overvoltage) also erode the margin.

## Candidate B: MAGIC to MAGIC-II (item: increased-QE superbialkali PMTs, about 34% peak QE)

- Light collection and threshold: the GaAsP HPD peak QE (about 50%) is only about 1.5x the PMT's. Weighted over the Cherenkov spectrum and with NSB included, S/sqrt(NSB) improves only about 1.2-1.4x, because GaAsP is more red/NSB-sensitive. That is inside ×0.5-2. No robust threshold requirement separates them.
- Afterpulsing: the PMT is about 0.1-0.5% (>4 pe), the HPD much lower. This affects the accidental trigger rate at low threshold, but trigger topology (next-neighbour multiplicity) and threshold are settings that defeat it (lesson 4). The ratio is also not robust once trigger logic is varied.
- NSB rate and moonlight: the higher NSB rate per pixel and the photocathode ageing under integrated charge (moonlight) hurt the HPD, not the PMT. Wrong direction.
- HPD gain and temperature behaviour: HPD gain is about 5e4 with a low-gain avalanche diode at about 8 kV, and the GaAsP dark rate and QE depend on temperature, so the HPD needs stabilisation or cooling. This favours the PMT. Wrong direction.
- Verdict B: NO WINDOW. The QE ratio of about 1.5 cannot be made robust under ×0.5-2. Every other cited property favours the adopted PMT or can be fixed by a routine trigger setting.

Sources: arXiv:1903.03663 (VUV4 at 163 K: DCR 0.137 Hz/mm², 0.161 correlated avalanches per pulse); arXiv:2209.07765 (FBK VUVHD3 0.19 Hz/mm², HPK VUV4 0.35 Hz/mm² at 163 K, 3 V overvoltage). The other figures are from domain knowledge and were not fetched.
