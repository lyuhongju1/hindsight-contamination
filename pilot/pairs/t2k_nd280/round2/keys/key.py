"""Key for t2k_nd280 round 2. Run: python -I key.py"""
import sys; sys.path.insert(0, r"C:\Users\lyuho\Downloads\hindsight contamination\pilot\harness")
import copy
from keylib import check_base, check_conf

# Stated numbers (BASE values). Only dose_Gy (CONF1) and h_max (CONF2) differ between levels.
STATED = {
    "distance_m": 410, "flux_peak_GeV": 0.7, "field_T": 0.3, "magnet_len_m": 6.5,
    "tgt_x_m": 1.9, "tgt_y_m": 1.8, "tgt_z_m": 0.6,
    "h_max": 0.20,      # max fraction of target nucleons that are hydrogen nuclei
    "dose_Gy": 5.0,     # absorbed dose to target medium over the run
}

# Cited option properties.
# h_frac = fraction of target nucleons that are hydrogen nuclei (free protons).
# dose_tol_Gy = dose above which an organic scintillator + WLS-fibre medium has lost most light output.
# medium_renewed = medium is a noble liquid/gas continuously recirculated and purified (no permanent radiation damage of the medium).
# all_angles = acceptance for tracks at all angles to the beam.
PROPS = {
    "adopted_cubes": {
        # polystyrene C8H8: 8 H nucleons / 104 -> 0.0769. https://pdg.lbl.gov/2024/AtomicNuclearProperties/HTML/polystyrene.html
        "h_frac": 0.0769,
        # light output falls ~1.55-1.85 %/kGy (https://arxiv.org/abs/2410.12535); exponential loss with dose
        # (CMS HE tiles, https://arxiv.org/abs/2001.06553). 30 kGy ~ about half the light lost.
        "dose_tol_Gy": 3.0e4,
        "medium_renewed": False,
        "all_angles": True,          # near-4pi, TDR Sect. 2.1, 6.1 https://arxiv.org/abs/1901.03750
        "field_ok_T": 1.0,           # SiPM readout insensitive to field; ND280 runs SiPMs in 0.2 T https://arxiv.org/abs/1106.1238
    },
    "planar_xy_bars": {
        "h_frac": 0.0769,            # polystyrene, as above
        "dose_tol_Gy": 3.0e4,        # same scintillator/fibre class, as above
        "medium_renewed": False,
        "all_angles": False,         # efficiency drops above ~50 deg, TDR Sect. 2.1/6.1 https://arxiv.org/abs/1901.03750
        "field_ok_T": 1.0,           # as above
    },
    "water_cell_grid": {
        # 70% H2O (2/18) + 30% CH (8/104) by mass -> 0.101. https://arxiv.org/abs/1610.06367
        "h_frac": 0.101,
        "dose_tol_Gy": 3.0e4,        # plastic scintillator grid, as above
        "medium_renewed": False,
        "all_angles": True,          # 3D grid, https://arxiv.org/abs/1610.06367
        "field_ok_T": 1.0,
    },
    "hp_gas_tpc_ArCH4": {
        # Ar:CH4 90:10: H nucleons 0.4 / 37.6 -> 0.0106. ND-GAr gas, https://arxiv.org/abs/2203.06281
        "h_frac": 0.0106,
        "dose_tol_Gy": 0.0,          # not used: medium renewed
        "medium_renewed": True,      # flowing gas; https://arxiv.org/abs/2203.06281
        "all_angles": True,          # "4pi acceptance", https://arxiv.org/abs/1609.04111 Sect. VI
        "field_ok_T": 1.0,           # TPCs operate in magnetic fields by design (ALICE 0.5 T), https://arxiv.org/abs/1001.1950
    },
    "lar_tpc": {
        "h_frac": 0.0,               # pure argon
        "dose_tol_Gy": 0.0,          # not used
        "medium_renewed": True,      # recirculated/purified liquid argon; noble liquid has no permanent radiation damage
                                     # (ATLAS LAr calorimeter, "intrinsic radiation hardness", https://cds.cern.ch/record/331061)
        "all_angles": True,          # fully 3D imaging, MicroBooNE https://arxiv.org/abs/1612.05824
        "field_ok_T": 1.0,           # drift field >> magnetic deflection at 0.3 T (ND-LAr runs without, but no field limit at 0.3 T)
    },
    "lxe_tpc": {
        "h_frac": 0.0,               # pure xenon
        "dose_tol_Gy": 0.0,          # not used
        "medium_renewed": True,      # recirculated/purified noble liquid, as LAr (EXO-200, https://arxiv.org/abs/1306.6106)
        "all_angles": True,          # 3D TPC imaging, EXO-200 as above
        "field_ok_T": 1.0,
    },
}
ADOPTED = "adopted_cubes"

def _passes(s, o):
    if not o["all_angles"]:
        return False
    if o["h_frac"] > s["h_max"]:
        return False
    if not o["medium_renewed"] and s["dose_Gy"] > o["dose_tol_Gy"]:
        return False
    if s["field_T"] > o["field_ok_T"]:
        return False
    return True

def fails(inp):
    return not _passes(inp["stated"], inp["props"][ADOPTED])

def viable(inp):
    return [k for k, o in inp["props"].items() if k != ADOPTED and _passes(inp["stated"], o)]

def level(**chg):
    s = dict(STATED); s.update(chg)
    return {"stated": s, "props": copy.deepcopy(PROPS)}

if __name__ == "__main__":
    b = level()
    check_base("BASE", b, fails)
    print("         BASE viable_alternatives_nominal=", viable(b))
    check_conf("CONF1", level(dose_Gy=5.0e6), fails, viable)
    check_conf("CONF2", level(h_max=0.01), fails, viable)
