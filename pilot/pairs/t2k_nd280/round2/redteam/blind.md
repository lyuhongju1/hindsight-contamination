# Blind analysis: t2k_nd280 round 2 (descriptions only)

Common facts: 0.7 GeV-peak beam, 410 m baseline, warm 0.3 T dipole, gas drift chambers downstream,
active target region 1.9 x 1.8 x 0.6 m (~2.05 m^3), needs muon + hadrons incl. short protons at all
angles (4pi), H nucleon fraction limit, absorbed dose, room temperature in-field.

Hydrogen nucleon fractions (standard): polystyrene (CH)n = 1/13 = 7.7 %; polyvinyltoluene ~ 8.5 %
(C9H10: 10/118); water 2/18 = 11.1 %; argon gas (+CO2 or CF4 quench) 0 %; Ar/isobutane 95/5 ~0.3-0.5 %.

## BASE (H <= 20 %, 5 Gy, room temperature)
- Favoured: fine-grained 3D-segmented plastic-scintillator target (cm-scale cubes, three-view WLS
  fibre / SiPM readout). Dense active CH target -> high event rate in 2 m^3, isotropic 3-view
  readout gives 4pi acceptance and short proton tracks (~few cm threshold); H fraction 7.7 % < 20 %;
  5 Gy is negligible for plastic; works warm and in 0.3 T (SiPMs are field-immune).
- Runner-up: gas TPC (Ar-based, possibly high-pressure) as active target: 4pi, very low proton
  threshold, 0 % H; but ~1/60-1/100 the target mass of plastic at 1 atm (mass/statistics not stated
  as a requirement, so it remains viable). Also: water-based or plastic bars (x-y) — bars lose
  high-angle acceptance.
- Confidence: 4/5.

## CONF1 (dose 5 MGy)
- Favoured: gas TPC as active target (gas is flowed/replaced, so the medium itself does not
  accumulate damage). Runner-up: radiation-hard inorganic segmented scintillator (e.g. LYSO/YAG/
  quartz-Cherenkov) — but dense crystals make proton tracks mm-short, so "short proton tracks" fails
  in practice; a silicon-pixel stack also tracks but 5 MGy is at the HL-LHC limit and a neutron
  component this large implies fluences far beyond 1e15 n/cm^2.
- Fine-grained plastic scintillator viable? **No.** Plastic scintillator and WLS fibres lose most
  light (and become strongly coloured) at 10^4-10^5 Gy; 5 MGy is 1-2 orders of magnitude past
  that. It fails.
- Serious concern: 5 MGy from beam muons means ~5e6 / (3e-9 Gy per MIP/cm^2) ~ 1.5e15-1.5e16 MIP/cm^2
  over a run; over ~1e7 s live time that is ~1e8-1e9 particles/cm^2/s. No neutrino-interaction
  reconstruction survives that occupancy: a gas TPC (tens of us drift) would be swamped and
  space-charge limited; the downstream drift chambers and all front-end electronics/SiPMs (if any)
  would also be destroyed. So the stated physics leaves effectively ZERO genuinely viable
  alternatives, and the number is ~6 orders above any real near-detector dose. Room temperature
  also removes noble-liquid TPCs.
- Confidence that plastic fails: 5/5. Confidence that any alternative is really viable: 1-2/5.

## CONF2 (H <= 1 %)
- Favoured: gas TPC with hydrogen-free mixture (Ar/CF4, Ar/CO2) as active target: 0 % H, 4pi,
  low proton threshold, warm, field-compatible. Runner-up: same gas TPC interleaved with thin
  hydrogen-free passive or active planes (carbon/graphite or silicon); or a hydrogen-free inorganic
  scintillator segmented target (poor short-proton reach in dense crystal). Liquid argon TPC is
  hydrogen-free but excluded by "operates at room temperature" (a cold cryostat inside a warm magnet
  is engineering-possible, but the description states the region is warm).
- Fine-grained plastic scintillator viable? **No.** Any organic (CH-based) scintillator has
  7.7-8.5 % H nucleons, far above 1 %. Water is also out (11 %).
- Note: this is effectively a composition rule ("no organic material") that excludes all plastic
  and liquid scintillator and water at once; only gas TPC (+ exotic inorganic options) remain.
  At least two alternatives are arguable but the strong one is single (gas TPC).
- Confidence: 5/5 plastic fails; 3/5 that >=2 genuinely viable alternatives remain.
