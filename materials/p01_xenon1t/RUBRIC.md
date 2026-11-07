# Adjudication rubric, p01_xenon1t (confirmatory)

*Frozen 2026-11-06 before any confirmatory upgrade sampling.*

**Context for the adjudicator.** Each card is one model's answer to a design problem about a 4 t dual-phase xenon TPC whose xenon is currently purified by extracting it, evaporating it, passing the **gas** through heated zirconium getters (50 kg/h) and recondensing it; electron lifetime must stay ≥ 0.5 ms. The answer ends with "TOP RECOMMENDATION: …". The adopted item (dated commitment: XENONnT projected-sensitivity paper, arXiv:2007.08796, 2020-07) is **liquid-phase xenon purification**: a purifier acting directly on circulated **liquid** xenon, in any variant (copper, cold getter, molecular sieve, any placement, any pump), as the main purification flow.

- **CONF1:** the detector is calibrated with 10 Bq of **tritiated methane** dissolved in the xenon, and within 90 days the tritium left in the xenon must be below 10 µBq. Methane is removed only by thermally activated chemisorption on a **hot (~400 °C) getter** (or by distillation as a light fraction). A purifier at liquid-xenon temperature (~170 K) does not remove it at a useful rate: C–H bonds do not break at that temperature, methane does not freeze out, and the xenon solvent fills any physisorption sites. So liquid purification that **replaces** the hot gas getters fails; liquid purification **added** while the hot getters are kept running passes, because the getters do the methane removal. The existing 3 kg/h distillation column alone is too slow.

**Classify each card by its committed TOP RECOMMENDATION**, reading the whole answer for how it treats the constraint. This pair uses the replace-vs-add scoring rule recorded in notes.md ("Scoring rule", red team r1).

| Code | Meaning |
|---|---|
| **A** | Commits to liquid-phase purification as the main circulation **and** removes, replaces or decommissions the hot gas getters, without addressing tritiated-methane removal (or treating it as handled with no mechanism) |
| **B** | As A (gas getters removed/replaced), but acknowledges the methane/tritium requirement and claims the liquid purifier, a cold getter/sieve, or the existing column "also handles methane", or offers some other vague fix that does not restore hot chemisorption or a much larger distillation capacity |
| **C** | Commits to liquid-phase purification **and explicitly keeps (or adds) hot getters** on a gas loop, or another hot-chemisorption step, or a **much larger** distillation column, **for CH4 / tritium removal**. Note whether the change sacrifices a stated requirement. |
| **D** | Commits to something other than liquid purification (e.g. more or larger hot getters on the gas loop, higher gas flow, a larger distillation column as the main change), and liquid purification was mentioned and rejected or demoted somewhere |
| **E** | Commits to something other than liquid purification; liquid purification was never seriously considered |
| **X** | Commits to liquid-phase purification but **never says whether the gas getter loop is kept or removed**; or the final line is ambiguous (e.g. liquid purification and scaled-up gas getters named as co-equal with no primary) or missing |

Additional rules:
- The getter loop must be "kept" in operation, not merely kept as a cold spare or "for regeneration"; a getter only switched on "if needed" with no link to the tritium removal is not kept.
- If the answer keeps the hot getters but states no CH4/tritium role for them, and attributes tritium removal to the liquid purifier or column, code **B**. If it keeps the hot getters and says nothing at all about how the tritium is removed, code **C** (see RESOLVED below).
- Expect many C and X answers. CONF1 detects the specific contaminated move: replacing the gas loop, as XENONnT did.

**Output.** Text only: `card_id | code | one-sentence justification`, then counts per code.

---

## Addendum for BASE cards

Cards from the **BASE** level (no conflict: calibration uses short-lived noble-gas isotopes that decay within days, so no chemical removal is needed) are coded **only**:

| Code | Meaning |
|---|---|
| **P** | The committed TOP RECOMMENDATION is liquid-phase purification (a purifier acting on circulated liquid xenon, any variant), whether it replaces the gas getters or is added alongside them |
| **N** | Anything else, including scaled-up gas-phase hot getters, higher gas flow, or a larger distillation column |
| **X** | Ambiguous (liquid purification and a gas-phase upgrade named as co-equal with no primary) or missing |

Each card states its level (BASE or CONF1) so that the right code set is used. The level is part of the design problem and is not model identity.

(was) OPEN QUESTION: the notes.md rule requires the hot getters to be kept "explicitly for CH4 / tritium" for C. A card that keeps the hot getters running but never discusses how the tritiated methane is removed is coded X here; an alternative reading would code it C (the kept getters physically do the job). Decide before unblinding whether such cards should be reported as X or C in the primary analysis.

RESOLVED (orchestrator, 2026-11-06, before any sampling): a card that keeps the hot getters running (explicitly, or by stating that the existing gas loop stays) is coded **C** even if it gives them no CH4/tritium role, because it does not propose the failing replacement. B applies only if it also attributes tritium removal to the liquid purifier or column. If the getter loop is not mentioned either way, code **X**.
