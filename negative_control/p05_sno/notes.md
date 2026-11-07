# p05_sno: negative-control notes (NC1)

*2026-11-07. Outcome: **NC-zero**. No NC_CONF.txt, nc_key.py or nc_kprobe.json was written. The reasons follow.*

## alt(u)
**PXE (phenyl-o-xylylethane) liquid scintillator** (with a fluor such as PPO) as the main fill of the sphere.
- It is the documented non-adopted alternative (dossier.md: "pseudocumene / PXE").
- It is the sound survivor of the main CONF1. Its density is ~0.985 g/cm3, a deficit of ~15 kg/m3, so the net load is ~14 kg/m3, within the 60 kg/m3 limit. It gives ~1e4 photons/MeV x 0.12 = ~1200 pe/MeV, above the 400 required.
- Pseudocumene also fails CONF1 by buoyancy (deficit ~124 kg/m3), so it cannot be alt(u).

## What an NC edit must do (keylib)
One added sentence or set of numbers must make PXE fail in >= 95% of x0.5-2 draws, keep LAB failing, and leave a third option viable in >= 95% of draws.
- Each property is drawn log-uniformly in [0.5, 2], so the 5th percentile is ~0.535 x nominal.
- So the separating property must differ between PXE and the survivor by a factor of about **3.5 or more** at nominal.
- The survivor must also stay robustly within the CONF1 buoyancy limit, so its net load must be <= ~29 kg/m3 at nominal, and within the light requirement, so it must give >= ~6,200 photons/MeV at nominal.

## Candidate mechanisms examined
1. **Light-attenuation requirement at the vessel scale** (e.g. "at least half of the light emitted at the centre reaches the wall", L >= ~7 m).
   - Purified PXE has an attenuation length of a few m to ~10 m at 430 nm (Borexino CTF PXE studies, from memory). The best organic solvent, LAB, has ~10-20 m: at most ~2-4x PXE, and LAB already fails buoyancy.
   - The fills near water density that pass buoyancy are:
     - di-isopropylnaphthalene (~0.96 g/cm3, deficit ~40, not robust under the limit at x2);
     - 1-methylnaphthalene (~1.02 g/cm3);
     - PXE/heavy-aromatic blends;
     - LAB30/MN70.
   - All of them are as transparent as PXE or less (naphthalenes are yellowish).
   - The only near-water fill with a long attenuation length is a water-based scintillator. Its yield is ~100-1000 photons/MeV, which gives 12-120 pe/MeV, so it fails the stated 400 pe/MeV by 3-30x.
   - **No survivor exists**: any threshold that kills PXE robustly kills every scintillator that passes buoyancy.
2. **Light-yield or emission requirement.** A survivor would need >= ~3.5x PXE's yield (~3.5e4 photons/MeV). No liquid scintillator comes close; PXE, LAB, PC, DIN and MN are all ~0.8-1.2e4. Emission spectrum and decay time give no stated-fact requirement that separates them by >= 3.5x, and naming a timing or spectral need would narrow the problem to a technology. **No survivor exists.**
3. **Sign-asymmetric load limit** (e.g. upward load <= ~3-5 kg/m3, downward <= 60). Robust failure of PXE needs an upward limit below 15 x 0.535 - 1.1 x 1.87 = ~6 kg/m3. The survivor would be a denser-than-water fill, such as 1-methylnaphthalene + PPO (excess ~20 kg/m3). The edit was rejected for four reasons:
   - (a) **Coherence.** It rewrites the CONF1 sentence ("upward or downward", "however restrained"). A wall limit that is asymmetric for any restraint is physically incoherent, because a hold-down net is the mirror of a hanging support. A red team would flag it under rule 7.
   - (b) **It is the same buoyancy mechanism retuned**, not a separate physical requirement. A ~5 kg/m3 window is also comparable to the drift in density difference from a few kelvin of temperature change (organics expand ~0.8 kg/m3/K more than water).
   - (c) **The trivial workaround stays open.** PXE plus a few percent of a dense aromatic (e.g. ~8% 1-chloronaphthalene) becomes denser than water. That is item plus add-on (C), and the edit cannot close it with a plain fact without also killing the survivor.
   - (d) **The only survivor is not credible to an expert.** Pure 1-methylnaphthalene is not credible as a 520 t fill viewed across 10 m: its transparency is poor and its light yield is unverified (the main study already flagged it as unverified).
4. **Other properties.**
   - Flash point: PXE's is high, so it is favourable.
   - Acrylic compatibility: PXE is compatible, so it is favourable.
   - 14C, U and Th content: there is no 3.5x separation among petroleum-derived solvents.
   - Refractive index: the mismatch with acrylic causes only small Fresnel or TIR losses, which are not robust.
   - None of these gives a robust physical separation in PXE's disfavour.

## Survivors
None under any honest single edit. Mechanisms 1 and 2 have no survivor. Mechanism 3's nominal survivor (1-methylnaphthalene) is not credible and the edit is incoherent.

## Fixed inputs
Not applicable (no key written). The CONF1 stated facts would have stayed fixed: radius 5 m, wall 1 cm, collection 0.12, 400 pe/MeV, 60 kg/m3.

## Doubts
- PXE and LAB attenuation lengths and solvent light yields are from memory, with no web fetch. The conclusion does not hinge on them: separating PXE from any buoyancy-passing scintillator by >= 3.5x on transparency or yield would need values far outside any reported range.
- A future relaxation of keylib robustness, or a two-sentence edit (e.g. lowering the light requirement so that water-based scintillator survives, plus an attenuation requirement), could produce an NC. Either would change the CONF1 physics goal (pep/CNO need high light yield), so it would not be minimal. It is not attempted.

## DIFF
CONF1 -> NC_CONF: none (NC-zero; no edit exists that defeats PXE robustly while leaving a credible survivor).
