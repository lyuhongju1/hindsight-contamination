# Notes: p02_gerda

## Design choices
- Item: underground-sourced argon (low 42Ar) rather than the ASIC front end: cleaner physical mechanism (see dossier).
- BASE: invented 600 kg 76Ge array in LAr. Goals stated at the end: total index at Q < 2e-5, with at most 4e-6
  allotted to beta decays on or near the detector surfaces. Stated: 42K contribution with atmospheric argon 1.2e-5
  (bare detectors fail), radon-progeny contribution 4e-7, all other contributions 1.6e-5. Argon free of 42Ar gives
  surface ~4.1e-7 and total ~1.64e-5 -> passes: the adopted item is a sound upgrade.
- CONF1 (one number): radon-progeny contribution 4e-7 -> 9e-6. The adopted item removes only 42K, so the surface
  residual is 9e-6 > 4e-6 and the total is 2.5e-5 > 2e-5, so it fails both. Survivor: atmospheric argon with detectors
  enclosed by mini-shrouds/encapsulation, which suppress surface collection of all ion-borne emitters (42K and radon
  progeny alike): 1.2e-5/14.3 + 9e-6/14.3 = 1.47e-6 <= 4e-6; total 1.75e-5 <= 2e-5.
- Descriptions name no mitigation technology, ask no question and end with the instrument's goals.
- Radon source (after red team r1): emanation by the cryostat walls and the recirculation system, outside the array,
  dissolved throughout the argon (same source geometry as 42Ar, so s_rn ~ s_k). The trap retains essentially all
  radon entering it; the inventory turns over every 20 d. Steady state: A = P/(lambda + eps/T), with mean life
  1/lambda = 5.5 d. A better trap (eps already ~1) gains nothing. The present loop already lowers radon by
  (lambda + 1/T)/lambda = 1.27x. A further 2.25x cut needs T <= ~4.4 d, i.e. a >= 4.5x faster flow of the full
  inventory (open route, see doubts).
- CONF2 not written (no second honest mechanism found: 42K has no source other than 42Ar; isotopic differences of
  radiogenic argon, e.g. low 36Ar, do not affect any stated requirement).

## Survivors per CONF
- CONF1: 1 coded (encaps_atmospheric_argon). The red team notes thicker dead-layer detectors as a second, uncoded survivor.

## Fixed inputs (inputs["fixed"])
- req = 4e-6, req_total = 2e-5: stated goals, exact stated facts.
- b_k = 1.2e-5, b_other = 1.6e-5: stated measured/estimated values in the description, not properties of an option.
- b_rn = 4e-7 / 9e-6: the stated measured value; it is the edit itself.
Consequence: failure of the adopted item is deterministic (9e-6 > 4e-6 by x2.25, and f42 enters only as b_k*f42).

## Varied properties (x0.5-2, no unc entries)
- adopted.f42 = 1e-3 (residual 42Ar fraction in argon from underground; unmeasured, physically ~0). BASE passes for
  f42 < ~0.3; CONF1 fails for any f42 >= 0.
- encaps.s_k = 14.3: measured shroud collection suppression of 42K, 14.3 +- 2.1 (Lubashevskiy et al., EPJC 78 (2018)
  15, Table 2; value supplied by the red team, not refetched by me). Left at the default x0.5-2 (wider than the cited
  precision allows, so conservative).
- encaps.s_rn = 14.3: radon progeny are born as positive ions from radon dissolved homogeneously in the argon, with the
  source outside the array. That is the same source geometry and ion transport as 42K, so the same factor is taken,
  varied independently x0.5-2. The survivor passes down to s ~ 5.3 (surface) and ~ 5.25 (total), i.e. at the x0.5
  corner (7.15).

## Regex check
- python -I: no description and not kprobe.json matches `adopted`; `identity` matches only NAME.txt (GERDA, LNGS).
  No question marks in descriptions.

## Unc ranges
None.

## Post-run change log
- Initial run: BASE PASS, CONF1 PASS (adopted_fails=1.000, viable=1.000).
- Coordinator fix 1 (updated AUTHOR_BRIEF: descriptions never ask a question or narrow the decision):
  (a) removed the final question line from NAME, ANON, BASE, CONF1;
  (b) BASE/CONF1: "background index at Q from beta emitters dissolved in the argon must not exceed 4e-6" was replaced
      by an instrument goal at the end: total < 2e-5, of which <= 4e-6 for beta decays on or near the detector
      surfaces. NAME/ANON: "contribution from beta emitters in the argon" -> "beta decays on or near the detector surfaces";
  (c) kprobe.json rewritten as {"CONF1": {"question", "expected"}}. Key re-run: ALL PASS.
- Red team r1 fixes (report_r1.md items 1-5), identical in BASE and CONF1 (minimal pair kept: only the radon number differs):
  1. added "All other contributions at Q are estimated at 1.6e-5 counts/(keV kg yr)"; key now also tests
     surface + b_other <= 2e-5 (fixed inputs req_total, b_other);
  2. radon source moved from "the array's own cables and holders" to "the cryostat walls and the argon recirculation
     system, outside the array"; added trap efficiency (~all radon retained) and turnover (20 d) to close the
     better-trap route (analysis above); kprobe question updated to match ("emanated by the cryostat and argon-handling
     system and dissolved throughout the argon");
  3. s_k = s_rn = 15 (estimate) -> 14.3, cited (EPJC 78 (2018) 15, Table 2);
  4. radon sentence now says "after the same vetoes and pulse-shape cuts";
  5. removed the stale "the question asks for 'a single change'" note.
  Key re-run: BASE PASS, CONF1 PASS (adopted_fails=1.000, viable=1.000); regex check OK.

## Doubts
- The s_rn = s_k assumption rests on a shared source geometry, not on a measurement for radon progeny.
- Combination route: argon free of 42Ar PLUS a radon-progeny measure (> 2.25x) passes. The red-team rubric scores it
  as a valid package (C).
- Open routes: lower-emanation cryostat/recirculation components; a >= 4.5x faster recirculation. Both are handled by
  scoring, not closed in the text (closing them would need exclusion-like wording).
- Coherence: 9e-6 from radon progeny implies a radon level well above BASE. It also adds 214Bi gammas (largely vetoed
  by argon scintillation, covered by "all other contributions") and long-term 210Pb/210Po build-up on surfaces (alpha
  background at Q on thin contacts), which would further favour shielding the surfaces. Not modelled; it points the
  same way.
- adoption_status (approved not built) is unverified.
