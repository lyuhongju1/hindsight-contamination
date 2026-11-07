"""NC key for p09_nemo3. Run: python -I nc_key.py
Target (treated as "adopted" here): alt(u) = 76 mm (3-in.) PMTs, one per cell, directly coupled (no light guide)
to small polystyrene cells, mu-metal shield (the sound survivor of the main CONF1).
Historical item (must still fail): 8-in. PMTs directly coupled to large blocks.
NC edit: the CONF1 separation 15 cm -> 6 cm (one number). Every stated fact is checked on every option:
energy resolution, time resolution, segmentation, depth >= 3 cm, operation in 3 mT.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

FIXED = {  # exact stated facts (NC_CONF lines 8-11), unchanged from the main key
    "res_req_fwhm_pct": 18.0,
    "t_req_ns": 0.6,
    "depth_req_mm": 30.0,
    "field_T": 3e-3,
    "diag_factor": math.sqrt(2.0),  # geometry: two points in one square cell can be pitch*sqrt(2) apart
}

PROPS = {
    # Historical item: values copied from materials/p09_nemo3/keys/key.py.
    "pmt200_direct_large_block": {
        "sensor_mm": 202.0, "shield_mm": 3.0, "wrap_mm": 1.0,
        "res_fwhm_pct": 7.5, "t_sigma_ns": 0.40, "depth_mm": 194.0, "max_field_T": 5e-3,
    },
    # alt(u): values copied from materials/p09_nemo3/keys/key.py (r2).
    "pmt76_direct_small_cube": {
        "sensor_mm": 76.0, "shield_mm": 1.0, "wrap_mm": 1.0,
        "res_fwhm_pct": 8.5, "t_sigma_ns": 0.25, "depth_mm": 110.0, "max_field_T": 1.8e-2,
    },
    # Third option (survivor): silicon photomultiplier array, 4x4 of 6x6 mm elements (Hamamatsu S13361-6050 class,
    # outer size ~25.8 mm, datasheet), directly on the back face of a ~26 x 26 mm polystyrene cell, 60 mm deep.
    "sipm_array_small_cell": {
        "sensor_mm": 25.8,       # array outer dimension (datasheet); the cell face is matched to it
        "shield_mm": 0.0,        # no magnetic shield needed
        "wrap_mm": 1.0,          # same reflector wrapping as the other options
        "res_fwhm_pct": 9.2,     # derived, same chain as the alt(u) 8.5 %: collection-saturation model, PDE ~40 %,
                                 # crosstalk excess noise x1.15 (see notes.md); default x0.5-2 range
        "t_sigma_ns": 0.20,      # SiPM-read plastic counters reach ~0.04-0.1 ns (MEG II pixelated timing counter); 0.2 taken
        "depth_mm": 60.0,        # design choice: 60 mm so that x0.5 still meets >= 30 mm (3 MeV e- range in PS ~1.5 cm)
        "max_field_T": 1.0,      # SiPMs operate in multi-tesla fields (e.g. CMS HCAL upgrade in 3.8 T); 1 T taken
    },
    # Extra options checked for completeness (not needed as survivors).
    "pmt25_direct_small_cell": {  # 1-in. PMT, one per cell
        "sensor_mm": 25.4, "shield_mm": 0.5, "wrap_mm": 1.0,
        "res_fwhm_pct": 9.5, "t_sigma_ns": 0.25, "depth_mm": 60.0, "max_field_T": 1.0e-2,
    },
    "pmt51_direct_small_cell": {  # 2-in. PMT, one per cell
        "sensor_mm": 51.0, "shield_mm": 0.8, "wrap_mm": 1.0,
        "res_fwhm_pct": 8.8, "t_sigma_ns": 0.25, "depth_mm": 80.0, "max_field_T": 1.2e-2,
    },
    "pmt130_direct": {
        "sensor_mm": 133.0, "shield_mm": 1.5, "wrap_mm": 1.0,
        "res_fwhm_pct": 7.9, "t_sigma_ns": 0.25, "depth_mm": 110.0, "max_field_T": 1.0e-2,
    },
    "pmt76_lightguide_present": {
        "sensor_mm": 76.0, "shield_mm": 1.0, "wrap_mm": 1.0, "cell_face_mm": 190.0,
        "res_fwhm_pct": 20.0, "t_sigma_ns": 0.30, "depth_mm": 110.0, "max_field_T": 1.8e-2,
    },
}

UNC = {  # cited precisions (x0.8-1.25, the narrowest allowed): datasheet dimensions only
    "props/pmt200_direct_large_block/sensor_mm": [0.8, 1.25],
    "props/pmt200_direct_large_block/res_fwhm_pct": [0.8, 1.25],
    "props/pmt76_direct_small_cube/sensor_mm": [0.8, 1.25],
    "props/sipm_array_small_cell/sensor_mm": [0.8, 1.25],
    "props/pmt25_direct_small_cell/sensor_mm": [0.8, 1.25],
    "props/pmt51_direct_small_cell/sensor_mm": [0.8, 1.25],
    "props/pmt130_direct/sensor_mm": [0.8, 1.25],
}

ALT = "pmt76_direct_small_cube"
HIST = "pmt200_direct_large_block"

def min_pitch(p):
    return max(p["sensor_mm"] + 2 * p["shield_mm"] + 2 * p["wrap_mm"], p.get("cell_face_mm", 0.0))

def passes(p, f):
    return (p["res_fwhm_pct"] <= f["res_req_fwhm_pct"]
            and p["t_sigma_ns"] <= f["t_req_ns"]
            and min_pitch(p) * f["diag_factor"] < f["sep_mm"]
            and p["depth_mm"] >= f["depth_req_mm"]
            and p["max_field_T"] >= f["field_T"])

def make(sep_mm):
    f = dict(FIXED); f["sep_mm"] = sep_mm
    return {"fixed": f, "props": PROPS, "unc": UNC}

def fails_alt(inp):
    return not passes(inp["props"][ALT], inp["fixed"])

def fails_hist(inp):
    return not passes(inp["props"][HIST], inp["fixed"])

def viable(inp):
    return [k for k, p in inp["props"].items() if k not in (ALT, HIST) and passes(p, inp["fixed"])]

if __name__ == "__main__":
    print("min pitch (mm, nominal):", {k: round(min_pitch(p), 1) for k, p in PROPS.items()})
    ok = check_base("NC_BASE", make(150.0), fails_alt)            # = main CONF1: alt(u) passes
    ok &= check_conf("NC_CONF", make(60.0), fails_alt, viable)    # alt(u) fails, third option survives
    ok &= check_conf("NC_HIST", make(60.0), fails_hist, viable)   # historical item still fails
    print("ALL PASS" if ok else "SOME FAIL")
