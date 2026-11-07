# p18_superk notes

## Feasibility (lesson 5, decided before building anything)

Question: does any physical requirement make Gd2(SO4)3 loading fail while GdCl3 or a non-Gd route survives, robustly under x0.5-2?

- **Attenuation length:** no window. At 0.01-0.1% Gd the light loss comes from the Gd3+ ion (narrow lines near 245-275 and 311 nm), not from the anion. SO4(2-) and Cl- are both transparent above about 200-230 nm. EGADS reached ~75% light left at 15 m with 0.2% Gd2(SO4)3, against ~80% for pure water. So any cut that fails sulfate also fails GdCl3. A cut placed between the pure-water and loaded values sits on a difference of a few percent, which does not survive x0.5-2. Routine band-pass filtration restores the transparency (an "item plus add-on" route, scored C, lesson 3).
- **Radio-impurities vs a low-energy background limit:** no window. The SK-Gd salt limits for solar neutrinos and low-energy work are 226Ra < 0.5 mBq/kg and 228Th < 0.05 mBq/kg in Gd2(SO4)3; commercial raw salt is 10-100x higher. The fix is chemical purification by the supplier, which is the same for either anion, so it does not separate sulfate from chloride. The impurities cannot be removed in situ by routine water purification, because ion exchange would also strip the Gd. But purified salt is a routine add-on (lesson 3), and Gd concentration can go continuously toward 0. A limit that H-only passes but a low-Gd load fails would need a contamination cut that x0.5-2 cannot hold robustly.
- **Sulfate and the water system:** no window, and the effect points the wrong way. Sulfate does not corrode stainless steel; chloride pits it (~700 ppm Cl- at 0.1% Gd). Sulfate issues are CaSO4/BaSO4 scaling (trace Ca and Ba are removed by RO pretreatment), sulfate-reducing bacteria (handled by routine UV sterilization), and the need for Gd-compatible band-pass or ion-exchange recirculation. All of these are routine engineering add-ons, not physical failures.
- **A stated requirement that H capture alone meets:** no window. The Gd concentration can be tuned continuously from 0. Any requirement that H-only capture meets is also met by a small enough Gd load (0.011% Gd already gives ~50% capture on Gd), so the item can always reach the H-only case (lesson 1: every variant of the item counts). No physics requirement in a water Cherenkov detector is harmed by an 8 MeV capture signal or a shorter capture time.
- **(Extra) solubility or high concentration:** no robust window. Gd2(SO4)3 solubility is ~3 g/100 g at 20 C and is retrograde, a ceiling of ~1.5% Gd, while GdCl3 is very soluble. Only a capture time well below ~2-3 us would need more Gd than that. Below that range, moderation time and the epithermal capture behaviour limit GdCl3 too, and so much salt changes the optics (Gd3+ absorption). The window is not credible or robust under x0.5-2.

## Decision
No robust window. kprobe.json = {}. No descriptions or keys were built. This is an acceptable zero-unit outcome (Brief, "If no honest CONF exists").

## Doubts
- The numbers above are from memory of the SK-Gd and EGADS literature (Ito et al. 2020 on salt purity; Marti et al. 2020 on SK-Gd; EGADS transparency). They were not re-fetched in this session, but none of the conclusions depends on them to better than a factor of ~2.
