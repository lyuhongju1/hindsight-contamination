# Adjudication rubric, p05_sno (confirmatory)

*Frozen 2026-11-06 before any confirmatory upgrade sampling.*

**Context for the adjudicator.** Each card is one model's answer to a design problem about an underground water-Cherenkov neutrino detector (520 t of water in a 10 m acrylic sphere immersed in shield water, 6,800 PMTs, 12% photon collection) whose next programme needs at least 400 photoelectrons per MeV inside the sphere, so the water must be replaced by a liquid scintillator. The answer ends with "TOP RECOMMENDATION: …". The adopted item (dated commitments: SNO+ papers arXiv:0810.3694, 2008-10, and arXiv:1405.3401, 2014-05) is **linear alkylbenzene (LAB) liquid scintillator** as the fill of the sphere, in any variant: any fluor (PPO etc.), any wavelength shifter, any loading, provided LAB is at least 50% of the fill by volume. A fill with less than 50% LAB by volume is not the item.

- **CONF1:** the sphere wall is **1 cm** thick (not 5 cm) and, counting its own weight, withstands a net vertical load of at most **60 kg per cubic metre** of contained volume, **however the sphere is restrained**. LAB (~0.86 g/cm³) is ~140 kg/m³ lighter than the surrounding water, so the buoyant load (~139 kg/m³) is more than twice the limit. Hold-down ropes, nets or ballast do not help, because the limit holds for any restraint (this closes the real detector's rope-net solution). A denser scintillator such as PXE (~0.985 g/cm³, deficit ~15 kg/m³) passes; water-based liquid scintillator meets the load limit but fails the light requirement.

**Classify each card by its committed TOP RECOMMENDATION**, reading the whole answer for how it treats the constraint.

| Code | Meaning |
|---|---|
| **A** | Commits to an LAB fill as the main change **without** addressing the buoyant load, or with wrong physics (e.g. claims LAB is close to water density; claims the load is within 60 kg/m³) |
| **B** | Commits to an LAB fill, **acknowledges** the buoyancy/load problem, and keeps it with a fix that does not genuinely meet the limit: hold-down ropes, a net, ballast or any other restraint (closed by "however the sphere is restrained"); a partial fill or inner bag; temperature control; changes to the shield water or the retained hardware; or "engineering margin"/"reinforce the sphere" with no physical route |
| **C** | Commits to LAB (≥ 50% by volume, or described as the base solvent) **plus a density-raising co-solvent or additive used to reduce the buoyant load** (e.g. a heavy aromatic such as 1-methylnaphthalene, 1-chloronaphthalene, benzyl benzoate, or a dense additive). Coded C as item plus workaround; note in the justification whether the stated blend plausibly reaches ~0.94 g/cm³ or denser, and whether it sacrifices a stated requirement (e.g. light yield). |
| **D** | Commits to something else (PXE, pseudocumene, water-based liquid scintillator, a fill with < 50% LAB such as a 30/70 LAB/1-methylnaphthalene blend, …), and LAB was mentioned and rejected or demoted somewhere |
| **E** | Commits to something else; LAB was never seriously considered |
| **X** | Final line ambiguous (e.g. LAB and PXE named as co-equal with no primary) or missing; or an LAB blend whose LAB fraction cannot be determined and in which LAB is not described as the base solvent |

**Output.** Text only: `card_id | code | one-sentence justification`, then counts per code.

---

## Addendum for BASE cards

Cards from the **BASE** level (no conflict: 5 cm wall, 300 kg/m³ load limit, so LAB's ~140 kg/m³ deficit is acceptable) are coded **only**:

| Code | Meaning |
|---|---|
| **P** | The committed TOP RECOMMENDATION is an LAB-based liquid scintillator fill (≥ 50% LAB by volume, any fluor, shifter, loading or restraint) |
| **N** | Anything else, including PXE, pseudocumene, water-based liquid scintillator, and fills with < 50% LAB |
| **X** | Ambiguous (LAB and another scintillator named as co-equal with no primary, or LAB fraction undeterminable) or missing |

Each card states its level (BASE or CONF1) so that the right code set is used. The level is part of the design problem and is not model identity.

(was) OPEN QUESTION: the r2 study decision codes "LAB plus a density-raising co-solvent or additive" as C "whatever its LAB fraction", while the r1 grading rule (kept in notes.md) says a fill with < 50% LAB is not the adopted item. This rubric applies the 50% threshold (a < 50% LAB blend is D/E, not C). If the study intends the r2 wording literally, < 50% LAB densified blends should be recoded C before unblinding.

RESOLVED (orchestrator, 2026-11-06, before any sampling): the 50% threshold stands. A fill with < 50% LAB is not the adopted item (D/E), whether or not it is densified. The r2 phrase 'whatever its LAB fraction' referred to fills of >= 50% LAB, which with a densifier are **C**.
