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
- CONF1: 1 (upstream tagger).

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
