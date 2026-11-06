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
def viable(inp): return [o for o in ("PXE", "PC", "WbLS", "LAB30_MN70") if ok(inp, o)]

props = {
    # LAB + ~2 g/L PPO: density 0.86 g/cm3 -> deficit vs water ~140 kg/m3; light yield ~1.1-1.2e4 photons/MeV
    # (SNO+ collab., JINST 16 (2021) P08059, arXiv:2104.11687)
    "LAB": {"density_deficit_kg_m3": 140.0, "photon_yield_per_MeV": 11000.0},
    # PXE + PPO: density ~0.985 g/cm3 -> deficit ~15 kg/m3; light yield ~1e4 photons/MeV
    # (Borexino CTF PXE studies, Back et al., NIM A 585 (2008) 48; density from PXE data sheets)
    "PXE": {"density_deficit_kg_m3": 15.0, "photon_yield_per_MeV": 10000.0},
    # pseudocumene + PPO: density 0.876 g/cm3 -> deficit ~124 kg/m3; ~1.1e4 photons/MeV (Borexino, NIM A 600 (2009) 568)
    "PC": {"density_deficit_kg_m3": 124.0, "photon_yield_per_MeV": 11000.0},
    # water-based liquid scintillator (~5% organic in water): density ~0.993 g/cm3 -> deficit ~7 kg/m3;
    # light yield ~100-300 photons/MeV (Yeh et al., NIM A 660 (2011) 51; Caravaca et al., EPJC 80 (2020) 867)
    "WbLS": {"density_deficit_kg_m3": 7.0, "photon_yield_per_MeV": 300.0},
    # 30% LAB / 70% 1-methylnaphthalene (density ~1.02 g/cm3) by volume: density ~0.972 -> deficit ~28 kg/m3;
    # light yield assumed ~8e3 photons/MeV (unverified). Not the adopted item under the <50%-LAB grading rule.
    "LAB30_MN70": {"density_deficit_kg_m3": 28.0, "photon_yield_per_MeV": 8000.0},
    # PMMA density ~1.19 g/cm3 -> excess over water ~190 kg/m3
    "acrylic": {"excess_density_kg_m3": 190.0},
}
base_fixed = {"sphere_radius_m": 5.0, "wall_m": 0.05, "collection_fraction": 0.12,
              "pe_per_MeV_required": 400.0, "load_limit_kg_m3": 300.0}
conf_fixed = dict(base_fixed, wall_m=0.01, load_limit_kg_m3=60.0)

check_base("BASE", {"fixed": base_fixed, "props": props}, fails)
# diagnostic (not part of the gate): WbLS must fail the light requirement even at x2 yield
f0 = dict(base_fixed)
assert 2 * props["WbLS"]["photon_yield_per_MeV"] * f0["collection_fraction"] < f0["pe_per_MeV_required"]
check_conf("CONF1", {"fixed": conf_fixed, "props": props}, fails, viable)
