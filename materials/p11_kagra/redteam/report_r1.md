# Red team r1 (confirmation): p11_kagra (2026-11-06). Verdict: NO HONEST CONFLICT (agrees with author)

**Core finding.** An optical lever's sensitivity, linear range and reference are all set by free design choices: lever arm, beam size, detector, mount (floor, bench, recoil cage, or fibre-fed in the cryostat) and imaging optics. Any requirement a local sensor meets on a given reference, a lever on the same reference with a comparable arm also meets. The window stays empty under ×0.5–2 variation.

**Routes examined (each fails):**
1. tilt coupling;
2. in-band sensing noise (floors ~1e-10 to 1e-9 rad/√Hz overlap);
3. short lever arm;
4. heat through apertures (favours the lever);
5. beam power and photon pressure (negligible);
6. stray light;
7. linear range (a lever's range is tunable from 0.5 to 50 mrad);
8. port count (a layout rule);
9. translation coupling (an imaging lens or normal incidence removes it);
10. cryogenic contamination (favours the ratio readout);
11. recoil-mass referencing, cold sources, DC drift.

**adoption_status:** unverified (from memory).

## Outcome
p11_kagra is a **zero-unit pair** (author plus red-team confirmation, per A2).
