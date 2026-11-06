"""Round-3 key for pair 'auger'. Run: python -I key.py
Adopted item: thin (~1 cm, ~4 m2) scintillator on each water station, read out with it.
Every stated fact is checked against every option (rule 8). No booleans (rule 9).
Viability is a list built from explicit checks, so no tie/first-key default exists
(fixes the round-1 all-zero bug, where evaluate() named the first option).
"""
import sys, copy
sys.path.insert(0, r"C:\Users\lyuho\Downloads\hindsight contamination\pilot\harness")
from keylib import check_conf, check_base

PDR = "https://arxiv.org/abs/1604.03637"
RD = "https://arxiv.org/abs/2305.10104"

import math
def sec(deg):  # air-mass factor = slant/vertical atmospheric depth: the linear physical variable for zenith
    return 1.0 / math.cos(math.radians(deg))

# v4.1: exact stated facts, not varied (see notes.md "Fixed inputs")
BASE_FIXED = {
    "spacing_km": 0.7,           # line 1, grid geometry
    "water_depth_m": 1.3,        # line 2 (CONF2 edits this)
    "duty_req": 1.0,             # line 6 'full-time exposure'
    "e_min_eV": 1e19,            # line 6, energy selection
    "sec_zen_min": sec(0),       # line 8, band 0-35 deg (CONF1: 80-84)
    "sec_zen_max": sec(35),
    "res_req": 0.30,             # line 9, stated requirement
    "headroom_m": 0.05,          # line 2, vessel filled to within 5 cm of its lid
    "channels_req": 2,           # line 7, two components measured separately
    # number of independent signals each option gives per shower (structural count, see notes)
    "channels": {"thin_scint_on_station": 2, "two_volume_tank": 2, "chambers_under_station": 2,
                 "buried_counter": 2, "radio_antenna": 2, "fluorescence_extension": 2,
                 "deepen_in_place_plus_panel": 2, "replace_vessel_plus_panel": 2,
                 "trace_electronics": 1},
}
BASE_STATED = {"n_stations": 1350, "area_km2": 570, "floor_m2": 11, "n_pmt": 2,
               "fd_duty": 0.12}  # stated but not decisive for any check

# Options with no lower (upper) zenith limit simply omit sec_zen_min (sec_zen_max).
PROPS = {
    "thin_scint_on_station": {   # adopted
        "sec_zen_max": sec(65),  # EM absorbed above ~65 deg: RD
        "depth_needed_m": 1.2,   # EM/mu contrast 'more than a factor two' vs a 1.2 m WCD: PDR sec 2.3.4, 4.1
        "res": 0.22,             # S_mu(800) 22% (p) / 14% (Fe): PDR sec 3.5
        "e_min_eV": 10**18.5,    # programme above 10^18.5 eV: PDR sec 2
        "max_spacing_km": 1.5,   # performance quoted for the 1.5 km grid: PDR sec 4.1
    },
    "two_volume_tank": {         # top layer relies on EM: same limit (RD)
        "sec_zen_max": sec(65),
        "depth_needed_m": 1.2,   # split 1.2 m tank: https://arxiv.org/abs/1405.5699
        "res": 0.20,             # 20% (p) / 16% (Fe) at 10 EeV: https://arxiv.org/abs/1405.5699
        "e_min_eV": 1e19,        # quoted >= 10^19 eV: https://arxiv.org/abs/1405.5699
        "max_spacing_km": 1.5,   # https://arxiv.org/abs/1405.5699
    },
    "chambers_under_station": {  # MARTA-type; EM = WCD signal minus shielded muon signal
        "sec_zen_max": sec(65),  # EM must reach ground for the subtraction; absorbed above ~65 deg: RD
        "depth_needed_m": 1.2,   # 170 g/cm2 shielding from the 1.2 m tank: https://arxiv.org/abs/1712.07685
        "res": 0.20,             # < 20% at 10^19 eV: https://arxiv.org/abs/1712.07685
        "e_min_eV": 1e19,        # https://arxiv.org/abs/1712.07685
        "max_spacing_km": 1.5,   # https://arxiv.org/abs/1712.07685
    },
    "buried_counter": {          # AMIGA/UMD-type, own soil shielding 1.3-2.3 m (PDR sec 9.6)
        "sec_zen_max": sec(65),  # EM = WCD minus buried muon count; EM absorbed above ~65 deg: RD
                                 # (also: 2.3 m soil x sec(82) ~ 16 m slant overburden, PDR sec 9.6)
        "depth_needed_m": 0.001, # does not use the water as absorber: PDR sec 9.6
        "res": 0.12,             # 1.12/sqrt(N_mu), ~100 mu in 30 m2 at 10^19.6 eV: PDR sec 3.4
        "e_min_eV": 10**17.5,    # infill operation at lower energies: PDR sec 1
        "max_spacing_km": 1.5,   # PDR sec 9.6
    },
    "radio_antenna": {           # EM energy in air + water muon signal
        "sec_zen_min": sec(70),  # fully efficient from ~70 deg: RD
        # no upper limit: 85 deg in RD is the analysis selection, footprint grows with zenith (see notes)
        "depth_needed_m": 0.001, # measures EM in air: RD
        "res": 0.09,             # MF(p-Fe) 1.60 with WCD -> equivalent 0.09 (round-1 key): RD
        "e_min_eV": 10**18.5,    # RD
        "max_spacing_km": 3.0,   # inclined footprints 'tens of km2' (author estimate, round-1 key): RD
    },
    "deepen_in_place_plus_panel": {  # add water to existing vessels, then the panel
        "sec_zen_max": sec(65),  # panel limit: RD
        "depth_needed_m": 1.2,   # PDR sec 2.3.4, 4.1
        "res": 0.22, "e_min_eV": 10**18.5, "max_spacing_km": 1.5,   # as panel: PDR
    },
    "replace_vessel_plus_panel": {   # new vessels built to the demonstrated depth, then the panel
        "sec_zen_max": sec(65),  # panel limit: RD
        # brings its own water depth (built to the 1.2 m of PDR sec 4.1): no depth check
        "res": 0.22, "e_min_eV": 10**18.5, "max_spacing_km": 1.5,   # as panel: PDR
    },
    "trace_electronics": {       # faster digitisation / trace-based muon counting, single water volume
        # muon content 'estimated only indirectly' from the one mixed signal: PDR sec 2.3
        "res": 0.22, "e_min_eV": 10**18.5, "max_spacing_km": 1.5,
    },
    "fluorescence_extension": {  # no zenith limit; continuous duty fails
        "duty": 0.29,            # 15% -> ~29%: PDR ch. 6
        "res": 0.10,             # direct Xmax (PDR sec 2.3)
        "e_min_eV": 10**18.5, "max_spacing_km": 3.0,
    },
}

ADOPTED = "thin_scint_on_station"


def passes(name, inp):
    s, p = dict(inp["stated"], **{k: v for k, v in inp["fixed"].items() if k != "channels"}), inp["props"][name]
    if "sec_zen_min" in p and p["sec_zen_min"] > s["sec_zen_min"]:
        return False                                   # zenith band, lower edge
    if "sec_zen_max" in p and p["sec_zen_max"] < s["sec_zen_max"]:
        return False                                   # zenith band, upper edge
    if inp["fixed"]["channels"][name] < s["channels_req"]:
        return False                                   # one mixed signal: components not separated
    if name == "deepen_in_place_plus_panel" and p["depth_needed_m"] - s["water_depth_m"] > s["headroom_m"]:
        return False                                   # vessel already full to within 5 cm of lid
    if name != "deepen_in_place_plus_panel" and p.get("depth_needed_m", 0) > s["water_depth_m"]:
        return False                                   # water depth / shielding / EM-mu contrast
    if p["res"] > s["res_req"]:
        return False                                   # muon-number resolution
    if p["e_min_eV"] > s["e_min_eV"]:
        return False                                   # energy band
    if p["max_spacing_km"] < s["spacing_km"]:
        return False                                   # grid spacing
    if "duty" in p and p["duty"] < s["duty_req"]:
        return False                                   # full-time exposure
    return True


def fails(inp):
    return not passes(ADOPTED, inp)


def viable(inp):
    return [k for k in inp["props"] if k != ADOPTED and passes(k, inp)]


def make(edit):
    fx = copy.deepcopy(BASE_FIXED); fx.update(edit)
    return {"fixed": fx, "stated": copy.deepcopy(BASE_STATED), "props": copy.deepcopy(PROPS)}


if __name__ == "__main__":
    b = make({})
    print("BASE viable alternatives (nominal):", viable(b))
    check_base("BASE", b, fails)
    check_conf("CONF1", make({"sec_zen_min": sec(80), "sec_zen_max": sec(84)}), fails, viable)
    check_conf("CONF2", make({"water_depth_m": 0.25}), fails, viable)
