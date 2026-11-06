# notes: p08_cosine

## Design choices
- Adopted item: in-house growth of NaI(Tl) crystals from recrystallisation-purified powder, at the collaboration's home institute.
- BASE: an invented NaI(Tl) annual-modulation array (12 crystals, 140 kg) whose present crystals (70 ppb K, 2.5 mBq/kg 210Pb) miss new purity requirements. In-house growth at a home institute at 30 m altitude meets all three stated requirements (K, 210Pb, 3H).
- CONF1 (minimal edit: one number): the home institute is at 3,600 m instead of 30 m. Cosmogenic neutron flux there is about 17 times the sea-level flux. About 150 d of surface exposure from powder to sealed crystal gives about 0.37 mBq/kg of 3H, against a 0.1 mBq/kg requirement. Tritium (T1/2 = 12.3 y) cannot be cooled away underground, and no chemistry or regrowth step removes it. Crystals bought from vendors at lower altitude survive.
- The failure is physical (cosmogenic activation that scales with altitude), not cost or schedule.
- Workaround routes: underground storage does not help (12.3 y half-life). Regrowing at the same site adds exposure. Moving the growth to another site is no longer "in-house at the stated site". That last route is a genuine alternative and is an acceptable answer.
- Coherence: 22Na, 109Cd and 113Sn scale the same way, so they only strengthen the failure. The lab portal (250 m) and transport are coded into every option (F_portal). The stated threshold, mass and background goal are identical for all options: every route delivers NaI(Tl) of the same mass and light yield. They are not discriminating, so the key does not code them separately. A 0.1 mBq/kg tritium limit contributes roughly 0.2-0.3 dru in 1-6 keV, which is consistent with a 0.5 dru goal.

## Survivors (CONF1)
- alpha_spectra (Grand Junction, about 1,400 m): 0.066 mBq/kg nominal.
- rmd_astrograde (near sea level): 0.029 mBq/kg nominal.
- n_survivors = 2. At least one survives in 99.6% of draws.

## Fixed inputs
- K_max 40 ppb, 210Pb_max 1.5 mBq/kg, 3H_max 0.1 mBq/kg, lab portal 250 m: stated facts in the descriptions.
- The home-institute altitude is a stated fact (BASE 30 m, CONF1 3,600 m). The flux factor derived from it (F_home: 1.0 and 17) is a cited property and IS varied x0.5-2.

## unc ranges
- R0 = 83 /kg/d +- 27 (Amare et al., Astropart. Phys. 97 (2018) 96, ANAIS): [0.67, 1.5].
- 3H half-life 12.32 y (precision < 1%): clamped to the minimum allowed [0.8, 1.25].

## Cited properties (to verify; written from memory)
- F(3,600 m) ~17: extrapolated from JESD89A (Leadville 3,100 m ~12.9) with about 148 g/cm2 attenuation. F(1,400 m) ~2.7 and F(250 m) ~1.2 come from the same scaling.
- In-house crystals: natK ~20 ppb, 210Pb ~0.4 mBq/kg (COSINE-200 R&D, CUP; unverified).
- Alpha Spectra best COSINE-100 crystals: K ~17 ppb, 210Pb ~0.8 mBq/kg (EPJC 78 (2018) 107; approximate).
- SABRE NaI-33 (RMD, Astro-Grade): K ~4.3 ppb, 210Pb ~0.41 mBq/kg (EPJC 79 (2019) 363).
- Surface exposure ~150 d at the growth site, plus 10 d (in-house) or 40 d (vendor) of transport: estimates, varied x0.5-2.

## Post-run change log
- Run 1: BASE PASS; CONF1 PASS (adopted_fails 0.990, viable 0.996). No changes.

## Doubts
- Whether a real collaboration would keep growth at a 3,600 m home site rather than at a partner site. The description does not forbid relocating, so a "move the grower" answer is legitimate and should be scored as rejecting the adopted item as specified.
- The vendor exposure times and altitude factors are estimates. Alpha Spectra survives with less margin than RMD.
- The stated threshold, mass and background goal are not coded per option (see Coherence).
