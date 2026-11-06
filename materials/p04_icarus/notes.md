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
