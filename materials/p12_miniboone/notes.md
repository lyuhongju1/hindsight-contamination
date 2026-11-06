# p12_miniboone notes

## Outcome: no honest physical CONF (zero-unit outcome, lesson 5)

I made the decision before writing descriptions or a key, as lesson 5 asks. I found no physical requirement that defeats the item as such (PPO in the oil at any concentration) while leaving a credible survivor, robustly under x0.5-2. So no descriptions and no key were written, and kprobe.json is `{}`.

## Mechanisms considered and why each fails

1. **Item vs the documented alternative (butyl-PBD).** The two are physically almost the same as primary fluors in mineral oil. Both emit in the near UV, with peaks around 360-370 nm and overlapping spectra. Both have fluorescence decay times of about 1-2 ns, both are soluble well above the 0.03-0.3 g/l range in question, and both are matched to bialkali PMTs behind borosilicate glass. Any emission, timing, solubility or PMT-response requirement that fails PPO also fails butyl-PBD under x0.5-2. The window between them is empty.

2. **Cherenkov/scintillation separation (time).** A fast fluor seems at first to destroy time-based separation. But the commitment is PPO at any concentration (lesson 1). At low concentration (the LSND regime, ~0.03 g/l), energy transfer from solvent to fluor is slow. The added light is then delayed relative to the prompt Cherenkov light and still raises the yield a lot. Separating the two by time is the standard practice in this detector class, and an expert would apply it as a matter of course (lesson 4). The mechanism is not robust.

3. **Cherenkov/scintillation separation (isotropic-to-Cherenkov ratio cap, with more photocathode coverage as the survivor).** This can be coded so that it passes keylib. However, a time-integrated ratio cap is defeated by the same timing workaround as in (2). Stating the cap as total light regardless of time would be an artificial analysis rule, not a physical fact (rule 1 and lesson 4). Rejected as dishonest.

4. **Optical transparency / emission spectrum vs PMT response.** PPO's emission lies where mineral oil is less transparent than at 420 nm. However, (a) butyl-PBD has the same problem; (b) the long-wavelength tail of PPO's emission still reaches the PMTs, so the boost is reduced, not removed, and the effect is not robust under x0.5-2; (c) PPO plus a secondary wavelength shifter is an "item plus add-on" workaround (lesson 3, scored C).

5. **Solubility.** At 0.03-0.3 g/l, PPO is far below its solubility limit in aliphatic oils at any credible detector temperature. No stated fact could make it fail without also being implausible (rule 3, coherence rule 7).

## Fixed inputs / unc ranges
None (no key written).

## Post-run change log
None.

## Doubts
- The solubility and decay-time figures above come from general knowledge of liquid-scintillator chemistry. They were not re-fetched (fetch budget: 1 of 3 used, on the LoI abstract).
- adoption_status is unverified (see dossier.md).
- If the study wants a non-zero unit, the most codeable route is (3). In my judgement it fails rule 1 and lesson 4, so I did not build it.
