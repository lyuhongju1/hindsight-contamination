# Eligibility round 2 (q10–q18, q14 skipped by lineage): result

## Verifier correction, applied before tallying round 2

pypdf can drop the spaces between words, and the earlier normalisation mishandled line-break hyphens in hyphenated words. Together these caused **false negatives** on genuine quotes; three of D2's round-2 claims were affected.

Quote matching now compares alphanumeric-only ("squashed") strings. The fuzzy fallback is a 60-character run plus ≥ 0.90 character-level match.

**All 33 claims from rounds 1–2 were re-verified with the corrected tool:**
- every earlier VERIFIED claim stays verified;
- the round-1 XENON1T paraphrase still FAILS;
- the fabricated self-test quote still FAILS;
- D2's three round-2 claims now verify.

No round-1 decision changes. Output: `claims/ALL_rounds1-2_verified.json`.

## Verdicts

| q | Field | Baseline | Verdict | Counted item(s) |
|---|---|---|---|---|
| 10 | astroparticle | KASCADE-Grande | NOT ELIGIBLE (D1 = D2) | No upgrade or successor |
| 11 | collider | NA48 (→ NA62 → HIKE) | NOT ELIGIBLE | **No item shared by both daters.** D1: shashlyk MEC; D2: small straws and LKr readout. The LoI itself lists "readout upgrade OR new MEC", so neither was committed. HIKE was never approved |
| 12 | dark_matter | COSINE-100 → COSINE-200 | **ELIGIBLE** | In-house ultra-pure NaI growth (arXiv:2004.06287v1, 2020-04). Direct PMT encapsulation: D2 only |
| 13 | double_beta | NEMO-3 → SuperNEMO | **ELIGIBLE** | 8-in. R5912-MOD PMT calorimeter modules (arXiv:1707.06823v1, 2017-07) |
| 14 | grav_waves | Virgo (2012) | SKIPPED | Lineage already selected (A1 addendum 2) |
| 15 | nu_accel | MicroBooNE | NOT ELIGIBLE (D1 = D2) | Only the CRT, committed in the baseline itself |
| 16 | nu_natural | Borexino → SOX | **ELIGIBLE** | 144Ce-144Pr antineutrino source (arXiv:1304.7721v1, 2013-04) |
| 17 | astroparticle | DAMPE | NOT ELIGIBLE (D1 = D2) | No upgrade; VLAST first on arXiv 2024 (I6) |
| 18 | collider | CLAS12 | NOT ELIGIBLE (D1 = D2) | µRWELL commitment internal (2020) or on arXiv only from 2024 |

## Selected so far: 10 of 14

**Round 1:** XENON1T, GERDA Phase II → LEGEND, Advanced Virgo, ICARUS, SNO → SNO+, AGATA, MEG.
**Round 2:** COSINE-100, NEMO-3, Borexino.

Caps:
- per-field cap 3: not reached;
- year-and-lab cap: LNGS-2017 now holds 2 (XENON1T, GERDA Phase II) and is full, so further LNGS-2017 baselines are skipped.

**Remaining in round 2:** astroparticle, collider, grav_waves and nu_accel continue down their queues.
