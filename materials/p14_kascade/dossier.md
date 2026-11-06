# p14_kascade dossier

Sources are cited from the author's knowledge; no web fetches were made. These are bibliographic pointers and have not
been re-verified this round.

## Baseline as built
- **KASCADE** (Karlsruhe, Germany): a particle-detector air-shower array of 252 scintillator stations on a 200 m x
  200 m grid, with a central hadron calorimeter and a muon tracking detector. Its goal was the cosmic-ray energy spectrum
  and composition around the knee (about 10^15–10^17 eV). Reference: Antoni et al., NIM A 513 (2003) 490.
- **LOPES**: the radio extension of KASCADE / KASCADE-Grande. Its antennas were inverted-V dipoles in the
  40–80 MHz band, triggered by the particle array. It first measured only the east-west polarisation, and later
  east-west and north-south. Reference: Falcke et al., Nature 435 (2005) 313.

## Item targeted
LOPES-3D tripole antennas: three orthogonal dipoles that measure all three electric-field components, including the
vertical one. This is the only counted item in row 14.

## Commitment document
arXiv:1303.6808v1 (2013-03), LOPES-3D (ICRC 2013 proceedings), from row 14 of search/SELECTED_PAIRS.md.

## Alternatives not adopted
Inverted-V dipoles with one or two horizontal polarisations, the existing LOPES design; LPDA and butterfly antennas
(row 14).

## adoption_status
**built and operated.** LOPES-3D stations were installed at KIT and took data until LOPES ended in 2013, as reported
in arXiv:1303.6808.

## Feasibility outcome
No robust physical conflict exists. The tripole is a superset of the horizontal-dipole measurement (see notes.md), so
no descriptions, keys or kprobe entries were produced. kprobe.json = {}.
