# NC notes: p02_gerda

*2026-11-07. Outcome: **NC-zero**. No honest NC_CONF exists, so no NC_CONF.txt, nc_key.py or nc_kprobe.json was written. No web fetches were used. The reasons follow.*

## alt(u)
**Atmospheric argon with the germanium detectors enclosed by an ion-collection barrier**, i.e. mini-shrouds (transparent nylon or PEN film, possibly with a wavelength-shifting coating) or encapsulation of the detectors.
- This is the dossier's "documented alternative not adopted" (GERDA Phase II / LEGEND-200 mini-shrouds).
- It is the only coded survivor of the main CONF1 (key.py: `encaps_atmospheric_argon`). It suppresses collection of all ion-borne emitters, 42K and radon progeny alike, by s ~ 14.3 (Lubashevskiy et al., EPJC 78 (2018) 15). Result: 1.2e-5/14.3 + 9e-6/14.3 = 1.47e-6 <= 4e-6, and the total is 1.75e-5 <= 2e-5.
- The adopted item (underground argon) fails CONF1 because radon progeny stay at 9e-6 > 4e-6.

## What an NC edit must do
Add one sentence or one set of numbers to CONF1 such that:
- every reasonable variant of the barrier fails robustly (x0.5-2). Variants: per-detector mini-shroud, per-string shroud, whole-array shroud, tight encapsulation, thin or thick film, with or without a wavelength-shifting coating;
- underground argon still fails;
- a THIRD option passes every stated fact. That option must be neither the barrier nor underground argon, and must not be a package containing either.

## Why no third option exists (the decisive constraint)
CONF1 keeps the 42K term at 1.2e-5, 3x the 4e-6 surface allotment. Any third option must therefore cut the post-cut 42K surface term by at least about 3.3x (about 5.3x once the 9e-6 radon term is included, if it addresses both) without underground argon and without a barrier. Here are the 42K routes I examined.
- **Underground argon:** this is the adopted item. A package "underground argon + radon measure" (faster recirculation >= 6.8x, low-emanation cryostat/recirculation parts) passes, but it contains the historical item. Using it as the NC survivor would make history-driven answers look like correct abandonment of alt(u), which biases toward H_NC. Excluded, as in p01 (NC-zero for the same reason).
- **Removing K+ ions from the argon by recirculation:** 42K is regenerated in place throughout the argon from 42Ar (33 yr). Its 12.4 h half-life would need full-inventory turnover much faster than 12 h, while the stated turnover is 20 d. Not credible.
- **Sweeping ions with an external drift field and no enclosing structure:** the detectors' own kV fields dominate near the surfaces. There is no measured suppression to cite, and a grounded open cage is itself a shroud variant (GERDA Phase I copper mini-shroud). Not credible as a distinct, robust survivor.
- **Thicker n+ dead layer / surface-insensitive detectors:** this is the only plausible non-barrier route. A 3.5 MeV beta loses about 0.7 MeV/mm in Ge, so about 2 mm of dead layer stops betas from depositing Q through the n+ surface. However:
  - ions also collect on the p+ contact and the passivated groove, which no dead layer covers;
  - the stated 42K and 214Bi terms are already after pulse-shape cuts, so the share of the residual from those small surfaces is unknown;
  - no measured post-cut suppression factor >= 5.3x on both terms exists that I could cite.
  As the sole survivor, its viability would rest on an uncited, unmeasured factor (rules 3 and 4).

## Why alt(u) cannot be defeated honestly (the other half)
Each candidate fact was checked against every variant of the barrier.
1. **Argon-veto light requirement** (scintillation from argon next to the detectors must reach the readout). Transparent or wavelength-shifted films (TPB-coated nylon, PEN) transmit or convert the light. That is the LEGEND-200 solution, and the light loss is tens of percent, not a robust factor of 2 or more. The workaround can only be closed with exclusion wording ("argon in direct contact with the detector surfaces"), which breaks rule 2.
2. **Radiopurity / material budget near the detectors.** The added mass (about 6 g of 125 um nylon per detector, about 1.4 kg for 600 kg) and its purity are settings within the item: film thickness and material choice (lesson 4, C1). A per-gram fact that applies to any material regardless of type is physically false.
3. **Free-space geometry** (gaps too small for a barrier at a distance of one beta range). With mm gaps, betas from ions collected on the barrier still cross argon and deposit hundreds of keV there, so they are largely vetoed. That is not a robust failure. A per-string or whole-array shroud is also a placement variant that a gap fact does not defeat (lesson 1).
4. **Radon source inside any enclosure** (emanation from holders or contacts next to the detectors). This contradicts CONF1's stated outside-the-array source, so it is not an additive edit. It would also leave 42K needing a barrier or underground argon (see above).
5. **Surface charge on insulators near the detectors.** Real, but not quantifiable to a robust x0.5-2 failure, and conductive or coated films are a routine fix.

## Survivors
- CONF1: alt(u) (coded); thicker dead layer (uncoded, uncited).
- Under any candidate NC edit, the only robust survivor is a package containing underground argon, so there is no valid third option.

## Fixed inputs
None (no NC key written). CONF1's stated values (req 4e-6, req_total 2e-5, b_k 1.2e-5, b_rn 9e-6, b_other 1.6e-5) were taken as given.

## Doubts
- A future measurement of post-cut 42K/214Bi suppression by thick-dead-layer detectors (>= ~10x nominal, covering the p+ and groove surfaces) could make that route a credible third option. Even then, a fact that robustly defeats every barrier variant without exclusion wording was not found.
- The decision is a judgement on credibility to a domain expert. A red team may disagree on the thick-dead-layer route.

## DIFF
CONF1 -> NC_CONF: none (NC-zero; no NC_CONF written).
