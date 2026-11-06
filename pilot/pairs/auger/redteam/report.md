# Red-team report, pair auger

Inputs read in step 2: keys/key.py, keys/key_output.txt, notes.md (dossier.md not needed). No web fetches used. Supplementary check: I re-ran the key's joint-draw test for 20 seeds (seeds 0-19, 2000 draws each) from a scratch script that imports key.py unchanged; results quoted below.

Reference for the real design used in identifiability notes: AugerPrime PDR, https://arxiv.org/abs/1604.03637 (SSD 3.8 m2, ~1 cm scintillator on the tank; Auger WCD 10 m2, 12 m3, 1.2 m water, 3 PMTs, 1660 stations, 1.5 km, ~3000 km2; upgrade also includes new electronics UUB and a small PMT).

---

## Cross-cutting findings

### (a) Cost / labour as the deciding gate
Key FoM = G x f_cov x MF^2. Pure-physics MF^2 (from the key's own numbers):

| option | MF^2 | EQ gate | EQ f_cov (EQ1) |
|---|---|---|---|
| thin panel (SSD) | 1.29 | pass | 1.00 |
| layered tank (LSD) | 1.29 | fail (interior locked) | 0.60 |
| RPC under tank | 1.69 | fail (no lift) | 0.20 |
| buried counter | 2.26 | pass | 0.10 (labour 4.8/48) |
| radio | 3.06 | fail (zenith band) | 1.00 |

- **EQ1-3: the winner depends on cost/labour, not physics.** The only option that survives the physics gate and the two installation gates besides the panel is the buried counter, and it has better per-event merit (MF^2 2.26 vs 1.29, x1.75). It loses solely through f_cov = labour/labour_need = 0.09-0.10. The other two rivals are excluded by installation rules (no-open, no-lift), which are site/operations rules, not physics; notes.md admits the no-lift framing of MARTA is the author's own reconstruction. Only radio is removed by physics.
- **ABS: same.** Veltrane has the *worst* resolution of the five (MF^2 0.94); Tessaline (MF^2 1.90) is physically usable and lost only to budget/labour (f_cov 0.09). Duolith and Korrin are removed by interior/lift rules (and also cost/labour), Orvane by zenith (physics).
- **CONF1 is the only level decided by stated physics** (zenith band: EM absorbed at 65-80 deg, so only an EM-cascade sensor is complementary).
- Conclusion: if the protocol requires "answers decided by stated physics", EQ1-3 and ABS do not meet it as written. Either (i) the protocol explicitly accepts stated budgets/labour as binding inputs (they are stated, numeric, and a solver can check them), or (ii) the buried-counter/Tessaline rival must be excluded by a stated physical fact (e.g. "caliche/bedrock within 0.3 m of the surface everywhere"), which is still a site condition, not shower physics. I recommend (i) with explicit wording in the protocol, because faithfulness to the real decision (PDR: AMIGA "not feasible for the 1660 surface detectors") is cost-driven.

### (b) CONF1's correct answer is itself AugerPrime history
- The radio antenna is the AugerPrime Radio Detector (added to every station for 65-85 deg showers). A model recalling "AugerPrime = SSD + UUB + small PMT + radio + UMD" can reach "radio" by recall, so CONF1 cannot separate reasoning from recall for the *correct* answer.
- For the narrower quantity "how often the adopted item (SSD) is still proposed when wrong", CONF1 still works: proposing the SSD for 65-80 deg is a recognisable error. But a contaminated model may propose "SSD + radio" (the full package); the scoring rule must say how a combined answer is counted. This matters: it is the most likely contaminated response.
- Redesign possible so the correct answer is a non-adopted Auger option, e.g. the **layered/segmented tank (LSD)**, which Auger rejected. Remove the no-open rule by stating the tanks are being drained and re-lined anyway, and set a zenith band (~55-70 deg) where a flat lid panel loses EM sensitivity (projected area ~cos theta, EM attenuation) while a volumetric two-layer tank still separates through-going muons from EM stopped in the top layer. Caveat: the key currently gives LSD and SSD identical sig_det (0.18), so the physics difference must be modelled with a cited zenith dependence or the margin will be ~1, not >=3. MARTA-style RPC under the tank (deployed only as an engineering array, never array-wide) with "new array, tanks not yet placed" is another route. Either route needs a sourced zenith-dependent resolution.

### (c) Robustness margins
- 20-seed re-run (joint draws, 2000 each): EQ1 min 0.952 / mean 0.957; EQ2 min 0.948 / mean 0.959, below 0.95 in 1/20 seeds; EQ3 min 0.950 / mean 0.958, below 0.95 in 2/20; ABS min 0.951 / mean 0.958; CONF1 min 0.970 / mean 0.979. NAME/ANON fall below 0.95 in 18/20 and 14/20 seeds.
- Binomial SE at p=0.95, n=2000 is ~0.005, so the reported 0.951 (EQ2) is within 0.2 SE of threshold. PASS for EQ2/EQ3 is seed-dependent; the seed is also shared sequentially across levels, so reordering LEVELS changes the results.
- Every flip in EQ1-3 goes to the buried counter, and in ABS to Tessaline: the fragility is exactly the cost/labour trade in (a).
- notes.md says the stated labour per station (4.4-4.8 h) was tuned to pass, while the real figure (5.8 h, NAME/ANON) fails. Tuning a description input until the gate passes is a weak point.
- Verdict: fragile. Recommend reporting the mean over >=20 seeds (or 20,000 draws), using an independent rng per level, and not treating 0.951 as a clean pass.

### (d) Identifiability
High for all EQs. A hybrid of a ~3000 km2 water-Cherenkov ground array, each tank with 2-4 PMTs, solar power, GPS and a radio link, plus fluorescence telescopes at ~13-17% duty cycle, run above 1e19 eV, is unique to the Pierre Auger Observatory. "Sealed tanks, one mixed EM+muon signal, add hardware for event-by-event p/Fe without opening or moving tanks" is the AugerPrime design brief almost word for word. Specifics:
- EQ1: "reflective bag", "three photomultipliers", "satellite timing", "radio link", ~2650 km2, "~13% of the time".
- EQ2: 3,100 km2 (~3000), "fluorescence telescopes on the basin rim" (Auger FD sites sit on the array perimeter), zenith up to 60 deg (Auger's standard vertical cut), "GPS and a wireless link".
- EQ3: least specific (2 PMTs, 12 telescopes at one site, cellular link), but still Auger-class.
- CONF1 is the worst: 10 m2, 12 m3, 1.2 m deep, 3 PMTs, reflective liner, ~12 t are the **exact** Auger tank parameters, and the 65-80 deg inclined-shower programme matches Auger's inclined-shower / radio analysis. "Ostrava" is a Czech city, and Czech institutes are Auger members (weak hint).
- ABS: the catalog maps one-to-one onto AugerPrime's choice set: Veltrane = SSD (3.5 m2 x 1.2 cm on the lid vs 3.8 m2 x 1 cm), Duolith = LSD, Korrin = MARTA (beneath), Tessaline = AMIGA (buried 2 m vs 2.3 m), Orvane = radio (">65 deg"). A knowledgeable reader decodes it.

---

## Per-level

### EQ1
1. Agreement: yes (blind: lid scintillator; runner-up buried counter).
2. Challenges:
   - Buried counter wins on physics (MF^2 2.26 vs 1.29); it loses only through labour (4.8 vs 48 h). See (a).
   - Forgotten option: an electronics-only upgrade (faster/finer digitisation, larger dynamic range, trace-based muon extraction / ML). It sits outside the sealed water volume and costs little. In reality the upgraded electronics (UUB) were part of AugerPrime itself (PDR, arXiv:1604.03637). The description does not exclude it, and the key does not model it. Add a stated sentence such as "the station electronics already sample at the maximum useful rate; trace-shape methods alone do not reach the required p/Fe separation".
   - f_cov treats a 10%-equipped array as giving 10% tagged exposure. That is acceptable as a simplification, but a partially equipped array (e.g. a dense infill) would cover a different energy range.
3. Leading wording: "one integrated signal in which electromagnetic particles and muons are mixed" points at a second detector with a different EM/mu ratio; "light vehicles on unpaved roads" points against excavation; the two installation rules exclude exactly LSD and MARTA. US$ 7.5k/station matches the real SSD cost scale.
4. Identifiability: high (see d).
5. Verdict: **FIX**: add the electronics-only exclusion; state explicitly in the protocol that budget/labour are binding stated inputs (or exclude the buried counter by a stated site fact); soften Auger-specific details (3 PMTs, reflective bag, satellite timing + radio link, 13% FD).

### EQ2
1. Agreement: yes.
2. Challenges: as EQ1. In addition, the 60 deg upper limit is where a flat lid panel's EM response is weakest. Labour 4.4 h vs SSD need 4.3 h means the panel itself is only 2% from losing coverage. Robustness 0.951 falls below 0.95 in 1/20 seeds.
3. Leading wording: as EQ1. "must remain untouched, so the tank response does not change" excludes LSD.
4. Identifiability: high (3,100 km2, FD on basin rim, 60 deg).
5. Verdict: **FIX**: same as EQ1, plus raise the labour slack or re-test robustness with more draws; change the area/zenith to depart from Auger's 3000 km2 / 60 deg.

### EQ3
1. Agreement: yes.
2. Challenges: as EQ1 (buried counter wins on physics, loses on labour 4.6 vs 48 h). Below 0.95 in 2/20 seeds. "Windy steppe" panel wind load is not decisive.
3. Leading wording: as EQ1 ("crews driving pickups between stations" again frames labour as per-stop work).
4. Identifiability: moderate-high (least Auger-specific of the three).
5. Verdict: **FIX**: same as EQ1; robustness marginal.

### CONF1
1. Agreement: yes (blind: radio antenna).
2. Challenges:
   - **Key bug:** when the radio gate is killed by a perturbed spacing (spacing x2 = 2 km > max_spacing x0.5 = 1.5 km), every FoM is 0 and `evaluate` returns the first dict key, which is the SSD. The whole 2.9% "adopted wins" in CONF1 is this tie artifact, not physics. `evaluate` should return "none" when s1 == 0, and the key must not count that as an adopted win.
   - max_spacing_inclined = 3 km is the author's own estimate; the gate is binary and unsourced.
   - Excluding the buried counter in the inclined band via "not complementary" is defensible: the WCD signal is muon-dominated at 65-80 deg, so N_mu is already measured, and the missing piece is an energy estimator independent of N_mu, which radio supplies.
   - The winner is decided by physics (good).
3. Leading wording: "more vertical showers are not part of it" emphasises the band (acceptable, as this is the conflict). There are no budget hints.
4. Identifiability: very high. The tank numbers are exactly Auger's; the 65-80 deg programme is Auger's radio/inclined analysis; "Ostrava" is a weak Czech hint.
5. Verdict: **FIX**: fix the all-zero tie bug; change the tank dimensions away from 10 m2 / 12 m3 / 1.2 m / 3 PMTs; rename the site. Consider redesigning per (b) so the correct answer is a non-adopted option (LSD or RPC with a sourced zenith-dependent resolution), and define how "SSD + radio" answers are scored.

### ABS
1. Agreement: yes (Veltrane is the only survivor of the gates).
2. Challenges:
   - Veltrane has the worst resolution (0.19). Tessaline (0.11, MF^2 1.90 vs 0.94) is physically usable and loses only on cost (14 vs 3.0) and labour (40 vs 3.6). Korrin and Duolith also have better resolution and are removed by installation rules. So the ABS answer is "the only one allowed by the gates", which tests constraint-reading rather than physics.
   - The "EM-to-muon ratio 2.4x" figure is decorative: sig_det is given directly.
   - Robustness min 0.951 over 20 seeds.
3. Leading wording: each rival carries exactly one disqualifier ("inside the cell's Brinol volume", "beneath the cell", "buried", ">65 deg"), so the puzzle structure reveals the answer.
4. Identifiability: the catalog is a one-to-one AugerPrime mapping (see d); the numbers 3.5 m2 / 1.2 cm / 2 m / 65 deg / 13 t / 14% are near-real.
5. Verdict: **FIX**: shift the near-real numbers (panel area/thickness, burial depth, angle threshold, mass, duty cycle), and add a decoy that is cheap, allowed and worse, so the winner is not simply the only survivor; same protocol decision as (a) on cost gates.
