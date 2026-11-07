# Notes: p01_xenon1t

## Design choices
- Item: purification acting on the circulated liquid, any variant (copper, cold getter, sieve, any placement). All variants work at ~170 K.
- CONF1 mechanism: a tritiated-methane calibration with a stated residual limit and window. To remove CH4 you need thermally activated chemisorption on a hot (~400 C) Zr getter. A purifier at LXe temperature does not remove CH4 at a useful rate: C-H bonds do not dissociate at that temperature, and the xenon solvent saturates any physisorption sites. So every variant of the item fails, whatever its flow (x0.5-2 on flow and efficiency gives at most ~0.0006 of the needed ln-removal per day).
- Survivor: the existing heated-getter gas loop at the stated 50 kg/h (about 140 SLPM, two getters). The stated 3 kg/h distillation column is checked as well and fails on its own, which closes that route with a stated number.
- BASE/CONF1 minimal pair: only the calibration sentence differs (diff is one line). BASE calibration uses short-lived noble-gas isotopes, which need no chemical removal, so the item passes BASE: its lifetime is about 12.7 ms against the 0.5 ms requirement.
- Every stated requirement (lifetime >= 0.5 ms; CONF1 residual <= 1 mBq within 90 d) is evaluated for every option.

## Survivors per CONF
- CONF1: 1 (gas_phase_getters). Viable in 97.5% of draws. The adopted item fails in 100% of draws.

## Fixed inputs (exact stated facts)
- M = 4000 kg, gas-getter flow 50 kg/h, column 3 kg/h, lifetime requirement 0.5 ms, A = 10 Bq, limit 1 mBq, window 90 d. All are numbers stated verbatim in BASE/CONF1.
- Efficiencies are clipped at 1 (they are physical fractions).

## unc ranges
- None. All cited properties are varied x0.5-2.

## Workarounds not closed (lesson 3)
- "Item plus keeping or adding a heated-getter loop on the gas" passes CONF1, because the hot getter does the methane removal. That is item plus add-on (score C). It cannot be closed by a plain physical fact, because the liquid purifier does nothing to prevent the gas loop from working. The existing gas loop is present in BASE as stated hardware, so a reader may naturally say "add liquid-phase purification and keep the getters". This is the main doubt about this pair. The CONF separates the item from the alternative only for the removal function, not as an exclusive choice.
- A larger distillation column would also remove CH4 (light fraction). That is an add-on and not the item.

## Log of post-run changes
1. First run: stated getter flow 40 kg/h. The survivor was viable in only 93.7% of draws, because the lifetime requirement failed in the corner where Q x2, eps x0.5 and K x0.5 combine. Changed the stated flow to 50 kg/h in BASE and CONF1 (still a credible two-getter rate of about 140 SLPM). The CONF1 edit and the adopted-item result were unchanged (fails 100%). Second run: PASS.
- (Before any run, while drafting: flow 70 changed to 40 kg/h for credibility, and window 60 changed to 90 d to keep the survivor robust at the lower flow.)

## Doubts
- The liquid-purifier CH4 efficiency of 1e-3 is a conservative upper bound from the physics argument, not a measured number. Even a value of 0.01 would still fail: residual ~10*exp(-(85+65)*90/4000) ~ 0.3 Bq.
- CH3T also soaks into PTFE and plastics and outgasses back (the LUX experience). That tail affects every option equally and is not modelled.
- CH4 is more volatile than Xe, so it enriches the gas phase above the liquid. This does not change the conclusion.
- Dossier sources were cited from memory (no fetches). The XENONnT adoption status (built and operated) is well established, but the exact figures are marked unverified.

## Post-run changes (r1, 2026-11-06, applied by the orchestrator from red-team r1)

- **CONF1 residual limit 1 mBq -> 10 µBq** (key limit_Bq 1e-3 -> 1e-5).
  - Reason: coherence. 1 mBq in 4 t is ~8,000 tritium decays per tonne-year below 18.6 keV, several times a XENON1T-class total ER background. 10 µBq is ~80 per tonne-year.
  - Outcomes are unchanged: the adopted item still fails (residual ~1.9 Bq), the getters still pass, the column still fails.
  - Minimal pair: the edit is inside the CONF1-only calibration sentence.
- **Break-even efficiency.** Removing CH4 needs sum(eps*F) >= ln(A0/limit)*M/90 d. With the 10 µBq limit that is ~614 kg/d. The liquid loop at 8,500 kg/d would need eps >= ~0.065. The stated physics (CH4 more volatile than Xe; physisorption sites occupied by the solvent; chemisorption needs several hundred C) gives eps << 0.01. Hot getters at nominal remove ~1,140 + 65 kg/d (about 2x break-even). In the joint x0.5 corner (getter and column eps) they remove ~600 kg/d, just below break-even; such corners make up the 2.6% non-viable fraction (alternatives viable in 97.4% of draws).
- **key.py comment** corrected to 50 kg/h.
- **kprobe:** the efficiency bar is now "above a few percent", matching the failure threshold (was "comparable to a 400 C getter").
- **40 -> 50 kg/h** (earlier change): survivor robustness 93.7% at 40 kg/h vs 97.5% at 50 kg/h; the adopted item fails 100% either way. Reported as disclosed tuning.

## Scoring rule (from red-team r1, to be frozen into the rubric)

- **A:** main circulation moved to liquid AND the gas getters removed or decommissioned.
- **B:** as A, with a claim that the liquid purifier or column "also handles methane".
- **C:** liquid purification added, with hot getters (or another hot-chemisorption step, or a much larger column) explicitly kept for CH4 / tritium.
- **X:** liquid purification proposed, getter loop not mentioned either way.
- **D/E:** a non-liquid answer (e.g. more getter flow).
- **Expect many C and X answers.** CONF1 detects the specific contaminated move (replacing the gas loop as XENONnT did).
