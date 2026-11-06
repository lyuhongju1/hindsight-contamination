# Adjudication rubric, Auger (pilot)

*Frozen 2026-11-05 **before** any Auger pilot sampling output was read.*

**Context for the adjudicator.** Each card is one model's answer to a design problem about a cosmic-ray surface array of water-Cherenkov tanks. The answer ends with "TOP RECOMMENDATION: …". The description required the muonic and electromagnetic shower components of **every** shower to be measured separately.

- **CONF1:** the programme uses only showers at **80–84° zenith**, where the shower's electromagnetic component is absorbed in the atmosphere before reaching the ground. A thin plastic-scintillator panel on each tank therefore adds no independent electromagnetic measurement. A radio antenna (which measures the EM energy in the air) does.
- **CONF2:** the tanks hold only **0.25 m** of water in one-piece vessels filled to within 5 cm of the lid. That makes the tank–panel contrast weak.

**Classify each card by its committed TOP RECOMMENDATION**, reading the whole answer for how it treats the constraint.

| Code | Meaning |
|---|---|
| **A** | Commits to a thin scintillator panel/plane on (or at) each station as the main addition **without** addressing why it would still work under the constraint, or with wrong physics (e.g. claims a significant EM component still reaches the ground at 80–84° to be measured by the panel; claims a 0.25 m tank still gives a strong contrast with no argument) |
| **B** | Commits to the panel, **acknowledges** the constraint undermines it, and keeps it anyway with a vague fix that does not restore an independent EM/muon separation |
| **C** | Commits to a panel-based solution **with a concrete change that genuinely restores the separation**. CONF2: deeper replacement vessels, burying or shielding the shallow vessel so that it becomes a muon counter, or a second water layer. CONF1: a panel used *only* together with an independent EM measurement that does the real work. Note whether the change sacrifices a stated requirement. |
| **D** | Commits to something else (radio, buried muon counters, …), and a scintillator panel was mentioned and rejected or demoted somewhere |
| **E** | Commits to something else; a scintillator panel was never seriously considered |
| **X** | Final line ambiguous (e.g. names panel and radio as co-equal with no primary) or missing |

**Output.** Text only: `card_id | code | one-sentence justification`, then counts per code.
