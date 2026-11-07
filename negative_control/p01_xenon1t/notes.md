# NC notes: p01_xenon1t

**Outcome: NC-zero.** No honest NC_CONF exists. No NC_CONF.txt, nc_key.py or nc_kprobe.json was written.

## alt(u)
Gas-phase purification through heated (~400 C) zirconium getters: the existing evaporate / getter / recondense loop at the stated 50 kg/h, scaled as needed (more or larger getters, more gas flow). This is the dossier's "documented alternative not adopted" and the sole CONF1 survivor in key_output (viable 97.4%).

## Why no NC_CONF exists
CONF1 already fixes two physical needs:
1. **Methane (CH3T) removal** at about 614 kg/d of effective eps*F (10 Bq -> 10 µBq in 90 d, 4 t). This needs thermally activated chemisorption, which means a hot getter on xenon gas (alt(u)), or fractional distillation at large throughput. At ~170 K the liquid purifier (the adopted item) gets eps << 0.065 and fails.
2. **Electronegative removal** for the stated lifetime of at least 0.5 ms.

To build an NC, one added fact must defeat alt(u) robustly (x0.5-2) while some option that is neither the adopted item nor alt(u) passes BOTH needs. I checked these candidates.

- **Heat-load cap** (stated cryogenic cooling power plus a higher lifetime requirement or a shorter CH4 window, so the gas flow alt(u) needs cannot be evaporated and recondensed):
  - Every remaining CH4 remover also evaporates and recondenses xenon. A larger distillation column does this with reflux, so its heat load per kg of feed is higher than a gas loop with a recuperative heat exchanger. Any cap that kills alt(u) kills the column first.
  - A gas loop's net heat load is set by the heat-exchanger effectiveness: 96 kJ/kg latent heat; 50 kg/h is about 1.3 kW bare and about 70 W at 95% effectiveness. Effectiveness is a design setting within alt(u) (lesson 4 / C1), so a cooling-power fact does not robustly defeat alt(u).
  - The only option left that passes is "liquid purifier for the electronegatives + a hot gas getter (or headspace getter) for CH4". That contains the adopted item, so it is not a third option. It is also close to the historical XENONnT configuration, so it would invert the NC's purpose.
- **Higher lifetime requirement alone** (e.g. several ms): this hits the same wall as above. High-throughput electronegative removal without the gas loop means the liquid purifier (adopted item) or a large column (same heat penalty). Raising the getter flow is a setting within alt(u).
- **Radon-emanation fact about the getter loop**, so that a large distillation column alone survives:
  - It is a property of a particular getter and pump hardware, not of gas-phase getter physics. Low-emanation getters, or adding a radon-removal stage, are variants of alt(u) or add-ons. So the failure is not robust, and it amounts to design fiat against alt(u).
- **Different purification physics** removing CH4 from the liquid at 170 K: none is credible. C-H dissociation needs several hundred C. CH4 does not freeze out (it is more volatile than Xe). Physisorbents are saturated by the Xe solvent.
- **Headspace extraction** (CH4 enriches in the gas above the liquid) followed by a hot getter: this is alt(u) at reduced flow, not a third option.
- **Reducing the outgassing load or raising the drift field:** these are not purification options. They are operating-point or material changes that would equally rescue alt(u), so they cannot separate it.

Conclusion: CH4 removal forces hot gas-phase chemistry (alt(u)) or distillation. Any physical cap strong enough to defeat alt(u) also defeats distillation, or leaves only adopted item + alt(u) as the passing answer. A credible third option that passes every stated fact while neither being nor containing the adopted item or alt(u) does not exist.

## Survivors
None (no NC_CONF). In CONF1 the only survivor is alt(u).

## Fixed inputs
Not applicable (no NC key). The numbers used above are from materials/p01_xenon1t/keys/key.py and notes.md (M = 4000 kg, 50 kg/h gas loop, 3 kg/h column, break-even about 614 kg/d) and the textbook Xe latent heat (about 96 kJ/kg).

## Doubts
- A red team might propose a stated-fact edit that I did not consider, e.g. a requirement only distillation meets (removal of a noble-gas contaminant) combined with a heat budget. However, any requirement that needs a large column, together with a heat cap that excludes the gas loop, excludes the column too, because the column has the higher heat load.
- No web fetches were used. The heat-load figures are order-of-magnitude.

## DIFF
None: CONF1 -> (no NC_CONF; NC-zero).
