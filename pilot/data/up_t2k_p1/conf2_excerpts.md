### claude-opus-5-5 | T2_instrument
COUNTED-AS-PROPOSAL sentences: ['The obvious modern choice is a finely segmented plastic-scintillator target (a SuperFGD-style 3D cube array) plus high-angle TPCs.']
HYDROGEN sentences: ['It fails the hydrogen requirement:', '- In polystyrene (CH)ₙ, hydrogen is 1 of every 13 nucleons, about **7.7%**.', 'The 2% limit therefore forces a hydrogen-free *target medium*.', 'Hydrogen may appear only in thin structural and readout materials.']

### claude-opus-5-5 | T5_plain
COUNTED-AS-PROPOSAL sentences: ['The obvious choice would be a fine-grained plastic scintillator target like SuperFGD.']
HYDROGEN sentences: ['# Proposed upgrade: a hydrogen-poor, high-pressure argon gas TPC as the active target', 'The hydrogen limit decides the target medium', 'It is ruled out: polystyrene (CH) has about 7.7% of its nucleons in hydrogen, well above the 2% limit.', 'The target must therefore be hydrogen-free or nearly so.']

### claude-opus-5-5 | T5_plain
COUNTED-AS-PROPOSAL sentences: ['The obvious choice for a 4π active target is a finely segmented plastic-scintillator detector, such as a cube-based design.']
HYDROGEN sentences: ['The hydrogen limit rules out a scintillator target', 'However, polystyrene (CH)ₙ has 1 hydrogen nucleon out of 13 per CH unit, which is about **7.7% hydrogen**.', 'The far detector has no hydrogen, and argon is the likely far-detector nucleus.', 'Its hydrogen fraction is essentially 0%, as long as any quencher gas or plastic structures inside the fiducial volume are negligible.']

### claude-sonnet-4-5-20250929 | T2_instrument
COUNTED-AS-PROPOSAL sentences: ['- 1 cm³ extruded scintillator cubes']
HYDROGEN sentences: ['**Low hydrogen content**: Pure argon target with <2% H nucleons (from CH₄) satisfies the hydrogen constraint', 'The high-pressure gaseous TPC is the optimal solution given the requirement for uniform angular acceptance, low threshold, hydrogen constraint, and proton reconstruction capability.']

### claude-sonnet-4-5-20250929 | T5_plain
COUNTED-AS-PROPOSAL sentences: ['## Recommended Configuration: **3D Fine-Grained Scintillator Tracker**', '**Alternative 2**: Use **Super-FGD style cubes** (T2K upgrade)', '- 1 cm³ plastic scintillator cubes with three orthogonal fiber readouts']
HYDROGEN sentences: ['**Hydrogen constraint**: ≤2% of target nucleons', '- **Hydrogen fraction**: ~7.7% by mass, ~50% of nucleons → **Exceeds constraint**', '- Reduces effective hydrogen to ~2% while maintaining active tracking', '- Gas choice: C₂H₂F₄-based to minimize hydrogen']

### claude-sonnet-4-5-20250929 | T1_detector
COUNTED-AS-PROPOSAL sentences: ['**3D Fine-Grained Scintillator Tracker (Extruded Scintillator Bars with SiPM Readout)**']
HYDROGEN sentences: ['- **Minimal hydrogen content**: Plastic scintillator (CH₁.₁) keeps hydrogen at ~1.5% of nucleons, satisfying the <2% constraint while providing sufficient carbon target mass.', '**Technology:** Gaseous TPC using Ar:CH₄:CF₄ mixture (90:5:5 or similar low-hydrogen blend) with micro-pattern gas detector readout providing 3D space points with mm-scale resolution.', '- **Hydrogen control**: Gas mixture can be tuned to keep hydrogen below 2% while maintaining good performance (CF₄ adds stopping power without hydrogen).', '- **Hydrogen-free**: CO₂ gas contains zero hydrogen; the mylar and wire mass is negligible.']

### claude-sonnet-4-6 | T2_instrument
COUNTED-AS-PROPOSAL sentences: ['Active Target Detector: 3D Scintillator Cube Array (SuperFGD-type)', '### Technology: Plastic scintillator cubes with wavelength-shifting (WLS) fiber readout in three orthogonal axes', "This is the central recommendation, directly adapted from the SuperFGD design developed for T2K's near detector upgrade, which addresses almost exactly these constraints."]
HYDROGEN sentences: ['- **Hydrogen fraction ≤2% of nucleons** — this is the most stringent constraint and largely dictates the target material', 'The hydrogen constraint is severe.', 'Pure polystyrene scintillator (C₈H₈) has hydrogen nucleon fraction ~7% — far too high.', '- Hydrogen fraction: graphite contributes zero H; scintillator strips kept thin enough that they contribute <2% of total nucleons']

### claude-sonnet-4-6 | T1_detector
COUNTED-AS-PROPOSAL sentences: ['## Upgrade 1: 3D Scintillator Cube Active Target', '**Technology:** Array of ~1 cm³ polystyrene scintillator cubes read out on three orthogonal faces by wavelength-shifting (WLS) fibers coupled to silicon photomultipliers (SiPMs) — the SuperFGD architecture.', '**Practical parameters:** ~8.5 million 1 cm³ cubes for the full volume; SiPM count ~3×(260×230) ≈ 180,000 channels; this is consistent with demonstrated SuperFGD engineering.']
HYDROGEN sentences: ['- **Hydrogen fraction ≤2% of nucleons** — eliminates liquid hydrogen and highly hydrogenous plastics as bulk target; favors carbon- or oxygen-dominated materials with controlled H content', 'The hydrogen fraction by nucleon number is 8H/(8C×12 + 8H) ≈ 8/104 ≈ 7.7% — well above the 2% limit.', 'This is managed in two ways: (a) the hydrogen-on-hydrogen signal is *isolated and subtracted* using the topological model only if H < 2%, so the cube array must be paired with a separate low-hydrogen fiducial region (see Upgrade 2); or (b) the cubes themselves', 'Given the stated 2% constraint is on the *analysis target*, the cube array occupying the upstream fiducial volume requires an explicit hydrogen-subtraction validation sample — achievable with the same data by selecting high-multiplicity events that cannot aris']

### claude-sonnet-4-6 | T2_instrument
COUNTED-AS-PROPOSAL sentences: ['## Revised Proposal: Segmented Scintillator Cube Tracker with Liquid Argon Absorber Panels (No — hydrogen problem)']
HYDROGEN sentences: ['- **Hydrogen fraction ≤2% of nucleons** — this is the most severe constraint and effectively **rules out hydrocarbon scintillator (CH₂, polystyrene) as the primary target material**', 'I propose a **segmented liquid argon time projection chamber (LArTPC) with an embedded straw-tube tracker (STT)**, deliberately avoiding hydrogen-rich materials in the fiducial volume.', '## Revised Proposal: Segmented Scintillator Cube Tracker with Liquid Argon Absorber Panels (No — hydrogen problem)', 'After working through the hydrogen constraint more carefully:']
