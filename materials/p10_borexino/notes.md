# Notes: p10_borexino

## Design choices
- Adopted item: 144Ce-144Pr electron-antineutrino emitter. It works only through inverse beta decay (IBD) on free protons, which gives a tag and the neutrino energy (E_nu = E_prompt + 0.78 MeV).
- BASE: an invented hydrocarbon liquid-scintillator detector with natural hydrogen. The adopted item passes because IBD gives about 5000 events, 3% of them outside +-10% in energy, at S/B about 20.
- CONF1 edit (one sentence): the solvent is fully deuterated (99.8% D), motivated by a neutral-current 8B measurement on deuterium. This leaves 1.2e26 hydrogen-1 atoms per m3 (500 times fewer).
  - IBD drops to about 10 events.
  - nu_bar + d -> n n e+ has a threshold of 4.03 MeV, above the 2.996 MeV 144Pr endpoint, so it gives zero events.
  - The remaining channels (nu_bar-e elastic scattering, NC deuteron breakup with threshold 2.22 MeV) give no per-event neutrino energy for a continuous spectrum, so they fail the "80% within 10%" requirement.
- The energy requirement is physics: the oscillation pattern must be traced in L/E. Line sources satisfy it intrinsically; IBD satisfies it through calorimetry.
- Workarounds closed by stated facts:
  - Replacing the target: "target liquid stays as it is"; deuteration is needed by the NC programme.
  - Moving the source: the stated chamber at 7.5 m holds up to 2.5 t.
  - The CC-on-deuterium route is closed kinematically.
- Coherence of deuteration:
  - Light yield is similar for deuterated aromatics. The stated value is kept, which is a mild doubt.
  - Neutron capture in C18D30 is dominated by 12C (about 65%; 3.5 mb; 4.95 MeV line), with D (0.5 mb; 6.25 MeV) second. The capture time is about 20 ms. This was corrected in r1. The sentence "event-by-event neutron detection by capture gammas" stays true.
  - Electron density per m3 is essentially unchanged.
  - Possible tritium in the deuterated solvent gives a 18.6 keV endpoint, below the 0.25 MeV threshold.
- No CONF2 written (optional).

## Survivors per CONF
- CONF1: 2 (51Cr 10 MCi, 37Ar 5 MCi), both by nu_e-e elastic scattering at line energies. Viable in 99.4% of draws (>= 1).

## Fixed inputs (exact stated facts in CONF1/BASE)
- D = 7.5 m, fiducial radius 3.4 m / 165 m3, T_run = 18 months: stated geometry and run length.
- N_req = 1500, outside_max = 0.2, SB_min = 1: stated requirements.
- Background 100/day in 0.25-0.6 MeV: stated.
- n_e = 2.9e29 /m3: stated, and identical in BASE and CONF1.
- The varied stated number is n_H1 (6e28 BASE, 1.2e26 CONF1). It is left varied (x0.5-2) to show robustness.

## unc ranges
- None. All props are varied x0.5-2.

## Cited properties (from memory; red team please check)
- 144Ce t1/2 284.9 d; 144Pr endpoint 2.996 MeV; IBD threshold 1.806 MeV; nu_bar-d CC threshold 4.03 MeV; d breakup 2.224 MeV.
- 51Cr t1/2 27.7 d with lines 0.746/0.751 MeV (~90%) and 0.426/0.431 MeV (~10%).
- 37Ar t1/2 35.0 d with lines 0.811/0.813 MeV.
- SOX activities: 100-150 kCi Ce and 10 MCi Cr (arXiv:1304.7721).
- Per-decay cross sections:
  - Ce IBD: 4e-44 cm2, the IBD cross section (Vogel & Beacom, PRD 60 (1999) 053003) averaged over the 144Pr spectrum. Red team r1 independently gets 3.95e-44.
  - Cr ES: 2.6e-45 cm2; Ar ES: 3.1e-45 cm2, both in the recoil window. They come from the standard tree-level nu-e elastic-scattering formula, dsig/dT = (2 G_F^2 m_e/pi)[gL^2 + gR^2(1-T/E)^2 - gL gR m_e T/E^2] with gL = 1/2 + sin2thW and gR = sin2thW for nu_e ('t Hooft, PLB 37 (1971) 195; Bahcall, Kamionkowski & Sirlin, PRD 51 (1995) 6146), integrated over the 0.25 MeV-to-Tmax window. Red team r1 finds them within 15%.
  - The CONF1 failure is set by the hydrogen-1 count and the kinematic threshold, not by these values.

## Post-run change log
- Run 1 (initial): ALL PASS. No changes to stated numbers after running.
- Red team r1 (2026-11-06), FIX items 1-4:
  1. The S/B sentence in BASE.txt and CONF1.txt is reworded identically to: "Over the counting period chosen for the analysis, source-induced interactions in the selected energy window must outnumber background events in that window." The minimal pair is kept. NAME/ANON keep the old wording; they are not keyed.
     - key.py: the survivor check now lets the analyst choose the window length w = k*tau, with k in 1.0-3.0 in steps of 0.1. Both N_req and S >= B must hold within that window. Previously the window was fixed at 1 tau.
     - At 3 tau: Cr S/B = 1.7, Ar S/B = 1.0. The best window is about 1 tau.
     - Result unchanged: CONF1 viable 0.994, both survivors.
  2. kprobe CONF1 is replaced by a question that asks for >= 1500 interactions with >= 80% energy-reconstructed, across all channels (expected NO).
  3. The neutron-capture physics is corrected (12C-dominated, 4.95 MeV, about 20 ms).
  4. The ES cross section now cites the standard formula, in notes.md and in key.py comments.
  - Re-ran key.py (ALL PASS) and gates.py p10_borexino (GATES PASSED). No stated numbers changed.
- Pre-run edit: BASE target mass sentence removed (the 400 t figure was inconsistent with a 4.6 m vessel). This was not a tuning change.

## Doubts
- 37Ar at 5 MCi has never been produced (SAGE made about 0.4 MCi). 51Cr at 10 MCi was never made either (Gallex made about 1.7 MCi). Both are proposal-level, as is the adopted Ce source.
- The 80% untagged "outside" fraction for Ce elastic scattering is an estimate. It fails even at x0.5.
- Elastic scattering of the Ce antineutrinos could still give a rate-only test. The stated energy requirement excludes it by physics, but a reader could argue for dropping the requirement.
- The adoption_status date and wording of the 2018 cancellation are unverified (no web fetch made).
- Coordinator request (2026-11-06): the same counting-period sentence was applied to NAME.txt and ANON.txt, so all four descriptions are consistent. Re-ran gates.py.
