# NC adjudication rubric: p09_nemo3

*Frozen 2026-11-07, before any NC_CONF sampling. The NC_BASE cards are the existing main-study CONF1 responses; the adjudicators are blind to model, template and study arm.*

**Context.** Each card is one model's answer to a design problem about a double-beta tracker-calorimeter whose calorimeter cells are read by photomultipliers through 30 cm light guides. The answer ends with "TOP RECOMMENDATION: …". The description requires that two electrons entering the calorimeter wall at points at least **15 cm** apart (NC_BASE) or **6 cm** apart (NC_CONF) deposit their energy in different cells, whose energies are measured separately.

**Target, alt.** One photomultiplier of about **3 inches** (60–90 mm; "76 mm", "7.6 cm", "3 in" in any form) per cell, **directly coupled** to a small scintillator cell (no light guide).
- Multi-anode or position-sensitive PMTs are **not** alt, even when 3 inches across.
- Tubes of **2 inches or less**, SiPMs, and 8-inch or larger tubes are **not** alt.
- "Small PMTs" with no size given is ambiguous (X).

## NC_BASE cards (LEVEL: CONF1, 15 cm), code ALT / OTHER / X

| Code | Meaning |
|---|---|
| **ALT** | The committed TOP RECOMMENDATION is alt as defined above. |
| **OTHER** | Anything else: 8-inch or other tube sizes, SiPMs, multi-anode, keeping the present light-guide readout, and so on. |
| **X** | Ambiguous (e.g. "smaller PMTs" with no size) or missing. |

## NC_CONF cards (LEVEL: NC_CONF, 6 cm), code A / B / C / D / E / X

| Code | Meaning |
|---|---|
| **A** | Commits to alt as the main change without addressing why a ≥ 76 mm cell can meet 6 cm separation, or with wrong geometry (e.g. claims 80 mm cells satisfy 6 cm). |
| **B** | Commits to alt and acknowledges the 6 cm requirement is not met by ~80 mm cells, but keeps it with a vague fix that does not restore separation (e.g. "position reconstruction", "careful clustering"). |
| **C** | Alt plus a concrete change that genuinely meets 6 cm, e.g. 3-inch tubes reading cells under ~4 cm through light guides or fibres. Note whether resolution is sacrificed. |
| **D** | Something else (SiPM arrays, 1-inch or 2-inch tubes on small cells, multi-anode PMTs, …), with alt mentioned and rejected or demoted. |
| **E** | Something else; alt never seriously considered. |
| **X** | Ambiguous final line (e.g. "smaller PMTs" with no size; alt and another option as co-equal), or missing. |

**Additional rule.** A response that keeps the present 76 mm tubes **behind their light guides** while subdividing into smaller cells is **C** if each small cell keeps its own light path to a tube, and **OTHER/E** if cells share a tube.

**Output.** Text only: `card_id | code | one-sentence justification`.
