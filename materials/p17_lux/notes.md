# p17_lux notes

## Feasibility (written first, per lesson 5) -- OUTCOME: NO ROBUST WINDOW

Item: Gd-loaded liquid-scintillator neutron veto, at ANY Gd concentration (lesson 1).
Alternatives: 10B (TMB)-loaded LS veto; water-Cherenkov-only veto.
Question: does a stated physical requirement defeat Gd-LS robustly (every cited property x0.5-2)
while one alternative passes against every stated fact?

Back-of-envelope (thermal neutrons, v = 2.2e5 cm/s, LS density 0.86 g/cm3):
- Gd at 0.1 wt%: n_Gd ~ 3.3e18 /cm3, sigma_nat ~ 4.9e4 b -> Sigma ~ 0.16 /cm; with H (Sigma ~ 0.022 /cm)
  tau ~ 25 us (consistent with the ~28 us usually quoted for 0.1% Gd-LS).
  Gd at 0.5 wt%: tau ~ 5-6 us. Gd-LS at 0.1-0.2% has been stable for >10 y (Daya Bay); higher loadings exist in R&D.
- Natural-B TMB at 5 wt% (B ~0.5 wt%): n_10B ~ 5e19 /cm3 x 3840 b -> Sigma ~ 0.19 /cm -> tau ~ 20-25 us,
  i.e. the SAME as 0.1% Gd. Only 10B-enriched loadings reach the ~2 us of commercial boron LS.

Candidate mechanisms examined:
1. Capture-time window vs dead-time budget at a stated veto singles rate. FAILS as a separator:
   (a) capture time is set by loading, not by the element; Gd at 0.3-1% matches enriched-10B LS within x2,
       and "any concentration" is the item (lesson 1);
   (b) the coincidence window after a TPC event is in practice set by neutrons moderating/diffusing in the
       inner materials (cryostat, PTFE, xenon, any inner acrylic) before reaching the veto; that time is common
       to every veto liquid, so swapping the capture agent does not shrink the window robustly;
   (c) lesson 4: the routine response to a singles-rate dead-time problem is to raise the veto threshold.
       Gd's ~8 MeV cascade allows a threshold above the 2.6 MeV 208Tl line; boron's ~0.48 MeV gamma +
       ~60 keVee quenched alpha does not. So a higher singles rate HELPS Gd relative to boron.
2. Gamma singles rate from radioactivity of the surroundings at the capture-signal threshold. Favors Gd
   (high-energy signal), the opposite direction. Water-Cherenkov-only: 2.2 MeV H capture is barely above
   Cherenkov threshold yields; it loses on any neutron-tagging-efficiency requirement.
3. 10B alpha (~60 keVee) vs Gd 8 MeV cascade. Favors Gd. The only boron advantage is locality (alpha
   deposited in place), which matters only for a geometrically thin veto. A thin-veto CONF would need a
   space constraint (lesson 2 risk: geometry/site rule) and an expert's workaround (thicker moderator +
   Gd-LS elsewhere, or higher Gd loading + segmented containment) is not closed by physics. Not robust.
4. Gd radio-impurities (U/Th chains, 152Gd, 227Ac) vs a stated limit. Purification of Gd salts by
   factors of 10-100 is standard practice (Daya Bay, JUNO, LZ screening campaign) -> lesson 4 routine tweak.
   Any stated limit is either met after purification or would be arbitrary; and TMB/LAB carry their own
   impurities. Not robust under x0.5-2.
5. Gd-LS optical stability. Chemistry/engineering, demonstrated stable over a decade; not a physical
   requirement that x0.5-2 variation can pin. Not usable (also borders on rule 1).
6. Also considered: cryogenic operation (freezes all LS alike, survivor only a liquid-xenon skin, which
   is not one of the documented alternatives and has poor neutron tagging); flammability/safety (rule 1;
   kills TMB-LS too); prompt Gd gammas reaching the TPC (self-vetoed by the coincident veto deposit).

Conclusion: no stated physical requirement found that defeats Gd-loaded LS at every concentration while
a boron-loaded LS or water-only veto passes. Every separator either favors Gd, is removed by a routine
tweak (threshold raise, purification, higher loading), or needs a non-physical geometry/site constraint.
Per the brief ("If no honest CONF exists ... say so ... That is an acceptable outcome"): zero-unit pair.

## Design choices
None: no descriptions or key were written. kprobe.json = {}.

## Survivors per CONF
None (no CONF).

## Fixed inputs / unc ranges
None.

## Log of post-run changes
None.

## Doubts
- A thin-geometry CONF (boron's local alpha vs Gd's escaping gammas) is the closest candidate. Rejected
  because the space limit is a geometry rule rather than a requirement of the physics goal, and because
  added passive moderator / longer containment closes it (lesson 3/8).
- No web fetches were made; the numbers above are standard textbook/collaboration values computed by hand
  and are only used to show that no window exists.
