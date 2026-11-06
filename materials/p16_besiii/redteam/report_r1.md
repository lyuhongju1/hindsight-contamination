# Red team r1: p16_besiii (2026-11-06). Verdict: DROP (no honest same-class conflict)

- **Class rule breached.** BASE and CONF1 describe a 13 TeV pp spectrometer, not an e+e- tau-charm detector. The rate conflict (1.5–10 MHz/cm²) exists only at hadron-collider luminosity; a tau-charm machine at ≤1e35 reaches about kHz/cm².
- **Internal physics is otherwise sound.**
  - Ceramic MRPCs demonstrably reach 95% efficiency at about 2e5 Hz/cm² (Laso Garcia et al., NIM A 2016; arXiv:1806.02629).
  - The LGAD survivor is credible, but the realistic per-layer inefficiency is 0.08, not 0.02.
  - Geometry error: 36 × 600 cm² does not fit the annulus.
- **Same-class routes examined, none robust:**
  - rate: MRPC margin ×10–100;
  - π/K TOF timing band: a 14 ps requirement is not robust against ~20 ps MRPCs at ×0.5, and tighter requirements also kill LGAD;
  - material budget in front of the endcap calorimeter: windows overlap;
  - low-momentum PID band: ample margin;
  - magnetic field: favours the MRPC.

## Outcome
p16_besiii is a **zero-unit pair** (author plus red team, per A2). The off-class materials are kept for the record only.
