# notes: p07_meg

## Design choices
- Target item: the downstream on-axis tagger for the low-energy positrons from radiative muon decay (only one counted item in the row).
- BASE: an invented mu+ -> e+ gamma instrument. The field falls from 0.5 T at the target to 0.25 T at both ends, so half of the isotropic low-energy positrons reach the downstream end. Adopted reduction is 0.5 x 0.5 x 0.9 = 22.5%, above the stated 10%.
- CONF1, minimal edit (the single field sentence): the field rises downstream to 2.0 T. That is a magnetic mirror with ratio 4. Only the loss cone sin^2(alpha) < 0.25 gets through: 0.5 x (1 - sqrt(0.75)) = 6.7% of the positrons. The adopted reduction is <= 6.7% even with f_rmd and eps_det capped at 1, so it fails the 10% requirement. The rest are reflected and leave upstream (93.3%).
- Survivor coded: an upstream thin-fibre tagger in the beam path (the documented, not-adopted alternative; it is the pair's distractor). It is checked against every stated fact:
  - background reduction;
  - signal loss from beam-muon misidentification and Michel hits;
  - beam-path material against the stated thinnable 50 mg/cm2 degrader;
  - radius against the 15 cm tracker inner radius;
  - calorimeter facts, which neither option changes.
  Other survivors an expert might propose (better photon resolution, thinner target to cut annihilation in flight) are not coded.
- Workaround closed: a tagger placed between the target and the field rise (< 5 cm) would sit where signal positrons and photons near 90 degrees pass at r < 15 cm. That costs signal efficiency and adds annihilation-in-flight material. The stated rise at 5-20 cm closes this route; it is not coded in the key (doubt).
- Coherence: the 2.0 T downstream region also mirrors signal positrons heading downstream. The tracker still sees them on the way out and back, and no stated requirement is affected. Non-stopped beam muons (5e6/s) are treated the same way in both levels.

## Survivors per CONF
- none (CONF1 withdrawn in r1; see 'r1 outcome').

## Fixed inputs (exact stated facts in BASE/CONF1, not varied)
- B_target 0.5 T, B_up 0.25 T, B_down 0.25 T (BASE) / 2.0 T (CONF1);
- R_beam 5e7/s, R_stop 4.5e7/s;
- degrader 50 mg/cm2;
- tracker r_min 15 cm;
- requirements 10% and 2%.

All are given as exact numbers in the descriptions.

## unc ranges
- None; all props are varied x0.5-2.

## Doubts
- The props are estimates from memory, not fetched: tagger efficiency 0.9, Michel reach 0.03, energy-cut survival 0.2, beam misidentification 1e-2, f_rmd ~0.5. The MEG II design report (arXiv:1801.04688) should confirm the order of magnitude.
- The key assumes the RMD low-energy positron direction is isotropic. Near the endpoint the neutrino pair balances the photon, so the positron direction is only weakly correlated with the photon.
- The upstream survivor's credibility rests on the beam-muon vs positron pulse-height separation in a 200 um fibre layer at 5e7/s, about 15x MIP for surface muons.
- adoption_status "built and operated" is from memory, not verified.

## Change log
- v1: initial. The key's ok_geom line was cleaned before the first saved run (no stated numbers changed).
- r1 (2026-11-06): CONF1 moved to abandoned/CONF1_r0_mirror.txt; r0 key, key_output and kprobe kept in abandoned/ (key_r0.py, key_output_r0.txt, kprobe_r0.json). kprobe.json set to {}. keys/key.py now checks BASE only. Scan scripts: abandoned/r1_scan.py, abandoned/r1_thin.py.

## r1 outcome: no honest conflict

Study decision (red team r1, N3): the adopted item is ANY radiative decay counter on the axis downstream of the target; position cannot be narrowed. A CONF must make every downstream on-axis placement fail the 10% requirement by a plain physical fact while a credible alternative passes. None was found. Evaluated (paraxial Boris tracking, abandoned/r1_scan.py; RMD e+ isotropic, p 1.4-5.5 MeV/c; beam spot sigma 1 cm; disks z = 0.2-120 cm, R = 0.5-15 cm; "signal-safe" = <= 2% of accepted signal events have e+ or photon crossing the disk; reduction = 0.5 x 0.9 x fR):

1. **r0 CONF1 field (rise 5-20 cm), acceptance near 90 deg (theta >= 70):** best disk z = 5 cm, R = 10 cm, fR = 0.49, reduction 22%. z = 3 cm, R = 5 cm gives fR = 0.44 (red team: 0.38-0.52). Route open, as N3 found.
2. **No low-field gap (rise 0.5 -> 2.0 T starting at the target, over 15 cm), theta >= 70:** best disk z = 2 cm, R = 4 cm, fR = 0.27, reduction 12%. Still passes. Removing the gap only moves the working disk closer to the target.
3. **Gap removed plus a stated signal acceptance of 40-140 deg (a shared sentence in BASE and CONF):** best ABSORBING disk is z = 5 cm, R = 3 cm, fR = 0.157, reduction 7.1% (7.9% at eps = 1). With theta >= 30: 5.7%. So a thick counter fails. But a THIN timing-only disk (about 0.5 mm plastic) costs accepted signal almost nothing (photon conversion ~0.1%, e+ scattering ~7 mrad). Its cost is the random veto from Michel e+ crossings, 4.5e7/s x fM x window (abandoned/r1_thin.py): for example z = 2 cm, R = 3 cm gives fR = 0.225 (reduction 10.1%) with fM = 0.195. The veto loss is 0.9% at a 1 ns window, 1.8% at 2 ns and 3.5% at 4 ns. z = 0.5 cm, R = 2 cm gives a 13.6% reduction with 1.3% / 2.6% loss at 1 / 2 ns. A ~1 ns window is credible for a thin scintillator (100-200 ps class). So whether this placement fails depends on a varied property (the window): the route is not closed robustly under rule 4. The edit also needs a new shared sentence in BASE, and it makes the forward e+ (40-60 deg) be mirrored before the tracker (coherence strain).
4. **Annihilation-in-flight budget (change "about half" to "about one in ten or less"):** this is airtight against every RMD tagger, because the reduction is at most f_rmd. It fails coherence (rule 7). Estimate: AIF photons in the window (y > 0.97) are ~2.6e-3 per e+ per X0 (Michel fraction above 51 MeV 0.069 x annihilation probability ~0.19/X0 at 50 MeV x hard-photon fraction ~0.2). RMD is ~4e-6 per muon. The two are equal at ~1.5e-3 X0 of e+ path, which is what the stated 120 um foil alone gives for e+ near 90 deg. AIF at 9x RMD needs ~2% X0 per e+, which contradicts the stated "low-mass tracker" and thin foil. Making pile-up dominant needs unstated calorimeter facts. A robust survivor also cannot be coded: with the AIF/pile-up split unstated, only resolution upgrades help every source, and their achieved resolution fails the x0.5-2 variation.
5. **Pile-up from Michel e+ in a thick (timing + energy) counter:** 4.5e7 x fM (0.2-0.3) x q_ecut (0.2) x 2 ns = 0.4-0.5%. Not decisive.
6. **Beam continuing downstream (non-stopped mu+):** 5e6/s at a 2 ns window is 1%. Surface mu+ stop in the front plastic and give no crystal hit, so the energy layer rejects them. Raising the non-stopped fraction changes stated rates and is still not robust.
7. **RMD e+ energy/angle and polarisation (N2):** not editable by an instrument fact. The polarisation asymmetry (|a| <= 1/3) pushes low-energy e+ downstream, which helps the adopted item.

Conclusion: no plain, minimal, coherent physical edit of BASE makes every downstream on-axis RDC placement fail robustly while an alternative passes. Per AUTHOR_BRIEF ("If no honest CONF exists ... that is an acceptable outcome") the pair has no CONF, and the study decision applies: DROP to zero units under A2, with replacement by the next eligible baseline (q32 BESIII). BASE and its key are unchanged.
