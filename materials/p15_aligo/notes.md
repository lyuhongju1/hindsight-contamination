# Notes: p15_aligo

## Outcome: NO honest physical CONF found. Pair left failing (zero-unit), per AUTHOR_BRIEF.
No CONF1.txt / CONF2.txt / kprobe.json written, deliberately.

## Why (mechanism analysis)
The only physical failure route specific to the adopted readout (vs. keeping DC readout) is relative phase
noise between the separately routed reference beam and the antisymmetric-port beam. It converts to fake
displacement by beating against the static carrier at the dark port that is in quadrature with the signal
(arm loss mismatch): x = L_eff * (2 pi / lambda) * dx / G, L_eff = offset_ref * sqrt(P_cd/P_ref).
DC readout is immune to first order (reference field co-propagates with the signal).

Two regimes, neither gives an honest robust conflict:
1. Optics beyond the port suspended (BASE): dx at 10 Hz is ~1e-15 m/rtHz or less; the adopted item passes
   by >100x. Raising dx enough to fail would need platform motion that also ruins the suspended core optics
   / is not credible for multi-stage suspended optics (isolation ~1e-6 at 10 Hz).
2. Optics rigidly mounted (attempted CONF1, dx = 3e-12 m/rtHz at 10 Hz): rigid mounts allow piezo actuation
   with kHz unity-gain frequency, so the reference-phase servo has gain >~1e3 at 10 Hz and the noise is
   suppressed below the limit (key: adopted_fails = 0.115 -> FAIL). The servo's own sensing noise, when it
   senses the same static field, is imprinted at ~ the readout shot-noise level, independent of P_cd, so it
   cannot be made decisive either. Forbidding fast actuation would require exclusion wording (rule 2) or an
   unphysical stated limit.
   Keeping the slow suspended-optic servo gain (G = 30) with rigid optics (CONF1slow) passes the checker
   but is dishonest: it ignores the obvious workaround. Not used.
Other routes checked and rejected: mode-matching loss of the reference beam (sub-% and not robust under
x0.5-2 on the loss budget); readout-path optical losses (parity with DC readout: one mode cleaner per
detected beam, same photodiode QE); scattered light and beam jitter (hit DC readout equally); radiation
pressure / thermal noise of reference-path optics (negligible, <1e-12 rad/rtHz); laser technical noise on
the reference (pickoff from the recycling cavity is filtered by the same coupled-cavity pole; balanced
subtraction cancels its intensity noise).

## Files
- dossier.md; descriptions NAME/ANON/BASE (BASE passes; usable if a later author finds a CONF).
- keys/key.py, keys/key_output.txt: BASE PASS; CONF1 (honest, fast servo) FAIL; CONF1slow shown for
  transparency only.

## Fixed inputs
LAM = 1.064e-6 m (stated wavelength; module constant, exact).  `tech_margin` = 10 is a stated factor but
is varied by keylib (left under stated, conservative).

## Cited properties (x0.5-2)
- loop_gain_10Hz: 30 for suspended-actuator servo (UGF tens of Hz); 1e3 for piezo on rigid mount (UGF kHz).
  Engineering estimates, no citation fetched.
- static_miscentre_w 0.01, waist 0.5 mm: typical output-mode-cleaner values (estimate).

## Doubts
- adoption_status 'approved not built' is unverified (no web fetch).
- BASE mentions the offset's couplings and a filter cavity being installed; this is instrument fact,
  but a red team may judge it hints at the adopted item.

## Post-run change log
- run 1: key_output initially saved by Tee-Object (UTF-16); re-saved as ASCII. No numbers changed.
