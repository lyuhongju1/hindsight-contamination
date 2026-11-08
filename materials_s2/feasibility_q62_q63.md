# Feasibility (AUTHOR_BRIEF lesson 5): q62, q63 (2026-11-08)

Figures are from memory; no web fetches were made. Values marked ~ are approximate.

## q62: ATLAS IBL, 3D silicon pixels at r ~ 3.3 cm. Verdict: NO WINDOW

- Fluence route: no window. 3D silicon (50 um electrode spacing) holds about 97% efficiency to ~1e16 neq/cm^2, and thin planar silicon also survives ~1e16 at high bias. To kill every silicon option robustly at x0.5 you need about 5e16 or more. At that fluence pCVD diamond also dies: 1/ccd = 1/ccd0 + k*Phi, with k ~1e-18 um^-1 cm^2 (24 GeV p), and worse for pions and neutrons. That gives ccd ~5-20 um, or ~0.2-0.7 ke at 36 e/um, below a ~1.5-3 ke threshold. Already at 5e15 diamond gives ccd ~95 um (~3.4 ke), which is marginal and not robust to x2. Such fluences at 3.3 cm also belong to an FCC-class machine, not an LHC pp inner layer, so this would be a class breach (compare p16).
- Leakage/cooling route: no window. Stating a warm coolant (~+15-20 C) as a fact is allowed under C1. But 3D sensors run at low bias (~50 V even irradiated), and lower bias, thinner sensors and lower front-end power are settings within the item. Example: 4e-17 A/cm x 3e15 x 0.023 cm x 50 V = ~0.14 W/cm^2, which is coolable. Thermal runaway is not robust under x0.5 fluence or alpha.
- Material route: no window. X0 is 12 cm for diamond and 9.4 cm for silicon; the sensors are similar in thickness and dominated by the chip, cooling and flex. The windows overlap.
- Timing route: no window. Both silicon and diamond meet 25 ns easily. GOSSIP's ~1 mm drift spread (~15-20 ns) is the marginal one, so timing works against the alternative.
- GOSSIP: no window. Any fluence or dose that kills silicon also kills its CMOS readout chip (the same FE class). At ~1e8-1e9 Hz/cm^2 at 3.3 cm, rate, discharges and ageing count against it.
- Planar versus 3D: a stated fact that kills 3D but not planar (fill factor or normal-incidence efficiency, capacitance or noise) is defeated by tilt and threshold settings, and is not robust. Even if it held, a planar survivor would be an intra-silicon geometry choice and not one of the row's alternatives (diamond, GOSSIP). It would not count as a clean rejection of the item.

## q63: LHCf, GSO layers replacing plastic, at 140 m. Verdict: NO WINDOW

- Bunch spacing/pile-up route (GSO tau ~30-60 ns): not robust. The tail left after 25 ns is exp(-25/tau) = 0.32-0.75 for tau 22-86 ns, against ~1e-4 to 0.7% for plastic (2-5 ns) and ~0 for quartz. That is a real difference. But the conflict needs a high per-crossing occupancy p, and then:
  - (a) tail subtraction using the previous crossing's measured energy, a short gate and a previous-crossing veto are routine settings (lesson 4 and C1). With GSO's high light yield the subtraction error is small.
  - (b) The usable fraction is (1-p)^n with n = 1-4 crossings over the x0.5-2 range of tau and p. It crosses any threshold on one side of the band only.
  - (c) Coherence: the luminosity needed for high zero-degree occupancy gives doses and neutron fluences that kill the item's position layers (fibres or silicon strips) too. That turns the instrument into a quartz ZDC, which is a class change (compare p16).
- Gd neutron capture route: no window. Thermal capture gammas (~8 MeV sum) arrive on a ~us timescale, outside any ~100 ns gate. Their effect on hadron energy resolution (already ~35-40%) is far below a x0.5-2 margin.
- Temperature route: no window. GSO light yield varies by ~-0.3 %/C, about 3% over +/-10 C. Temperature monitoring and calibration correction is a routine setting.
- Dose route: no window. Above ~1e2-1e3 Gy, plastic fails and GSO (tested to ~7e5-1e6 Gy) passes, which favours the item. Only a dose of ~>1e7 Gy, where quartz survives, could separate them, and GSO's failure dose is not established there, so it is not robust. Such a dose also kills the position layers, the same coherence breach as (c).
- I4 weakness (the alternatives are not explicitly weighed): this does not change the verdict, because no window exists. It would only weaken the hindsight claim if a conflict had been found.
