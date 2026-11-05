# Date check: LIGO-T1300433 (for the APS V3 table `tab:dating`)

*Checked 2026-11-05 by Claude from web sources. A human should confirm before the table is signed off.*

## (a) What the document is

| Field | Value |
|---|---|
| Title | **Instrument Science White Paper**, LIGO Scientific Collaboration. The DCC abstract says: "This is the 2013-14 instrument science white paper. The 2014-15 version is T1400316." |
| Authors | Listed as **LIGO Scientific Collaboration** (DCC author group LSC). No individual authors are listed on the record |
| Versions | Only v3 is public. Earlier editions in the series are LIGO-T1200199 (v2) and LIGO-T1200008 |
| Record | https://dcc.ligo.org/LIGO-T1300433/public (mirror: https://dcc-lho.ligo.org/LIGO-T1300433/public) |
| PDF | https://dcc.ligo-wa.caltech.edu/public/0103/T1300433/003/T1300433-v3.pdf |

Evidence for the date:

- **Cover page of the PDF:** "Technical Note LIGO-T1300433–v3 **2013/06/04**".
- **PDF metadata:** CreationDate and ModDate are both 2013-06-04 10:25 −07:00.
- **Internal noise-budget plot:** "created using gwinc.m on 03-Jun-2013".

## (b) Was it public before the baseline (arXiv:1411.4547, 2014-11)?

**Probably yes, but the exact public-release date is not documented on the record.**

- The DCC page shows no "public since" date.
- Its change notes say only that the paper was "made … a publicly viewable doc" "about July 4", with **no year**.
- The most natural reading is about July 2013, one month after v3, since the document is the 2013-14 edition and was superseded by T1400316 in 2014. July 2014 cannot be ruled out from the record alone.
- Either way it is public before November 2014. Even on the later reading (July 2014) the gap is only about 4 months, which would be "Cont." rather than "Pre". On the likely reading (July 2013) the gap is about 16 months, which is "Pre".

**Confidence:**

| Claim | Confidence |
|---|---|
| Content dated June 2013 | High |
| Public by mid-2013 | Medium |

## (c) Does it propose frequency-dependent squeezing with a filter cavity?

**Yes.** It does so for the post-aLIGO upgrade designs in the facility (the "Red", "Blue" and "Green" strawman designs, which keep the aLIGO configuration). Quotation from §3.1.1, p. 9:

> "All designs keep the standard aLIGO configuration, namely dual-recycled Fabry-Perot Michelson, while all of them employ frequency dependent squeezing with an input filter cavity of 100-m class length for reduction of quantum noises."

Section 4.2.1, "Frequency-dependent squeezing angle (input filtering)", and §4.7.2, "Optical Loss in Filter Cavities", treat the topic in detail. The Red design specifies a 300 m filter cavity with 30 ppm roundtrip loss.

## Fallback source

arXiv:1305.1599 (https://arxiv.org/abs/1305.1599):

- M. Evans, L. Barsotti, J. Harms, P. Kwee, H. Miao, "Realistic Filter Cavities for Advanced Gravitational Wave Detectors", **v1 submitted 2013-05-07**, published as Phys. Rev. D 88, 022002 (2013).
- It proposes a practical filter-cavity route to frequency-dependent squeezing for Advanced LIGO.
- Its arXiv timestamp is unambiguous, but it is a paper by collaboration members, not a collaboration document. Under the hindsight paper's new rule it counts as a "plan precursor"; under the APS V3 rule it counts as a collaboration paper proposing the item.

## Recommendation for V3

Keep **"2013-06, LIGO-T1300433, Pre"**, citing the v3 cover date (2013-06-04). Add arXiv:1305.1599 (2013-05) as corroboration, because it has a verifiable public timestamp. The classification is "Pre" under either source.
