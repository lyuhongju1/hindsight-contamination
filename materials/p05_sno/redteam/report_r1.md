# Red-team report r1, p05_sno (returned as text; saved by the orchestrator, 2026-11-06)

**Verdicts:**

| Level | Verdict | Reason |
|---|---|---|
| BASE | FIX (minor) | Only 1.5× margin: LAB fails at a ×2 deficit |
| CONF1 | FIX | Mechanism and survivor (PXE) fine, but the 40 kg/m³ "however restrained" limit is ~8× below acrylic membrane capacity, so it works by fiat |

**FIX items:**
1. Retune the limits to BASE 300 / CONF1 60 kg/m³, keeping the ratio of 5.
   - Checked against the key: LAB still fails in 100% of CONF1 draws (worst case 67.7 > 60); PXE survives (30 < 60); BASE LAB passes robustly (277 < 300).
   - Update the kprobe to 60.
   - Alternative: a restraint-independent max pressure difference across the wall (~2.5 kPa), which is cleaner but implies a weak wall.
2. Code water-based scintillator as an option: it fails the light requirement even at ×2. Optionally code an LAB plus heavy co-solvent blend.
3. **Grading rule (pre-register):** a fill with less than 50% LAB by volume is not the adopted item. Density-matching LAB needs at least ~62–79% heavy solvent, so it is no longer LAB-based.
4. Minor: pseudocumene density is 0.876, not 0.889 (immaterial).

**Notes:**
- Physics only: OK.
- PXE survivor credible against every stated fact.
- Minimal pair OK.
- A 1 cm, 10 m acrylic sphere has never been built (SNO used 5.5 cm): mild coherence oddity.
- Inner-balloon route: exotic, noted only.
- **Identifiability: very high (the SNO → SNO+ story almost verbatim).** A model recalling SNO+ will reach for "LAB + hold-down ropes", the route closed by the load-limit clause. This is the likely point of dispute and the core of the contamination test.
