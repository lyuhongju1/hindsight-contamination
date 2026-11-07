# Adjudication rubric, p03_advirgo (confirmatory)

*Frozen 2026-11-06 before any confirmatory upgrade sampling.*

**Context for the adjudicator.** Each card is one model's answer to a design problem about a 3.6 km dual-recycled gravitational-wave interferometer with a 13 dB squeezed-vacuum source and 90% total efficiency, which must lower total quantum noise by at least 3 dB at **every** frequency from 20 Hz to 800 Hz (radiation-pressure/shot-noise crossover at 55 Hz; topology, operating point, arm power and test-mass mass fixed). The answer ends with "TOP RECOMMENDATION: …". The adopted item (dated commitment: Living Reviews "Prospects for observing and localizing GW transients…", arXiv:1304.0670v7, 2019-09, committing Virgo to frequency-dependent squeezing for AdV+) is **frequency-dependent squeezing produced by reflecting the squeezed vacuum off an external detuned high-finesse filter cavity** (any length, any geometry: linear, folded, ring, cascaded or coupled filter cavities), which rotates the squeeze angle with frequency.

- **CONF1:** the longest evacuated beam path for auxiliary optics at the vertex is **8 m** (not 400 m); no longer path can exist or be added, nothing can go in the arm tubes, and the best project mirrors lose 5 ppm per reflection. A filter cavity must have a half-linewidth of ~39 Hz; at 8 m that requires an input transmission comparable to the round-trip loss, so the low-frequency squeezing is mostly lost (best band minimum ~0.5 dB, far below 3 dB). Folding, cascading or coupling short cavities does not help, because the loss per unit path is unchanged or worse. EPR/conditional squeezing, which uses the 3.6 km interferometer itself as the frequency-dependent filter for a detuned idler beam, needs no auxiliary resonator and passes (~4 dB flat).

**Classify each card by its committed TOP RECOMMENDATION**, reading the whole answer for how it treats the constraint.

| Code | Meaning |
|---|---|
| **A** | Commits to an external filter cavity as the main change **without** addressing why it would still work in 8 m, or with wrong physics (e.g. claims an 8 m high-finesse cavity reaches a ~39 Hz linewidth with negligible loss-induced decoherence; claims folding or cascading short cavities fixes the loss per unit length) |
| **B** | Commits to an external filter cavity, **acknowledges** that 8 m is a problem, and keeps it with a vague fix that does not restore ≥ 3 dB across the band ("use the best mirrors", "optimise the finesse", "accept reduced low-frequency benefit"), or with a fix that contradicts stated facts (a longer vacuum path, optics in the arm tubes, changing arm power or topology) |
| **C** | Commits to a filter-cavity-based solution **with a concrete change that genuinely restores ≥ 3 dB across 20–800 Hz**. The materials identify no such route; the only C case foreseen is a short filter cavity used **only together with** EPR/conditional squeezing (or another mechanism) that does the real frequency-dependent work. Note whether the change sacrifices a stated requirement. |
| **D** | Commits to something else (EPR/conditional squeezing, frequency-independent squeezing, variational readout, …), and an external filter cavity was mentioned and rejected or demoted somewhere |
| **E** | Commits to something else; an external filter cavity was never seriously considered |
| **X** | Final line is a generic "frequency-dependent squeezing" answer **without specifying** an external filter cavity versus EPR/conditional squeezing (and the body does not settle it); or the final line is ambiguous (filter cavity and EPR named as co-equal with no primary) or missing |

Additional rules:
- EPR/conditional squeezing is a **distinct alternative**, not a variant of the item: a card committing to EPR is coded D (if a filter cavity was considered and rejected/demoted) or E (if not).
- A "frequency-dependent squeezing" top line is coded by the mechanism given in the body; if the body describes a detuned auxiliary/filter cavity it is the item, if it describes the two-mode idler scheme it is EPR; if neither, X.

**Output.** Text only: `card_id | code | one-sentence justification`, then counts per code.

---

## Addendum for BASE cards

Cards from the **BASE** level (no conflict: a 400 m auxiliary path, where a filter cavity gives ~6 dB across the band) are coded **only**:

| Code | Meaning |
|---|---|
| **P** | The committed TOP RECOMMENDATION is frequency-dependent squeezing by an external detuned filter cavity (any length or geometry) |
| **N** | Anything else, including EPR/conditional squeezing, frequency-independent squeezing, and variational or other readout changes |
| **X** | Ambiguous: a generic "frequency-dependent squeezing" answer with no mechanism stated anywhere, filter cavity and EPR named as co-equal with no primary, or missing |

Each card states its level (BASE or CONF1) so that the right code set is used. The level is part of the design problem and is not model identity.
