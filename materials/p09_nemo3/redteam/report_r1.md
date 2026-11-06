# Red team r1: p09_nemo3 (2026-11-06). Verdict: BASE FIX, CONF1 FIX; mechanism, key logic, minimal pair and kprobe OK

**Blind answers:**
- BASE: 8-inch tubes directly coupled to ~22–28 cm blocks are favoured; the adopted item is sound (a weak preference at 18%).
- CONF1: small cells ≤10.6 cm each read directly by a 3-inch tube; the adopted item is unsound (a cell must be ≥21 cm across).

## FIX list
1. **Coherence (BASE and CONF1, identical edit):** 45 mg/cm² over 21 m² = 9.45 kg. Change "About 40 kg" to "About 9 kg".
2. **Survivor resolution:**
   - The NEMO-3 figure is verified: NIM A 536 (2005) 79, physics/0402115, Table 11, σ/E = 7.3 ± 0.1% at 1 MeV for 3-inch blocks (FWHM 17.2%). Replace the memory citation.
   - The ÷1.20 direct-coupling factor was measured for 8-inch tubes on SuperNEMO blocks and does not transfer. The survivor passes 18% only because of the ×0.8–1.25 floor.
   - Recommended: (i) re-derive from the 8-inch measurement (7.5 ± 0.2%, arXiv:1707.06823 Table 7), scaled by photocathode coverage (~71% for 76 mm on 80 mm, against ~49% for 202 mm on 256 mm) and by QE. That gives ~9–11%, which is robust. Write the derivation in notes.md.
   - Alternatives: (ii) a direct measurement; (iii) a bound argument plus raised requirements.
3. **notes.md:** the failure is shape-independent (any cell holding a directly coupled 202 mm tube has diameter ≥202 mm > 150 mm). The criterion is strict (<).
4. **Optional wording:** "...in different cells, whose energies are measured separately"; "Track curvature determines only the sign of the charge."

## Workarounds
- **8-inch tubes on ≤10 cm cells via light guides:** passes physically (~10.6% with the étendue loss). Not closed by a fact.
- **Segmented scintillator on one PMT:** closed ("used individually").
- **Tracker energy:** closed (multiple scattering means ≥30% momentum resolution).
- **Thinner wall:** irrelevant.

**Identifiability:** high.

## Study decision (2026-11-06)
- **Scoring:** 8-inch tubes reading small cells through light guides = **C** (adopted tube plus valid workaround). This applies the same C-code logic as p02/p05 and does not narrow the item.
- The FIX round applies 1–3 (and 4 if it stays neutral).
