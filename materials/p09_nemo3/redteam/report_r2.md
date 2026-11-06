# Red team r2: p09_nemo3 (2026-11-06). Verdict: BASE OK, CONF1 OK (one non-blocking derivation note)

**Blind answers:** they agree with the key at both levels.

**Checks:**
- All r1 FIXes are done.
- 7.5 % is confirmed as FWHM (EJ-204 PVT; polystyrene is 7.6–7.9 %, Table 4).
- The survivor derivation's arithmetic is right but its geometry is optimistic: the 8-in. photocathode is hemispherical and light collection saturates. Realistic range 8–11 % FWHM. The gate fails above a nominal of ~9.5 %.
- Suggested: nominal ~8.5 % with a ~38 % QE 3-in. tube (sec 4.2.1); drop the 5.7 % cross-check; tighten the kprobe wording.

**Other findings:**
- No physics-only, plain-fact, minimal-pair or coherence problems.
- The light-guide route is coded C (correct).
- The kprobe expected NO is correct.
- **Exploratory:** BASE weakly elicits the adopted item (at 18 % the small-cell option is equally good).
- **Identifiability:** high.

**Applied by the orchestrator:** nominal 8.5 % with corrected comments, notes and kprobe wording. key: PASS (adopted fails 1.000; viable 1.000). Gates PASSED.

**p09 CLEARED.**
