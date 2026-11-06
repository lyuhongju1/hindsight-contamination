# Dossier: p15_aligo (Advanced LIGO -> A+ readout)

## Baseline as built (O1, 2015)
Source: LIGO Scientific Collaboration, "Sensitivity of the Advanced LIGO detectors at the beginning of gravitational wave astronomy", PRD 93, 112004 (2016), arXiv:1604.00439.
- Two dual-recycled Fabry-Perot Michelson interferometers (Hanford, Livingston), 4 km arms, 1064 nm Nd:YAG pre-stabilised laser (~20-25 W input in O1, ~100 kW circulating arm power).
- Test masses 40 kg fused silica on quadruple pendulum suspensions; in-vacuum seismic isolation (BSC/HAM ISI platforms).
- GW readout: DC readout. A small differential-arm (DARM) offset (~10 pm) lets carrier leak to the antisymmetric port; this carrier is the local reference field, co-propagating with the signal sidebands, filtered by a suspended output mode cleaner (OMC) on the HAM6 isolated platform, detected on in-vacuum DC photodiodes (~20 mA).
- O1 strain sensitivity ~1e-23 /rtHz near 100 Hz; BNS range ~60-80 Mpc. Goal: first direct detection of compact-binary coalescences.

## Item targeted
Balanced homodyne readout in A+ (replacing DC readout). Only one counted item in the row. A separate carrier beam picked off inside the interferometer is routed to the output and combined with the antisymmetric-port beam on a 50/50 beamsplitter; two OMCs; differential photocurrent. Motivation: removes the DARM offset (and its laser-noise and radiation-pressure couplings), allows choosing the readout quadrature (useful with frequency-dependent squeezing), reduces sensitivity to laser technical noise.

## Commitment document
arXiv:1304.0670v7 (2019-09), "Prospects for observing and localizing gravitational-wave transients with Advanced LIGO, Advanced Virgo and KAGRA" (Living Reviews), as verified by both daters in search/SELECTED_PAIRS.md (A2 update). Caveat from row: the 2018 A+ design curve (LIGO-T1800042) may already include it; not on arXiv.

## Alternative not adopted
Keep DC readout (DARM offset; reference field co-propagating with signal).

## adoption_status
approved not built -- UNVERIFIED (from knowledge: BHD was part of the A+ design; to my knowledge it was not installed for O4 and its schedule relative to O5 was uncertain/deferred). No web fetch made.
