# Expert panel instrument (draft)

*For design v2 §4.3, gate 1. Administer as an online form (Qualtrics, REDCap, or a static form), one problem per page. Panelists never see model output, the study hypotheses, or which problems are derived from real instruments.*

---

## Structure of one panelist's packet

| Block | Content | Count |
|---|---|---|
| A | Consent and instructions | 1 |
| B | Design problems, in randomized order | ~12–16 per panelist |
|   | — equivalent twins (EQ) | ~5 |
|   | — conflict twins (CONF) | ~3 |
|   | — abstract twins (ABS) | ~2 |
|   | — unnamed real descriptions (ANON), for the expert–history agreement measure | ~2 |
|   | — **filler problems** (invented instruments not derived from any study pair, with expert-chosen answers) | ~3 |
| C | Recognition questions, asked **after** all of block B is locked | one per problem |
| D | Background and debrief | 1 |

- **Session length:** keep each panelist under about 2.5 hours. Split into two sessions if needed.
- **Allocation:** each twin is rated by 5 panelists from its field. A panelist never sees both an ANON description and a twin of the same pair, so the real instrument cannot leak into the twin rating.

---

## Block A — Instructions (verbatim draft)

> You will see short descriptions of physics instruments and the constraints they operate under. Some are invented. For each, imagine you are on the design review for its next upgrade. Answer from the physics as stated. If a description differs from instruments you know, follow the description.
>
> There are no trick questions, and we are not testing you. We need your professional judgement about which upgrades the stated physics favours. Please do not search the web or consult colleagues while answering.

---

## Block B — Per problem

**Problem text:** the frozen description, exactly as models will see it (without the model-facing template).

**B1. Open proposals.** "List up to three hardware upgrades you would recommend most strongly for this instrument's next phase, in order. One line each."

- Free text. Answer locked before B2 appears.
- This gives the human analogue of the model task, scored with the same rubric as model responses (secondary analysis: the human proposal rate).

**B2. Candidate rating.** Show 4–6 candidate upgrades in randomized order:

- the historical choice;
- the keyed alternative (for CONF problems);
- the pair's two distractors;
- one or two plausible fillers.

For each candidate, ask:

> "Given the stated physics, this upgrade is: **best option / co-best / acceptable but inferior / clearly wrong / can't judge**."

**B3. Conflict check** (CONF problems only, asked of every problem so as not to reveal which ones are CONF):

> "Is there anything in the stated constraints that would make any of the candidates above a poor choice? If yes, which, and why?"

**B4. Confidence.** "How confident are you in your B2 ratings?" (1–5)

### Inclusion rules (applied to B2; from design v2 §4.3)

- **Equivalent and abstract twins:** ≥ 4 of 5 panelists rate the historical choice *best* or *co-best*.
- **Conflict twins:**
  - ≥ 4 of 5 rate the keyed alternative *best* or *co-best*; **and**
  - ≥ 4 of 5 rate the historical choice *acceptable but inferior* or *clearly wrong*.
- "Can't judge" counts as non-agreement.
- **Reported:** Fleiss' κ per field and overall; expert–history agreement on the ANON problems; and the full rating distribution for every twin, including twins that failed.

---

## Block C — Recognition (after block B is locked)

For every problem seen:

> "Did this description remind you of a real instrument? If yes, which one, and how sure are you (1–5)?"

This gives a **human identifiability rate** for each twin, as a check on the model identification probe (design v2 §5). If experts often recognize a twin, its expert rating may be anchored on history. Such twins are flagged, and the sensitivity of the results to excluding them is reported.

---

## Block D — Background

- Subfield(s), and years of experience in detector design.
- Membership, past or present, of any collaboration on a list shown here. The list covers all study pairs and is displayed only at this point.
- "Did you recognise any problem as a disguised version of a real experiment *while answering block B*?" (Y/N, which).
- Debrief: the purpose of the study, revealed now.

---

## Scoring and data handling

- Free-text B1 answers are scored by two coders blind to which problems are which, using the frozen rubric.
- Responses are stored without names, under a panelist ID. The key linking IDs to names is kept separately and is used only for honoraria.
- Panelists are acknowledged by name only with their opt-in consent.

## Logistics to settle

- **Panel size:** 5 per field across ≥ 5 fields means ~25–30 panelists. If recruitment falls short, the pre-registered fallback is 3 panelists with **unanimous** agreement.
- **Honorarium:** suggest a flat fee per completed packet. Budget it before the IRB submission.
- **Pilot:** run the instrument on 2 colleagues with the pilot pairs. Time it, and check that the fillers are indistinguishable from twins.
