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

## r2 light check (2026-11-06): two mechanical FIXes, both applied verbatim by the orchestrator, so CLEARED

1. CONF1.txt had CRLF line endings (from an orchestrator edit on Windows). Normalized to LF; a plain diff BASE/CONF1 now shows only line 7. CRLF was also found and fixed in p02 and p16 description files; .gitattributes now enforces LF for descriptions.
2. notes.md break-even margin reworded: the joint ×0.5 corner falls just below break-even and accounts for the 2.6% non-viable fraction.

Everything else is OK: the 10 µBq limit is coherent (~5% of the ER background below 18.6 keV), the kprobe bar is consistent, the scoring rule is recorded, and outcomes are unchanged. Gates PASSED.
