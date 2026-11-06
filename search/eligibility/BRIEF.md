# Eligibility assessor and dater: brief

You assess whether a baseline instrument can supply a confirmatory item, under `pair_selection_rules.md` (criteria I2–I4 and I6) and the dating protocol (§6). You work alone; another assessor works on the same baselines independently, and you must not try to coordinate.

**Inputs:** one candidate file per assigned baseline, `search/eligibility/candidates/qNN_<recid>.json`. Each holds the baseline record plus the INSPIRE documents that cite it and look like upgrade documents. The list may be incomplete: if it is empty or thin, search INSPIRE and arXiv yourself (and lab servers such as CERN CDS if needed).

## Definitions (from the frozen rules)

| Term | Definition |
|---|---|
| Baseline date | the baseline record's `date` field |
| Item | a specific **hardware or technology choice** adopted by the baseline's upgrade program (or a declared successor detector of the same collaboration) that was absent from the baseline as built. Not names, schedules or mere scale-ups |
| First public adoption commitment | the earliest public document in which the **collaboration** proposes the item **for this program**: LoI, CDR, TDR, technical proposal, collaboration paper or approved proposal. Not the invention of the technology, not R&D-only studies, not outsiders' proposals |

## Criteria per item (all must hold)

| Criterion | Requirement |
|---|---|
| **I2** | Commitment date ≥ **24 months** after the baseline date |
| **I3** | Hardware or technology choice |
| **I4** | At least one plausible alternative to the item existed at the commitment date and was **not** adopted, with a citation |
| **I6** | Commitment date ≤ **2023-06-30** |

## Task, per baseline

1. Identify the baseline's upgrade program(s) and up to **two** candidate items that satisfy I2–I4 and I6. Prefer items whose failure could be forced by a stated **physical** constraint (rate, fluence, energy band, composition, temperature, geometry…), and note one such constraint idea in a few words. This is only a hint for later authors.
2. For each item, find the first public adoption commitment and give a **dating claim**:
   - the document as `arXiv:<id>` or `inspire:<recid>` (it must have an arXiv full text);
   - a **verbatim quote**, copied exactly from that document's text (one or two sentences), showing that the collaboration proposes the item for this program. A script will fetch the document and check the quote character by character, and claims that fail are discarded, so copy exactly.
3. If no item qualifies, state which criterion fails.

## Output

Text only. Do not write files.

For each baseline, a short block followed by a JSON array of dating claims:

```
BASELINE qNN <recid> — <title>
items:
 1. <item, one line> | commitment <YYYY-MM> | gap <months> | alternative not adopted: <name> (<citation>) | conflict idea: <few words>
 2. ...
verdict: ELIGIBLE (items 1[,2]) | NOT ELIGIBLE (<criterion>: <reason>)
CLAIMS_JSON
[{"item":"<recid>/<short_item_slug>","dater":"<your dater id>","doc":"arXiv:XXXX.XXXXX","quote":"<verbatim>","baseline_date":"<baseline date>"}]
END_CLAIMS
```

## Limits

- At most **8 web fetches per baseline**.
- If a tool call is denied, do not work around it: stop and report it.
- Do not open project files other than your candidate files and this brief.
