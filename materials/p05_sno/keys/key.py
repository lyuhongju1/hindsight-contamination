"""Key for p05_sno (target item: LAB liquid scintillator). Run: python -I key.py"""
import math, sys
sys.path.insert(0, r"C:\Users\lyuho\Downloads\hindsight contamination\pilot\harness")
from keylib import check_base, check_conf

def shell_term(inp):
    f = inp["fixed"]
    r, t = f["sphere_radius_m"], f["wall_m"]
    shell_vol = 4 * math.pi * r**2 * t
    inner_vol = 4 / 3 * math.pi * r**3
    # the wall is denser than water, so its weight partly offsets the buoyancy of a lighter fill
    return inp["props"]["acrylic"]["excess_density_kg_m3"] * shell_vol / inner_vol

def ok(inp, opt):
    f, p = inp["fixed"], inp["props"][opt]
    light = p["photon_yield_per_MeV"] * f["collection_fraction"] >= f["pe_per_MeV_required"]
    net = p["density_deficit_kg_m3"] - shell_term(inp)     # net upward load per m3 of contained volume
    load = abs(net) <= f["load_limit_kg_m3"]
    return light and load

def fails(inp): return not ok(inp, "LAB")
def viable(inp): return [o for o in ("PXE", "PC") if ok(inp, o)]

props = {
    # LAB + ~2 g/L PPO: density 0.86 g/cm3 -> deficit vs water ~140 kg/m3; light yield ~1.1-1.2e4 photons/MeV
    # (SNO+ collab., JINST 16 (2021) P08059, arXiv:2104.11687)
    "LAB": {"density_deficit_kg_m3": 140.0, "photon_yield_per_MeV": 11000.0},
    # PXE + PPO: density ~0.985 g/cm3 -> deficit ~15 kg/m3; light yield ~1e4 photons/MeV
    # (Borexino CTF PXE studies, Back et al., NIM A 585 (2008) 48; density from PXE data sheets)
    "PXE": {"density_deficit_kg_m3": 15.0, "photon_yield_per_MeV": 10000.0},
    # pseudocumene + PPO: density 0.889 g/cm3 -> deficit ~111 kg/m3; ~1.1e4 photons/MeV (Borexino, NIM A 600 (2009) 568)
    "PC": {"density_deficit_kg_m3": 111.0, "photon_yield_per_MeV": 11000.0},
    # PMMA density ~1.19 g/cm3 -> excess over water ~190 kg/m3
    "acrylic": {"excess_density_kg_m3": 190.0},
}
base_fixed = {"sphere_radius_m": 5.0, "wall_m": 0.05, "collection_fraction": 0.12,
              "pe_per_MeV_required": 400.0, "load_limit_kg_m3": 200.0}
conf_fixed = dict(base_fixed, wall_m=0.01, load_limit_kg_m3=40.0)

check_base("BASE", {"fixed": base_fixed, "props": props}, fails)
check_conf("CONF1", {"fixed": conf_fixed, "props": props}, fails, viable)
