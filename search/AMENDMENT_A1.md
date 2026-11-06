# Amendment A1 to pair_selection_rules.md

*Dated 2026-11-06. Committed before any eligibility (I2–I6) assessment and before any draw.*

## Change

The frozen rules (§4) assess eligibility (I2–I6) for **all** I1-screened baselines and then draw at random within field. A1 replaces this with an **equivalent sequential draw**:

1. The 81 I1-included, non-pilot baselines (`screening/included_nonpilot.csv`) are put in a random order within each field. The seed is the SHA-256 of `pair_selection_rules.md` as frozen at commit `721e55f` (`d3282f64…`), as §4 specifies.
2. Fields are visited round-robin in sorted order, as in `inspire_search.py draw`. Within a field, baselines are assessed for I2–I6 in their random order.
3. The first baseline in a field that passes I2–I6 is selected for that round. Assessment continues until **14 pairs** are selected, or the list is exhausted. The per-field cap (3) and the year-and-lab cap (2) still apply.
4. Every assessed baseline and its outcome (pass, or which criterion failed) is logged, including those assessed but not selected.

## Rationale

Assessing all 81 baselines would require dating and alternative-finding agents for every one. Under a random order, each eligible baseline in a field has the same chance of selection as under assess-all-then-draw, so the selection distribution is unchanged and the effort scales with the target instead of the frame.

## Effect on the frozen seed

None. The same seed and the same caps are used.

## A1 addendum: I6 boundary (2026-11-06, before any eligibility assessment)

I6 requires the adoption commitment to be public ≥ 18 months before the earliest training cutoff among the confirmatory models. The earliest such cutoff is taken, conservatively, as early 2025. The I6 boundary is therefore fixed at **commitment date ≤ 2023-06-30**.

## A1 addendum 2: one baseline per program lineage (2026-11-06, before round 2)

The frame contains several baselines from the same program lineage: Virgo (2012) and Advanced Virgo (2014); GERDA (2012) and GERDA Phase II (2017); aLIGO twice; KAGRA twice; and others. Selecting two of them would put the same upgrade program, and possibly the same items, into the study twice, so the units would not be independent.

**Rule:** once a baseline is selected, later queue entries from the same collaboration lineage, meaning the same experiment or its direct predecessor or successor, are **skipped** and logged as "lineage already selected". This applies identically to every field.

**Skipped by this rule before round 2:**
- q14 Virgo (2012): Advanced Virgo is selected;
- q20 GERDA (2012): GERDA Phase II is selected.

## A1 addendum 3: meaning of "adopted" (2026-11-06, before any round-3 selection)

The frozen rules define an item as a choice "adopted by the upgrade program", and the commitment as the earliest collaboration document "proposing the item for this program". Round-3 daters flagged commitments worded as plans (KAGRA: "We plan to substitute…; the investigation is in progress"). Some selected items were also committed but never built (Borexino SOX: source production failed; MiniBooNE PPO: LoI).

**Interpretation applied uniformly:** an item counts if the collaboration's own document commits to it **as the program's chosen plan**. If the document presents it as one of several open options ("X or Y"; NA48/HIKE in round 2), it does not count.

Whether the item was eventually **built and operated / approved but not built / cancelled** is recorded per item as an **exploratory covariate** (`adoption_status`), filled in at the materials stage. It is not a selection criterion. Rationale: the study measures whether models reproduce a collaboration's recorded choice against stated physics, and a recorded choice exists whether or not construction followed.

## Amendment A2: replacement of pairs that admit no honest conflict (2026-11-06)

*Before any confirmatory model sampling; no confirmatory item has been shown to any study model.*

**Trigger.** p04_icarus yields no honest physical conflict for its counted item. The author found that per-channel synchronous digitisation is at least as good as multiplexing on every physical criterion; its drawbacks are cost, density and power engineering, which rule 1 excludes. The red team concurred that the earlier conflict tested a different item.

**Rule.**
- When a selected pair is concluded, after author and red-team rounds, to admit no honest physical conflict, it is **retained in the report as a zero-unit pair**.
- It is replaced by the **next eligible-but-not-selected baseline in queue order** (any field, subject to the per-field cap of 3, the year-and-lab cap, and the lineage rule).
- If none remain, assessment resumes down the queue under A1.

**Consequence for scope, to be disclosed.** The confirmatory population becomes "baseline–upgrade pairs whose counted item admits an honest physical conflict". This is a scope restriction defined by the item's physics, not by any model behaviour.

**First replacement.** q28 aLIGO → A+ (balanced homodyne readout; double-verified, arXiv:1304.0670v7, 2019-09). grav_waves rises to 3 pairs (Advanced Virgo, KAGRA, aLIGO), which is within the cap of 3. BESIII (q32) is next if needed.

### A2 log (2026-11-06)

**p15 aLIGO** and **p08 COSINE-100** are zero-unit pairs (each by author plus red-team rounds). BESIII (q32) replaced aLIGO. The eligible-but-not-selected list is exhausted, so assessment **resumes down the queue under A1**.

**Order.** The next unassessed baselines in queue order are q19 LUX, q23 Super-Kamiokande, q26 ADMX, q27 CUORE-0, q30 IceCube, q33 LZ and so on. Each is assessed by two independent daters, with the verifier as before. The first eligible baseline replaces the next zero-unit pair.

**Clarification of the caps** (fixed before any of these assessments):
- Zero-unit pairs do **not** count toward the per-field cap of 3 or the year-and-lab cap, because the caps exist to balance the units actually analysed.
- The lineage rule still applies to zero-unit pairs: their lineages are not re-entered.

**p07 MEG** is also a zero-unit pair (2026-11-06). Zero-unit pairs so far: p04, p15, p08, p07. Replacements still owed: 2, both from the resumed queue (q19 LUX and q23 Super-K are under assessment).

**p11 KAGRA** is also a zero-unit pair (2026-11-06). Zero-unit pairs: p04, p15, p08, p07, p11. Replacements owed: 3. Assessment extended to q26 ADMX, q27 CUORE-0 and q30 IceCube (two daters each), in queue order.

**p16 BESIII** is also a zero-unit pair (2026-11-06). Replacements owed: 4 (p08, p07, p11, p16).

**p06 AGATA** and **p12 MiniBooNE** are also zero-unit pairs (2026-11-06). Zero-unit pairs: p04, p15, p08, p07, p11, p16, p06, p12. Replacements owed: 6, of which 2 are filled by p17 LUX and p18 Super-K, so **4 still open** (q26, q27, q30, q34, q37 and q38 are under assessment).
