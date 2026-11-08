# Dossier: s2_q60_danss (PROVISIONAL; second dater still running)

## Baseline as built
- DANSS (2016): about 1 m3 of segmented plastic scintillator, 2500 strips of 1x4x100 cm, coated with a Gd-loaded reflective layer (Gd2O3 in the TiO2 coating), read through WLS fibres by SiPMs (each strip) and PMTs (modules of 50 strips). The detector sits on a movable lifting platform below a 3.1 GW(th) WWER-1000 core at the Kalinin NPP, 10.7-12.7 m from the core centre. It has about 50 m water equivalent of overburden from the reactor structures. Physics goal: a search for sterile neutrino oscillations at short baselines, via the ratio of positron spectra at different distances, plus reactor monitoring. Sources: Alekseev et al., JINST 11 (2016) P11011, arXiv:1606.02896. Upgrade: arXiv:2112.04973.
- Delayed signal in DANSS: neutron capture on Gd, about 8 MeV cascade, with a delayed-energy cut of a few MeV, in a 1 m3 volume that contains much of the cascade.

## Item targeted
- Neutron tagging by gadolinium capture, in any implementation (coating, film, or loaded plastic). The upgrade moves Gd into separate Gd2O3-polyethylene films. Item 1 (strip geometry) has no window (feasibility_q60.md).

## Commitment document
- arXiv:2112.04973 (DANSS upgrade), as in the candidate row. The film specification has not been checked here (it comes from the candidate row).

## Alternatives not adopted
- 6Li capture with pulse-shape identification: 6Li-doped PSD plastic (SANDD, arXiv:2105.00083) or 6LiF:ZnS sheets (SoLid).

## adoption_status
- built and operated (Gd tagging is in operation in DANSS; the upgrade retains Gd films). Source: arXiv:2112.04973 and the DANSS operation papers. The upgrade build status is not checked here.

## Mechanism (Route A of feasibility_q60)
- In a compact stated volume (about 25 L), the Gd cascade mostly escapes. A delayed threshold above 208Tl (2.6 MeV) gives low efficiency. A low threshold admits the ambient gamma singles rate, so accidentals exceed the stated accidental-to-signal limit. 6Li with PSD survives both.
