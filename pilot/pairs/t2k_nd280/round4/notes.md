# Notes: t2k_nd280 round 4 (CONF1 only)

## Outcome
**I found no honest CONF1, so CONF1 is left FAILING.**
- `descriptions/CONF1.txt` is the round-3 CONF1, unchanged: the proton KE requirement goes from 60 to 12 MeV. It is kept as the best candidate because:
  - its failure physics is right (the red team agreed);
  - its mechanism is distinct from CONF2.
- BASE.txt and CONF2.txt are byte-identical copies of round 3. The regex check finds no hits in any of the three files.

## Why no CONF1 qualifies
Rule 4 says CONF1 may only change a quantity that BASE already states. The quantities BASE states are:
- distance 410 m and flux peak 0.7 GeV;
- field 0.15 T and magnet length 6.5 m;
- target region 2.6 x 2.3 x 0.9 m;
- muon efficiency >= 25% at all angles;
- proton KE 60 MeV;
- hydrogen fraction <= 20%.

Each one was checked against the 1 cm cubes:
- **Distance, flux peak.** Neither has a value that is coherent with the scenario and makes the cubes fail.
  - A closer station or a higher flux raises pile-up, and that favours fast scintillator.
  - Lowering the energy toward decay-at-rest removes the CC muon.
  - Raising the energy is still handled by a plastic target.
- **Field.** SiPMs work to about 7 T. Fields that high are incoherent with a warm dipole, and they also kill LAr (0.55 T).
- **Muon efficiency.** The cubes reach about 0.9, the best of any option, so no requirement can fail them.
- **Target dimensions.** The only lever is a WLS-fibre run longer than about 3.5 m. That is not a hard physical limit: the light is attenuated, not lost, and fibres can be read from both ends. A red team would rightly reject it.
- **Hydrogen fraction.** CONF2 already uses this mechanism.
- **Proton KE.** Cubes have a 46.8 MeV threshold. keylib needs a margin of at least about 2.6x on each side, so survivors must have thresholds of about 7 MeV or less. Only low-density TPCs get there:
  - LAr is at about 21–47 MeV;
  - nuclear emulsion with water (NINJA-type) is at about 21 MeV.
- **A second sentence change to the far-detector line** (making argon the far-detector nucleus, with lighter nuclei <= 20%): rejected.
  - It is the same target-composition mechanism as CONF2, on the same sentence.
  - It has the same survivors (LAr plus an argon gas TPC).
- **Mass.** In this 5.4 m^3 region, a 10 atm argon gas TPC holds at most about 90 kg in a rectangular vessel, or about 27 kg in a cylinder. That is below any credible target mass. So every mechanism whose second survivor is a gas TPC fails the round-4 requirement.
- **Dense options.** None of the dense options that pass BASE (LAr, empty grid) is separated from the cubes by about 7x on any stated axis.

## Key changes (round-3 key + round-4 criterion)
- `MASS` (density with a PDG source, and an encoded fill fraction) and `CRIT` (`m_min_kg` = 500 kg) are held outside the round-3 inputs.
  - 500 kg is about half of one ND280 FGD module (1.1 t, arXiv:1106.1238). It is an author criterion, not a stated fact.
- `TECH` holds class labels. They are strings, not varied, and not capabilities.
- `viable_distinct()` filters the round-3 `viable()` to survivors that pass the mass floor, keeping one per class. It is used only for CONF1.
- BASE and CONF2 use exactly the round-3 inputs, functions and seeds, so their output is unchanged (PASS).
- **CONF1 result:**
  - nominal survivors under round-3 `viable()`: two gas TPCs, one class;
  - masses: ~90 kg and ~4.5 kg;
  - after the filter: none. FAIL.
- **Diagnostic only:** under the same round-4 criterion, CONF2 would keep only LAr.
  - The 10 atm gas TPC (~90 kg) is below the 500 kg floor.
  - The orchestrator may want to re-judge CONF2's second survivor by the same standard.

## K-probe
- CONF1: the answer-revealing range parenthetical is removed. The question now asks about "a track with measured direction".
- CONF2: unchanged from round 3.

## Log of stated-number changes
None. No description numbers were changed in round 4.

## Doubts
- The 500 kg floor and the fill fractions (LAr 0.5, empty grid 0.2) are author estimates. The CONF1 failure does not depend on them: 90 kg against any floor above about 0.2 t still fails.
- Web fetches: none.
