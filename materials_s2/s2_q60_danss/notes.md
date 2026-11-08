# notes: s2_q60_danss (PROVISIONAL: the second dater is still running)

## Outcome
A robust window holds, but it is narrow. CONF1 PASSES keylib (adopted item fails in 0.996 of draws; >= 1 survivor in 0.961). The window only exists for a stated volume near 30 L and a stated ambient rate near 65-80 Hz/m2 (see the scan below).

## Design choices
- Item: neutron tagging by gadolinium capture in ANY form (coating, film or loaded plastic). The key models the item's physics once (shared props `gd`) and treats the delayed threshold (1.0 to 3.6 MeV in 0.2 MeV steps) and a topology cut (>= 2 gamma clusters, or none) as settings of the item: 28 settings. **The item fails only if every setting fails** (C1, lesson 4).
- Mechanism (Route A of feasibility_q60): in a 30 L cube (31 cm per side) most of the ~8 MeV Gd cascade (about 4 gammas of ~2 MeV, lambda ~20 cm in plastic) escapes.
  - Threshold above 208Tl (2.6-3.6 MeV): delayed efficiency 0.04-0.12, below 30%. Accidentals from >2.7 MeV singles plus ambient neutron captures are also marginal (0.66-2.9 x signal).
  - Low threshold (1.0-2.0 MeV): efficiency 0.18-0.37, but the delayed singles are the ambient gamma rate (80 Hz/m2 x 0.58 m2 = 46 Hz). Accidentals are 6-28 x the detected signal (topology cut included), against a stated limit of 1.
  - 6Li with PSD: delayed singles are 1% gamma leakage plus ambient neutron captures (~0.4 Hz). Accidentals are 0.17 x signal, and efficiency is 0.47.
- BASE (0.9 m3): the same model gives Gd 0.41-0.72 efficiency and acc/signal 0.02-0.7 for most settings, so the upgrade from hydrogen capture is sound. Hydrogen capture (the present state) fails BASE on accidentals (19 x signal), so the upgrade is motivated.
- Prompt threshold: raising the prompt cut to ~2.7 MeV would be a routine setting that rescues Gd at low delayed threshold (prompt singles fall ~100x). It is closed by a plain physics requirement: the positron spectrum must be recorded from 1 MeV upward (needed for the fuel-composition goal). It is coded as `prompt_thr_MeV` under fixed.
- Requirements: the delayed efficiency is >= 30% (as instructed; the SANDD survivor reaches 34.8% at 9 L, and the model gives 47% at 30 L). Most of the robustness comes from the accidental route.
- Minimal pair: BASE and CONF1 differ in one sentence (cube volume, side and bar length; diff checked).
- Workarounds: extra shielding to cut the ambient rate is a separate add-on (C1: scored C; the conflict stands). It is not closed by a fact, and no space or site rule is used. A larger volume is excluded by the stated volume (an instrument fact, C1). A shorter Gd capture time (higher loading) is a setting: see the sensitivity check.

## Survivors per CONF
- CONF1: 2 at nominal: 6Li-doped PSD plastic (SANDD type), and 6LiF:ZnS sheets (SoLid type, estimated props). Hydrogen capture fails.

## Fixed inputs (stated facts or constants)
- V_L 900 / 30, P_th 3.0 GW, L 10 m, ambient rate 80 Hz/m2 above 1 MeV, EFF_REQ 0.30, ACC_REQ 1.0, prompt_thr 1.0 MeV: these are stated in the descriptions.
- H density 4.86e22 /cm3 (C8H8 at 1.05 g/cm3), 200 MeV per fission, 208Tl 2.614 MeV, and the Gd cascade energy 7.9 MeV (157Gd Q = 7.94 MeV): physical constants.
- Gd cascade multiplicity 4: an integer structural count. The sensitivity check with 3 and 5 still leaves no Gd setting passing at nominal.
- Gd settings grid (thresholds, topology): reader choices, scanned exhaustively.

## unc ranges
- sigma_f (IBD yield per fission, 5.8e-43 cm2): x0.8-1.25. The reactor flux x cross-section is known to a few % (Huber-Mueller-class).
- lam_gamma 19.7 cm: x0.8-1.25. NIST XCOM mu/rho for polystyrene at 2 MeV.
- All other props use the default x0.5-2. That includes the estimates: fractions of ambient singles above 2.0 MeV (0.25) and above 2.7 MeV (0.01), ambient neutron captures (0.6 Hz/m2), the window-to->1 MeV gamma ratio (1.0), the multi-segment ambient fraction (0.4), and all ZnS-sheet props.

## Calibration
- The neutron escape model is escape = 1 - exp(-ell*S/(4V)). ell = 10.2 cm reproduces the 51.9% escape of SANDD at 9 L with a PE layer (arXiv:2105.00083). Gd uses ell = 9 cm (shorter capture time, 29.6 us, PANDA).
- The 6Li efficiency factors come from SANDD: 12.8% on H, a 95.7% energy cut, PSD 0.918 (derived), and a 34.8% total at 9 L. The model at 9 L gives 0.37 (published 0.348).
- Gd containment: binomial over 4 gammas, each interacting with p = 1-exp(-(a/3)/lambda) and depositing U[0, E_gamma] (this ignores dead material, the PE and Gd films, and the fill factor: optimistic for Gd). PANDA36 check (360 L, 3 MeV): the model gives 0.299 against a published 0.355 (19.4% model systematic, arXiv:1404.7309). So the model is about 16% LOW there, within PANDA's systematic. A 1.2x correction would not rescue Gd: the highest CONF1 high-threshold efficiency would go from 0.12 to about 0.14.
- Coherence: 30 L at 10 m from 3 GWth gives about 540 IBD/day in the volume and about 200/day detected with 6Li (a daily statistical precision of about 7%), which is adequate for day-by-day power tracking. At 80 Hz/m2 the singles rate is 46 Hz in CONF1 and about 450 Hz in BASE, which is plausible for a shielded detector at a reactor site. The cascade escape that defeats Gd also cuts the positron annihilation containment, but the 80% prompt efficiency is the SANDD 9 L value, so it is conservative at 30 L.

## Robustness scan (logged before choosing the stated numbers; no post-run tuning beyond this)
- An initial choice of 27 L and 50 Hz/m2 passed (0.983 / 0.959), but failed the sensitivity check with a Gd capture time of 10 us (adopted fails 0.884).
- Scan (tau_Gd 30 / 10 us): 30 L at 80 Hz/m2 passes both (0.996/0.961 and 0.955/0.964). At 27 L and 80 Hz/m2 the survivor drops to 0.945. At 120 Hz/m2 the survivor drops to 0.88. A limit of acc <= 0.5 x signal pushes the survivor below 0.95.
- Final choice: 30 L and 80 Hz/m2. The survivor's margin is set by its own efficiency (neutron escape x2 brings 6Li to about 0.28).

## Doubts
- The window is narrow (survivor 0.961 vs 0.95). It relies on estimated ambient-spectrum fractions and on a SANDD-calibrated escape model. No direct MC exists for Gd in a 30 L cube.
- Gd loading so high that tau is below 10 us (or a very short window) was not tested beyond tau = 10 us. At 10 us, adopted fails 0.955 (borderline).
- The 80 Hz/m2 figure is unverified (danss_gd_efficiency_check.md found no Hz figure). It is a stated site fact, but a red team may question its realism.
- Correlated backgrounds (fast neutrons) are not modelled. They affect both capture agents.
- Recognition: small 6Li-PSD reactor monitors (SANDD, PROSPECT-class) are well known.
- The dossier's Gd-film details for the upgrade come from the candidate row and have not been checked.

## Post-run change log
- (none after the final key run)


## Gate note (orchestrator, 2026-11-08)
Gate A flags NAME.txt for 'gadolinium'. The real DANSS baseline already used a Gd-loaded coating; NAME describes the real instrument, so this is not a leak of the adopted item (the separate Gd2O3-polyethylene film). Documented exception. BASE, CONF1 and ANON are clean.
