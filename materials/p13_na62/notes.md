# p13_na62 notes

## feasibility (decided before any description was written)

Item: straws of diameter < 5 mm (HIKE proposal, arXiv:2204.13394v1) vs the existing 9.8 mm straws.
Reference numbers (from memory of NA62 detector paper, JINST 12 (2017) P05025): 9.8 mm straws,
36 um PET wall, 30 um Au-plated W wire, ~2.1 m long, 4 chambers x 4 views x 4 layers, ~0.45-0.5% X0 per chamber.
No web fetches were used.

Candidate mechanisms, each quantified (script inline in the session; numbers below):

1. Material budget per station (multiple scattering vs a stated angular/momentum resolution).
   For close-packed layers the mean wall material crossed per layer is ~ pi*t/X0, INDEPENDENT of diameter
   (36 um PET: 4.0e-4 X0 per layer). Wire material scales 1/d but is negligible (2e-5 -> 4e-5 X0/layer for 15 um
   radius W). Gas material scales with d (smaller straws are lighter). Hoop stress ~ p*r/t, so a small straw can use
   a thinner wall (20 um: 2.2e-4 X0/layer). Hits per track are set by layer count, not diameter.
   => Material favours (or is neutral to) the small straw. No conflict; a thinner-wall small straw escapes anyway.

2. Straw-wall and wire count ~ 1/d. Wall area per unit station area is constant (pi per layer), so wall count is
   not a material penalty; wire/channel count ~ 1/d is a channel-count/cost/power issue only (rule 1). Electronics
   heat in vacuum ~ channels is closed by routine cooling (lesson 4).

3. Wire sag: s = m g L^2 / (8T), independent of straw diameter; tolerance (relative to radius) is tighter by 2x
   for the small straw, but closed by tension and still a factor-2 effect only.

4. Electrostatic stability / maximum length. At equal surface field E_a (equal gain),
   T_c = (C V)^2 L^2 / (2 pi^3 eps0 b^2) with C V = 2 pi eps0 a E_a, so T_c ~ a^2 E_a^2 L^2 / b^2.
   Wire break load ~ a^2 sigma, so the a-dependence cancels: L_max ~ b sqrt(sigma/safety)/E_a.
   Numbers: T_c(2.1 m) = 9.6 g for b = 4.9 mm, 40 g for b = 2.4 mm; with a 100 g working tension
   L_max = 6.8 m (9.8 mm straw) vs 3.3 m (4.8 mm straw).
   The window between the two is exactly the diameter ratio, x2. Under x0.5-2 variation of E_a (gas/gain), wire
   strength and safety factor, L_max(small) spans ~1.7-6.6 m and L_max(large) ~3.4-13.5 m: no stated length is
   above the first range and below the second in >=95% of draws. In addition, intermediate wire supports/spacers
   (used in 4 mm straws of the ATLAS TRT, and long COMPASS straws) are the routine expert add-on (lessons 3, 4),
   and any straw-length requirement can be met by splitting straws at mid-plane (more dead material, but this
   is again a factor-of-order-1 effect). Fails rule 4 and rule 8.

5. Others checked qualitatively: rate capability, drift time, space charge, ageing (charge per wire length),
   Lorentz angle, all favour small straws. Single-hit resolution (~120-130 um sigma for both 4 mm and 10 mm
   straws in the literature, from memory) and cluster-count inefficiency near the wall differ by far less than x2,
   and gas choice is a workaround. Vacuum leak/permeation scales with wall area per station area (diameter-
   independent) and with 1/t (only if the wall is thinned, which is optional).

Conclusion: the only properties that robustly separate the item from the 9.8 mm straw are channel count, cost and
mechanical load (rule 1). The one physical mechanism (electrostatic maximum length) has a x2 window, equal to the
diameter ratio, which x0.5-2 variation destroys and which wire supports close. No honest conflict exists.
Outcome: no CONF written, kprobe.json = {}. This is the acceptable zero-unit outcome (brief, lesson 5).

## doubts
- Reference numbers are from memory, not fetched; they do not affect the conclusion because the decisive
  scalings (material independent of d, L_max ~ b) are geometric.
