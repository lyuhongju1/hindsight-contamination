# p04_icarus notes

## Design choices
- Target item: one serial ADC per wire channel with synchronous sampling (warm, outside the vessel), replacing multiplexed ADCs. Only counted item in the row.
- BASE: invented ~300 t LAr TPC (20,000 wires, 4 mm pitch, 1.8 m drift) moving to a shallow site; new vessel with 40 roof ports (20 cm) for wire signals. Per-channel synchronous digitization passes all stated requirements (S/N, 50 ns common time reference, continuous recording, dead time) and port capacity (40 x ~600 pairs = 24,000 >= 20,000).
- CONF1 (minimal edit: number of ports assigned to wire signals 40 -> 8). Mechanism: feedthrough capacity. Any outside-vessel digitizer needs one analog pair per wire through the wall; 8 x ~600 = 4,800 << 20,000. Digitizing and serializing inside the liquid (~16 channels per pair-equivalent) gives ~77,000 capacity. Workaround closed by plain fact: "the roof shell cannot take additional openings" and ports are the only penetrations.
- CONF2: not written. A cable-capacitance noise mechanism (long analog cables to a remote anode) was considered but its margins (warm/cold ENC ratio ~2-3) cannot survive x0.5-2 variation of preamp slope and cable pF/m.
- Descriptions name no readout technology; the existing readout is described only by its behaviour (10 bit, 500 ns, staggered sampling instants). Forbidden-term check: gates.py.

## Survivors per CONF
- CONF1: 1 (cold_asic: in-liquid front end with digitization and serial links). Multiplexed warm readout fails (port capacity, 50 ns timing, dead time).

## Fixed inputs (not varied)
- n_wires = 20000, ports = 40/8, snr_req = 10, skew_req_ns = 50, drift_ms = 1.2: exact stated facts in the description.
- dead_req = 0.03: stated "dead time below a few percent", taken as 3%.
- warm_ch_per_pair = 1: integer structural count; an analog signal digitized outside the vessel needs its own conductor pair through the wall.

## Cited properties (author knowledge, no web fetch; unverified)
- ~600 signal pairs per 20 cm roof port: overhauled T600 flanges carry ~576 wire channels each.
- Cold front end ~16 channels per pair-equivalent: 128-channel cold boards (DUNE-type) use ~4 data links plus clock/control and power.
- ENC: warm ~1200 e, cold ~500 e; MIP induction signal on 4 mm wires ~15,000 e (2.1 MeV/cm, W = 23.6 eV, ~0.7 recombination survival, ~0.6 induction fraction).
- No unc ranges used; all props varied x0.5-2.

## Post-run change log
- Run 1: CONF1 with 6 ports gave >=1_viable = 0.949 (FAIL, survivor capacity margin too thin: 6 x 600 x 16 = 57,600 vs 20,000 under a product of two varied props). Changed CONF1 stated port count 6 -> 8 (adopted still fails in 100% of draws: max 8 x 1200 = 9,600 < 20,000). Run 2: PASS (0.980). No property values changed.

## Doubts
- The mechanism is geometric/feedthrough capacity rather than detector physics proper; a red team may judge it close to an engineering constraint. Justification: it is a stated physical fact about the vessel, not cost or schedule.
- A hybrid answer (cold preamplifier + per-channel ADC inside the vessel) would also survive and might be scored as "adopted" by the regex (per-channel ADC). The real adopted item is warm, outside the vessel; scoring should be checked against this.
- adoption_status (built and operated) from author knowledge; citation unverified.

## r1 revision (after red team report_r1.md, 2026-11-06)
### Outcome: no honest CONF exists for the counted item; p04 yields no unit (PREREGISTRATION §7)
The counted item is "one serial ADC per channel with synchronous sampling, replacing multiplexed ADCs". I looked for a stated physical requirement that this choice itself fails while another option (multiplexed/staggered sampling, or another architecture) passes. No web fetches were used. Candidates and why each fails:
- **Power or heat budget** (for example, electronics in the liquid where boiling must be avoided). ADC power scales with total conversions per second (Walden figure of merit). One ADC multiplexed 16:1 at 16x the rate dissipates about the same as 16 per-channel ADCs. No robust ×0.5–2 margin, and the lever is really the location of the electronics, not the ADC architecture.
- **Coherent pickup from synchronous switching.** All ADCs sampling at the same instant inject a correlated disturbance. It sits at the sampling clock (above the shaping band) and aliases to a pedestal shift that can be subtracted. It depends on implementation, not physics, and staggered sampling only spreads it out.
- **Channel-to-channel matching.** A shared ADC gives identical gain and nonlinearity across its channels, but per-channel mismatch (~0.1–1%) is calibrated with test pulses. Making this decisive would need an exclusion-style fact ("no calibration"), which rule 2 forbids.
- **Timing, bit depth, bandwidth and dead time.** Per-channel synchronous sampling is better or equal on every one of these.
- **Count, space or cost of components.** These are the real trade-offs, but rule 1 and the coordinator exclude them.
Conclusion: on physics alone, per-channel synchronous digitization dominates multiplexed sampling. Its disadvantages are density, power-per-board engineering and cost, not a physical requirement it fails. I could not write an honest CONF1.

### r1 changes (all files)
- `descriptions/CONF1.txt` (40 -> 8 ports): withdrawn, moved to `abandoned/CONF1_r0_ports.txt`. The red team was right that it tested whether the electronics sit outside the vessel, not the counted item, and that it was an infrastructure lever.
- `kprobe.json`: the r0 CONF1 probe moved to `abandoned/kprobe_r0.json` (it also used the 600 pairs/port figure that the description withheld). `kprobe.json` is now `{}`, since there is no CONF.
- `descriptions/BASE.txt`:
  - Removed the roof-port sentence. It existed only as the shared fact for CONF1, and its 1.2x margin failed about 40% of draws.
  - Changed the stated S/N requirement from 10 to 6 (logged post-run change, rule 6). Reason: the nominal margin was 1.25x (15,000 e / 1,200 e = 12.5 vs 10). With 6 it is 2.08x, meeting the coordinator's >=2x margin for BASE. An S/N >= 6 on induction planes is still a credible LAr TPC requirement.
- `keys/key.py`: BASE-only. It reports per-requirement nominal margins (min 2.08x) and the fraction of x0.5–2 draws in which the adopted item passes (0.893; informational, since S/N is a ratio of two varied properties). It exits non-zero if the nominal margin is below 2x. The r0 key and output are in `abandoned/`.
- NAME/ANON are unchanged. Survivors per CONF: none (no CONF).
