# Notes: t2k_nd280 round 3

## Design choices
- The instrument is invented: the Kestrel Flats near station.
  - 410 m from the target, flux peak 0.7 GeV.
  - Warm dipole: **0.15 T** (was 0.3 T) over a 6.5 m inner volume.
  - Target region **2.6 x 2.3 x 0.9 m**, changed from 1.9 x 1.8 x 0.6 m to move away from the real ~1.92 x 1.84 x 0.56 m.
- Each description has 6 lines. The regex check (scratchpad script, scoring_regex.json t2k_nd280 patterns) found no hits.
- Removed from all three texts, following the red team:
  - the room-temperature sentence, so there is no temperature fact and cryogenic options are legitimate;
  - the dose sentence, since the old CONF1 mechanism is dropped.
- Every stated physical fact is a numeric check on every option in `_passes`:
  - proton kinetic-energy threshold <= required KE;
  - minimum muon efficiency over all angles >= required (the all-angle requirement, now numeric);
  - hydrogen nucleon fraction <= h_max;
  - field <= the readout's demonstrated field;
  - size: for fibre-read options, the longest dimension <= WLS-fibre attenuation length; for TPCs, half the smallest dimension <= demonstrated drift length.
- Distance and flux peak are context only. They are in `inputs`, but no option property depends on them.
- There are no booleans. `fibre_read` is a 0/1 numeric selector of which geometric quantity is compared; it is never near a threshold under variation.
- BASE: the adopted item passes every check: 46.8 <= 60 MeV, 0.9 >= 0.25, 7.7% <= 20%, 0.15 T <= 7 T, 2.6 m <= 3.5 m. BASE does not claim it is the best option.

## Conflict mechanisms
- **CONF1, granularity versus proton range** (replaces the dose mechanism). The one edit is the proton KE requirement, 60 -> 12 MeV.
  - A 12 MeV proton has a CSDA range of ~2 mm in polystyrene, well below one 1 cm cell. The three-view cube threshold is 300 MeV/c = 46.8 MeV (TDR).
  - Survivors are low-density media where the same proton travels centimetres:
    - 10 atm gas TPC: 3 MeV, arXiv:1910.06422;
    - 1 atm gas TPC: ~0.5 MeV, derived by range scaling.
  - LAr (40 MeV), all grids and the bars fail.
  - Coherence: a lower proton-energy goal has no side effect on the beam, magnet, drift chambers or rates.
- **CONF2, hydrogen content** (fixed). The one edit is h_max, 20% -> 2% (was 1%).
  - Polystyrene has 7.7% hydrogen nucleons and fails by 3.8x.
  - The gas TPC now uses a cited low-hydrogen mixture, Ar:CF4:iC4H10 95:3:2 (T2K TPC gas): 0.48%, 4.2x below the limit.
  - The 1 atm TPC uses Ne:CO2:N2 (ALICE), 0% hydrogen.
  - LAr is 0% and is legitimate now that no temperature is stated.
  - Three survivors at nominal (two gas TPCs and LAr), all passing every other stated fact.
  - Unlike round 2, the 2% limit is above the hydrogen content of the quenched gas, so it is not a de facto "no hydrogenous material" rule.

## Log of stated-number changes (relative to round 2)
All of these were fixed before the first round-3 key run. There were no changes after it.
- Field 0.3 -> 0.15 T, so the LAr field demonstration (0.55 T) gives a robust margin. Chosen before the run, with the margin in mind.
- Target 1.9 x 1.8 x 0.6 -> 2.6 x 2.3 x 0.9 m (red-team rule 7).
- Dose and room-temperature sentences removed.
- New stated numbers:
  - muon efficiency >= 25% at every angle;
  - proton KE 60 MeV (BASE, CONF2) and 12 MeV (CONF1).
- CONF2 h_max 1% -> 2%.
- Thresholds were chosen with the keylib x0.5-x2 robustness in mind. A ratio of >= ~2.6 to the nearest option is needed on each side, which is why 25% (not 30-40%) and 12 MeV (not 20 MeV) were picked.

## Doubts
- **Gas-TPC survivors in CONF1.** Both survivors are gas TPCs, at 10 atm and at 1 atm: two pressures, two vessel concepts, two gases. A reader may see this as close to a single survivor class.
  - Target mass is small: 5.4 m^3 holds ~90 kg of Ar at 10 atm and ~5 kg of Ne at 1 atm. No rate or mass requirement is stated, so none is applied.
  - A red team may object that a 1 atm gas target is not a real neutrino target. If so, CONF1 has only one survivor.
- **Derived 1 atm threshold.** The 0.54 MeV is derived by range scaling from the cited 3 MeV at 10 atm, not measured. Only the threshold is derived; the margin is ~22x.
- **Encoded efficiency values.** The mu_eff_min values for the gas TPCs (0.9), the grids (0.8) and LAr (0.5) encode qualitative "flat / full angular acceptance" claims. They are not measured efficiencies. The LAr value (arXiv:1905.09694) is from memory and was not fetched.
- **High-pressure operation of the T2K gas.** The mixture is cited at 1 atm; arXiv:1910.06422 says only that "other mixtures are also under consideration" besides Ar:CH4 90:10. Using it in the 10 atm option for the hydrogen value is an extrapolation.
- **Unverified citations.** These are from memory and were not fetched:
  - the 2.5 m drift (ALICE) applied to the high-pressure TPC;
  - SiPM 7 T (Espana 2010);
  - ALEPH 1.5 T;
  - LAr 0.55 T (Badertscher);
  - Y-11 attenuation > 3.5 m.

  Their DOIs or URLs may be imprecise. None of them is decisive in either CONF.
- **Cube fibre length.** Cube fibre runs of 2.6 m against a 3.5 m attenuation length are fine nominally. Under variation this only affects BASE, which is checked at nominal.
- **Web use.** 3 fetches (arXiv:2203.06281 twice, gave no numbers; ar5iv 1910.06422) and 1 search.
