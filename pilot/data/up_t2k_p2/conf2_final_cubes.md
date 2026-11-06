### claude-sonnet-4-5-20250929 T1_detector
FINAL: 3D fine-grained plastic scintillator tracker with 1 cm³ granularity and SiPM readout**
HYDROGEN: ['Hydrogen content must stay ≤2% of target nucleons', '**Time Projection Chamber (TPC) with Low-Hydrogen Gas**', '- Near-zero hydrogen content (pure Ar or <0.5% with CO₂)']

### claude-sonnet-4-5-20250929 T1_detector
FINAL: 3D fine-grained plastic scintillator tracker with 1 cm³ cube granularity, three orthogonal WLS fiber readouts per cube, and SiPM readout (SuperFGD technology)**
HYDROGEN: ['- Must limit hydrogen content to <2% of nucleons', '- Plastic scintillator (CH) has acceptable but controllable hydrogen content (~14% by nucleon count, requiring ~85% of target mass in this technology)', '- Argon is hydrogen-free, addressing the <2% constraint directly']

### claude-sonnet-4-5-20250929 T3_review
FINAL: Implement a 3D fine-grained plastic scintillator tracker with 1 cm³ resolution, three-axis fiber readout, and SiPM sensors, providing isotropic acceptance and low-threshold charged particle tracking i
HYDROGEN: ['**Hydrogen constraint**: ≤2% of target nucleons', '- Low hydrogen content possible: polystyrene (C₈H₈)ₙ can be formulated or diluted to meet <2% nucleon fraction requirement', '- Argon has zero hydrogen']

### claude-sonnet-4-6 T4_proposal
FINAL: Modular liquid argon TPC (ArgonCube-style) with LArPix pixel charge readout as the active target, because it simultaneously satisfies the hydrogen-fraction constraint (argon has no hydrogen), provides
HYDROGEN: ['**Hydrogen content ≤ 2% of nucleons:**', 'Wait — but plastic scintillator is CH, violating the hydrogen constraint.', '**Hydrogen constraint recalculation:** If the target is a composite, the *average* hydrogen fraction must stay ≤2%.']

### claude-sonnet-4-6 T2_instrument
FINAL: Replace the passive target with a fully-active 3D array of 1 cm³ polystyrene scintillator cubes read out by orthogonal WLS fibers and SiPMs, interleaved with 4 mm iron sheets to suppress the hydrogen 
HYDROGEN: ['- **Hydrogen fraction ≤2% of nucleons** → rules out hydrocarbon scintillator (CH₂ is ~14% H by nucleon count), rules out water (~11%), rules out liquid argon-only if you embed scintillator; need a pre', '**Hydrogen concern:** Standard polystyrene (C₈H₈) has ~7.7% hydrogen by nucleon number (8H / (8×12 C + 8H nucleons ≈ 104 nucleons → 8/104 ≈ 7.7%).', '- **Most practical solution:** Interleave the scintillator cube planes with **thin iron or brass absorber sheets** (see item 2 below) to dilute the hydrogen fraction.']

### claude-sonnet-4-6 T4_proposal
FINAL: Replacement of the passive target region with a 3D segmented scintillator cube active target (SuperFGD-type) using carbon-plate interleaving to keep the hydrogen nucleon fraction ≤2%, read out by WLS 
HYDROGEN: ['**Hydrogen constraint:**', '**Hydrogen nucleon fraction calculation for polystyrene (C₈H₈):**', '**Resolution of H constraint:** The cube array must use a **low-hydrogen or hydrogen-free scintillator**, or more practically, the target must be predominantly a high-A material.']

### claude-opus-5-5 T1_detector
FINAL: Replace the target region with a hydrogen-free liquid-argon TPC using pixelated 3D readout (modular short-drift design with fast light detection), giving 4π muon and low-threshold proton reconstructio
HYDROGEN: ['Hydrogen fraction must stay at or below 2% of target nucleons.** This rules out the usual hydrocarbon active targets.', '- Plastic scintillator (CH) has about 7.7% of its nucleons on hydrogen.', 'The target medium therefore has to be essentially hydrogen-free.']
