# Feasibility (lesson 5): q69 ALICE (G1, G2) and q71 TOTEM (G3), 2026-11-08

Figures are from memory of the TDRs and literature (no web fetches). sigma = rms.

## q69 G1: MAPS ITS vs hybrid pixels
- Route fluence/TID. MAPS of the ALPIDE type are qualified to about 1e13 neq/cm2 and a few Mrad. Depleted and modified-process MAPS (TJ-modified, MALTA, Monopix) reach about 1e15 neq/cm2 and tens of Mrad. Those are process and implant variants within the committed class "CMOS MAPS" (lesson 1). For the bare item to fail under x0.5-2, the stated fluence must be at least 4e15. Planar hybrids also degrade at that level, so only 3D-sensor hybrids would survive (about 1e16).
- Route fluence/TID, coherence. A heavy-ion LHC experiment collects about 10 nb^-1 of Pb-Pb plus a few fb^-1 of pp over its life. That gives about 1e12-1e13 neq/cm2 at r = 2 cm (ITS2 TDR: about 1.7e12 and 270 krad including the safety factor). Reaching 4e15 needs hundreds of fb^-1 of pp, which is the general-purpose-detector or HL-LHC class. That is the p16 class breach. The resulting TID (hundreds of Mrad) and pp pile-up are also incoherent with a low-pT heavy-ion tracker.
- Route material vs fluence trade-off. A material limit loose enough to admit hybrids (about 1-2% X0 per layer) also admits MAPS, so material cannot separate the two. The fluence would have to do all the work, and that fails on the two lines above.
- Route rate/integration time. ALPIDE integrates over about 5-10 us. Strobe length is a setting, and depleted MAPS reach 25 ns, both within the class. In-class Pb-Pb rates (at most about 50 kHz) give no robust failure.
- **Verdict G1: NO WINDOW.**

## q69 G2: ungated GEM TPC vs gated MWPC
- Route IBF/space charge at a sub-gating rate (for example 1 kHz with a tight distortion tolerance). Space charge scales with (1 + eps), where eps = IBF x gain.
  - GEM, nominal: IBF 0.7% at gain 2000 gives eps of about 14.
  - GEM, within settings: a 4-GEM stack, voltage tuning and lower gain give IBF 0.3-0.5% at gain about 1000, so eps of about 3-5. Each change costs some energy resolution, but sigma(E)/E stays about 12% at 55Fe.
  - Gated MWPC: closed-gate IBF about 1e-4 at gain about 1e4, so eps is at most about 1. The primary-ion term is common to both.
  - The ratio of distortions, best GEM to worst MWPC, is (1+3)/(1+2), about 1.3, and only about 2-7 nominally. Under x0.5-2 on IBF, gain and rate, the ranges overlap.
  - At 1 kHz the absolute GEM distortion is also small: about 10 cm at 50 kHz scales to about 2 mm. Calibration corrects it to about 0.1 mm, and that is routine procedure (lesson 4).
  - A tolerance written to forbid correction would be design fiat.
- Route energy resolution plus a gain fixed by noise, used to pin eps at 12 or more. ALICE GEM stacks meet about 12% sigma at IBF 0.7%. The IBF/resolution trade-off is a set of voltage settings, so eps at about 6 still passes, and the margin over the MWPC is still not x4.
- Route rate. Above about 3 kHz the gated MWPC fails. That favours the item (the BASE direction), not a CONF.
- **Verdict G2: NO WINDOW.**

## q71 G3: scCVD diamond timing vs quartz Cherenkov or LGAD
- Route timing with a stated number of planes (an allowed instrument fact).
  - Diamond: about 80-100 ps per plane single-layer, and about 50 ps double-diamond, which is a variant of the item.
  - LGAD: about 30-40 ps per plane.
  - QUARTIC: about 15-40 ps per bar.
  - For any N, the per-plane ratio of diamond to the alternatives is at most about 2-3. Under x0.5-2 on the per-plane sigma, diamond's best (25 ps/plane) overlaps LGAD's worst (80 ps/plane).
- Route radiation near the beam (about 1e15-1e16 neq/cm2 at the hot spot for high-luminosity running; negligible in low-luminosity special runs). Diamond is the hardest option. LGADs lose gain above about 1e15. This favours the item.
- Route rate or occupancy. Diamond handles MHz per pad, and pad or strip segmentation is a setting. Neither gives a failure.
- Route material. Diamond is about 0.5 mm per plane, while quartz bars are cm-scale. This favours the item.
- Route signal size. The small diamond signal is handled by an amplifier choice, a setting or a routine design choice. Its effect is already inside the timing figures above.
- **Verdict G3: NO WINDOW.**

## Summary
q69: NO WINDOW (G1, G2). q71: NO WINDOW (G3). Both are zero-unit candidates per lesson 5.
