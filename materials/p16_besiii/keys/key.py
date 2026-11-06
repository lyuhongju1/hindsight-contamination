"""Key for p16_besiii. Run: python -I key.py"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

# Cited properties (varied x0.5-2 by keylib). Sources in notes.md.
ADOPTED_VARIANTS = {
    # rate95: highest charged flux (Hz/cm^2) with >=95% efficiency demonstrated; sigma_ps: single-layer resolution there
    "float_glass":   {"rate95": 1.0e3, "sigma_ps": 50.0,  "B_max_T": 20.0, "dose_max_Gy": 1.0e6, "fluence_max": 1.0e16},  # ALICE/STAR-type float glass ~1e12-1e13 ohm cm
    "lowres_glass":  {"rate95": 3.0e4, "sigma_ps": 55.0,  "B_max_T": 20.0, "dose_max_Gy": 1.0e6, "fluence_max": 1.0e16},  # ~1e10 ohm cm glass, CBM-type R&D
    "ceramic":       {"rate95": 5.0e5, "sigma_ps": 120.0, "B_max_T": 20.0, "dose_max_Gy": 1.0e6, "fluence_max": 1.0e16},  # Si3N4/SiC 5e9 ohm cm; 95% at 2e5 (~120 ps), most generous quoted flux 5e5 used
}
ALTERNATIVES = {
    # three-layer silicon sensors with internal gain (pads ~1.3 mm): sigma per hit at ~4e14 neq/cm^2, inefficiency per layer
    "lgad_3layer":      {"rate95": 1.0e8, "sigma_ps": 35.0, "ineff": 0.02, "B_max_T": 20.0, "dose_max_Gy": 2.0e6, "fluence_max": 1.5e15},
    # fine plastic scintillator tiles (1 cm^2) + SiPM at room temperature: single-MIP timing lost above ~1e12 neq/cm^2
    "scint_tile_sipm":  {"rate95": 1.0e7, "sigma_ps": 45.0, "ineff": 0.01, "B_max_T": 20.0, "dose_max_Gy": 5.0e4, "fluence_max": 1.0e12},
    # cooled LYSO tiles + SiPM (barrel-timing-layer type)
    "lyso_sipm_cooled": {"rate95": 3.0e6, "sigma_ps": 40.0, "ineff": 0.01, "B_max_T": 20.0, "dose_max_Gy": 5.0e5, "fluence_max": 2.0e14},
    # improved large plastic counters (600 cm^2) with fine-mesh PMTs: rate95 per cm^2 = per-channel limit 1e7 Hz / 600 cm^2
    "scint_counter_pmt":{"rate95": 1.7e4, "sigma_ps": 90.0, "ineff": 0.01, "B_max_T": 2.5, "dose_max_Gy": 1.0e4, "fluence_max": 1.0e13},
}
# integer structural counts (fixed): layers per option; MRPC stacking allowed up to 4 layers (generous)
N_LAYERS = {"lgad_3layer": 3, "scint_tile_sipm": 2, "lyso_sipm_cooled": 1, "scint_counter_pmt": 1}

def make(flux_min, dose, fluence):
    return {"fixed": {"flux_min": flux_min, "dose": dose, "fluence": fluence, "B": 2.0,
                      "sigma_req": 60.0, "eff_req": 0.95, "n_mrpc_max": 4, "n_layers": dict(N_LAYERS)},
            "props": {"adopted": {k: dict(v) for k, v in ADOPTED_VARIANTS.items()},
                      "alt": {k: dict(v) for k, v in ALTERNATIVES.items()}}}

def env_ok(p, f):
    return p["rate95"] >= f["flux_min"] and p["B_max_T"] >= f["B"] and p["dose_max_Gy"] >= f["dose"] and p["fluence_max"] >= f["fluence"]

def fails(inp):
    f = inp["fixed"]
    for p in inp["props"]["adopted"].values():  # any electrode variant, stacked up to n_mrpc_max layers
        if env_ok(p, f) and p["sigma_ps"] / math.sqrt(f["n_mrpc_max"]) <= f["sigma_req"]:
            return False
    return True

def track_ok_fraction(p, n):
    """fraction of tracks with enough hits that the averaged time meets sigma_req"""
    q = min(max(p["ineff"], 0.0), 1.0)
    return lambda sig_req: sum(math.comb(n, k) * (1 - q) ** k * q ** (n - k)
                               for k in range(1, n + 1) if p["sigma_ps"] / math.sqrt(k) <= sig_req)

def viable(inp):
    f = inp["fixed"]; out = []
    for name, p in inp["props"]["alt"].items():
        if env_ok(p, f) and track_ok_fraction(p, f["n_layers"][name])(f["sigma_req"]) >= f["eff_req"]:
            out.append(name)
    return out

if __name__ == "__main__":
    # BASE: inner-edge flux (strictest for a pass); CONF1: outer-edge flux (strictest for a failure)
    ok = check_base("BASE", make(2.0e3, 20.0, 8e10), fails)
    ok &= check_conf("CONF1", make(1.5e6, 1.0e5, 4e14), fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
