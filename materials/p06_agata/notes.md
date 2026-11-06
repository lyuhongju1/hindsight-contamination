# p06_agata notes

## feasibility (decided before any description was written; lesson 5)

Item (scoring_regex "item"): Ethernet-based readout of pre-processed data, i.e. the Phase-2
digitiser-to-farm path in which each crystal's digitised, FPGA-pre-processed preamplifier traces are
streamed over standard Ethernet to the processing farm. Alternative not adopted: the Phase-1
GGP/ATCA custom-backplane carrier boards feeding the farm over PCIe.

Figures used (from general knowledge of the AGATA design; no web fetch was made, the outcome does not
depend on their exact values, and each was varied x0.5-2 below):
- 38 channels per crystal (36 segments + core at two gains); sampling ~100 MS/s, 14-bit ADC (stored as 16 bit).
- Design maximum ~50 kHz per crystal; trace ~100 samples per channel per event after the local trigger.

Candidate 1: sustained bandwidth per crystal.
  38 ch x 100 samples x 2 B x 50 kHz = 0.38 GB/s = 3.0 Gb/s per crystal.
  x0.5-2 on every factor (4 factors) spans ~0.2-48 Gb/s. A 10 GbE link covers the nominal case;
  at the high corner the answer is more links per crystal (2x10, 25, 40 or 100 GbE, all standard),
  trace shortening, or on-FPGA compression. Lesson 4: more links, buffering and compression are
  routine. The ATCA/PCIe path faces the same per-crystal bandwidth and scales the same way
  (PCIe Gen3 x8 ~ 63 Gb/s vs 100 GbE). Neither option fails where the other passes across the box.
  Even fully streamed raw (untriggered) data, 38 x 100 MS/s x 16 b = 61 Gb/s, fits a 100 GbE link
  or a PCIe x8/x16 link alike. No window.

Candidate 2: latency / time synchronisation for a physics trigger.
  Timestamps are applied at the digitiser from a distributed clock (separate global
  timing/trigger distribution); the transport to the farm only has to deliver data within the
  buffer depth, not with fixed latency. The time resolution needed for coincidences with
  ancillary detectors (ns-level) is set by the clock distribution and the pulse-shape timing,
  not by the data link. A hard-real-time first-level trigger with a few-us fixed latency
  would be met by keeping the decision on the digitiser FPGA or a separate trigger path
  (the add-on route of lesson 3, and routine per lesson 4). Ethernet's variable latency
  (us-ms) is absorbed by memory buffers of ~GB, i.e. seconds of data. No window.

Candidate 3: packet loss and deadtime at stated rates.
  UDP/TCP over a dedicated, non-shared link at <50% occupancy has negligible loss; lost
  packets would be a transport engineering issue fixed by flow control, TCP or link
  over-provisioning (routine). Deadtime is set by the digitiser trigger/pre-processing
  and the farm (pulse-shape analysis CPU), which are identical for both transports.
  No window.

Other physical properties considered: radiation (digitisers sit near the array in both
schemes; no difference), power/heat in the electronics (engineering, and comparable),
cable length (fibre for both), electromagnetic noise pickup into the HPGe preamplifiers
(set by digitiser placement and grounding, not by the transport protocol downstream).

Conclusion: every separating property between the two readouts (cost, use of commercial
switches, vendor support for ATCA, maintainability, scalability of the farm, schedule) is
non-physical (rule 1). Any physically stated rate or latency requirement that defeats
Ethernet within x0.5-2 defeats the ATCA/PCIe path equally, or is closed by a routine add-on
(more links, buffering, compression, FPGA-side trigger). No honest CONF exists.
Outcome: zero units; kprobe.json = {}; no descriptions or keys written.

## doubts
- Figures were not re-verified by web fetch (none needed: the conclusion holds over x0.5-2
  and beyond, since both transports scale with standard link counts).
- The selected-pairs row already marks this pair as "Weak" with a 2016 first commitment not on arXiv.
