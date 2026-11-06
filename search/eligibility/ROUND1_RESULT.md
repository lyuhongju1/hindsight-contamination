# Eligibility round 1 (q01–q09): result

**Rule (pair_selection_rules.md §6):** an item counts only if **both** daters' claims are VERIFIED by `verify_dating.py` and fall in the same class (Post-primary, ≥ 24 months), with the commitment ≤ 2023-06-30 (I6).

| q | Field | Baseline | Verdict | Items counted | Notes |
|---|---|---|---|---|---|
| 01 | astroparticle | MACRO | NOT ELIGIBLE (D1 = D2) | — | No upgrade programme or successor |
| 02 | collider | ANKE | NOT ELIGIBLE (D1 = D2) | — | Commitments before the baseline, within 24 months, or not on arXiv |
| 03 | dark_matter | XENON1T | **ELIGIBLE** | liquid-phase Xe purification (arXiv:2007.08796, 2020-07) | Gd water neutron veto **indeterminate**: D2's quote was a paraphrase, not verbatim (verifier FAIL) |
| 04 | double_beta | GERDA Phase II → LEGEND-1000 | **ELIGIBLE** | underground argon; ASIC front end (arXiv:2107.11462, 2021-07) | LEGEND accepted as declared successor (merged GERDA + Majorana) by both daters |
| 05 | grav_waves | Advanced Virgo → AdV+ | **ELIGIBLE** | frequency-dependent squeezing (arXiv:1304.0670**v7**, 2019-09) | Version-aware dating; quote absent in v6. 100 kg test masses: D2 only (D1 judges it a scale-up) |
| 06 | nu_accel | ICARUS T600 → SBN | **ELIGIBLE** | serial ADC per channel (arXiv:1503.01520, 2015-03) | Cosmic-ray tagger: D2 only |
| 07 | nu_natural | SNO → SNO+ | **ELIGIBLE** | LAB scintillator (arXiv:0810.3694, 2008-10); Te-130 loading (arXiv:1405.3401, 2014-05; D2 fuzzy match) | |
| 08 | other | AGATA | **ELIGIBLE (weak)** | Phase-2 Ethernet readout (arXiv:2011.06092, 2020-11) | The true first commitment (2016) is not on arXiv; the date is late but still eligible |
| 09 | precision | MEG → MEG II | **ELIGIBLE** | radiative decay counter (arXiv:1801.04688, 2018-01) | |

**Selected under A1 (round-robin, first eligible per field):** XENON1T, GERDA→LEGEND, Advanced Virgo, ICARUS, SNO, AGATA, MEG. That is **7 of 14**.

**Next:** astroparticle and collider continue down their queues (q10 and q11), then round 2 for every field.

**Verifier improvement, made during the round:** version-aware arXiv dating (`arXiv:<id>v<N>`: date of vN from the submission history; quote must be absent in vN−1). It was needed because multi-version papers were otherwise dated by v1.
