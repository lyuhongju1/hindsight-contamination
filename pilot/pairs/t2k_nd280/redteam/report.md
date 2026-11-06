# Red-team report: t2k_nd280

Step-2 inputs read: keys/key.py, keys/key_output.txt, dossier.md, notes.md. Blind answers: blind.md (written before these were opened).
Extra checks: redteam/propvar.py, propvar2.py, be.py load key.py unchanged and vary option properties; output in propvar_out.txt and below. No web fetches made; no cited property value is disputed with a source.

## Cross-cutting findings

### A. Robustness does not vary technology properties (protocol violation)
VARIED = [L, W, H, p_med, frac_hi, f_mu_ha, f_p_ha] holds only level inputs; per-option rho, eps_fwd, eps_ha, p_th, w_water are never varied (notes.md admits this). The reported 100% covers only knobs that act almost identically on all options.

Re-run with every option property also varied x0.5-x2 (single-factor, then joint log-uniform, 4000 draws; efficiencies and w_water clipped at 1):

| level | single-factor property failures | joint, props only | joint, props + inputs | keyed wins with margin >= 3 (props only) | verdict |
|---|---|---|---|---|---|
| EQ1 | cube p_th x2 -> two-view bars; two-view p_th x0.5 -> two-view | 58% | 55% | 21% | FAIL |
| EQ2 | same two | 59% | 55% | n/c | FAIL |
| EQ3 | same two | 59% | 55% | n/c | FAIL |
| CONF1 | none under key rule (adopted loses trivially, w_water = 0) | 100% | 100% | intended winner water_grid wins 70% (53% with margin >= 3) | PASS by rule, fragile in substance |
| ABS | Korrin p_th x2 -> dry Brindle | 63% | 59% | 24% | FAIL |

Break-even proton thresholds (other values at key defaults):

| level | option | cited p_th (MeV/c) | margin < 3 at | loses at |
|---|---|---|---|---|
| EQ1 / EQ2 / EQ3 | cube | 300 | 363 / 352 / 358 | ~520 |
| ABS | Korrin | 270 | 356 | 499 |
| CONF1 | water grid | 450 | 467 (+4%) | 598 (to FGD2-like) |

Many x2 efficiency excursions are unphysical (clipped at 1). The decisive realistic sensitivity is the adopted threshold relative to the stated proton median: medians of 290-320 MeV/c sit on the 300 MeV/c threshold, so F(p_th) ~ 0.5, where the survival function is steepest.

### B. Equivalents tuned toward the answer
notes.md: at real T2K parameters (NAME/ANON) the margin is only 2.35, and the twins use a softer beam because "a margin of 3 or more needs a regime where both the threshold and the angular advantages matter more". The EQ levels are chosen to clear the bar; they are not equivalent to the real decision. Disclose, or revisit the margin criterion for this pair.

### C. Missing expert consideration
In a 0.5-0.8 m tall box, high-angle muons exit sideways and miss the downstream chambers; their momentum needs range or added high-angle tracking (the real upgrade added HA-TPCs and ToF). The FoM credits any high-eps_ha option fully. This is equal for all isotropic options, so the winner is unchanged, but the target-only framing understates what was needed.

## EQ1
1. Agreement: yes (3-view fine-cell cubes). Key runner-up two-view bars 0.2125; water grid and dry grid within 2%.
2. Challenges: margin 4.14 rests on cube p_th = p_med = 300; cube p_th ~363 gives margin < 3; two-view p_th 250 ties (1.05). Runners-up bunched at ~0.21; water grid p_th x0.5 gives 1.27, dry grid rho x2 gives 2.11. Fails property robustness. Angle-momentum independence ignores softer high-angle protons (would help cubes).
3. Leading wording: "Because the beam energy is low, about 55% ... more than 50 degrees" plus "far detector ... uniform acceptance in angle" spells out isotropic acceptance; "kinematically complete" + "leading recoil proton" point to low threshold. Legitimate FoM statement, but the 50 degree cutoff is the TDR one.
4. Identifiability: high. Two gas drift chambers alternating with two x/y ~1 cm polystyrene-bar planes perpendicular to beam (ND280 tracker); instrumented return steel as muon ranger (SMRD); lead-plastic ECal barrel; SiPMs; water far detector; "upstream end of the bore will be cleared" (P0D removal); box near SuperFGD 1.9 x 1.8 x 0.56 m. The solenoid swap is a thin disguise.
5. Verdict: FIX. (i) Vary option properties in robustness; the level then fails (~55%, margin 3 not robust): lower the bar or redesign. (ii) Drop "alternates two gas drift chambers with two planar targets", "flux-return steel ... muon ranger", "upstream end of the bore will be cleared"; change box aspect.

## EQ2
1. Agreement: yes. Key runner-up two-view bars 0.324, water grid 0.317.
2. Challenges: threshold fragility as EQ1 (margin < 3 at cube p_th 352); fails property robustness. The 0.5 m vertical favours a horizontal planar target with tracking above/below; the volume-only FoM ignores containment and track length.
3. Leading wording: "transverse-momentum-imbalance analyses" names the TDR physics case (TKI).
4. Identifiability: very high, the most recognizable. "off-axis near detector"; dipole 7.5 x 3.2 x 3.4 m (UA1 is 7.0 x 3.5 x 3.6); "scintillator counters between the return-yoke plates" (SMRD); "three gas tracking chambers and two segmented plastic targets of 1.0 cm square polystyrene bars ... transverse" (3 TPCs + 2 FGDs, 0.96 cm bars); calorimeter on four sides; water far detector; TKI.
5. Verdict: FIX. Rewrite the detector description (chamber count, magnet type/dimensions; drop off-axis, TKI, 1.0 cm square bars); vary properties (the level then fails the margin-3 bar).

## EQ3
1. Agreement: yes. Key runner-up two-view bars 0.255.
2. Challenges: as EQ1 (margin < 3 at cube p_th 358); fails property robustness.
3. Leading wording: "timing is available at the nanosecond level" is irrelevant to the FoM and hints at the real ToF/neutron story.
4. Identifiability: moderate-high. Dipole with yoke scintillator slabs; x/y polystyrene-strip target + gas drift chambers + lead-plastic calorimeter; WLS fibres onto SiPMs; "imaging water" far detector (Super-K); "8% must fall below 4%" echoes TDR ~6% -> ~4%.
5. Verdict: FIX. Vary properties (then fails); drop the ns-timing sentence; change the halve-to-4% systematic pattern.

## CONF1
1. Agreement: yes. Blind winner water-filled 3D grid (WAGASCI-like); blind runner-up water layers between x/y planes = key runner-up (FGD2-like, 0.0497).
2. Challenges:
   - Internal inconsistency: "no subtraction of other target materials is foreseen" contradicts the key. Both surviving options are 30-49% plastic by mass; the key credits them by w_water, assuming perfect vertex assignment to water vs plastic, which is not achievable with 2.5 cm cells / 3 mm bars or 2.5 cm water layers. Read strictly, no key option is valid.
   - Thinnest margin (3.38): drops below 3 if grid p_th 450 -> 467 (+4%), or grid eps_ha or rho x0.5, or FGD2 water fraction underestimated. With properties varied, the intended winner wins 70%, 53% with margin >= 3.
   - The pass rule ("adopted loses") is satisfied by construction (w_water = 0), so it tests nothing.
   - Options forgotten: water-based liquid scintillator target (fully active, mostly oxygen by mass, some carbon); 3-view fine-cell geometry with water cells.
3. Leading wording, check (b): YES, the constraint gives away the answer. "Only interactions on oxygen nuclei in water count ... no subtraction" eliminates 5 of 7 key options (including the adopted cubes) before any trade-off; the reader is told "the target must be water", leaving a two-way choice decided by the stated high-angle fractions. It tests reading, not whether a constraint flips the answer. Fix: state a physics requirement the reader must translate (e.g. only the far-detector nucleus model may be assumed; each non-matching-nucleus event carries a stated model-uncertainty penalty), so water fraction trades against threshold and acceptance and the cubes are not zeroed by fiat.
4. Identifiability: as EQ3 (near-identical text); a water-target requirement in an ND280-like detector maps to the 2016 WAGASCI reference option.
5. Verdict: FIX. (i) Resolve the no-subtraction contradiction (allow vertex/statistical rejection, or apply a purity penalty in the key). (ii) Turn the constraint into a quantitative penalty. (iii) Vary properties; the margin is at the edge of 3 and not robust to the grid threshold.

## ABS
1. Agreement: yes. Korrin margin 4.85 (blind estimate ~4-5). Key runner-up dry Brindle 0.126, Quessel 0.123.
2. Challenges: Korrin p_th 270 sits on the median 280; margin < 3 at 356; at x2 (540) dry Brindle wins (1.03). Quessel p_th x0.5 near-ties (1.05). Fails property robustness (59-63%). Spectrum shape (Weibull) not stated; a different shape with the same median and 6% tail shifts F(270) and F(430-480) noticeably.
3. Leading wording: Korrin listed first; the only option with flat high efficiency and a sub-median threshold; it dominates every dense option in every column, so the problem is a lookup.
4. Identifiability: low for the instrument; invented names work. The catalogue maps transparently to SuperFGD / FGD / FGDXY / WAGASCI water / WAGASCI empty / HPgTPC ("twin-view", mesh "flooded" vs "dry", "vapour chamber"); densities scaled ~0.7 with ratios kept.
5. Verdict: FIX. Vary properties (then fails); optionally state the spectrum shape or the fraction above each threshold.

## Summary of required key change
Add rho, eps_fwd, eps_ha, p_th, w_water of every option to the robustness draws (clip at 1). Under x0.5-x2 property variation EQ1-3 and ABS fall to ~55-63% (FAIL); CONF1 passes only via its trivial rule. A +20% shift of the adopted threshold (~360 MeV/c) already breaks margin 3 at every EQ level.