# Check: Gd vs 6Li delayed-tag efficiency in a compact (~10-30 L) segmented plastic detector

The claim (feasibility_q60.md, item 2, Route A): Gd capture tagged above ~2.6 MeV in ~25 L is only ~10-20% efficient (at most ~25-30%), while 6Li with PSD reaches ~40-50%.

## Numbers found

### Gd (Gd2O3-coated film around plastic bars): PANDA36
Source: Oguri et al., "Reactor antineutrino monitoring with a plastic scintillator array as a new safeguards method", https://arxiv.org/abs/1404.7309 (text taken from the PDF, Tables 2-3)
- Detector: 36 modules of 10 kg each, 360 kg total (about 350 L, about 60 x 60 x 100 cm), wrapped in Gd2O3-coated polyester (4.9 mg Gd/cm2). This is the same Gd-film geometry as the item.
- Delayed selection: 3 MeV <= Etotal <= 8 MeV, multi-module topology cut (E3rd/Etotal), and a time window of 8-150 us.
- Delayed efficiency (Geant4, given the prompt passed): trigger 48.8% x Etotal cut 79.1% x E3rd cut 91.9%, giving **35.5% total delayed efficiency** (19.4% model systematic). The time window then contributes 91.2%.
- Overall IBD efficiency: **3.15%**. The prompt side is also hurt by escape (9.7%).
- Authors: the larger PANDA100 is projected at 9.24% overall, a gain of about 3x "because the capture efficiency of cascade gamma-rays in delayed event increases". In other words, escape of the Gd cascade dominates at this scale.
- Related Geant4 numbers (PANDA slides, https://www.awa.tohoku.ac.jp/AAP2010/2ndDay/AAP2010_panda.pdf): capture on Gd with foil-wrapped bars is 85.7% for 6 cm bars and 76.0% for 10 cm bars (capture time 29.6 and 62.4 us).

Implication: even at about 14x the item's volume, Gd delayed tagging with a 3 MeV threshold is only about 35%. In 10-30 L (20-30 cm per side, comparable to one or two PANDA module cross-sections), cascade containment is much worse, and the neutron also escapes more often. A delayed efficiency of <= ~20-25% above ~2.6-3 MeV is therefore well supported as an upper bound. No direct MC value for a 25 L cube was found.

### 6Li-doped PSD plastic: SANDD (LLNL / U. Michigan)
Source: "SANDD: A directional antineutrino detector with segmented 6Li-doped pulse-shape-sensitive plastic scintillator", https://arxiv.org/abs/2105.00083 (text taken from the PDF)
- Detector: **9 L**, 0.1 wt% 6Li PSD plastic, segmented, with a polyethylene layer around it.
- Neutron capture efficiency (simulated): **45.4%**. Of the captured neutrons, 87.2% capture on 6Li and 12.8% on H. **51.9% of neutrons exit the detector** and 2.7% capture in the polyethylene. Mean capture time is 37.2 us, and the mean neutron travel is 7 cm. The authors note that capture efficiency rises with the polyethylene thickness.
- Energy-cut efficiency is 95.7% (window about 0.37-0.64 MeVee). The PSD cut efficiency is 73.6% / 94.7% / 92.7% by component, with gammas rejected at the 99% level.
- **Total IBD neutron detection efficiency: 34.8%.** Positron efficiency is 80.2%, coincidence efficiency 71.7%, and **overall IBD efficiency 20.0%**.
- Earlier talk value (preliminary): neutron 34%, overall 19%. Source: https://indico.fnal.gov/event/19348/contributions/186359/attachments/129493/157099/neutrinos_SANDD_2020_sutanto.pdf

Not retrieved within budget: PROSPECT, SoLid and CHANDLER efficiencies. These detectors are 1-4 t, so they are not representative of 10-30 L. Their per-segment 6Li tag efficiencies are higher mainly because neutrons do not escape.

### Ambient-gamma singles rate in small shielded monitors
Not found within budget. The SANDD PSD cut rejects gammas at 99% in the neutron energy window. PANDA36 shows that surface uncorrelated backgrounds "cannot be fully eliminated" even with a 3 MeV delayed threshold, but no Hz figure was extracted. The stated ~10^2 Hz figure is unverified.

## Verdict: UNCLEAR (Gd side SUPPORTED; 6Li side NOT supported at the stated level)

- **Gd side: supported.** Measured and simulated Gd-film plastic with a 3 MeV delayed threshold gives only 35.5% delayed efficiency in 350 L (PANDA36). A ~25 L detector must do worse, so <= ~25% is robust and ~10-20% is plausible. A dedicated MC was not found.
- **6Li side: the ">= ~40%" claim fails at the small end.** The only real ~10 L 6Li-PSD-plastic detector (SANDD, 9 L) reaches **34.8%** neutron detection efficiency, because 52% of the neutrons escape. Reaching 40-50% would need the ~30 L end of the range and/or a thicker moderator/reflector. That is plausible, since capture rises with volume and polyethylene, but it is not demonstrated.
- The ratio still favours 6Li by about 1.5-2x+ at equal size, with a far lower singles rate in the delayed window thanks to PSD. However, the stated gap of "~10-20% vs 40-50%" is overstated at 10 L. Any requirement must be set at the level 6Li actually reaches in the stated volume: about 30-35% at 10 L, perhaps about 40%+ at 30 L with a reflector. Otherwise the survivor also fails. A safer framing: fix the volume at the ~25-30 L end with a polyethylene reflector and set the delayed-efficiency requirement at about 30%. The accidental-rate argument then carries most of the weight against a ~1 MeV Gd threshold.
