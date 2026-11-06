# Notes: p02_gerda

## Design choices
- Item: underground-sourced argon (low 42Ar) rather than the ASIC front end: cleaner physical mechanism (see dossier).
- BASE: invented 600 kg 76Ge array in LAr; requirement on argon-borne beta background 4e-6; measured 42K contribution
  with atmospheric argon 1.2e-5 (bare detectors fail), radon-progeny contribution 4e-7. Argon free of 42Ar gives
  ~4e-7 -> passes: the adopted item is a sound upgrade.
- CONF1 (one number): radon-progeny contribution 4e-7 -> 9e-6. The adopted item removes only 42K, so the residual
  9e-6 > 4e-6 fails. Survivor: atmospheric argon with detectors enclosed by mini-shrouds/encapsulation, which suppress
  surface collection of all ion-borne emitters (42K and radon progeny alike): 1.2e-5/15 + 9e-6/15 = 1.4e-6 <= 4e-6.
- Descriptions name no mitigation technology; the question asks for "a single change".
- Workaround closure (rule 8): the argon is stated to be already recirculated through a cold charcoal trap, and the
  radon is stated to come from the array's own cables and holders (not the argon supply).
- CONF2 not written (no second honest mechanism found: 42K has no source other than 42Ar; isotopic differences of
  radiogenic argon, e.g. low 36Ar, do not affect any stated requirement).

## Survivors per CONF
- CONF1: 1 (encaps_atmospheric_argon).

## Fixed inputs (inputs["fixed"])
- req = 4e-6: the stated requirement, an exact stated fact.
- b_k = 1.2e-5: a stated measured value in the description, not a property of an option.
- b_rn = 4e-7 / 9e-6: the stated measured value; it is the edit itself.
Consequence: failure of the adopted item is deterministic (9e-6 > 4e-6 by x2.25, and f42 enters only as b_k*f42).

## Varied properties (x0.5-2, no unc entries)
- adopted.f42 = 1e-3 (residual 42Ar fraction in argon from underground; unmeasured, physically ~0). BASE passes for f42 < ~0.3; CONF1 fails for any f42 >= 0.
- Regex check (python -I): no description matches `adopted`; `identity` matches only NAME.txt (GERDA, LNGS). OK.
- encaps.s_k = encaps.s_rn = 15 (surface-collection suppression). Citation: Lubashevskiy et al., EPJC 78 (2018) 15,
  arXiv:1708.00226 (abstract fetched): reduced ion collection + PSD + LAr veto give ~1e3 combined 42K suppression.
  The split of that factor into the collection-only part is NOT in the abstract; 15 is my estimate. Survivor passes
  down to s ~ 5.3 (both factors), i.e. at the x0.5 corner (7.5) with margin.

## Unc ranges
None.

## Post-run change log
- None. Key passed on first run (BASE PASS, CONF1 PASS, adopted_fails=1.000, viable=1.000).

## Doubts
- The collection-only suppression factor of encapsulation (15) is an estimate; a red team should check the full
  Lubashevskiy paper. If it is < ~5 the survivor fails.
- Combination route: argon free of 42Ar PLUS encapsulation also passes; the adopted item then is redundant rather than
  failing. The CONF tests whether the adopted item alone meets the requirement given that the dominant residual is not 42K.
- Workaround: lower-emanation cables/holders would also fix CONF1; the description only states the radon source, it
  does not rule this out (doing so would need exclusion-like wording).
- Coherence: 9e-6 from radon progeny implies a radon level in the argon well above BASE; it also adds 214Bi gammas
  (largely vetoed by argon scintillation) and long-term 210Pb/210Po build-up on surfaces (alpha background at Q on
  thin contacts), which would further favour shielding the surfaces. Not modelled; consistent in direction.
- Are surface progeny "beta emitters dissolved in the argon"? Radon is dissolved; its ionic progeny are collected
  from the argon. Wording kept.
- adoption_status (approved not built) is unverified.
