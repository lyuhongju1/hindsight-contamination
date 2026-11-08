# Feasibility (lesson 5): q54, q55

## q54 HERMES -> Recoil Detector
- C1 route dose/SR: a silicon-killing synchrotron or beam-halo dose behind a ~0.1-1 mm Al wall is barely attenuated for keV-MeV photons and charged halo, so trackers outside the wall get the same dose. Both fail together, so there is no survivor.
- C1 route wakefield/RF heating: HERMES-type silicon sits behind the storage-cell wall, which carries the image current. Where the module is mounted behind the cell or a thin RF screen is a setting of the item (C1), so this does not kill the item in every implementation.
- C1 route low-p threshold: the physics favours the item. A 135 MeV/c proton has T~9.7 MeV, CSDA range ~0.2 g/cm2. A self-supporting vacuum wall (~0.15 g/cm2 Be to 0.27 g/cm2 Al at r~5-10 cm) plus the cell wall gives a threshold of ~135-160 MeV/c outside, versus ~100-125 MeV/c inside. The outside-only alternative fails; the item passes.
- C1 route outgassing/target polarisation: the cell is pumped separately, and this is not a robust x0.5-2 mechanism.
- C1 VERDICT: NO WINDOW. No physical requirement fails in-vacuum silicon in every implementation while outside-only tracking passes all requirements.
- C2 route material/low-p threshold: fibre diameter and layer count are settings. 0.25-1 mm fibres in 2-4 layers give 0.05-0.4 g/cm2, which spans the drift-chamber wall/window budget. Low-p protons are already covered by the inner silicon. The window is x<2, not robust.
- C2 route rate/timing: 96 ns HERA bunch spacing versus drift times of a few hundred ns, and a high halo rate near the beam. Both favour the fibres (item), not gas.
- C2 route 1 T field: fibres with clear-fibre/MAPMT readout outside the field work. The drift-chamber Lorentz angle is correctable. Neither fails.
- C2 route multiple scattering: 1% X0 of fibres gives theta0 ~5 mrad at 500 MeV/c protons, negligible and tunable by fibre thickness.
- C2 VERDICT: NO WINDOW.

## q55 PandaX-I/II -> PandaX-4T
- D1 route muon-induced neutrons: these are made more in Pb (yield per g/cm2 ~A^0.76, about 6x water). This favours the water item, so it cannot fail water.
- D1 route gamma attenuation per thickness: 2.6 MeV attenuation length is ~23 cm water versus ~2 cm Pb. Water fails only under a thickness/hall-size limit, which is a SPACE rule and forbidden. Without one, thicker water passes.
- D1 route radiopurity: 210Pb bremsstrahlung and U/Th in Pb hurt the layered shield, not water. Ultrapure water has U/Th/K far below Pb/PE.
- D1 route neutron moderation: water is hydrogenous, comparable to PE. No separation.
- D1 route radon/active veto: radon displacement by water, and the Cherenkov veto (add-on), both favour water.
- D1 VERDICT: NO WINDOW. Every physical mechanism favours the adopted water shield or is space-bound.
- D2 route x-y resolution near wall: sigma_xy ~ pitch/sqrt(N_pe). Pitch 3" (~8 cm) versus 1" (~3 cm) gives an item/alternative ratio of ~2.7. A x0.5-2 window needs >=4 once S2 size and pitch vary. PMT-to-liquid-surface distance and reconstruction are also item settings. Not robust.
- D2 route light collection/threshold: 3" PMTs give higher photocathode coverage and lower dead area. This favours the item.
- D2 route PMT radioactivity per photocathode area: the R8520 is higher per cm2 than the R11410. This favours the item.
- D2 VERDICT: NO WINDOW. The only adverse mechanism (position resolution) has a factor of ~2.7, below the x4 needed, and is partly tunable by mounting height.
