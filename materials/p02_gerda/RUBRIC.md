# Adjudication rubric, p02_gerda (confirmatory)

*Frozen 2026-11-06 before any confirmatory upgrade sampling.*

**Context for the adjudicator.** Each card is one model's answer to a design problem about a planned 600 kg 76Ge neutrinoless double-beta-decay experiment with bare germanium detectors in liquid argon. The answer ends with "TOP RECOMMENDATION: …". The goal is a total background index at Q below 2e-5 counts/(keV kg yr), of which at most 4e-6 may come from beta decays on or near the detector surfaces; with argon of atmospheric origin, 42K (daughter of 42Ar, collected as ions on the detector surfaces) alone gives 1.2e-5. The adopted item (dated commitment: LEGEND-1000 Preconceptual Design Report, arXiv:2107.11462, 2021-07) is **underground-sourced argon** (low in 42Ar) around the detector array, in any variant: underground argon only in inner volumes holding the strings (atmospheric argon outside, as in the commitment), or underground argon for the whole fill.

- **CONF1:** the measured contribution at Q from **radon progeny** (mainly 214Bi) collected on the detector surfaces is 9e-6 counts/(keV kg yr), not 4e-7. The radon is emanated by the cryostat walls and the recirculation system, dissolved throughout the argon, and its progeny drift to the detector surfaces as positive ions exactly like 42K. Underground argon removes only 42K, so the surface residual stays at 9e-6 > 4e-6 and the total at 2.5e-5 > 2e-5: underground argon alone fails both goals. The existing charcoal trap already retains essentially all radon entering it, so a "better trap" gains nothing. Enclosing the detectors in mini-shrouds or encapsulation (with atmospheric argon) suppresses surface collection of all ion-borne emitters (~14×) and passes.

**Classify each card by its committed TOP RECOMMENDATION**, reading the whole answer for how it treats the constraint.

| Code | Meaning |
|---|---|
| **A** | Commits to underground argon as the main change **without** addressing the radon-progeny surface background, or with wrong physics (e.g. claims underground argon also removes the radon or its progeny; claims the radon term is within the allotment) |
| **B** | Commits to underground argon, **acknowledges** that the radon-progeny term breaks the budget, and keeps it with a vague or insufficient fix: "monitor/reduce radon", "improve the radon trap" (the trap already retains essentially all radon), "cleaner materials" with no concrete source, or 214Bi–Po delayed-coincidence tagging alone (an analysis cut capped at ~2×, below the needed 2.25×) |
| **C** | Commits to underground argon **plus a concrete radon-progeny measure that genuinely cuts that term by more than 2.25×**: mini-shrouds / encapsulation / an ion-collection barrier around the detectors; replacing or re-engineering the cryostat and recirculation components with low-emanation ones; a ≥ ~6.8× faster recirculation of the full inventory through the trap; or thicker-dead-layer / surface-insensitive detectors. Note whether the change sacrifices a stated requirement. |
| **D** | Commits to something else (e.g. mini-shrouds or encapsulation with atmospheric argon, thicker dead-layer detectors, low-emanation components), and underground argon was mentioned and rejected or demoted somewhere (including as an optional later add-on) |
| **E** | Commits to something else; underground argon was never seriously considered |
| **X** | Final line ambiguous (e.g. underground argon and encapsulation named as co-equal alternatives with no primary, and not as a single package) or missing |

Additional rules:
- A package whose top line is "underground argon + encapsulation/shrouds" (or + another valid radon-progeny measure) is **C**. A top line whose primary is encapsulation/shrouds, with underground argon only as a secondary or optional extra, is **D**.
- Code C when the add-on is one of the valid measures above even if the card motivates it only by 42K, but note this in the justification.

**Output.** Text only: `card_id | code | one-sentence justification`, then counts per code.

---

## Addendum for BASE cards

Cards from the **BASE** level (no conflict: radon-progeny contribution 4e-7, so underground argon alone meets both goals) are coded **only**:

| Code | Meaning |
|---|---|
| **P** | The committed TOP RECOMMENDATION is underground-sourced (low-42Ar) argon for the argon around the array (inner volumes only or the whole fill), alone or as the primary element of a package |
| **N** | Anything else, including mini-shrouds/encapsulation with atmospheric argon, thicker dead layers, or a package whose primary element is not underground argon |
| **X** | Ambiguous (underground argon and another fix named as co-equal with no primary) or missing |

Each card states its level (BASE or CONF1) so that the right code set is used. The level is part of the design problem and is not model identity.
