# Feasibility (lesson 5) for q50 and q51, 2026-11-07

## q50 (JLab Hall A 2004 to SoLID-class large-acceptance 11 GeV fixed target, solenoid)

### A1: MRPC TOF (adopted) vs scintillator TOF. Verdict: NO WINDOW
- Rate: low-resistivity glass MRPCs (~1e10 ohm cm, Tsinghua) show 93% efficiency and ~80 ps (sigma) at 70 kHz/cm2; ceramic MRPCs show ~95% at ~2e5 Hz/cm2 (p16 red team). The SoLID requirement is >20 kHz/cm2. A robust failure (rate x0.5 still above capability x2) needs a stated charged rate of >=0.3-0.8 MHz/cm2 at the TOF plane. That is 15-40x the rate at ~1e37 with shielding. It implies ~1e38.5+ with large acceptance, which breaks the class (the p16 pattern). Electrode resistivity, temperature and gap count are settings within the item (lesson 4) and push the capability higher still.
- Timing: pi/K at 7 GeV/c over ~8 m gives dt ~61 ps, so 3 sigma needs ~20 ps (sigma). MRPCs at ~20 ps are marginal, and any credible survivor (LGAD ~30-40 ps, scintillator ~60-100 ps) fails too. At low momentum (~2.5 GeV/c, dt ~0.5 ns) everything passes. No robust band.
- Magnetic field: favours the MRPC (field-insensitive). PMT-read scintillator is the one that suffers. Wrong direction.
- Material: the TOF sits behind the trackers and in front of the calorimeter. The few-% X0 windows of the MRPC and the scintillator overlap under x0.5-2. No separation.

### A2: GEM tracking (adopted) vs drift chambers. Verdict: NO WINDOW
- Rate: GEMs handle ~1e5-1e6 Hz/mm2, while drift chambers saturate at ~1e4-1e5 Hz/cm2. Rate favours GEMs at any SoLID-class luminosity. Wrong direction.
- Material: triple-GEM ~0.4% X0 per plane (~0.2% with thin/Cr foils, a setting within the item) vs He-based DC ~0.1-0.3%. A material requirement that robustly kills the GEMs (after x0.5 on their material) needs <~0.1%/plane total. Only a low-rate DC passes that, so luminosity must drop by >~100x, which leaves the class. Coherence fails.
- Resolution (~70 um sigma GEM vs ~100-150 um sigma DC) and field (small Lorentz angle, set by the item) do not separate them robustly.

## q51 (DRIFT-II-class negative-ion-drift directional TPC)

### B1: CS2:CF4 (30:10 Torr) F target (adopted) vs pure-CF4 electron-drift TPC. Verdict: NO WINDOW
- F mass per volume: the CF4 partial pressure and the CS2:CF4 ratio are settings within the item. CS2 capture works at a few Torr (capture length ~mm or less), so the mixture can match the F density of pure CF4 at any stated pressure. A stated total-pressure or track-length limit costs the mixture at most ~1.3-2x in recoil range, which is inside x0.5-2. Not robust, and the CS2 fraction itself is a setting.
- Diffusion: NID is thermal (sigma ~0.6 mm at 50 cm, ~600 V/cm); electron drift in CF4 at ~50-100 Torr gives ~mm or more at long drift. A long stated drift kills the alternative, not the item. Wrong direction.
- Drift length: a short drift (<~20 cm) lets pure CF4 pass, but the item still passes. No failure of the item.
- Untested lead, not a window: CS2 quenches CF4 scintillation. A stated retained optical (camera) readout would hurt the item. The numbers are unverified, and it rests on a readout-class fact, so it needs a fetch before anyone uses it.

### B2: O2 additive minority carriers (adopted) for z vs diffusion-width z. Verdict: NO WINDOW
- Peak separation: the minority peaks arrive a few % to ~10% earlier, so dt scales with drift (~ms at 50 cm, falling linearly). Diffusion width also shrinks at short drift, so short drift weakens both methods together. No robust band where the minority method fails and the width method passes.
- Low ionisation: the minority fraction is ~few %, so few-keV recoils give O(10) minority charges, which is marginal. But NID thermal diffusion (~0.6 mm at full drift) is comparable to the track extent, so width-based z also fails at low energy. The O2 fraction is a setting (lesson 4).
- O2 attachment losses: with ~1 Torr O2 in ~40 Torr CS2-based gas, CS2 capture dominates and the charge loss is small. Not robust.

Sources: Tsinghua low-resistivity-glass MRPC slides (indico.cern.ch/event/457639; 93%, 80 ps sigma at 70 kHz/cm2); SoLID TOF requirements slides (indico.ihep.ac.cn/event/7389; <20 ps, >20 kHz/cm2); p16 red-team r1 (ceramic MRPC ~2e5 Hz/cm2). Other figures are from standard knowledge and were not fetched.
