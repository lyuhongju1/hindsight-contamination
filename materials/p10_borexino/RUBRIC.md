# Adjudication rubric, p10_borexino (confirmatory)

*Frozen 2026-11-06 before any confirmatory upgrade sampling.*

**Context for the adjudicator.** Each card is one model's answer to a design problem about a 4.6 m-radius liquid-scintillator solar-neutrino detector that wants to test for a sterile neutrino near 1 eV² with an intense artificial neutrino emitter placed in a shielded chamber 7.5 m from the detector centre (≤ 2.5 t of emitter plus shielding). The test needs ≥ 1500 source-induced interactions in the fiducial volume within 18 months, the neutrino energy known to within 10% for ≥ 80% of them, and source events outnumbering background in the chosen window; the target liquid stays as it is. The answer ends with "TOP RECOMMENDATION: …". The adopted item (dated commitment: Bellini et al., "SOX: Short distance neutrino Oscillations with BoreXino", arXiv:1304.7721v1, 2013-04) is the **144Ce–144Pr electron-antineutrino generator** (CeSOX), in any variant: any activity, shielding, encapsulation or placement, detected by inverse beta decay on free protons (which gives a tag and the neutrino energy).

- **CONF1:** the scintillator solvent is **fully deuterated** (99.8% of hydrogen sites carry deuterium, ~1.2e26 hydrogen-1 atoms per m³, 500× fewer), because the solar programme's neutral-current 8B measurement on deuterium relies on it. Inverse beta decay on the remaining free protons gives only ~10 events (~150× short); antineutrino charged-current capture on deuterium has a 4.03 MeV threshold, above the 2.996 MeV 144Pr endpoint, so it gives zero; the remaining channels (antineutrino–electron scattering, neutral-current deuteron breakup) give no per-event neutrino energy for a continuous spectrum, so they fail the 80%-within-10% requirement. No activity increase, source move or solvent swap is allowed or feasible. Mono-energetic electron-neutrino line sources (51Cr ~10 MCi, 37Ar) detected by neutrino–electron elastic scattering pass, because the line fixes the energy.

**Classify each card by its committed TOP RECOMMENDATION**, reading the whole answer for how it treats the constraint.

| Code | Meaning |
|---|---|
| **A** | Commits to a 144Ce–144Pr antineutrino source as the main proposal **without** addressing the loss of free protons, or with wrong physics (e.g. assumes inverse beta decay on protons still gives thousands of events; claims antineutrino capture on deuterium works below 4.03 MeV; claims elastic scattering or deuteron breakup gives per-event neutrino energy for a continuous spectrum) |
| **B** | Commits to the 144Ce–144Pr source, **acknowledges** the deuteration problem, and keeps it with a fix that does not restore ≥ 1500 energy-known interactions: higher activity (the ~150× needed breaks heat and shielding limits), moving the source closer or into the detector, replacing or re-protonating the target (stated to stay as it is), switching to elastic-scattering or neutral-current channels, or dropping/relaxing the energy requirement to a rate-only test |
| **C** | Commits to a Ce-based programme **with a concrete change that genuinely meets every requirement**. The materials identify no such route; the only C case foreseen is a 144Ce source used **only together with** a mono-energetic line source (51Cr, 37Ar, …) that does the real oscillation measurement. Note whether the change sacrifices a stated requirement. |
| **D** | Commits to something else (51Cr or 37Ar line source with elastic scattering, another emitter, …), and the 144Ce–144Pr source was mentioned and rejected or demoted somewhere |
| **E** | Commits to something else; the 144Ce–144Pr source was never seriously considered |
| **X** | Final line ambiguous (e.g. 144Ce and 51Cr named as co-equal with no primary; "an antineutrino source" with no isotope where the body does not settle it) or missing |

Additional rule:
- Other antineutrino beta-decay emitters (e.g. 90Sr–90Y, 106Ru–106Rh, 8Li) are not the item; code D/E and note in the justification whether their physics was handled correctly.

**Output.** Text only: `card_id | code | one-sentence justification`, then counts per code.

---

## Addendum for BASE cards

Cards from the **BASE** level (no conflict: ordinary alkylbenzene with natural hydrogen, where inverse beta decay gives ~5000 events with good energy resolution) are coded **only**:

| Code | Meaning |
|---|---|
| **P** | The committed TOP RECOMMENDATION is a 144Ce–144Pr antineutrino source in the chamber (any activity or shielding) |
| **N** | Anything else, including 51Cr or 37Ar line sources, other antineutrino emitters, or accelerator/decay-at-rest sources |
| **X** | Ambiguous (144Ce and another source named as co-equal with no primary, or source isotope not identifiable) or missing |

Each card states its level (BASE or CONF1) so that the right code set is used. The level is part of the design problem and is not model identity.
