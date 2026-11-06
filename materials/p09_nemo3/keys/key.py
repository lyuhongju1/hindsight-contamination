"""Key for p09_nemo3. Run: python -I key.py
Adopted item: calorimeter cells read one-to-one by ~200 mm (8-in.) high-QE hemispherical PMTs
directly coupled to large polystyrene blocks.
Every stated fact is checked on every option: energy resolution, time resolution, cell segmentation
(two entry points >= X apart must be in different cells), cell depth >= 3 cm, operation in 3 mT.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

FIXED = {  # exact stated facts (descriptions, lines 8-11)
    "res_req_fwhm_pct": 18.0,   # energy resolution requirement, FWHM at 1 MeV
    "t_req_ns": 0.6,            # time resolution requirement, sigma at 1 MeV
    "depth_req_mm": 30.0,       # minimum cell depth
    "field_T": 3e-3,            # field the calorimeter must work in
    "diag_factor": math.sqrt(2.0),  # geometry: two points inside one square cell can be up to pitch*sqrt(2) apart
}

PROPS = {
    # Adopted: 8-in. high-QE PMT (Hamamatsu R5912-MOD class) directly coupled to large PS block.
    "pmt200_direct_large_block": {
        "bulb_mm": 202.0,        # R5912 datasheet max bulb diameter 202 mm (exact datasheet value)
        "shield_mm": 3.0,        # iron magnetic shield wall around each module (arXiv:1707.06823 sec 4.1/4.2.2; thickness estimate)
        "wrap_mm": 1.0,          # PTFE + aluminised Mylar wrapping per side (arXiv:1707.06823: 600 um PTFE + 12 um Mylar)
        "res_fwhm_pct": 7.5,     # 7.5 +- 0.2 % FWHM at 1 MeV, C256 block + R5912-MOD (arXiv:1707.06823 Table 7)
        "t_sigma_ns": 0.40,      # requirement met by design, 400 ps (arXiv:1707.06823 sec 2.2); taken as nominal
        "depth_mm": 194.0,       # block depth 194 mm, front face to photocathode >= 141 mm (arXiv:1707.06823 sec 4.1)
        "max_field_T": 5e-3,     # iron shield designed for 2.5 mT (arXiv:1707.06823); x2 headroom estimate
    },
    # Survivor: 76 mm (3-in.) PMT directly coupled (no light guide) to small PS cubes, mu-metal shield.
    "pmt76_direct_small_cube": {
        "bulb_mm": 76.0,         # 3-in. PMT bulb diameter (datasheet class value, exact)
        "shield_mm": 1.0,        # mu-metal tube; saturation check: B_wall ~ B_ext*D/(2t) = 3mT*38 = 0.11 T < 0.7 T
        "wrap_mm": 1.0,          # same wrapping as above
        "res_fwhm_pct": 14.2,    # NEMO-3 3-in. modules with light guide ~17% FWHM at 1 MeV (NIM A 536 (2005) 79)
                                 # divided by the measured direct-coupling gain 1.20 +- 0.02 (arXiv:1707.06823 sec 4.1)
        "t_sigma_ns": 0.25,      # NEMO-3 time resolution ~250 ps at 1 MeV (NIM A 536 (2005) 79)
        "depth_mm": 110.0,       # design choice: 11 cm deep cube (>10 cm for gamma efficiency, arXiv:1707.06823 sec 2.1)
        "max_field_T": 1.8e-2,   # mu-metal saturation limit ~0.7 T * 2t/D = 0.7*2/76 (estimate)
    },
    # Not adopted / not survivors (listed for completeness; checked on every fact).
    "pmt130_direct": {           # 5-in. PMT, direct coupling
        "bulb_mm": 133.0,        # R6594 class 5-in. bulb (datasheet class value)
        "shield_mm": 1.5, "wrap_mm": 1.0,
        "res_fwhm_pct": 11.7,    # NEMO-3 5-in. ~14% / 1.20 (same sources as above)
        "t_sigma_ns": 0.25, "depth_mm": 110.0, "max_field_T": 1.0e-2,
    },
    "pmt254_direct_large_block": {  # 10-in. PMT
        "bulb_mm": 253.0,        # 10-in. hemispherical bulb (datasheet class value)
        "shield_mm": 3.0, "wrap_mm": 1.0,
        "res_fwhm_pct": 9.0,     # worse photoelectron collection than 8-in. (arXiv:1707.06823 sec 4.2); estimate
        "t_sigma_ns": 0.45, "depth_mm": 194.0, "max_field_T": 4e-3,
    },
    "pmt76_lightguide_present": {   # present cells, stated in the description
        "bulb_mm": 76.0, "shield_mm": 1.0, "wrap_mm": 1.0,
        "cell_face_mm": 190.0,   # stated
        "res_fwhm_pct": 20.0,    # stated
        "t_sigma_ns": 0.30,      # stated
        "depth_mm": 110.0,       # stated
        "max_field_T": 1.8e-2,
    },
}

UNC = {  # cited precisions (x0.8-1.25, the narrowest allowed)
    "props/pmt200_direct_large_block/bulb_mm": [0.8, 1.25],  # datasheet dimension
    "props/pmt200_direct_large_block/res_fwhm_pct": [0.8, 1.25],  # +-0.2 % stated (Table 7)
    "props/pmt76_direct_small_cube/bulb_mm": [0.8, 1.25],    # datasheet dimension
    "props/pmt76_direct_small_cube/res_fwhm_pct": [0.8, 1.25],  # product of two measurements; 1.20 +- 0.02 stated
    "props/pmt130_direct/bulb_mm": [0.8, 1.25],
    "props/pmt254_direct_large_block/bulb_mm": [0.8, 1.25],
}

ADOPTED = "pmt200_direct_large_block"

def min_pitch(p):
    face = p["bulb_mm"] + 2 * p["shield_mm"] + 2 * p["wrap_mm"]
    return max(face, p.get("cell_face_mm", 0.0))

def passes(p, f, sep_mm):
    return (p["res_fwhm_pct"] <= f["res_req_fwhm_pct"]
            and p["t_sigma_ns"] <= f["t_req_ns"]
            and min_pitch(p) * f["diag_factor"] <= sep_mm
            and p["depth_mm"] >= f["depth_req_mm"]
            and p["max_field_T"] >= f["field_T"])

def make(sep_mm):
    f = dict(FIXED); f["sep_mm"] = sep_mm  # stated separation, line 10
    return {"fixed": f, "props": PROPS, "unc": UNC}

def fails(inp):
    return not passes(inp["props"][ADOPTED], inp["fixed"], inp["fixed"]["sep_mm"])

def viable(inp):
    return [k for k, p in inp["props"].items() if k != ADOPTED and passes(p, inp["fixed"], inp["fixed"]["sep_mm"])]

if __name__ == "__main__":
    print("min pitch (mm, nominal):", {k: round(min_pitch(p), 1) for k, p in PROPS.items()})
    ok = check_base("BASE", make(400.0), fails)
    ok &= check_conf("CONF1", make(150.0), fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
