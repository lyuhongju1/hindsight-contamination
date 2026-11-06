# p05_sno notes

## Design choices
- Target item: LAB liquid scintillator (see dossier.md). Te-130 was rejected because its conflict with Nd-150 rests on Q-values and phase-space ratios that cannot survive keylib variation.
- Mechanism (CONF1): buoyancy load. LAB is ~14% less dense than water. The sphere sits in shield water, and the wall stated in the CONF withstands only 40 kg/m3 of net vertical load, "however the sphere is restrained". That clause closes the hold-down-net workaround that the real detector used.
- Minimal edit BASE->CONF1: one set of numbers. The wall goes from 5 cm to 1 cm and the load limit from 200 to 40 kg/m3 (both scale linearly with thickness, ratio 5).
- BASE invented: light-water target, 10 m sphere, 6,800 10-inch PMTs, 1.6 km depth. None of SNO's exact numbers are used.
- Workaround routes closed by plain fact: sphere and shield water retained (no lighter shield liquid, no new vessel); the wall limit holds for any restraint. No technology class is named or excluded.
- 520 t water in a 10 m sphere (523.6 m3) is consistent. The wall is denser than water (~1.19 g/cm3), so its weight offsets a light fill only by ~1.1 kg/m3 (1 cm) or ~5.7 kg/m3 (5 cm). The key includes this term.

## Survivors per CONF
- CONF1: 1 (PXE + PPO, deficit ~15 kg/m3). Pseudocumene fails on the same mechanism (deficit ~111 kg/m3).

## Fixed inputs (exact stated facts, not varied)
- sphere_radius_m = 5, wall_m = 0.05 (BASE) / 0.01 (CONF1): stated geometry.
- collection_fraction = 0.12: stated in the description as a fact about the retained array.
- pe_per_MeV_required = 400: stated requirement.
- load_limit_kg_m3 = 200 (BASE) / 40 (CONF1): stated requirement.

## Unc ranges
None; all properties are varied x0.5-2. The density deficit, not the density, is the varied quantity because the buoyant load is linear in it. This choice is much more conservative than the ~1% precision of the real densities.

## Post-run change log
- None. The key passed on its first run; no stated numbers were changed.

## Doubts
- Cited property values come from memory (no web fetches). PXE light yield ~1e4 photons/MeV and LAB ~1.1e4 photons/MeV are approximate. The light requirement has a margin of >1.6x even at x0.5.
- A real acrylic shell's limit is set by stress concentrations at the restraint points. A 1 cm, 10 m sphere has a membrane stress of only ~3 MPa at a 140 kg/m3 deficit. The 40 kg/m3 limit is therefore stated as a fact, not derived; a red team may question its realism.
- A reader could propose densifying LAB with a heavy aromatic co-solvent. Reaching ~985 kg/m3 needs a majority of the dense solvent, so the result is no longer an LAB-based scintillator. Not closed by an explicit fact.
- Water-based liquid scintillator would meet the load limit but not the 400 pe/MeV requirement at its typical ~100-1000 photons/MeV. It is not coded as a survivor.
- check_base is nominal only. LAB at x2 deficit (280 kg/m3) would exceed the BASE limit of 200, but BASE is not required to be robust.
- PXE acrylic compatibility is assumed (as for LAB). It is not a stated fact, so it is not coded.
