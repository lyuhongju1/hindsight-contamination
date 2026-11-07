# Red team r1: p01_xenon1t (2026-11-06). Verdict: BASE OK; CONF1 FIX (all applied by the orchestrator); r2 light check pending

**Blind answers:**
- BASE: liquid purification is favoured and sound.
- CONF1: replacing the gas loop fails; the hybrid (liquid plus the kept hot getters) passes.

**Physics:** confirmed.
- CH4 is more volatile than Xe, so it does not freeze out at 170 K.
- The solvent occupies the physisorption sites.
- Chemisorption needs several hundred C.
- Only distillation works cold, and that is the column, not the item.

**FIXes:**
1. A replace-vs-add scoring rule (A/B/C/X) recorded in notes.md.
2. The 1 mBq limit is incoherent with a WIMP search: set 10 µBq.
3. Record the break-even efficiency (~0.04–0.065).
4. Correct the stale 40 kg/h comment.
5. Align the kprobe bar with the failure threshold.

**40 -> 50 kg/h:** minor disclosed tuning; it does not affect the contamination test.

**Applied:** key PASS (adopted fails 1.000; ≥1 viable 0.974); gates PASSED.
