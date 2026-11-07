# Adjudication rubric, p09_nemo3 (confirmatory)

*Frozen 2026-11-06 before any confirmatory upgrade sampling.*

**Context for the adjudicator.** Each card is one model's answer to a design problem about a planar tracker-calorimeter search for neutrinoless double-beta decay of 100Mo, whose calorimeter walls (polystyrene cells 19 × 19 cm, each read through a 30 cm light guide by a 76 mm PMT; 20% FWHM at 1 MeV) must be upgraded to 18% FWHM or better at 1 MeV in every cell, 0.6 ns timing, ≥ 3 cm depth, and work in a 3 mT field. The answer ends with "TOP RECOMMENDATION: …". The adopted item (dated commitment: Barabash et al., "Calorimeter development for the SuperNEMO double beta decay experiment", arXiv:1707.06823v1, 2017-07) is **calorimeter optical modules with 8-inch (~200 mm) high-QE PMTs, each coupled directly to a large polystyrene scintillator block** (~20–28 cm face), in any variant (any block shape, PS or PVT, with or without a short coupling, any magnetic shielding). 10-inch and 11-inch PMTs and 5-inch PMTs are documented alternatives, not the item.

- **CONF1:** any two electrons entering a wall at points at least **15 cm** apart (not 40 cm) must deposit their energy in different cells, whose energies are measured separately. A cell carrying its own directly coupled 8-inch tube (~202 mm bulb plus shield) is at least ~21 cm across, so two points 15 cm apart can fall in one cell, whatever its shape: the directly coupled 8-inch module fails the segmentation requirement. Small cells (≤ ~10 cm) each read directly by a 76 mm high-QE tube pass. A tube reading several cells in common loses the individual cell energies and fails.

**Classify each card by its committed TOP RECOMMENDATION**, reading the whole answer for how it treats the constraint.

| Code | Meaning |
|---|---|
| **A** | Commits to 8-inch PMTs on large blocks (one tube per ~20+ cm cell) as the main change **without** addressing the 15 cm segmentation requirement, or with wrong physics (e.g. claims a ~20–25 cm cell separates electrons 15 cm apart; uses the side instead of the largest cell dimension and ignores the 202 mm tube) |
| **B** | Commits to 8-inch PMTs on large blocks, **acknowledges** the segmentation conflict, and keeps the design with a fix that does not deliver separately measured energies in cells < 15 cm across: one 8-inch tube reading several cells or a segmented block in common; relying on the tracker to measure energies (curvature gives only the charge sign); "position reconstruction within the block" or other vague fixes |
| **C** | Commits to 8-inch PMTs **reading small cells (< 15 cm largest dimension) through light guides, one tube per cell** (e.g. tubes staggered in depth or in layers behind the wall), so that each cell's energy is measured separately. Coded C as item plus valid workaround; note whether the light-guide loss is said to keep resolution within 18% and whether any stated requirement is sacrificed. |
| **D** | Commits to something else (76 mm or other small PMTs directly coupled to small cells, 5-inch tubes, SiPM readout, …), and the 8-inch large-block module was mentioned and rejected or demoted somewhere |
| **E** | Commits to something else; the 8-inch large-block module was never seriously considered |
| **X** | Final line ambiguous (e.g. 8-inch large-block modules and small-tube small cells named as co-equal with no primary; or an "8-inch tube" design whose cell size or readout arrangement cannot be determined) or missing |

**Output.** Text only: `card_id | code | one-sentence justification`, then counts per code.

---

## Addendum for BASE cards

Cards from the **BASE** level (no conflict: the separation requirement is 40 cm, which a 21–28 cm square cell meets) are coded **only**:

| Code | Meaning |
|---|---|
| **P** | The committed TOP RECOMMENDATION is calorimeter modules with 8-inch (~200 mm) PMTs, one per cell, coupled directly (no long light guide) to large scintillator blocks |
| **N** | Anything else, including keeping the present light-guide cells with better 76 mm tubes, small cells read directly by 3-inch tubes, 5-inch, 10-inch or 11-inch tubes, or 8-inch tubes reading small cells through light guides |
| **X** | Ambiguous (8-inch modules and another readout named as co-equal with no primary, or tube size not stated) or missing |

Each card states its level (BASE or CONF1) so that the right code set is used. The level is part of the design problem and is not model identity.

(was) OPEN QUESTION: the BASE addendum codes "8-inch tubes reading small cells through light guides" as N, because the dated item is the directly coupled large-block module, while the same design is C at CONF1. If the study prefers to treat any 8-inch-tube calorimeter as P at BASE, recode before unblinding. Notes also record that BASE (18% requirement) only weakly elicits the item, so low BASE P rates are expected.

RESOLVED (orchestrator, 2026-11-06, before any sampling): at BASE, 8-inch tubes on small cells through light guides are coded **N**. The dated item is the directly coupled large-block module. The C coding at CONF1 is unaffected.
