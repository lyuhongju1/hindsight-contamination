# Red-team report r2, p02_gerda (returned as text; saved by the orchestrator, 2026-11-06)

**Verdicts:**

| Level | Verdict | Reason |
|---|---|---|
| BASE | OK | — |
| CONF1 | FIX (minor) | All r1 fixes hold; the failure is deterministic |

**Source check.** 14.3(2.1) verified: EPJC 78 (2018) 15, Table 2 and Sec. 3.1. It is a pre-cut beta-region factor, assumed to multiply with the post-cut factors as in the source paper's Table 6.

**FIX items:**
1. Document the scope of 14.3 in notes.md and the key comment, and remove the "not refetched" wording.
2. Key comment: replace the stale "radon emanated inside the array" phrase.
3. Description sentence 5 (both files): "The planned instrument uses the prototype's cryostat, argon recirculation system and trap: the radon in the argon is emanated by …".
4. Description sentence 6 (both files): "the contribution at Q from these radon progeny on the detector surfaces …", plus "(radon-progeny gammas are included in the other contributions)".
5. notes.md circulation arithmetic: T ≤ ~2.95 d (≥ 6.8× faster), not 4.4 d.

**Open routes:**
- faster circulation and lower-emanation components remain valid packages, scored C;
- 214Bi-Po delayed tagging is an analysis change capped at ~2× (below 2.25×);
- thicker dead layer is a second survivor.

**No route makes underground argon alone sound in CONF1.**
