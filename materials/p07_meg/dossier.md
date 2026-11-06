# Dossier: p07_meg

Status of sources: written from memory, no web fetches. Any item marked (unverified) was not checked against a document in this task.

## Baseline as built
- MEG (PSI piE5 beam line), physics run 2009-2013; final result arXiv 1605.05081 (BR(mu+ -> e+ gamma) < 4.2e-13, 90% CL). The pair row cites the MEG detector baseline (INSPIRE 1223321, 2013-03; detector paper).
- Surface mu+ beam (about 28 MeV/c), about 3e7 mu+/s stopped in a thin slanted polyethylene target at the centre of a gradient-field superconducting solenoid (COBRA; about 1.27 T at the centre, falling toward both ends). The gradient sweeps positrons out quickly and gives a bending radius nearly independent of emission angle.
- Positrons: drift chambers plus scintillator timing counters. Photons: about 900 l liquid-xenon calorimeter with PMTs.
- Signal: back-to-back 52.8 MeV e+ and gamma, in time. The dominant background is accidental: a Michel positron plus an uncorrelated high-energy photon from radiative muon decay (RMD) or from positron annihilation in flight.

## Target item (adopted in MEG II)
- Radiative decay counter on the beam axis downstream of the target. A high-energy RMD photon (Eg > ~48 MeV) comes with a low-energy positron (about 1-5 MeV). That positron has small transverse momentum, so it spirals along the axis and is carried by the gradient field to the downstream end. There a counter made of plastic scintillator timing plates and LYSO crystals (energy) tags it in time with the photon, and the accidental-photon background is vetoed.
- Commitment document (from row): MEG II design report, arXiv:1801.04688 (2018-01).
- Projected effect: the downstream counter tags a sizable fraction of the RMD photons in the analysis window, about a 10-20% reduction in accidental background (unverified exact figure).

## Documented alternative, not adopted
- Upstream RDC: a second counter upstream of the target, in the beam path. It would also catch the RMD positrons that go upstream, but it must sit in the full muon beam (about 1e8/s). It therefore has to be very thin (scintillating fibres) so it does not degrade the beam, and it must cope with the beam rate. It was studied in the design report and not built in the baseline (unverified details).

## adoption_status
- **built and operated**: the downstream RDC was installed for the MEG II engineering and physics runs (2021 onward). Basis: my knowledge of MEG II run papers. Not verified against a document in this task.
