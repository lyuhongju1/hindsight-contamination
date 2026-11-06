# p16_besiii notes

Written by a second author after the first author stalled. Every other file in this folder (dossier, descriptions, key, kprobe) belongs to the previous author and was left unchanged. These notes describe those files as they are.

## Design choices
- **Item:** the chamber technology of the endcap timing layer, i.e. a gaseous timing chamber with resistive electrodes (MRPC), in any placement or readout (lesson 1). The key covers three electrode variants: float glass, low-resistivity glass and ceramic. Each may be stacked up to 4 layers.
- **Mechanism (CONF1):** rate capability. Above about 1e6 Hz/cm^2, no demonstrated resistive-electrode chamber keeps 95% efficiency, but the requirements ask for 95% at the local flux everywhere. The timing (60 ps), field (2 T) and radiation requirements do not separate the item from its alternatives. Rate is the only separator.
- **Edit:** one sentence (luminosity, flux, dose, fluence). The CONF values are the BASE values times 5000 (1e31 to 5e34). This keeps flux, dose and fluence consistent with each other in both texts.
- **Instrument class:** BASE/CONF is a 13 TeV pp general-purpose spectrometer, not a tau-charm e+e- machine. A tau-charm machine cannot coherently reach MHz/cm^2 at its endcap (see doubt 1). Because of this, the "same class" link to BESIII rests only on the endcap-TOF subsystem: plastic counters, fine-mesh PMTs and degradation from upstream secondaries.
- **Workaround routes:** no CONF2 was written. Two routes are only partly closed: adding more chamber layers (the key allows up to 4, which does not help against rate) and heating the electrodes (not modelled; see doubt 2).

## Survivors per CONF
| CONF | n_survivors | survivors |
|---|---|---|
| CONF1 | 1 | lgad_3layer (three layers of silicon sensors with internal gain, ~1.3 mm pads) |

Rejected alternatives in the key: scintillator tiles + SiPM (fails on fluence, 1e12 vs 4e14), cooled LYSO + SiPM (fails on fluence, 2e14 vs 4e14), large plastic counters + fine-mesh PMT (fails on rate, about 1.7e4 Hz/cm^2).

## Fixed inputs (`inputs["fixed"]`)
| input | value | justification |
|---|---|---|
| flux_min | BASE 2.0e3, CONF1 1.5e6 Hz/cm^2 | Exact stated facts. BASE uses the inner-edge flux, the strictest test for "adopted passes". CONF1 uses the outer-edge flux, the strictest test for "adopted fails". |
| dose | BASE 20 Gy, CONF1 1.0e5 Gy | Exact stated fact |
| fluence | BASE 8e10, CONF1 4e14 neq/cm^2 | Exact stated fact |
| B | 2.0 T | Exact stated fact |
| sigma_req | 60 ps (per track; the description does not say σ or FWHM; read as σ) | Exact stated requirement |
| eff_req | 0.95 | Exact stated requirement |
| n_mrpc_max | 4 | Integer structural count. Generous: real endcap MRPC TOF systems use one chamber layer, and the conflict is on rate, which stacking does not help. |
| n_layers | lgad 3, tile 2, LYSO 1, counter 1 | Integer structural counts. Three LGAD layers is at the upper end of real endcap timing layers (2 to 3 hits per track with overlaps). |

## unc ranges and citations
keylib varies every property in `props` by ×0.5–2. No tighter range is used. key.py says "Sources in notes.md", but the stalled author never wrote notes.md. The only source information is in the key.py comments, reproduced below. **None of these comments is a bibliographic citation.** Each is therefore marked UNCITED, and must be sourced before the red team.

| property | value | key.py comment | status |
|---|---|---|---|
| float_glass rate95, sigma, B/dose/fluence limits | 1e3 Hz/cm^2, 50 ps, 20 T, 1e6 Gy, 1e16 | "ALICE/STAR-type float glass ~1e12-1e13 ohm cm" | UNCITED (experiment named, no reference) |
| lowres_glass rate95, sigma | 3e4 Hz/cm^2, 55 ps | "~1e10 ohm cm glass, CBM-type R&D" | UNCITED (programme named, no reference) |
| ceramic rate95, sigma | 5e5 Hz/cm^2, 120 ps | "Si3N4/SiC 5e9 ohm cm; 95% at 2e5 (~120 ps), most generous quoted flux 5e5 used" | UNCITED ("quoted" by whom is not stated) |
| lgad_3layer rate95, sigma, ineff, dose, fluence | 1e8, 35 ps, 0.02, 2e6 Gy, 1.5e15 | "sigma per hit at ~4e14 neq/cm^2, inefficiency per layer" | UNCITED |
| scint_tile_sipm | 1e7, 45 ps, 0.01, 5e4 Gy, 1e12 | "single-MIP timing lost above ~1e12 neq/cm^2" | UNCITED |
| lyso_sipm_cooled | 3e6, 40 ps, 0.01, 5e5 Gy, 2e14 | "barrel-timing-layer type" | UNCITED |
| scint_counter_pmt | 1.7e4, 90 ps, 0.01, 2.5 T, 1e4 Gy, 1e13 | "per-channel limit 1e7 Hz / 600 cm^2" | UNCITED |
| all B_max_T = 20 T (except PMT) | 20 T | none | UNCITED (placeholder meaning "field-insensitive") |

## Post-run changes
None are known. The previous author's log was not saved, so any tuning of stated numbers before this handover cannot be ruled out or reconstructed.

## Doubts

**(1) Coherence of the CONF1 flux.** The stated flux (1.5–10 MHz/cm^2 at 2.5 m, η 2–3) is about 4 orders of magnitude above any real tau-charm endcap. BESIII's endcap rate, dominated by beam background, is of order 1e1–1e2 Hz/cm^2 (author knowledge, not fetched). Even a 1e35 super tau-charm factory would plausibly reach only about kHz/cm^2. Within the text, however, the number is coherent because the description puts the instrument at a 13 TeV pp collider at 5e34. A rough check:
- σ_inel ≈ 80 mb gives 4e9 interactions/s. With dN_ch/dη ≈ 6, the primary flux on a disk at z = 2.5 m is R·(dN/dη)/(2πr^2).
- η = 3 (r ≈ 25 cm): about 6 MHz/cm^2. η = 2 (r ≈ 69 cm): about 0.8 MHz/cm^2. Secondaries and loopers (×1.5–2) bring this to the stated 1.5–10 MHz/cm^2.
- Fluence and dose: 5e34 over about 2e7 s is about 1000 fb^-1. That gives about 1e14 charged/cm^2 at r = 25 cm, so 4e14 neq with albedo neutrons and about 30 kGy from MIPs, roughly 100 kGy with electromagnetic background. These are consistent to within a factor ~3.
- Pileup is about 125.
- BASE (1e31) scales down consistently.

So the edit is coherent, but only because the instrument is no longer of the tau-charm class. A tau-charm luminosity or beam-background increase could not make it coherent. This weakens the pair's mapping to BESIII. The red team may also argue that the CONF now describes an HL-LHC endcap timing layer, which carries its own recognition cue.

Minor geometry inconsistency: the annulus for η 2–3 at 2.5 m (r 25–69 cm, about 1.3e4 cm^2) cannot hold 36 counters of 600 cm^2 (2.2e4 cm^2). The real counters would be about 330 cm^2 each. This does not change any verdict: the counter rate limit would be about 3e4 Hz/cm^2, still far below 1.5e6.

**(2) Low-resistivity glass and ceramic electrodes.** These do not defeat the conflict at nominal values, but the margin is thin and uncited:
- Low-resistivity glass (~1e10 Ω cm) has demonstrated a few ×1e4 Hz/cm^2 at >90% efficiency. Even ×2 (6e4) is 25× below the 1.5e6 outer-edge flux.
- Ceramic (Si3N4/SiC) is the real threat. The key uses 5e5 Hz/cm^2 ("most generous quoted"). ×2 gives 1e6, only 1.5× below the outer-edge flux.
- If a published ceramic or semiconductive-electrode result shows ≥95% efficiency at ~1e6 Hz/cm^2, the ×0.5–2 envelope crosses 1.5e6 at the outer edge and the robust failure is lost there.
- At the inner edge (10 MHz/cm^2) the margin is about 10× and the failure would still hold. But the requirement applies "everywhere", and a hybrid (chambers at the outer radii, something else inside) would be "item plus add-on", scored C (lesson 3).
- Expert tweaks that were not modelled (lesson 4): heating the electrodes (resistivity falls by roughly ×2–3 per 10 °C), and thinner electrodes, lower-gain operation and a more sensitive front end. Together these plausibly gain ×2–5 in rate capability.
- Ceramic σ ≈ 120 ps per layer also needs 4 stacked layers to reach 60 ps, which is marginal.

Verdict: the conflict holds against glass. Against ceramic it is defensible only if the 5e5 figure is sourced and no ~1e6 result exists. This is the main risk of the pair.

**(3) LGAD survivor credibility.** Credible: it is essentially the solution built for HL-LHC endcap timing (1.3 mm pads, 2–3 hits per track, about 35–50 ps per hit at end of life, fluences up to ~1.5–2.5e15 neq/cm^2 with replacement of the innermost ring; author knowledge, not fetched).
- **Area:** about 1.3 m^2 per layer per endcap, so 3 layers × 2 endcaps ≈ 8 m^2. This is the same order as the real HL-LHC devices (~6–14 m^2).
- **Radiation:** at 4e14 the gain-layer acceptor loss is modest (~10–30%) and is recovered with bias. 100 kGy is well within tolerance. 2 T is irrelevant.
- **Caveats:**
  - It needs cooling to about −25 to −30 °C to control leakage at 4e14. The description does not forbid this, but an expert would ask.
  - The key's per-layer inefficiency of 0.02 (×2 gives 0.04) is optimistic. Inter-pad no-gain regions give fill factors of ~85–95%.
  - At σ_hit = 35 ps one hit suffices and the survivor is robust. At ×2 (70 ps) two of three hits are needed: per-layer inefficiency of 0.10 still gives 97.2% ≥ 95%, but 0.15 gives 93.9% and fails.
  - The survivor is credible but should be stated with fill-factor-aware inefficiency (≤0.1 via staggered overlaps) and cooling. n_survivors = 1.
