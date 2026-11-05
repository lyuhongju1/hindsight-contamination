# Pair search: how to run it

This folder holds the tool for `pair_selection_rules.md`, sections 2–4 and 9. **Run it as the research assistant**: not the PI, and with no language model in the loop.

## Steps

1. **Self-test.** `python -I inspire_search.py selftest` prints only hit counts. On 2026-11-05 the counts were: NIM A 155, JINST 120, EPJ C (instrumentation) 43, PTEP (instrumentation) 6, arXiv physics.ins-det 369. They overlap, so expect a few hundred unique records.
2. **Baselines.** `python -I inspire_search.py baselines --out runs/` writes:
   - `runs/baselines.csv`;
   - `runs/query_log.tsv`, with the exact query, UTC time and hit count;
   - the raw JSON pages in `runs/raw/`.
   Then fill in by hand:
   - `I1_instrument_paper(Y/N)`: the paper describes a constructed detector as built, not physics results or R&D;
   - `field`: one of the fields in §2.3.
3. **Upgrade documents.** `python -I inspire_search.py upgrades --baselines runs/baselines.csv --only-included --out runs/` writes `runs/upgrade_documents.csv`, listing the documents that cite each baseline and look like an LoI, CDR, TDR or TP.
   - This search is **recall-oriented and incomplete**. Also check the lab document servers named in §2.2 by hand, and log those searches in the same CSV format.
   - The hand-filled columns are: item, commitment, date, gap, I3, I4, I6, dater, confidence.
   - Each item needs two daters working independently (§6), with one CSV copy each.
4. **Draw.** Make `included.csv` with one row per pair that passed I1–I6, and columns `pair_id, field, n_primary_units`. Then run:

   `python -I inspire_search.py draw --included included.csv --frozen ../pair_selection_rules.md --per-field 3 --target-pairs 14 --out runs/`

   The seed is the SHA-256 of the frozen rules file **as it stands at the freeze**, so freeze the rules first and never edit them afterwards. The draw is round-robin over fields in alphabetical order. A test on made-up data drew 13 of 14 pairs when the field cap of 3 was binding, and logged the shortfall as intended.

## Not automated (check by hand)

- **§4 cap:** at most 2 pairs sharing a baseline year and laboratory. Apply it to `included.csv` before the draw.
- **Leakage audit (I5):** use the companion study's regex audit script on each baseline text, plus a content read by a second person.

## Notes

- Before the freeze, the frozen queries can be edited at the top of `inspire_search.py` (`BASELINE_QUERIES`, `UPGRADE_TERMS`). The freeze package includes this file's hash.
- INSPIRE syntax: `fc i` returns nothing. Use `inspire_categories.term:Instrumentation`, which is already fixed in the script.
- The script sleeps between requests to respect INSPIRE's rate limit. A full `upgrades` run over a few hundred baselines takes tens of minutes.
