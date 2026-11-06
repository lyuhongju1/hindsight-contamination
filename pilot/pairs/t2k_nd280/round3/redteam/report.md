# Red-team report, t2k_nd280 round 3

*Returned as text by the red-team agent (no files written, no web fetches, no denied tools). Saved by the orchestrator, 2026-11-05.*

| Level | Blind agreement | Verdict | Reason |
|---|---|---|---|
| BASE | Yes | OK | 46.8 ≤ 60 MeV, 0.9 ≥ 0.25, 7.7% ≤ 20%; field and fibre length fine. |
| CONF1 | Yes (gas TPCs survive) | FIX (DROP if no second distinct survivor class) | The physics of the failure is right: a 12 MeV proton travels ≈ 1.7 mm in polystyrene and stays inside the vertex cell. But the survivors are one technology at two pressures, and the 1-atm option (~4.5 kg) is not a credible neutrino target, so in effect there is one survivor. A stated rate or mass requirement would leave one class; LAr cannot be brought in by moving the threshold (its ~21–47 MeV threshold against the cubes' 46.8 MeV leaves no room for a ≥ 2.6× margin). The 10-atm option is also optimistic: a rectangular 10-atm vessel is unrealistic, a cylinder in the 0.9 m depth holds ~27 kg, and the wall mass exceeds the gas. Also fix the calorimetric loophole: say explicitly that the protons need their direction and energy measured. |
| CONF2 | Yes (LAr top, gas TPC runner-up) | OK (minor) | LAr and the 10-atm Ar gas TPC are distinct classes and pass every stated fact. The 1-atm survivor is weak but not needed. |
| K-probe | — | CONF1 FIX / CONF2 OK | The CONF1 question states the ~2 mm range, which is the answer. Remove it, and ask for a "track with measured direction". CONF2 is correct and neutral. |

**Confirmed by the red team:**
- target masses;
- the 1-atm threshold scaling;
- hydrogen fractions (polystyrene 0.0769, Ar:CF4:iC4H10 95:3:2 at 0.48%);
- no booleans used;
- the CONF2 robustness worst case (3.85% against the 4.0% limit) holds.

**Identifiability is high** (0.7 GeV, an off-axis-style near station, a warm low-field dipole, emphasis on high-angle muons). This is measured, not gated.
