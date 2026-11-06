"""Key for t2k_nd280 round 4 (round-3 key + round-4 CONF1 criterion). Run: python -I key.py
Every stated fact is checked on every option (rule 8); no booleans (rule 9)."""
import sys; sys.path.insert(0, r"C:\Users\lyuho\Downloads\hindsight contamination\pilot\harness")
import copy
from keylib import check_base, check_conf

# Stated numbers (BASE). Only p_KE_req_MeV (CONF1) and h_max (CONF2) change.
STATED = {
    "distance_m": 410, "flux_peak_GeV": 0.7,       # context only; no option property depends on them
    "field_T": 0.15, "magnet_len_m": 6.5,
    "tgt_x_m": 2.6, "tgt_y_m": 2.3, "tgt_z_m": 0.9,  # z along the beam
    "mu_eff_req": 0.25,      # min muon efficiency required at every angle
    "p_KE_req_MeV": 60.0,    # protons must be reconstructed down to this kinetic energy
    "h_max": 0.20,           # max fraction of target nucleons that are hydrogen nuclei
}

# Option properties.
#  p_KE_th_MeV   proton kinetic-energy reconstruction threshold
#  mu_eff_min    lowest muon reconstruction efficiency over all angles to the beam
#  h_frac        hydrogen nuclei / all target nucleons
#  field_tol_T   largest field in which the readout has been demonstrated to work
#  extent_m      fibre options: WLS-fibre attenuation length (compared with the longest target dimension);
#                TPC options: drift length (compared with half the smallest dimension, central cathode)
#  fibre_read    1 = extent compared with longest dimension, 0 = drift (TPC). Numeric selector, not a capability;
#                it only picks which geometric quantity is compared and is never close to a threshold.
# p -> KE: KE = sqrt(p^2 + 938.27^2) - 938.27.
PROPS = {
    "adopted_cubes": {
        "p_KE_th_MeV": 46.8,   # 300 MeV/c with three views, TDR Sect. 2.1/6.4.1 https://arxiv.org/abs/1901.03750
        "mu_eff_min": 0.90,    # >90% muon efficiency at all angles, TDR https://arxiv.org/abs/1901.03750
        "h_frac": 0.0769,      # polystyrene C8H8, 8/104 https://pdg.lbl.gov/2024/AtomicNuclearProperties/HTML/polystyrene.html
        "field_tol_T": 7.0,    # SiPMs tested up to 7 T, Espana et al., NIM A 613 (2010) 308 https://doi.org/10.1016/j.nima.2009.11.066
        "extent_m": 3.5,       # Kuraray Y-11 attenuation length > 3.5 m https://www.kuraray.com/products/psf
        "fibre_read": 1,
    },
    "planar_xy_bars": {
        "p_KE_th_MeV": 124.9,  # ~500 MeV/c with two views, TDR Sect. 2.1 https://arxiv.org/abs/1901.03750
        "mu_eff_min": 0.20,    # high-angle (ToF-based) selection ~20%, TDR Sect. 6.1 https://arxiv.org/abs/1901.03750
        "h_frac": 0.0769,      # polystyrene, as above
        "field_tol_T": 7.0,    # SiPM, as above
        "extent_m": 3.5,       # Y-11, as above
        "fibre_read": 1,
    },
    "water_cell_grid": {
        "p_KE_th_MeV": 102.3,  # ~450 MeV/c, https://arxiv.org/abs/1610.06367
        "mu_eff_min": 0.80,    # 3D grid, large-angle acceptance claimed qualitatively, https://arxiv.org/abs/1610.06367 (encoded 0.8)
        "h_frac": 0.101,       # 70% H2O (2/18) + 30% CH (8/104) by mass, https://arxiv.org/abs/1610.06367
        "field_tol_T": 7.0,
        "extent_m": 3.5,
        "fibre_read": 1,
    },
    "empty_grid": {
        "p_KE_th_MeV": 26.6,   # 200-250 MeV/c (225 used), https://arxiv.org/abs/1610.06367
        "mu_eff_min": 0.80,    # as water grid
        "h_frac": 0.0769,      # polystyrene scintillator only
        "field_tol_T": 7.0,
        "extent_m": 3.5,
        "fibre_read": 1,
    },
    "gas_tpc_10atm_ArCF4iC4H10": {
        "p_KE_th_MeV": 3.0,    # HPgTPC reconstructs protons "as low as 3 MeV kinetic energy", https://arxiv.org/abs/1910.06422
        "mu_eff_min": 0.90,    # "flat acceptance over the full angular range", https://arxiv.org/abs/1910.06422 (encoded 0.9)
        # Ar:CF4:iC4H10 95:3:2 (T2K TPC gas, https://arxiv.org/abs/1106.1238): H 0.2 / (38+2.64+1.16) = 0.0048
        "h_frac": 0.0048,
        "field_tol_T": 1.5,    # ALEPH TPC in 1.5 T, NIM A 294 (1990) 121 https://doi.org/10.1016/0168-9002(90)91831-U
        "extent_m": 2.5,       # ALICE TPC drift length 2.5 m (ND-GAr reuses ALICE chambers) https://arxiv.org/abs/1001.1950
        "fibre_read": 0,
    },
    "gas_tpc_1atm_NeCO2N2": {
        # 1 atm Ne (0.84 kg/m3) vs 10 atm Ar (16.6 kg/m3): same track length needs KE scaled by (rho ratio)^(1/1.75)
        # (range ~ KE^1.75, PDG passage-of-particles https://pdg.lbl.gov/2024/reviews/rpp2024-rev-passage-particles-matter.pdf):
        # 3 MeV * 0.0506^0.571 = 0.54 MeV. Derived, not measured.
        "p_KE_th_MeV": 0.54,
        "mu_eff_min": 0.90,    # same TPC imaging as above (encoded 0.9)
        "h_frac": 0.0,         # Ne:CO2:N2 90:10:5, ALICE TPC https://arxiv.org/abs/1001.1950
        "field_tol_T": 1.5,    # ALEPH, as above
        "extent_m": 2.5,       # ALICE drift 2.5 m https://arxiv.org/abs/1001.1950
        "fibre_read": 0,
    },
    "lar_tpc": {
        "p_KE_th_MeV": 40.0,   # LAr proton threshold 40 MeV, https://arxiv.org/abs/1910.06422 (MicroBooNE 47 MeV)
        "mu_eff_min": 0.50,    # MicroBooNE CC-inclusive efficiency vs angle, https://arxiv.org/abs/1905.09694 (encoded 0.5, conservative)
        "h_frac": 0.0,         # pure argon
        "field_tol_T": 0.55,   # LAr TPC operated in 0.55 T, Badertscher et al., NIM A 555 (2005) 294 https://arxiv.org/abs/physics/0505151
        "extent_m": 2.56,      # MicroBooNE drift 2.56 m, https://arxiv.org/abs/1612.05824
        "fibre_read": 0,
    },
}
ADOPTED = "adopted_cubes"

def _passes(s, o):
    dims = (s["tgt_x_m"], s["tgt_y_m"], s["tgt_z_m"])
    need = max(dims) if o["fibre_read"] >= 0.5 else 0.5 * min(dims)
    return (o["p_KE_th_MeV"] <= s["p_KE_req_MeV"]
            and o["mu_eff_min"] >= s["mu_eff_req"]
            and o["h_frac"] <= s["h_max"]
            and s["field_T"] <= o["field_tol_T"]
            and need <= o["extent_m"])

def fails(inp):
    return not _passes(inp["stated"], inp["props"][ADOPTED])

def viable(inp):
    return [k for k, o in inp["props"].items() if k != ADOPTED and _passes(inp["stated"], o)]

def level(**chg):
    s = dict(STATED); s.update(chg)
    return {"stated": s, "props": copy.deepcopy(PROPS)}

# ---- Round 4: CONF1 survivors must be credible targets of DISTINCT technology classes. ----
# Not a stated fact of the description: it is the round-4 acceptance criterion (brief + round-3 red team).
# Kept in a separate dict so BASE and CONF2 use exactly the round-3 inputs and draws.
#  rho_kg_m3  density of the target medium
#  fill_frac  fraction of the stated target-region volume that can hold that medium (encoded, author estimate)
MASS = {
    "planar_xy_bars":  {"rho_kg_m3": 1060.0, "fill_frac": 0.9},   # polystyrene, PDG (URL above)
    "water_cell_grid": {"rho_kg_m3": 1000.0, "fill_frac": 0.8},   # water-dominated, arXiv:1610.06367 (encoded)
    "empty_grid":      {"rho_kg_m3": 1060.0, "fill_frac": 0.2},   # scintillator lattice only, arXiv:1610.06367 (encoded)
    # argon gas 1.662e-3 g/cm3 at 1 atm, x10; fill 1.0 = optimistic rectangular vessel (red team: cylinder ~0.3)
    "gas_tpc_10atm_ArCF4iC4H10": {"rho_kg_m3": 16.6, "fill_frac": 1.0},  # https://pdg.lbl.gov/2024/AtomicNuclearProperties/HTML/argon_gas_Ar.html
    "gas_tpc_1atm_NeCO2N2":      {"rho_kg_m3": 0.84, "fill_frac": 1.0},  # neon gas 0.839e-3 g/cm3, https://pdg.lbl.gov/2024/AtomicNuclearProperties/HTML/neon_gas_Ne.html
    "lar_tpc":         {"rho_kg_m3": 1396.0, "fill_frac": 0.5},   # LAr 1.396 g/cm3, https://pdg.lbl.gov/2024/AtomicNuclearProperties/HTML/liquid_argon.html; 0.5 for cryostat (encoded)
}
# Minimum credible target mass: ~half of one ND280 FGD module (1.1 t, https://arxiv.org/abs/1106.1238). Author criterion.
CRIT = {"m_min_kg": 500.0}
# Technology class labels (not numbers, so not varied; they are labels, not capabilities).
TECH = {"planar_xy_bars": "scint_bars", "water_cell_grid": "scint_grid", "empty_grid": "scint_grid",
        "gas_tpc_10atm_ArCF4iC4H10": "gas_tpc", "gas_tpc_1atm_NeCO2N2": "gas_tpc", "lar_tpc": "lar_tpc"}

def viable_distinct(inp):
    """Round-3 viable(), then keep only credible-mass survivors, one per technology class."""
    s = inp["stated"]; vol = s["tgt_x_m"] * s["tgt_y_m"] * s["tgt_z_m"]
    out, seen = [], set()
    for k in viable(inp):
        m = inp["mass"][k]["rho_kg_m3"] * inp["mass"][k]["fill_frac"] * vol
        if m >= inp["crit"]["m_min_kg"] and TECH[k] not in seen:
            seen.add(TECH[k]); out.append(k)
    return out

def level4(**chg):
    x = level(**chg); x["mass"] = copy.deepcopy(MASS); x["crit"] = dict(CRIT)
    return x

if __name__ == "__main__":
    b = level()
    check_base("BASE", b, fails)
    print("         BASE viable_alternatives_nominal=", viable(b))
    c1 = level4(p_KE_req_MeV=12.0)
    print("         CONF1 diag: round-3 viable_nominal=", viable(c1), "(single class, below mass floor)")
    check_conf("CONF1", c1, fails, viable_distinct)
    check_conf("CONF2", level(h_max=0.02), fails, viable)
    print("         CONF2 diag (not the CONF2 verdict): credible distinct survivors_nominal=", viable_distinct(level4(h_max=0.02)))
