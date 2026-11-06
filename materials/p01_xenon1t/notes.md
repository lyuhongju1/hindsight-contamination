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
