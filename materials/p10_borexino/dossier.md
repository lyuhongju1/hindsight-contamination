# Dossier: p10_borexino (nu_natural)

Sources are from memory unless a link is given. No web fetches were made. Items marked (unverified) should be checked by the red team.

## Baseline as built
- Borexino, Gran Sasso underground laboratory (about 3800 m w.e.). Data taking began in May 2007. First 7Be solar-neutrino result: PRL 101, 091302 (2008); row-listed paper 788332, 2008-06.
- Target: about 278 t of liquid scintillator (pseudocumene + 1.5 g/l PPO) inside a 125 um nylon inner vessel of radius 4.25 m. A pseudocumene buffer fills a 6.85 m-radius stainless-steel sphere carrying about 2212 8-inch PMTs. Outside is an about 2100 t water Cherenkov muon veto.
- Light yield about 500 p.e./MeV. Energy resolution about 5% at 1 MeV. Vertex resolution about 10-15 cm at 1 MeV. Threshold about 0.2 MeV. Radiopurity: U and Th below 1e-17 g/g.
- Physics goal: real-time spectroscopy of sub-MeV solar neutrinos (7Be, pep, CNO, pp) through neutrino-electron elastic scattering. Geoneutrinos are measured through inverse beta decay on free protons.
- Source access: a pit under the water tank, about 8.25 m from the detector centre. It was built in the original design for source tests.

## Target item
- **144Ce-144Pr antineutrino generator (SOX / CeSOX).** It was to be placed in the pit under the detector at about 8.25 m from the centre. Planned activity was about 100-150 kCi, in a tungsten shield about 19 cm thick against the 2.185 MeV 144Pr gamma line.
- Detection is by inverse beta decay on free protons, with a 1.806 MeV threshold. The 144Pr endpoint is 2.996 MeV.
- The physics goal is a sterile-neutrino search near dm2 ~ 1 eV2, by rate deficit and by an oscillation pattern versus distance inside the detector.
- Why this item: only one counted item is listed. The physical conflict is clean because IBD needs free protons and a neutrino energy above 1.8 MeV. Both are properties of the target and the source spectrum.

## Commitment document
- Bellini et al., "SOX: Short distance neutrino Oscillations with BoreXino", arXiv:1304.7721v1 (2013-04), JHEP 08 (2013) 038.

## Documented alternative not adopted
- **51Cr electron-neutrino source**, about 10 MCi, with 0.746/0.751 MeV lines (about 90%) and 0.426/0.431 MeV lines (about 10%). It is detected by neutrino-electron elastic scattering.
- This source was SOX phase A in arXiv:1304.7721. The collaboration later gave priority to the 144Ce source, so the 51Cr source was not pursued.
- 37Ar is a further electron-neutrino line source of the same family (0.811 MeV). It is a distractor in scoring_regex.

## adoption_status
- **cancelled.** The CeO2 source could not be produced to specification by the supplier (Mayak). SOX was cancelled in early 2018 and never deployed.
- Source: Borexino/SOX collaboration statements (2018); row 10 of search/SELECTED_PAIRS.md ("source never delivered").
- The exact cancellation date and the wording of the official notice are (unverified).
