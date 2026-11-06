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
