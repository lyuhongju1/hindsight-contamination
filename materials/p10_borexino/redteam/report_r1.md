# Red-team report r1, p10_borexino (returned as text; saved by the orchestrator, 2026-11-06)

**Verdicts:**

| Level | Verdict | Reason |
|---|---|---|
| BASE | FIX (wording only) | — |
| CONF1 | **OK, with the same wording FIX** | Failure honest and kinematically robust (~150× short); deuteration coherent; 51Cr survivor credible (~2× demonstrated activity) |
| kprobe | FIX | — |

**Independent checks (red team's own calculations):**
- residual 1H gives ~10 IBD events;
- spectrum-averaged IBD cross section 3.95e-44 cm² per decay (key: 4e-44);
- CC threshold on deuterium 4.03 MeV > 2.9975 MeV endpoint;
- NC breakup open for ~24% of the spectrum but gives no per-event energy;
- ES cross sections for 51Cr and 37Ar within 15% of the key.

No route rescues the Ce item: ×150 activity breaks heat and shielding; moving the source is closed by wording; swapping the solvent is closed by wording; no isotope has an endpoint above 4.03 MeV.

**FIX items:**
1. The counting window is a hidden decisive choice: S/B is computed over one mean life, while a full-18-month reading kills both survivors. Reword identically in BASE and CONF1: "Over the counting period chosen for the analysis, source-induced interactions in the selected energy window must outnumber background events in that window." Alternatively, vary the window length in the key (τ × [1–3]).
2. The kprobe could be answered YES by keeping only the tagged events. Use the reworded question (expected NO) that asks for ≥ 1500 interactions with ≥ 80% energy-reconstructed, across all channels.
3. notes.md: neutron capture in C18D30 is dominated by 12C (~65%; 4.95 MeV line; ~20 ms capture time), not D (6.25 MeV). Correct this; it does not change the outcome.
4. Cite the standard ES formula in the notes instead of "estimate".

**Identifiability:** high (Borexino/SOX).
