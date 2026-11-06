"""Round-2 key for pair 'auger'. Run: python -I key.py
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

BASE_STATED = {
    "n_stations": 1350, "spacing_km": 1.4, "area_km2": 2300, "floor_m2": 11, "n_pmt": 2,
    "water_depth_m": 1.3,        # line 2 (CONF2 edits this)
    "fd_duty": 0.12,             # line 5
    "duty_req": 1.0,             # line 6 'full-time exposure'
    "e_min_log10": 19.0,         # line 6
    "zen_min_deg": 0.0001,       # line 8 (0 deg; tiny value so it is numeric and >0)
    "zen_max_deg": 55,           # line 8 (CONF1 edits this band)
    "res_req": 0.30,             # line 9
}

PROPS = {
    "thin_scint_on_station": {   # adopted
        "zen_max_deg": 65,       # EM absorbed above ~65 deg, scintillator method for vertical showers: RD
        "zen_min_deg": 0.0001,
        "depth_needed_m": 1.2,   # EM/mu contrast 'more than a factor two' vs a 1.2 m WCD: PDR sec 2.3.4, 4.1
        "res": 0.22,             # S_mu(800) 22% (p) / 14% (Fe): PDR sec 3.5
        "e_min_log10": 18.5,     # programme above 10^18.5 eV: PDR sec 2
        "max_spacing_km": 1.5,   # designed for the 1.5 km grid: PDR sec 4.1
    },
    "two_volume_tank": {         # layered water volume
        "zen_max_deg": 65,       # same EM-absorption limit (RD); top layer relies on EM
        "zen_min_deg": 0.0001,
        "depth_needed_m": 1.2,   # demonstrated by splitting a 1.2 m tank: https://arxiv.org/abs/1405.5699
        "res": 0.20,             # 20% (p) / 16% (Fe) at 10 EeV: https://arxiv.org/abs/1405.5699
        "e_min_log10": 19.0,     # performance quoted >= 10^19 eV: https://arxiv.org/abs/1405.5699
        "max_spacing_km": 1.5,   # per-station method, studied on 1.5 km grid: https://arxiv.org/abs/1405.5699
    },
    "chambers_under_station": {  # MARTA-type
        "zen_max_deg": 65,       # vertical analysis; EM-absorption limit RD
        "zen_min_deg": 0.0001,
        "depth_needed_m": 1.2,   # shielding 170 g/cm2 supplied by the 1.2 m tank: https://arxiv.org/abs/1712.07685
        "res": 0.20,             # < 20% up to 1000 m at 10^19 eV: https://arxiv.org/abs/1712.07685
        "e_min_log10": 19.0,     # https://arxiv.org/abs/1712.07685
        "max_spacing_km": 1.5,   # https://arxiv.org/abs/1712.07685
    },
    "buried_counter": {          # AMIGA/UMD-type, own soil shielding 1.3-2.3 m (PDR sec 9.6)
        "zen_max_deg": 65,       # vertical analysis (round-1 key; RD)
        "zen_min_deg": 0.0001,
        "depth_needed_m": 0.001, # does not use the water as absorber: PDR sec 9.6 (buried 1.3-2.3 m)
        "res": 0.12,             # 1.12/sqrt(N_mu), ~100 mu in 30 m2 at 10^19.6 eV: PDR sec 3.4 Table 3.2
        "e_min_log10": 17.5,     # infill operation at lower energies: PDR sec 1
        "max_spacing_km": 1.5,   # PDR sec 9.6
    },
    "radio_antenna": {           # EM energy in air, combined with water muon signal
        "zen_max_deg": 85,       # 65-85 deg analysis: RD
        "zen_min_deg": 70,       # fully efficient from ~70 deg: RD
        "depth_needed_m": 0.001, # measures EM in air; water only gives the muon signal (inclined): RD
        "res": 0.09,             # MF(p-Fe) 1.60 with WCD -> equivalent 0.09 (round-1 key): RD
        "e_min_log10": 18.5,     # RD
        "max_spacing_km": 3.0,   # inclined footprints 'tens of km2' (author estimate, round-1 key): RD
    },
    "fluorescence_extension": {  # longer FD operation
        "duty": 0.29,            # 15% -> ~29%: PDR ch. 6
        "zen_max_deg": 85, "zen_min_deg": 0.0001,  # geometry-independent (PDR ch. 6)
        "res": 0.10,             # direct Xmax; equivalent merit (PDR sec 2.3)
        "e_min_log10": 18.5, "max_spacing_km": 3.0,
    },
}

ADOPTED = "thin_scint_on_station"


def passes(name, inp):
    s, p = inp["stated"], inp["props"][name]
    if p["zen_min_deg"] > s["zen_min_deg"] or p["zen_max_deg"] < s["zen_max_deg"]:
        return False                                   # zenith band
    if p.get("depth_needed_m", 0) > s["water_depth_m"]:
        return False                                   # water depth / shielding / EM-mu contrast
    if p["res"] > s["res_req"]:
        return False                                   # muon-number resolution
    if p["e_min_log10"] > s["e_min_log10"]:
        return False                                   # energy band
    if p["max_spacing_km"] < s["spacing_km"]:
        return False                                   # grid spacing
    if p.get("duty", s["duty_req"] * 2) < s["duty_req"]:
        return False                                   # full-time exposure (particle/radio: continuous)
    return True


def fails(inp):
    return not passes(ADOPTED, inp)


def viable(inp):
    return [k for k in inp["props"] if k != ADOPTED and passes(k, inp)]


def make(edit):
    st = copy.deepcopy(BASE_STATED); st.update(edit)
    return {"stated": st, "props": copy.deepcopy(PROPS)}


if __name__ == "__main__":
    b = make({})
    print("BASE viable alternatives (nominal):", viable(b))
    check_base("BASE", b, fails)
    check_conf("CONF1", make({"zen_min_deg": 70, "zen_max_deg": 84}), fails, viable)
    check_conf("CONF2", make({"water_depth_m": 0.25}), fails, viable)
