# Blind assessment, pair auger (written before opening key, dossier or notes)

Common frame for EQ1-3: sealed water-Cherenkov tanks (WCD), one mixed EM+muon signal, need event-by-event p/Fe at near-vertical to moderate zenith (<50-60 deg), on the always-on array; no opening tank, no lifting/moving tank, per-station budget of US$ 6.8-9 k, 4.4-4.8 person-hours per station.
Option space I considered: (A) thin scintillator panel on the tank lid (EM-weighted second detector, matrix inversion with WCD); (B) buried / shielded muon counter beside tank; (C) muon counter or RPC under tank; (D) segmenting the water volume / second inner PMT layer; (E) radio antenna per station; (F) electronics upgrade only (faster ADC, larger dynamic range, trace-based muon extraction / ML); (G) more FD duty cycle (doesn't meet "every shower, ground array").

## EQ1 (Corvel Ridge, <55 deg, >3e19 eV, $7.5k / 4.8 h per station)
- Favoured: (A) surface scintillator panel on the lid. Different EM/muon response than the WCD lets you solve the 2x2 system for muon and EM content station by station; mounts without touching the interior or lifting the tank; panel-scale hardware fits a ~$7.5k, ~5 h budget.
- Runner-up: (B) buried muon counter beside tank (cleanest muon measure, but trenching 2-3 m at each of 1,200 stations needs heavy machinery and far more than 4.8 h; "light vehicles" points against it).
- Confidence: 4.
- Competitive second option: (F) electronics-only upgrade (outside the sealed interior: dome electronics) + trace analysis. With 3-PMT time traces at fine sampling, muon spikes can be extracted (muon fraction / risetime / ML), giving mass sensitivity at very low cost and labour. Whether it reaches "proton vs iron shower by shower" is not stated, so the text cannot rule it in or out. The description gives no resolutions, so the choice A vs B vs F rests on unstated numbers - the winner is decided by gates (no lift, no open, cost, labour) more than by stated physics. (C) under-tank counters excluded by no-lift. (E) radio excluded physically at <55 deg on 1.6 km grid (footprint too small).

## EQ2 (Halden Basin, <=60 deg, >2e19 eV, $6.8k / 4.4 h, 1.3 km grid, 4 PMTs)
- Favoured: (A) lid scintillator, same reasoning.
- Runner-up: (B) buried counters (excluded practically by labour 4.4 h/station).
- Confidence: 4.
- Competitive option: (F) electronics; (E) radio at exactly 60 deg on 1.3 km grid is marginal but the bulk of showers <60 deg have footprints too small. Note: scintillator EM sensitivity degrades towards 60 deg (projected area ~cos theta and EM attenuation), so performance at the top of the range is weakest - a reviewer could argue for a buried counter if budget were not binding.

## EQ3 (Mirelle Steppe, <50 deg, >4e19 eV, $9k / 4.6 h, 1.8 km grid, 2 PMTs, windy)
- Favoured: (A) lid scintillator.
- Runner-up: (B) buried counters.
- Confidence: 3-4.
- Arguments against: "windy steppe" - a 3-4 m2 panel on the lid has wind loading, but it is fixable with a frame; not decisive. 1.8 km spacing means fewer stations per event near the core where the scintillator signal is large; buried counters have the same problem. (F) electronics again cheapest. Most budget-generous level ($9k), so a smaller buried counter might squeeze in on cost but not on labour (4.6 h).

## CONF1 (Ostrava Flats, 65-80 deg only, 1.0 km grid, $7k / 5.5 h)
- Favoured: (E) radio antenna at each station. At 65-80 deg the radio footprint spans many km2 (dozens of stations on a 1 km grid); radio gives the calorimetric EM energy, the WCD signal at these angles is essentially pure muons, so EM (radio) + muon number (WCD) gives a mass estimator per event. Cheap, mast-mounted, no tank access.
- Runner-up: none strong. Lid scintillator is the trap: at 65-80 deg the EM component is absorbed (old showers) and the flat panel's projected area is cos(theta) ~0.17-0.42 of nominal, so it adds little. Buried muon counters add muon info the WCD already provides at these angles. Runner-up I'd rank: electronics/ML on WCD traces, or doing nothing hardware-wise (WCD alone already measures N_mu; the missing piece is an energy estimator independent of N_mu - radio supplies it).
- Confidence: 4.
- Competitive option: (G) the FD supplies energy for 14% of events - doesn't meet "always-on". None found that beats radio on stated physics.

## ABS (Nemora, <60 deg, Delta ln N_mu = 0.30, sigma_p 0.14, sigma_Fe 0.06; budget 3.0 / 3.6 h)
Gates:
- Veltrane: 2.2 / 3.0 - fits; usable <60. r = 0.19.
- Duolith: inside the cell -> forbidden; labour 7.0 > 3.6.
- Korrin: beneath cell -> requires lifting -> forbidden; also 6.5 > 3.0, 20 > 3.6.
- Tessaline: 14 / 40 -> fails budget and labour only (physically allowed, best usable resolution 0.11).
- Orvane: only >65 deg footprint -> fails zenith goal.
- Favoured: Veltrane sheet (only survivor of the gates).
- Figure of merit (Delta / sqrt((s_p^2+s_Fe^2)/2), s^2 = intrinsic^2 + r^2): Veltrane 0.30/0.218 = 1.37; Tessaline r=0.11: s_p=0.178, s_Fe=0.125, merit 0.30/0.154 = 1.95; Korrin 0.14: s_p=0.198, s_Fe=0.152, merit 1.71; Duolith 0.17: merit ~1.55.
- Runner-up: none physically allowed; on physics alone Tessaline > Korrin > Duolith > Veltrane.
- Confidence: 5 that the key picks Veltrane; but **Veltrane is the worst-resolution option of the five** and wins only because the cost/labour gates (Tessaline) and installation gates (Korrin, Duolith) remove the better ones. Tessaline's exclusion is purely cost/labour, not physics.
- Note: Veltrane "3.5 m2, 1.2 cm, on lid, EM/mu ratio 2.4x" closely mirrors a real surface scintillator design; the abstract level is not fully abstract.
