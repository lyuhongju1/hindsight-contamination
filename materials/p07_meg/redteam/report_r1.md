# Red team r1: p07_meg (2026-11-06). Verdict: BASE OK; CONF1 FIX (else DROP); kprobe OK (minor)

## Blind answers
- **BASE:** the downstream on-axis tagger is favoured (~20% reduction); the adopted item is sound.
- **CONF1:** an upstream in-beam tagger is favoured. A counter at the end of the bore fails, with the mirror-ratio-4 loss cone giving ≤6.7%. **But a downstream on-axis counter a few cm behind the target, before the field rise, works.**

## Findings
- **N1. The loss cone is correct.** Tracking simulation: 4.7–7.5% transmission at 1–5 MeV. Failure does not depend on adiabaticity (canonical angular momentum is conserved for on-axis birth).
- **N2. Muon polarisation.** The Michel asymmetry (a ≲ 1/3) raises escape to ≤0.088. Not decisive; add it to the notes or code an asymmetry parameter.
- **N3 (main). Open route.**
  - A disk at z=3 cm with R=5 cm is crossed by 38–52% of the RMD positrons, giving ~20% reduction (pass). At z=6 cm the reduction is 11–19%. The working condition is B(z) ≲ 0.72 T.
  - The notes' closure argument (signal near 90° passes at r<15 cm) is wrong: 90° photons never cross a disk at z=3 cm, and signal positrons clear it for θ ≥ 60°.
  - The red team found no plain fact that closes this route. Its options:
    - (a) redefine the adopted item as the bore-end RDC;
    - (b) close it with a plain fact;
    - (c) DROP.
- **N4. Upstream survivor.** Broadly credible. Add to the notes: radiation dose ~0.04 Gy/s in the fibres (a replaceable layer); the q_ecut implies an annular crystal (q=1 still passes); the timing window.
- **N5. r_max comment.** It says diameter but means radius (2r_g ≈ 13 cm, or ~10 cm after expansion); a nominal of 7 is low. Remove ok_geom or move r_max to "fixed" as a derived quantity.
- **N8 (optional).** State the downstream bore length in CONF1, as in BASE.
- **N9. Coherence note.** A 2 T mirror 5 cm from the target reflects Michel positrons back through the target and tracker. Signal positrons cross the rise non-adiabatically, and the maximum radius in 2 T is ~17.6 cm. Replace the notes' coherence line with this.
- **N10. kprobe.** Replace "rises slowly (adiabatically)" with "rises smoothly over 15 cm".
- **N11. Identifiability:** very high (MEG / MEG II).

## Study decision on N3 (2026-11-06)
- Option (a) is **rejected**. The verified dating quote commits only to "the Radiative Decay Counter (RDC)", with no position, so narrowing the item would bypass dating (same rule as p04_icarus). A near-target downstream counter IS the adopted item.
- CONF1 must therefore make **every** downstream on-axis counter placement fail by a plain physical fact, or the pair is DROPPED to zero units under A2 (replacement: next eligible baseline, q32 BESIII).
