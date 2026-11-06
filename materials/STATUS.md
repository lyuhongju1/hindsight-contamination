# Materials status (phase 3)

*Updated by the orchestrator as work lands. A pair is ready for the K premise check and the freeze when its red team reports no open FIX.*

| Pair | Item | CONF mechanism | Survivors | Stage |
|---|---|---|---|---|
| p01 XENON1T | liquid-phase Xe purification | — | — | **author running** |
| p02 GERDA | underground argon | radon-progeny surface background dominates; UG argon alone leaves budget unmet | 1 (encapsulation / shroud) | r1 FIX → fixed; r2 minor FIX → fixed; gates pass. **Red-team cleared** (scoring note: UG argon + radon measure = C) |
| p03 Adv. Virgo | FDS via external filter cavity | 8 m absolute path limit + 5 ppm mirror loss → cavity linewidth unreachable | 1 (EPR / conditional squeezing) | r1 FIX → fixed; r2 FIX (band-wide requirement + sideband key) → **fix round running** |
| p04 ICARUS | serial ADC per channel | — | — | **No honest physical conflict** (r1 showed CONF tested a different item; author found per-channel synchronous digitisation dominates on physics). **Zero-unit pair; replaced under A2 by p15 aLIGO** |
| p05 SNO | LAB scintillator | buoyancy load limit on thin acrylic sphere | 2 (PXE; LAB30/MN70 blend, not counted as LAB) | **CLEARED** (r2; densified-LAB blends scored C) |
| p06 AGATA | Ethernet readout | — | — | not started |
| p07 MEG | downstream RDC | magnetic mirror reflects low-energy positrons upstream | 1 (upstream tagger) | **Zero-unit pair** (r1 red team + author scan: a thin near-target counter survives every coherent edit; the AIF budget that would close it contradicts a low-mass tracker). Replacement: A1 queue |
| p08 COSINE | in-house crystal growth | home institute at 3,600 m → cosmogenic tritium | 2 (Alpha Spectra marginal; RMD/Astro-Grade) | **Zero-unit pair** (r2 + final attempt: in-house method demonstrably reaches Astro-Grade K/210Pb, so the windows are empty; altitude route needs a logistics rule). Replacement: resume A1 queue (q19 LUX) |
| p09 NEMO-3 | 8-in. high-QE PMTs | granularity: 15 cm two-electron separation vs >=210 mm cell pitch | 1 (76 mm PMTs on small cubes) | **CLEARED** (r2; survivor 8.5% FWHM, credible 8-11%) |
| p10 Borexino | 144Ce-144Pr source | fully deuterated scintillator kills IBD | 2 (51Cr, 37Ar) | r1: CONF1 OK, wording/kprobe FIX → fixed; gates pass. **Red-team cleared** |
| p11 KAGRA | optical levers | — | — | **Zero-unit pair** (author + red-team confirmation: lever geometry is free, so no robust window). Replacement: A1 queue |
| p12 MiniBooNE | PPO doping | — | — | **author running** |
| p13 NA62 | small-diameter straws | — | — | not started |
| p14 KASCADE | tripole antennas | — | — | not started |
| p15 aLIGO (A2 replacement) | balanced homodyne readout | — | — | **Zero-unit pair** (author + red-team confirmation: no honest conflict). **Replaced under A2 by p16 BESIII** |
| p16 BESIII (A2 replacement) | endcap TOF upgrade to MRPC | charged flux 1.5 MHz/cm2 vs resistive-electrode rate capability (coherence doubt) | 1 (3-layer LGAD) | key PASS; notes.md being written; r1 next |

**Scoring notes collected from the red teams** (to be frozen into the per-pair rubrics):
- **p03:** adopted item = rotation by an *external filter cavity*. EPR is a distinct alternative; a generic "frequency-dependent squeezing" answer = X.
- **p02:** UG argon + any radon-progeny measure (> 2.25×) = C.
- **p05:** a fill with < 50% LAB by volume ≠ adopted item; LAB plus a density-raising co-solvent or additive = C (workaround).
- **p04:** n/a (zero-unit pair).
- **p09:** 8-inch tubes reading small cells through light guides = C (workaround).
