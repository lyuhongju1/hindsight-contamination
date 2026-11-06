# Red-team report, t2k_nd280 round 2

*The agent's own Write call to this file was blocked by the harness ("Subagents should return findings as text"). The agent did not work around the block and returned its findings as text. The orchestrator saved them here verbatim, 2026-11-05.*

| Level | Blind agreement | Verdict | Reason |
|---|---|---|---|
| BASE | Yes (3D plastic-scintillator cubes pass) | OK (minor) | Passes every stated fact (7.7% H < 20%, 5 Gy negligible, warm, 0.3 T fine). The 1.9 × 1.8 × 0.6 m target region nearly copies the real one (~1.92 × 1.84 × 0.56 m); rule 7 asks for variation. |
| CONF1 | Yes on the failure, no on the survivors | DROP (replace the mechanism) | The key has no temperature check, so the LAr and LXe TPCs survive despite "room temperature", leaving only the gas TPC. 5 MGy ≈ 1.6e16 MIPs/cm² ≈ 1e13 muons/s through the target: the gas TPC, its readout and the drift chambers could not reconstruct anything. Any dose that damages plastic (> ~1e4 Gy) implies rates no near detector can handle, so retuning the number cannot fix it. |
| CONF2 | Yes on the failure, no on the survivors | FIX | The key's only survivors (LAr and LXe TPCs) contradict the stated room temperature. Its warm gas TPC uses Ar:CH4 at 1.06% H, which fails the limit. Coded honestly, nothing survives. The 1% limit also acts in effect as a "no hydrogenous material" rule. |

**Notes:**

- **CONF1.** The key's dose exemption for the gas TPC rests on `medium_renewed`, a boolean that is never varied. Only the gas is renewed, not the field cage, readout plane or electronics, and CH4 ageing at that dose is severe. The K-probe question and its "no" are correct.
- **Fix for CONF2.** Either add temperature to the key, or remove the room-temperature sentence from all three texts. Removing it is cleaner: a LAr TPC becomes legitimately viable and two distinct options survive. Replace Ar:CH4 with a cited low-hydrogen gas: Ar/CO2 or Ar/CF4 (0%), or Ar/CF4/iC4H10 95:3:2 (~0.48%). The K-probe question and its "no" are correct.
- **Robustness 0.999 / 0.988 is misleading.** The properties that decide the survivors (`medium_renewed`, `all_angles`) are booleans that are never varied, and the short-proton requirement is not coded at all. notes.md admits most of these weaknesses but not the room-temperature contradiction, which breaks both conflicts.
