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
  - Neutron capture on D is slow (0.5 mb) with a 6.25 MeV gamma. This is still "event-by-event neutron detection by capture gammas", so the sentence stays true.
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
- Per-decay cross sections (Ce IBD 4e-44 cm2; Cr ES 2.6e-45; Ar ES 3.1e-45 in window) are order-of-magnitude estimates, not fetched. The outcome is insensitive to them: the CONF1 failure is set by the hydrogen-1 count and the kinematic threshold.

## Post-run change log
- Run 1 (initial): ALL PASS. No changes to stated numbers after running.
- Pre-run edit: BASE target mass sentence removed (the 400 t figure was inconsistent with a 4.6 m vessel). This was not a tuning change.

## Doubts
- 37Ar at 5 MCi has never been produced (SAGE made about 0.4 MCi). 51Cr at 10 MCi was never made either (Gallex made about 1.7 MCi). Both are proposal-level, as is the adopted Ce source.
- The 80% untagged "outside" fraction for Ce elastic scattering is an estimate. It fails even at x0.5.
- Elastic scattering of the Ce antineutrinos could still give a rate-only test. The stated energy requirement excludes it by physics, but a reader could argue for dropping the requirement.
- The adoption_status date and wording of the 2018 cancellation are unverified (no web fetch made).
