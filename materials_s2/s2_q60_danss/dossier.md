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
- The pair is BASE 0.9 m3 against CONF1 30 L. Both have the same 5 cm polyethylene layer, the same 3 GWth core at 10 m, and the same ambient rate of 80 Hz/m2 above 1 MeV. The positron spectrum must be recorded from 1 MeV, the delayed efficiency must be >= 30%, and accidentals must be <= the signal.
- In CONF1 the Gd cascade mostly escapes:
  - At thresholds of 2.6 MeV and above, efficiency is 0.04-0.12.
  - At thresholds of 1.0-2.0 MeV, accidentals are 6-28 x the signal, even with a topology cut.
- 6Li-PSD plastic (0.47 efficiency, 0.17 acc/signal) survives, and so do 6LiF:ZnS sheets.
- keylib: BASE PASS; CONF1 PASS (0.996 / 0.961). See notes.md for the narrow-window caveats.

## Citations
- PANDA36: arXiv:1404.7309 (35.5% delayed efficiency, 350 L, above 3 MeV).
- SANDD: arXiv:2105.00083 (34.8% neutron efficiency, 9 L, 51.9% escape).
- DANSS: arXiv:1606.02896. DANSS upgrade: arXiv:2112.04973.
