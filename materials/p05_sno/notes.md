# p05_sno notes

## Design choices
- Target item: LAB liquid scintillator (see dossier.md). Te-130 was rejected because its conflict with Nd-150 rests on Q-values and phase-space ratios that cannot survive keylib variation.
- Mechanism (CONF1): buoyancy load. LAB is ~14% less dense than water. The sphere sits in shield water, and the wall stated in the CONF withstands only 60 kg/m3 of net vertical load, "however the sphere is restrained". That clause closes the hold-down-net workaround that the real detector used.
- Minimal edit BASE->CONF1: one set of numbers. The wall goes from 5 cm to 1 cm and the load limit from 300 to 60 kg/m3 (was 200/40 before r1) (both scale linearly with thickness, ratio 5).
- BASE invented: light-water target, 10 m sphere, 6,800 10-inch PMTs, 1.6 km depth. None of SNO's exact numbers are used.
- Workaround routes closed by plain fact: sphere and shield water retained (no lighter shield liquid, no new vessel); the wall limit holds for any restraint. No technology class is named or excluded.
- 520 t water in a 10 m sphere (523.6 m3) is consistent. The wall is denser than water (~1.19 g/cm3), so its weight offsets a light fill only by ~1.1 kg/m3 (1 cm) or ~5.7 kg/m3 (5 cm). The key includes this term.

## Survivors per CONF
- CONF1: 2 at nominal (PXE + PPO, deficit ~15 kg/m3; 30% LAB / 70% 1-methylnaphthalene blend, deficit ~28 kg/m3). Pseudocumene fails on the same mechanism (deficit ~124 kg/m3). Water-based liquid scintillator meets the load limit but fails the light requirement (300 photons/MeV x 0.12 = 36 pe/MeV, still below 400 at x2).

## Grading rule (pre-registered, r1 FIX 3)
- A fill with <50% LAB by volume is not the adopted item. Density-matching LAB to water needs at least ~62-79% heavy co-solvent, so such a fill is no longer LAB-based.

## Fixed inputs (exact stated facts, not varied)
- sphere_radius_m = 5, wall_m = 0.05 (BASE) / 0.01 (CONF1): stated geometry.
- collection_fraction = 0.12: stated in the description as a fact about the retained array.
- pe_per_MeV_required = 400: stated requirement.
- load_limit_kg_m3 = 300 (BASE) / 60 (CONF1): stated requirement.

## Unc ranges
None; all properties are varied x0.5-2. The density deficit, not the density, is the varied quantity because the buoyant load is linear in it. This choice is much more conservative than the ~1% precision of the real densities.

## Post-run change log
- r0: the key passed on its first run; no stated numbers were changed.
- r1 (red-team report_r1.md, FIX 1): load limits retuned from BASE 200 / CONF1 40 to 300 / 60 kg/m3. Reasons: BASE had only a 1.5x margin (LAB at a x2 deficit failed), and 40 was ~8x below acrylic membrane capacity. The ratio of 5 and the wording are kept, so the minimal pair holds. kprobe.json updated to 60 (expected answer still NO: net ~139 > 60).
- r1 FIX 2: water-based liquid scintillator coded as an option (deficit 7 kg/m3, 300 photons/MeV); it fails the light requirement. An assert in key.py checks that it fails even at x2 yield. Also coded a 30/70 LAB/1-methylnaphthalene blend (deficit 28, 8e3 photons/MeV, light yield unverified); it survives but is not the adopted item under the grading rule.
- r1 FIX 4: pseudocumene density corrected from 0.889 to 0.876 g/cm3 (deficit 111 -> 124 kg/m3). Immaterial to the outcome.
- r1: grading rule added (see above).
- After r1, key.py: BASE PASS, CONF1 PASS (adopted_fails=1.000, viable=1.000); gates.py p05_sno: GATES PASSED.

## Doubts
- Cited property values come from memory (no web fetches). PXE light yield ~1e4 photons/MeV and LAB ~1.1e4 photons/MeV are approximate. The light requirement has a margin of >1.6x even at x0.5.
- A real acrylic shell's limit is set by stress concentrations at the restraint points. A 1 cm, 10 m sphere has a membrane stress of only ~3 MPa at a 140 kg/m3 deficit. The 60 kg/m3 limit (40 before r1) is stated as a fact, not derived. It is still a few times below membrane capacity, so a red team may question its realism.
- A reader could propose densifying LAB with a heavy aromatic co-solvent. Reaching ~985 kg/m3 needs a majority of the dense solvent. This is handled by the grading rule (<50% LAB is not the adopted item), not by a stated fact.
- Water-based liquid scintillator is now coded (r1) and fails the light requirement. Some quote WbLS yields up to ~1000 photons/MeV; even that gives 120 pe/MeV < 400.
- check_base is nominal only. After r1, LAB at a x2 deficit (280 kg/m3) is within the BASE limit of 300.
- PXE acrylic compatibility is assumed (as for LAB). It is not a stated fact, so it is not coded.

- Red team r1 noted that a 1 cm, 10 m acrylic sphere has never been built (mild coherence oddity), and that identifiability is very high (the SNO -> SNO+ story).
