# Blind answers, t2k_nd280 (written before opening keys/dossier/notes)

Common physics for EQ1-3/CONF1: low-energy (~0.3-0.4 GeV) CC events, majority of muons and protons at >50 deg, proton median ~300 MeV/c with only ~6% above ~600 MeV/c. The figure of merit is (target mass) x eff_mu(angle) x eff_p(angle) x P(p_proton > threshold). Planar x/y bar targets perpendicular to the beam have poor efficiency at high angle (tracks run along planes) and a proton threshold of several hundred MeV/c (must cross several 1-cm layers / reach downstream chambers). Dense active target is required by mass: a gas target in a ~2 m3 box is ~4 kg at 1 atm (~40 kg at 10 bar) vs ~2 t of plastic, a factor 50-500 in rate.

## EQ1 (box 1.6 x 1.6 x 0.8 m, any nucleus)
- Favoured: a finely 3D-segmented scintillator target (~1 cm cubes, three orthogonal WLS-fibre views read by SiPMs). Isotropic acceptance matches the 55%/65% high-angle populations and matches the far detector's uniform angular acceptance; ~1 cm granularity gives a proton threshold near ~300 MeV/c, i.e. it keeps roughly half of the leading protons; full plastic density keeps the mass.
- Runner-up: the existing planar x/y bar technology turned so planes lie parallel to the beam (horizontal target), or a 3D grid (mesh) of scintillator bars in three orientations. Better high-angle acceptance than perpendicular planes but proton threshold/efficiency worse than cubes.
- Confidence: 4.
- Competitive alternatives: (i) low-density gas/TPC active target: lowest threshold (~100 MeV/c, ~all protons) and isotropic, but loses a factor >=50 in mass; only competitive if the dense option's threshold is near or above the proton median, since then P(p>thr) collapses (median 300 MeV/c - a dense threshold of 300 keeps ~50%, of 450 keeps ~15-20%). (ii) A dry, low-density 3D mesh/grid structure (~0.2 g/cm3) with a lower threshold: mass x3.5 lower but threshold gain could make it within a factor ~3-4. The answer is sensitive to where the cube option's proton threshold sits relative to the median.

## EQ2 (box 2.4 x 2.2 x 0.5 m, 0.5 m vertical; any nucleus)
- Favoured: 3D-segmented scintillator cube target, same reasons. Thin vertical extent (0.5 m) favours an isotropic 3D readout over planes; the box would naturally hold a horizontal slab.
- Runner-up: horizontal (beam-parallel) planar bar target or 3D grid mesh.
- Confidence: 4.
- Competitive alternative: with only 0.5 m vertical, a horizontal planar target with tracking above/below is geometrically natural and may close the gap for high-angle tracks exiting vertically; gas target loses on mass as in EQ1. Containment of high-angle muons in 0.5 m is poor for every option, which affects all options roughly equally.

## EQ3 (box 1.8 x 2.0 x 0.7 m, any nucleus)
- Favoured: 3D-segmented scintillator cube target.
- Runner-up: 3D grid mesh / horizontal planar bars.
- Confidence: 4.
- Competitive alternative: as EQ1; the ns timing mention hints at time-of-flight / neutron capability, which favours cubes further but is not in the figure of merit.

## CONF1 (box 2.1 x 1.7 x 0.65 m, oxygen-in-water only)
- Favoured: an active target in which water is the target medium: a 3D grid (mesh) of thin scintillator bars filled with water (high water mass fraction, ~80%, with 3D-ish high-angle acceptance), read by WLS fibres + SiPMs.
- Runner-up: alternating water layers and x/y scintillator planes (water-modules interleaved with planes) - poorer high-angle acceptance and needs subtraction of carbon, which the text says is not foreseen; or a water-based liquid scintillator.
- Confidence: 3 (the "only oxygen counts, no subtraction" sentence removes all pure-plastic options outright; among water options the choice depends on whether a hydrocarbon mesh counts as 'needing subtraction').
- Competitive alternative: a water-based liquid scintillator (WbLS) or a water Cherenkov-type fine-grained target: if events on the scintillator mesh must be rejected by vertex, the mesh's ~20% non-water mass just reduces yield; an option with higher water fraction but worse threshold could tie. Pure plastic (cubes) gets zero under the stated rule.
- Note: the decisive constraint is stated in one blunt sentence; it essentially says "the target must be water", which pre-selects the family.

## ABS (box 1.5 x 1.5 x 0.9 m = 2.025 m3, any nucleus)
Rough calculation, independent angle and momentum, proton momentum crudely modelled (median 280, 6% > 560): P(p>270)~0.52, >430~0.20, >440~0.19, >480~0.13, >210~0.72, >120~0.95.
Muon eff = 0.45*eff_fwd + 0.55*eff_hi; proton eff = 0.35*eff_fwd + 0.65*eff_hi.
| option | rho | eps_mu | eps_p | P(thr) | rel. yield (rho x eps x eps x P) |
|---|---|---|---|---|---|
| Korrin | 0.74 | 0.88 | 0.88 | 0.52 | ~0.30 |
| Lathe | 0.75 | 0.52 | 0.46 | 0.20 | ~0.036 |
| Quessel | 0.75 | 0.79 | 0.80 | 0.13 | ~0.06 |
| Brindle flooded | 0.72 | 0.66 | 0.66 | 0.19 | ~0.06 |
| Brindle dry | 0.21 | 0.66 | 0.66 | 0.72 | ~0.066 |
| Pellow | 0.013 | 0.92 | 0.92 | 0.95 | ~0.010 |
- Favoured: Korrin array, by a factor ~4-5 over the next.
- Runner-up: dry Brindle mesh (or flooded Brindle / Quessel, all ~0.06).
- Confidence: 4 on the given numbers.
- Arguments against: Korrin's threshold (270) sits essentially on the proton median (280), so its proton acceptance is the most sensitive quantity in the problem. If Korrin's threshold were ~x1.6-2 higher (430-540 MeV/c), P drops to ~0.07-0.2 and the dry Brindle mesh (threshold 210, kept low) becomes competitive or wins. Correlation between proton angle and momentum (high-angle protons are softer) would further hurt the high-threshold options, not Korrin. Pellow is out by mass unless pressurized x10+.
