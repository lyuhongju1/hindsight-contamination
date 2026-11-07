# p19_cuore0 notes (PROVISIONAL pair): NO ROBUST WINDOW, even under C1

Outcome: no CONF written; kprobe.json = {}. Descriptions and key not built (nothing honest to key).

## Mechanism tested: 2nbb random-coincidence pile-up with stated crystal size and stated resolving time (C1)
Pile-up background index b = tau * A^2 * f * (3.156e7 s/yr) / M, with A = (A/M)*M the 2nbb rate per crystal,
tau the effective resolving time, f ~ 1e-4 /keV the spectral density of two-event sums near Q
(order of magnitude, Chernyak et al., EPJC 72 (2012) 1989, arXiv:1301.4248; abstract fetched, numbers not
in abstract; CUPID CDR arXiv:1907.09376 treats the same term). So b scales as tau * M * (A/M)^2.

Specific activities (computed): Li2(100)MoO4 (97%, T1/2 7.1e18 yr) 1.03e-2 Hz/kg; Zn(82)Se (95%, 8.7e19 yr)
9.8e-4 Hz/kg; enriched TeO2 (92%, 7.9e20 yr) 9.5e-5 Hz/kg. (A/M)^2 ratio Li2MoO4/ZnSe = 110: at equal
geometry the intrinsic pile-up separation is ample.

Li2MoO4 pile-up b, nominal (counts/(keV kg yr)); ZnSe at the same crystal volume in brackets:
| crystal mass M | tau | Li2MoO4 b | ZnSe b |
|---|---|---|---|
| 0.28 kg (45 mm cube) | 1 ms | 9.3e-5 | 1.5e-6 |
| 0.38 kg (50 mm cube, CUORE-holder size) | 3 ms (NTD-Ge light detector, slow) | 3.8e-4 | 6.0e-6 |
| 0.50 kg (upper credible LMO/ZnSe crystal) | 10 ms (generous; ~heat-channel only) | 1.7e-3 | 2.6e-5 |
If the CDR-scale figure (~3.5e-4 at 0.28 kg, 1 ms) is used instead of f = 1e-4, multiply by ~4: still <= ~7e-3 at the extreme row.

## Why it still fails (the obstacle is the survivors, not the pile-up physics)
- C1 lets M and tau be stated, so the Li2MoO4 pile-up can be pinned. But for Li2MoO4 to fail robustly
  (95% of x0.5-2 draws on T1/2, f, abundance, ...) the stated background requirement R must sit below
  roughly 0.3-0.5x the nominal b above, i.e. R <~ 1e-4 to 5e-4 at credible (M, tau), <~ 1e-3 at the stretched row.
- A survivor must meet the SAME total background requirement with its own credible, cited background:
  - ZnSe (CUPID-0): demonstrated ROI background (3.5 +1.0 -0.9)e-3 counts/(keV kg yr) (CUPID-0 Phase I,
    PRL 123, 032501 (2019); from memory). With x0.5-2 it spans 1.75e-3 to 7e-3: above every R that defeats
    Li2MoO4, by ~5-20x at credible (M, tau). Also ~20 keV FWHM (vs ~5-7 keV), so any resolution requirement
    tightens this further. ZnSe pile-up is never the problem; its radiopurity is.
  - TeO2 + Cherenkov: Cherenkov signal ~100 eV needs NTL/TES-class light detectors, i.e. a new readout class
    (not the stated retained light detectors), so it is itself "item + add-on"; and Q = 2527 keV < 2615 keV gives a
    208Tl gamma floor of order 1e-3 (CUORE gamma component, from memory), again above R.
  - CdWO4 (116Cd): pile-up similar to ZnSe ((A/M)^2 ratio ~70), but no demonstrated bolometric background near
    1e-4; crystal 228Th of order 1e-5-1e-4 Bq/kg (Aurora 116CdWO4, from memory). Not a credible survivor at R <~ 5e-4.
- To make R loose enough for ZnSe (R >~ 7e-3) Li2MoO4 would need nominal b >~ 2-3e-2, i.e. tau*M ~ 100 kg*ms
  (e.g. 0.5 kg with ~200 ms resolving time). No credible light-detector or heat-channel resolving time is that slow,
  and pulse-shape pile-up rejection on the given detectors is a routine within-item setting (lesson 4 / C1).
- Coherence check: CUORE-holder 5 cm cubes give 0.38 kg Li2MoO4, 0.66 kg ZnSe, 0.75 kg TeO2: credible for all,
  but this does not change the gap above.

Conclusion: under C1 the pile-up term can be stated into a failure for Li2MoO4, but no documented
alternative meets a background requirement strict enough to make that failure robust. The x110 pile-up
advantage of ZnSe is swamped by its ~10x worse demonstrated radiopurity background. Agrees with the earlier
feasibility file, now for a different reason (survivor background, not mass/tau tweaks).

## Survivors per CONF
- none (no CONF).

## Fixed inputs / unc ranges
- none used. Tighter T1/2 precision (100Mo ~2%, CUPID-Mo 2020) would justify unc x0.8-1.25, but it does not open the window.

## Log
- 2026-11-06: one web fetch (arXiv API, Chernyak et al. 2012 citation confirmed). No post-run changes.

## Doubts
- CUPID-0, CUORE gamma and CdWO4 numbers are from memory, not fetched. The verdict needs the survivor
  background to be wrong by more than ~5x (and a credible M, tau), so it is not sensitive to them at the factor-2 level.
