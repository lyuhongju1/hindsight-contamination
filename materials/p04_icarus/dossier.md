# p04_icarus dossier

Sources: from author knowledge; no web fetches used. Items marked (unverified) were not checked against a primary source.

## Baseline as built (ICARUS T600, LNGS, CNGS run 2010-2013)
- Two identical LAr TPC modules, ~760 t total LAr, ~476 t active; each module has two TPCs sharing a central cathode, 1.5 m drift, 500 V/cm (drift ~1.6 mm/us, ~1 ms max drift time).
- Three wire planes per TPC (induction-1, induction-2, collection), 3 mm pitch, ~53,000 wires in total; wires up to ~9 m long.
- Readout: warm electronics outside the cryostat, signal cables through roof flange feedthroughs; analog boards with front-end amplifiers, 10-bit ADCs **multiplexed** over 16 channels, 400 ns sampling per channel (so channels inside a group are sampled at staggered times).
- PMTs (8-inch, TPB-coated) for the trigger. Deep underground (LNGS, ~3400 m w.e.).
- Physics goal at LNGS: CNGS nu_mu -> nu_tau/nu_e appearance, LSND-like anomaly search, atmospheric/solar studies.

## Target item
**One serial ADC per wire channel, all channels sampled synchronously, replacing the multiplexed ADCs** (only one counted item in the row). Implemented on new compact flange-mounted (warm) boards; 12-bit, 400 ns sampling (unverified for bit depth).

Motivation for the overhaul: T600 moved to shallow depth (~3 m overburden) as SBN far detector at Fermilab, 600 m from BNB target; ~11 cosmic muons per 1 ms drift window; need better S/N, no inter-channel time skew (simpler track/coherent-noise treatment), and higher readout bandwidth.

## Commitment document
arXiv:1503.01520 (2015-03), ICARUS-WA104 / SBN proposal (row 4 of SELECTED_PAIRS.md).

## Alternatives not adopted
1. Keep the multiplexed ADC architecture (existing warm boards).
2. Cold in-cryostat front-end ASICs (preamp, and possibly digitization, inside the LAr; as later chosen for DUNE).

## adoption_status
**built and operated**: the T600 was overhauled at CERN (WA104, 2015-2017), moved to Fermilab (2017), and has taken data in the BNB/NuMI beams since 2020-2021 with the new per-channel-ADC warm electronics. Source: author knowledge of ICARUS collaboration publications (e.g. ICARUS commissioning paper, Eur. Phys. J. C 2023) (citation unverified).
