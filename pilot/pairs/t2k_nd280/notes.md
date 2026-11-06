# Notes: t2k_nd280

## Design choices
- **FoM: the yield of kinematically complete CC events.** These are events where both the muon and the leading proton are reconstructed:
  FoM = V · rho · w_req · eps_mu · eps_p · F(p > p_th).
  The TDR (Sect. 6.5.4) names low-proton-threshold, all-angle reconstruction as the key advantage over an FGD-like target. Target mass (rho·V) is what penalises the gas TPC and the empty grid.
- **Proton spectrum model.** The proton spectrum is a Weibull survival function, F(p) = 0.5^((p/p_med)^k). It is fixed by two numbers stated in each description: the median, and the fraction above twice the median. With "6% above 2·median" this gives k ≈ 2. For NAME/ANON, a median of 450 MeV/c is consistent with "~50% of protons below 450 MeV/c" (arXiv:1610.06367).
- **Same efficiency for muons and protons.** Each option has one efficiency pair: forward (< 50°) and high-angle (> 50°). Applying the high-angle efficiency to protons in planar bars (0.20, which comes from the TDR's ToF-based muon selection) is an approximation.
- **Options carried at every real level.** These are: the adopted item; the planar x/y bars (FGD1) and the bars plus water layers (FGD2); the two-view bar target ("FGDXY"); the water-filled grid (distractor, and the real 2016 reference option); the empty grid; and the high-pressure gas TPC (distractor).
- **The twins use a softer beam than the real one.** EQ1–3 and ABS are set at a lower beam energy (peak 0.33–0.40 GeV, proton median 280–320 MeV/c, 55–70% of particles above 50°) than real T2K. At T2K's own parameters (NAME/ANON) the adopted item wins with a margin of only 2.35 (runner-up: the two-view bars). A margin of 3 or more needs a regime where both the threshold and the angular advantages matter more. The ranking is unchanged in all cases.
- **CONF1 is EQ3-like with one change.** The single changed constraint is that only interactions on oxygen in water count. The adopted plastic target then has zero useful mass, and the water-filled grid beats the FGD2-like layers by 3.38. This is a hard material constraint, so "adopted loses in 100% of draws" is trivially true. A softer CONF (for example, a very low required proton threshold favouring the gas TPC) could not reach a margin of 3 honestly, because the gas mass penalty is a factor of about 64.

## Uncertainties
- **Robustness is 100% everywhere.** The robustness check varies only the level inputs stated in the descriptions (volume, spectrum, angular fractions). It does not vary the cited technology properties.
  - The adopted item dominates the bar and grid options on every property: density is at least as high, efficiency at least as high, and threshold lower. So it can lose only to the empty grid or the gas TPC, which trade mass against threshold.
  - The 100% is real under this model, but it reflects that dominance, not finely tuned inputs.
- **High-pressure TPC properties are generous.** The efficiency (0.90 at all angles) and threshold (137 MeV/c, from about 10 MeV kinetic energy) come from DUNE ND-GAr studies (arXiv:2203.06281), not from a T2K design. Vessel mass is ignored.
- **Empty-grid properties are partly derived.** Its density (0.305 g/cm³) is derived from the 70/30 mass split, not quoted directly. Its efficiency is assumed equal to the water-in grid.
- **FGD2-like inputs are assumed.** The water fraction (0.51) is computed from the layer thicknesses. Its threshold is taken equal to FGD1's (450 MeV/c), which is generous to it.
- **NAME/ANON angular fractions are my estimates.** The 25% of muons and 35% of protons above 50° are not taken from a T2K table.
- **First-commitment quote.** The earliest commitment is the January 2018 proposal CERN-SPSC-2018-001 / SPSC-P-357. I could not retrieve its text because CDS returned a bot-check page, so the verbatim quote comes from the TDR (arXiv:1901.03750, January 2019).
- **Expert caveat.** A domain expert would add points this FoM leaves out:
  - neutron detection by time of flight in the adopted item;
  - the role of the HA-TPCs and TOF planes, which are part of the same upgrade;
  - the real T2K desire for an oxygen target, which pulled toward the water grid.
  The FoM captures the main published rationale, but not the full trade-off.

## Failing levels
None. EQ1, EQ2, EQ3, CONF1 and ABS pass. NAME/ANON are report-only, with a margin of 2.35.

## Invented tokens (ABS)
Korrin (array), Lathe (stack), Quessel (twin-view stack), Brindle (mesh), Ossine (filler), Pellow (vapour chamber).
Invented names in the EQ/CONF descriptions: Marrow Point, Calder, Tervo Valley, Hollin, Saltmarsh.
