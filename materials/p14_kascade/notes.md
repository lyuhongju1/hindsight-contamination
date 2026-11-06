# p14_kascade notes

## Feasibility (decided first, per lesson 5)

Outcome: **no robust window. No CONF written; the pair is left failing (zero units).**

The core problem is structural. A tripole is a superset of the alternatives' measurement: its two horizontal arms are
the same horizontal dipoles an inverted-V or LPDA/butterfly station provides (same band, same pattern class). The third,
vertical arm only adds a channel. So a stated physical requirement can defeat the tripole only if the vertical arm
actively degrades something the station must deliver. Without that, "tripole" passes whenever the alternative passes.
Under lesson 1 the item is any three-component antenna, so the CONF must defeat every variant of it. Cost, channel
count and DAQ load are rule-1 exclusions.

Candidates checked:

1. **Vertical-dipole ground coupling and horizon gain** (for a stated band of tens of MHz and a stated ground
   conductivity). Real ground makes the vertical arm's gain near the horizon, and its calibration, depend strongly on
   soil permittivity and conductivity. This makes the vertical channel less precise; it does not make the station
   fail. The horizontal channels are unchanged. The adopted item still meets any requirement that the alternative meets.
   Not a conflict.
2. **Self-noise, or galactic-noise-limited sensitivity of a short vertical dipole.** A noisier or less sensitive
   vertical channel lowers the value of the third component. It does not make the horizontal measurement worse.
   Not a conflict.
3. **RFI from a stated local vertically polarised transmitter.** This saturates or contaminates only the vertical
   channel. The fixes are a notch or band filter on that channel, or ignoring it in the analysis. That is an
   "item plus add-on/tweak" workaround (lessons 3 and 4), scored C rather than a rejection. Horizontal channels are
   unaffected, because the cross-polar response of the horizontal arms is the same with or without the vertical arm.
   Not robust.
4. **Mutual coupling between the three arms.** This is real but modest at the 10–30 % level in the pattern. It can be
   removed by routine design: arm spacing, separate feed points, or modelling the coupling into the antenna response
   (lesson 4). It also cannot be made to fail robustly under x0.5–2 without inventing an unphysical coupling strength.
   Not robust.
5. **Stated zenith-angle range restricted to near-vertical showers.** The vertical field component is then roughly
   proportional to sin(zenith) and small, so the third arm adds little. "Adds little" is a cost and value argument,
   not a physical failure: the tripole still measures both horizontal components as well as the alternative does.
   Not a conflict. This is the most natural way to make the item *pointless*, but pointless is not *failing*, and a
   scoring rubric that rejected it would rest on a rule-1 (cost) judgement.

Also considered: deriving the vertical component from the two horizontal ones plus the reconstructed arrival
direction (far-field E is perpendicular to k). This shows the third arm can be *redundant*. It does not show that the
arm *fails*, so it does not help.

Conclusion: every mechanism either degrades only the optional third channel (the item still passes on its horizontal
arms) or is closed by a routine filter or design tweak. No requirement separates the tripole from inverted-V or
LPDA/butterfly antennas robustly under x0.5–2 without a cost criterion. Per the brief, this is reported as an honest
zero-unit outcome.

## Design choices / fixed inputs / unc ranges
None. No key was built.

## Survivors per CONF
Not applicable (no CONF).

## Post-run change log
- 2026-11-06: feasibility assessed; pair declared infeasible before any description was drafted. No web fetches used.

## Doubts
- A site where a vertical structure is physically impossible (e.g. a stated requirement that antennas lie flat on or
  under a surface) would be a geometric, site-type rule close to lesson 2. A tripole variant with a short or
  ground-plane-mounted vertical element would also survive it. Rejected.
- If the red team accepts "the third component carries no physical information in the stated zenith range" as a
  physical conflict, a CONF could be built on candidate 5. I judge that it would be scored as a cost/value argument and
  not a failure.
