# Red team r2: p05_sno (2026-11-06). Verdict: BASE OK; CONF1 OK after a grading-rule FIX

**Blind answers:**
- BASE: LAB is favoured and sound.
- CONF1: LAB fails (net load ~139 vs 60 kg/m³); PXE survives (~14 kg/m³).

**r1 FIXes:** 1, 2 and 4 are done (dossier still said 0.889; now fixed). FIX 3 (the grading rule) is inadequate because the r1 limit change from 40 to 60 moved the threshold.

**Open route:** a ≥50% LAB fill densified with a co-solvent of density ≳1.02 g/cm³ passes.
- 1-methylnaphthalene is borderline (1.00–1.02).
- Denser aromatics (1-chloronaphthalene, benzyl benzoate) pass clearly.
- A plain fact cannot close this without naming chemical classes.
- Red-team FIX: score such fills as a workaround.

**Closed:** rope or ballast load paths; partial fill or inner bag (by the "inside the sphere" light requirement); temperature; shield changes; metal loading; water-based scintillator.

**K-probe:** OK (expected NO). **Identifiability:** very high.

## Study decision (2026-11-06)
- **Grading rule adopted:** LAB plus a density-raising co-solvent or additive used to reduce the buoyant load is coded **C (adopted item plus valid workaround)**, whatever its LAB fraction. This applies the same C-code logic used for p02 (UG argon plus radon measure). It does not narrow the dated item.
- Not touched: the stated numbers. Retuning the limit was rejected by both red-team rounds.
- **p05 CLEARED.**
