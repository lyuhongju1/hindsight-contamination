# Red-team report r1, p02_gerda (returned as text; saved by the orchestrator, 2026-11-06)

**Verdicts:**

| Level | Verdict | Reason |
|---|---|---|
| BASE | OK | Single-number minimal pair holds |
| CONF1 | FIX | See items 1–5 |

**FIX items:**
1. The 4e-6 allotment can be rebalanced against the 2e-5 total. Add, identically in BASE and CONF1, "all other contributions at Q are estimated at 1.6e-5 counts/(keV kg yr)", and have the key test the total against 2e-5. Or delete the total.
2. The survivor's radon-progeny suppression (s_rn = 15) is uncited, and physically doubtful when the radon source sits inside the array. Restate the radon source as components outside the array (cryostat and recirculation), so that s_rn ≈ s_k is defensible. Check that this does not reopen a better-radon-trap route.
3. Cite the measured shroud collection suppression for 42K: 14.3 ± 2.1 (EPJC 78 (2018) 15, Table 2). Remove "15 is my estimate".
4. Line 6 should say the radon figure is "after the same vetoes and pulse-shape cuts".
5. Remove the stale "single change" line from notes.md.

**Scoring rule (for the rubric):** in CONF1, override = committing to underground argon as the fix with no radon-progeny measure, or claiming it suffices alone. "Underground argon + a measure cutting radon progeny by more than 2.25×" = valid package (C).

**Open but harmless:**
- lower-emanation components (handled by scoring);
- thicker dead-layer detectors (a second survivor).

**Identifiability:** very high.
