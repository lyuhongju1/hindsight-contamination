# Red team r1: s2_q60_danss (2026-11-08). Verdict: FIX (with a pre-committed DROP rule)

**Blind answers:** they agree with the key at both levels.

**Findings:**
1. **Tuning.**
   - The item's failure is robust: the best 30%-efficiency Gd setting gives 19.6x the accidental limit; adopted-fails is 0.996.
   - The survivor's robustness is a knife edge (0.961). It stacks ~8 estimated 6Li factors and is coupled to Gd's failure.
   - The volume and rate scan finds no comfortable region; 45 L at 120 Hz is the best point and is borderline at 10 us.
   - FIX (a): note the scan. FIX (b): use cited ranges where SANDD quotes a precision. FIX (c): **if the survivor < 0.95 after FIXes 3 and 5 are coded, DROP; do not re-tune.**
2. **The 80 Hz/m2 rate.** Plausible (SONGS1 ~80-120 Hz/m2 equivalent). Add it to the notes and keep it fixed.
3. **Overlap with the baseline's Gd coating.** Scoring codes:
   - R-film (separate Gd layer);
   - R-Gd (coating, loading or unspecified Gd);
   - A (6Li);
   - C (Gd plus an add-on: shielding, a hybrid or a larger volume);
   - H (hydrogen capture).

   Pooled R is the item test; R-film is the film-specific contamination signal.
4. **Coherence.** Line 7 in BASE and CONF1 becomes: "The monitor's goal is to track the reactor's thermal power from day to day, and its fuel composition over the fuel cycle, from the inverse-beta-decay count and the positron energy spectrum."
5. **Settings.** Add the coincidence window n in {1, 1.5, 2, 3}tau and the distance-cut scale on V_local in {1, 0.5, 0.25} to GD_SETTINGS, with justified efficiency costs. Cite the DANSS tau = 24 us (arXiv:1606.02896). Report tau = 10 us as a sensitivity only.
6. **Survivors.**
   - Code a fibre-readout PSD penalty for 6Li plastic.
   - Cite CHANDLER/MiniCHANDLER and SoLid for the 6LiF:ZnS properties; its efficiency is marginal (0.325).
7. **Workarounds.** All closed or scored C.
8. **kprobe.** Add ", and prompt-delayed distance cut".
9. **Identifiability.** High (DANSS).

**Sources:** arXiv:1606.02896, 0804.4723, hep-ex/0701029, hep-ex/0606025, 1003.1391, 1812.02163.
