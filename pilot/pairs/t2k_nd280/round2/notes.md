# Notes: t2k_nd280 round 2

## Design choices
- The instrument is invented: the Kestrel Flats near station, 410 m from the target, with a 0.7 GeV flux peak, a 0.3 T warm dipole, a 6.5 m inner volume and a 1.9 x 1.8 x 0.6 m target region. Round-1 identifiers are left out: no yoke scintillator, no P0D removal, no chamber/target alternation, no TKI, no off-axis, no 4% systematic.
- Round 2 uses pass/fail requirements, not a figure of merit. The key checks four requirements:
  - acceptance at all angles (qualitative, boolean);
  - fraction of target nucleons that are hydrogen nuclei <= h_max;
  - absorbed dose to the target medium <= the medium's tolerance;
  - field 0.3 T (no option is limited by it).
- BASE: h_max = 20% and dose = 5 Gy. The adopted item passes: 7.7% H, and 5 Gy is far below 30 kGy. The water-cell grid and the three TPC options also pass. BASE does not claim that the adopted item is the best option.
- The descriptions contain no proton-threshold number. Under the keylib x0.5-x2 variation of every leaf, a threshold comparison cannot give the >= 2.6 ratio margin needed on both sides (round-1 red team, finding A). The proton need is stated qualitatively.
- regex_check.py checks every description against scoring_regex.json: no hits. Each description has 7 lines.

## Conflict mechanisms
- CONF1 (radiation damage to the organic scintillator and WLS fibres): the one edit is the dose, 5 Gy -> 5 MGy.
  - Polystyrene scintillator loses about 1.6-1.9 %/kGy, with exponential loss at high dose (arXiv:2410.12535; CMS HE, arXiv:2001.06553). The tolerance is taken as 3e4 Gy, about half the light lost.
  - 5 MGy is about 170x that tolerance.
  - The water grid and the bars fail as well, since they use the same medium.
  - Survivors: the HP Ar-CH4 gas TPC, the LAr TPC and the LXe TPC. Their media are recirculated, so they take no permanent damage.
- CONF2 (hydrogen content of the hydrocarbon): the one edit is h_max, 20% -> 1%.
  - Polystyrene C8H8 has 8/104 = 7.7% of its nucleons as hydrogen.
  - Survivors: the LAr TPC and the LXe TPC (0%). The Ar:CH4 90:10 gas TPC (1.06%) is marginal and is not needed.
  - The edit states a model-validity fact about the far-detector extrapolation. It does not name a material class. It differs from round-1 "only oxygen counts": the round-1 rule zeroed the useful mass by nucleus identity, while this one is a quantitative contamination limit that the reader must translate from chemical composition.

## Log of stated-number changes
- None. The numbers were fixed before the first key run.
- One wording edit was made before the first run: the hydrogen sentence became "removed with a model that stays adequate only while ...", so that it reads as a physical fact rather than a bare rule.

## Doubts
- CONF1 plausibility: 5 MGy to a near-detector target is far above any real near detector. It is physically consistent only for a station close to a dump.
  - Readout electronics of the TPC alternatives would also need placing or shielding. The key models only the dose to the medium.
  - Gas-detector ageing from CH4 radiolysis is ignored.
- The noble-liquid "no permanent damage" claim is cited qualitatively (ATLAS LAr TDR, EXO-200), not as a number. It is encoded as the boolean medium_renewed, so robustness does not vary it.
- The field_ok_T = 1.0 T values are loose engineering statements. They never decide anything: under x0.5-x2 variation they cause the small viability shortfall in CONF2 (0.988).
- CONF2 survivors are both noble-liquid TPCs. A reader may see the hydrogen limit as close to a material rule. It still leaves >= 2 survivors and needs the composition to be translated.
- The CONF2 survivors (LAr and LXe TPCs) carry no target-mass or proton-threshold requirement. The descriptions do not state one, so none is applied.
- The sentence about short proton tracks is not coded as a number. All four options with all_angles=True are assumed to track short protons. For the water grid, with its 2.5 cm cells, that assumption is generous.
- Search used: 1 web search (plastic scintillator dose damage). No fetches.
