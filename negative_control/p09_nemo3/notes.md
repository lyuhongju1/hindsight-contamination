# NC notes: p09_nemo3

Outcome: **NC_CONF written; nc_key ALL PASS** (NC_BASE, NC_CONF and NC_HIST all PASS). It still needs a red-team check, especially on the point under "Doubts 1".

## alt(u)
alt(u) is a 76 mm (3-in.) PMT, one per cell, inside a thin mu-metal shield, directly coupled (no light guide) to a small polystyrene cell of about 80 mm.
- It is the only survivor of the main CONF1 (materials/p09_nemo3/notes.md, key.py `pmt76_direct_small_cube`).
- Nominal values: 8.5 % FWHM at 1 MeV, 0.25 ns sigma, 110 mm deep, works up to about 18 mT.

## NC edit (one number)
DIFF CONF1 -> NC_CONF, line 10: "at points at least **15 cm** apart" -> "at points at least **6 cm** apart".
- Nothing else changes. This was checked with `diff`.
- The CONF1 sentence and its mechanism are kept. Only the stated separation is tighter.

## Mechanism
The mechanism is calorimeter segmentation, the same physics as CONF1, applied one size down.
- **alt(u) fails.** A cell that carries its own directly coupled 76 mm tube has a largest dimension of at least 76 mm, whatever its shape. That is more than 60 mm, so two entry points 6 cm apart can fall in the same cell.
  - The failure is robust even at the datasheet-precision floor: 0.8 x 76 = 61 mm > 60 mm, independent of shape.
  - The square-cell sqrt(2) factor in the key adds margin: nominal diagonal 113 mm, minimum over draws 89 mm.
  - A tube reading several cells in common loses the individual energies (stated: "whose energies are measured separately").
- **The historical 8-in. item fails a fortiori.** Its pitch is about 210 mm, against 60 mm.
- **Choice of 6 cm rather than 5 cm.** With 6 cm the SiPM survivor has a wide margin (worst-case diagonal about 51 mm < 60 mm), and alt(u) still fails shape-independently.

## Survivors (coded against every stated fact)
1. **SiPM array on small cells.** A 4x4 array of 6x6 mm SiPMs (Hamamatsu S13361-6050 class, outer size about 25.8 mm, datasheet) sits on the back face of a polystyrene cell of about 26 x 26 mm, 60 mm deep.
   - **Segmentation.** Pitch 27.8 mm, diagonal 39 mm < 60 mm. Worst case is about 51 mm.
   - **Resolution, derived nominal 9.2 % FWHM.**
     - The derivation follows the same chain as alt(u)'s 8.5 %. It uses the collection-saturation model c = A_pc/(A_pc + (1-R)A_wall), with R = 0.96.
     - SiPM: A_pc = 576 mm2, A_wall about 6950 mm2, so c = 0.67. With PDE about 0.40 at the polystyrene emission, the product is 0.27.
     - alt(u): c = 0.72 and QE = 0.38, so the product is 0.27. The two are the same.
     - A crosstalk excess-noise factor of x1.15 raises the result from 8.5 to about 9.2 %.
     - Under x2 the value is 18.4 %, above 18 % in about 2 % of draws. The key gives viable = 1.000 because the 1-in. option covers those draws.
   - **Timing.** 0.20 ns sigma taken. SiPM-read plastic counters reach about 0.04-0.1 ns (MEG II pixelated timing counter). The requirement is 0.6 ns.
   - **Field.** 3 mT is irrelevant to SiPMs, which run in multi-tesla fields (CMS HCAL, 3.8 T).
   - **Depth.** 60 mm >= 30 mm. The range of a 3 MeV electron in polystyrene is about 1.5 cm.
   - **Noise.** Dark rate is about 50 kHz/mm2 x 576 mm2, or about 30 MHz, which gives about 1-2 p.e. in a 50 ns gate. That is small against about 1000 p.e. per MeV.
2. **1-in. PMT, one per cell** (pitch 28 mm, nominal 9.5 % FWHM). This survives in the key. It is a different tube size from alt(u), just as 3-in. differs from 8-in. in CONF1.

Counted survivors: 2. Other options fail segmentation: 2-in. (diagonal 77 mm), 5-in., present light-guide cells and 8-in.

## Fixed inputs
These are the same as the main key: 18 % FWHM, 0.6 ns, 30 mm, 3 mT and the sqrt(2) geometric factor. The separations 150 mm (NC_BASE = CONF1) and 60 mm (NC_CONF) are exact stated requirements.

## unc ranges
- Only sensor dimensions use x0.8-1.25, because they are datasheet dimensions: the PMT bulbs, as in the main key, and the SiPM array outer size.
- Everything else uses the default x0.5-2. The SiPM depth (a design choice) was set to 60 mm so that x0.5 still meets 30 mm.

## Coherence checks
- **Lateral spread of electrons.** At 1 MeV the range in polystyrene is about 4 mm; at 3 MeV it is about 15 mm. Leakage across the edges of 26 mm cells is larger than in 80 mm cells but still minor at 1 MeV. "Deposit their energy in different cells" is read as the main deposit, as it is for CONF1.
- **Tracker.** Entry points are known to about 1 mm from the Geiger cells, so a 6 cm requirement is meaningful.
- **Field and timing.** The 3 mT field and the 0.6 ns timing requirement are unaffected.
- **Radiopurity.** None is stated. The SiPM survivor needs none, and none is invoked.
- **Wording.** No forbidden regex (adopted or identity) matches NC_CONF.txt or nc_kprobe.json. No "3-inch" wording is present (checked by script).

## Rejected mechanisms
- **A tighter energy resolution.** To fail alt(u) robustly the requirement would need to be below about 4.3 % FWHM (8.5 x 0.5). No plastic option reaches that. A better scintillator would also help 3-in. tubes.
- **Timing.** Failing alt(u) needs < 0.125 ns sigma, and no 3rd option on cells of at least 3 cm passes robustly with x2.
- **Radioactivity budget per wall area.** Ultra-low-background 3-in. tubes (metal-body, about 0.6 mBq 226Ra per tube) would have to be beaten by a factor of 4 or more, including SiPM front-end electronics. No cited numbers support that. A budget limited to the light sensors would also look like fiat, because the scintillator alone (about 80 kg/m2) is of comparable activity.

## Doubts
1. **Form of the edit.** The NC edit changes the CONF1 number (15 -> 6 cm) rather than adding a new sentence. It is "one set of numbers", and the adopted item still fails for the CONF1 reason. A red team may still judge that NC_CONF should keep 15 cm and add a separate fact.
2. **Inherited wording.** Line 5, inherited unchanged from CONF1, contains "76 mm photomultiplier" (the present light-guide readout). It is not the NC edit and not alt(u)'s configuration, but it names alt(u)'s tube size.
3. **Close workarounds.** These are not closed by plain fact, as in the main study:
   - 3-in. tubes reading small cells through light guides, staggered in depth or in layers. This would be coded C (alt(u) plus a workaround).
   - A multi-anode or position-sensitive PMT reading several cells on separate anodes. This is a different readout class (C1), not alt(u).
4. **1-in. survivor.** A 1-in. PMT survives. Some may see it as "the same family" as alt(u). The NC rubric should code it as abandoning alt(u), consistent with 3-in. counting as abandoning 8-in. in CONF1.
5. **Derived resolutions.** The SiPM resolution (9.2 %) is derived, not measured, with a margin of x1.96 to 18 %. alt(u)'s own 8.5 % rests on a similar derivation.

## Post-red-team changes (2026-11-07; NC red team r1: CLEARED, notes and rubric FIXes applied before the NC freeze)

- **Lateral spread** (replaces "still minor at 1 MeV"):
  - In 26 mm cells a substantial share of 3 MeV electrons (order 30%), and a smaller share at 1 MeV, share energy with a neighbour cell.
  - Clustering adjacent cells recovers the energy, at the cost of a low-energy tail from wrap losses.
  - Line 10 is still satisfied, because clusters of electrons 6 cm apart do not overlap.
  - Cells up to about 40 mm square (diagonal < 60 mm), with 5x5 or 6x6 arrays of 6 mm SiPMs, halve the edge fraction and remain survivors.
- **Survivors:**
  - 2-in. tubes fail with square cells (diagonal 77 mm).
  - With round or hexagonal cells under 60 mm across they are a marginal additional survivor, not counted in the key.
- **Doubt (line 5):** line 5 names the present 76 mm tubes. A preference for reusing existing hardware may inflate B_alt and O_alt for this unit. That bias works against H_NC, so it is conservative.
