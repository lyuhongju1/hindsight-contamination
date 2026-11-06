# Selected baseline–upgrade pairs (confirmatory set)

*Selection completed 2026-11-06 under `pair_selection_rules.md` (frozen at commit 721e55f), Amendment A1 and its three addenda. Every counted item has **two independent dating claims, both VERIFIED** by `verify_dating.py`: metadata date, verbatim quote checked against the arXiv text, class Post-primary (≥ 24 months after the baseline), commitment ≤ 2023-06-30. Raw verdicts: `eligibility/verdicts/`; claims: `eligibility/claims/`.*

| # | Field | Baseline (recid, date) | Upgrade programme | Counted item(s) | Commitment (verified) | Alternative not adopted (distractor seed) | Caveats |
|---|---|---|---|---|---|---|---|
| 1 | dark_matter | XENON1T (1618326, 2017-08) | XENONnT | Liquid-phase Xe purification | arXiv:2007.08796, 2020-07 | Gas-phase-only getter purification | Gd neutron veto indeterminate (one quote failed) |
| 2 | double_beta | GERDA Phase II (1634658, 2017-11) | LEGEND-1000 | Underground-sourced argon; ASIC front end | arXiv:2107.11462, 2021-07 | Atmospheric LAr with 42K mitigation; discrete JFET front end | LEGEND accepted as declared successor (merged GERDA + Majorana) |
| 3 | grav_waves | Advanced Virgo (1311317, 2014-08) | AdV+ | Frequency-dependent squeezing | arXiv:1304.0670v7, 2019-09 | Frequency-independent or EPR squeezing | Version-aware dating (quote absent in v6) |
| 4 | nu_accel | ICARUS T600 (912685, 2011-06) | SBN (WA104 overhaul) | Serial ADC per channel | arXiv:1503.01520, 2015-03 | Multiplexed ADCs; cold front end | — |
| 5 | nu_natural | SNO (509079, 1999-10) | SNO+ | LAB liquid scintillator; Te-130 loading | arXiv:0810.3694 (2008-10); arXiv:1405.3401 (2014-05) | Pseudocumene/PXE; Nd-150 loading | Proceedings "for the collaboration" |
| 6 | other | AGATA (955239, 2011-11) | AGATA Phase 2 | Phase-2 Ethernet readout (STARE) | arXiv:2011.06092, 2020-11 | Phase-1 GGP/ATCA readout | Weak; true first commitment (2016) not on arXiv |
| 7 | precision | MEG (1223321, 2013-03) | MEG II | Radiative decay counter | arXiv:1801.04688, 2018-01 | Upstream RDC | — |
| 8 | dark_matter | COSINE-100 (1630770, 2017-10) | COSINE-200 | In-house ultra-pure NaI crystal growth | arXiv:2004.06287v1, 2020-04 | Commercial (Alpha Spectra) crystals | Subset-of-collaboration authorship |
| 9 | double_beta | NEMO-3 (645078, 2004-02) | SuperNEMO | 8-in. high-QE R5912-MOD PMT calorimeter modules | arXiv:1707.06823v1, 2017-07 | 5-, 10- and 11-in. PMTs; PVT scintillator | Possibly earlier non-arXiv commitment |
| 10 | nu_natural | Borexino (788332, 2008-06) | SOX | 144Ce-144Pr antineutrino source | arXiv:1304.7721v1, 2013-04 | 51Cr neutrino source | SOX cancelled (source never delivered): adoption_status |
| 11 | grav_waves | KAGRA (1704344, 2018-11) | post-O3GK KAGRA | Optical levers for marionette damping | arXiv:2203.07011v1, 2022-03 | Improved photo-sensors | Plan-level wording ("investigation in progress"), counted under A1 addendum 3 |
| 12 | nu_accel | MiniBooNE (789156, 2008-06) | Enhanced MiniBooNE | PPO doping of the mineral oil | arXiv:1210.2296v1, 2012-10 | Butyl-PBD fluor | LoI, possibly never implemented: adoption_status |
| 13 | collider | NA62 (1519167, 2017-03) | HIKE | Small-diameter (< 5 mm) straws | arXiv:2204.13394v1, 2022-04 | Existing 9.8 mm straws | HIKE not approved: adoption_status |
| 14 | astroparticle | KASCADE (636731, 2003) | LOPES (radio extension of KASCADE-Grande) | LOPES-3D tripole antennas | arXiv:1303.6808v1, 2013-03 | Inverted-V dipoles; LPDA/butterfly antennas | LOPES formally a separate collaboration with substantially the same members (accepted by both daters) |

## Selection statistics

| | Count |
|---|---|
| Assessed (two daters each) | 25 baselines |
| Eligible and selected | 14 |
| Eligible but not selected (field already filled that round) | 2: aLIGO → A+ (balanced homodyne readout); BESIII (ETOF MRPC) |
| Not eligible | 9: MACRO, ANKE, KASCADE-Grande, NA48, MicroBooNE, DAMPE, CLAS12, FACT, OPERA |
| Skipped by lineage rule | 2: Virgo 2012, GERDA 2012 |

**Dater agreement on eligibility:** 25 of 25. NA48 was decided by the both-daters-same-item rule.

**Verifier record:**
- one dater paraphrase was caught (XENON1T Gd veto);
- the verifier was corrected mid-stream for pypdf extraction false negatives, and all claims were re-verified uniformly;
- the fabricated-quote control fails throughout.

**Caps:**
- field cap 3: no field above 2;
- LNGS-2017 year-and-lab cap: reached (XENON1T, GERDA Phase II).

## Next stage

Materials. For each pair, the author agents (brief v2, rules 1–10) write BASE plus 1–2 CONF, followed by keylib v4.1, red team, the K premise check, and recognition probes. The materials stage also records `adoption_status` per item (built and operated / approved not built / cancelled), as an exploratory covariate.

## A2 update (2026-11-06)

- **p04 ICARUS:** zero-unit pair (no honest physical conflict for the counted item).
- **Replacement:** **p15 aLIGO → A+**
  - item: balanced homodyne readout (arXiv:1304.0670v7, 2019-09; both daters verified);
  - alternative not adopted: DC readout;
  - caveat: the LIGO A+ design curve (2018) may already include BHD; not on arXiv.
