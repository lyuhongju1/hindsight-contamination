"""Key for s2_q77_clas (PROVISIONAL). Run: python -I key.py
Adopted item: a lead/scintillator-strip pre-converter section (~5-6 X0, stereo strips) added in front of the
RETAINED lead/scintillator sampling calorimeter (stated sigma/E = 12%/sqrt(E)).
Settings of the item scanned: section depth (3-8 X0), strip pitch (1.5-6 cm), and its own sampling term down
to a_pre_min. Every stated fact is checked on every option: pi0 two-shower separation at 10 GeV/c at 6.5 m,
photon resolution at 2 GeV, free depth 60 cm, field 1 mT at the calorimeter, dose 50 Gy/yr.
All resolutions are sigma.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

FIXED = {  # exact stated facts (BASE/CONF1 lines 2-7) and definitions
    "E_GeV": 2.0,          # stated photon energy of the resolution requirement
    "p_pi0_GeV": 10.0,     # stated max pi0 momentum
    "m_pi0_GeV": 0.135,    # pi0 mass (PDG, exact)
    "L_cm": 650.0,         # stated target-calorimeter distance
    "depth_free_cm": 60.0, # stated free depth
    "field_T": 1e-3,       # stated field at the calorimeter
    "dose_Gy_yr": 50.0,    # stated dose at the face
    "a_ec": 0.12,          # stated stochastic term of the present (retained) calorimeter
    "k_sep": 2.0,          # two showers resolved if separation >= 2 x max(cell pitch, shower core width): definition
}

PROPS = {
    "item_preconv_plus_retained": {   # adopted; settings scanned in item_res()
        "a_pre_min": 0.08,     # best stochastic term of a strip-readout Pb/scint section (EC-type 11.6%, NIM A460 (2001) 239; finer sampling estimate)
        "c": 0.01,             # constant term (estimate; only helps the item when small)
        "X0_cm": 3.3,          # effective X0 of Pb(2.2 mm)/scint(10 mm) stack (15 layers ~ 5.5 X0 ~ 18 cm)
        "core_cm": 4.0,        # shower core width in the first X0 of a Pb/scint stack (estimate, feasibility note)
        "Ec_MeV": 7.4,         # critical energy of Pb (PDG) for the longitudinal profile
        "b_prof": 0.5,         # longitudinal profile slope parameter (PDG review, Longo 1975)
        "max_field_T": 5e-3,   # shielded PMT readout (estimate)
        "rad_tol_Gy_yr": 1e4,  # plastic scintillator damage ~1e4 Gy (estimate)
    },
    "pbwo4_pmt": {             # survivor: homogeneous crystal calorimeter, PMT readout
        "a": 0.026,            # PrimEx/PRad HyCal PbWO4 part, 2.6%/sqrt(E) sigma (Gasparian et al.; Xiong et al. Nature 575 (2019) 147) - NOT fetched
        "b_GeV": 0.01,         # noise term with PMT readout (estimate)
        "c": 0.005,            # constant term (CMS test beam 0.3%, JINST 3 (2008) S08004; HyCal ~0.5-1%)
        "X0_cm": 0.89,         # PbWO4 X0 (PDG)
        "n_X0": 22.0,          # crystal length in X0 (CMS 23 cm = 25.8 X0; HyCal 18 cm = 20 X0)
        "RM_cm": 2.0,          # PbWO4 Moliere radius (PDG); 2 cm cells
        "pitch_cm": 2.05,      # crystal cell
        "max_field_T": 5e-3,   # shielded PMT (estimate)
        "rad_tol_Gy_yr": 1e5,  # CMS PbWO4 operated at up to ~Gy/h with recoverable loss (estimate)
    },
    "shashlik_fine": {         # alternative sampling rebuild (counted if it survives)
        "a": 0.03,             # KOPIO-type 0.275 mm Pb / 1.5 mm scint, ~3%/sqrt(E) sigma (Atoyan et al., NIM A531 (2004) 467) - NOT fetched
        "b_GeV": 0.01, "c": 0.01,
        "X0_cm": 3.4, "n_X0": 16.0, "RM_cm": 6.0, "pitch_cm": 11.0,
        "max_field_T": 5e-3, "rad_tol_Gy_yr": 1e4,
    },
    "lead_glass": {            # not a survivor
        "a": 0.055, "b_GeV": 0.01, "c": 0.01,
        "X0_cm": 2.5, "n_X0": 16.0, "RM_cm": 3.7, "pitch_cm": 4.0,
        "max_field_T": 5e-3, "rad_tol_Gy_yr": 50.0,
    },
}
UNC = {  # cited precisions of measured/material values (narrowest allowed, x0.8-1.25)
    "props/pbwo4_pmt/a": [0.8, 1.25],      # measured stochastic term
    "props/pbwo4_pmt/X0_cm": [0.8, 1.25],  # material constant (PDG)
    "props/pbwo4_pmt/RM_cm": [0.8, 1.25],  # material constant (PDG)
}
ADOPTED = "item_preconv_plus_retained"

def sep_cm(f):
    return f["L_cm"] * 2 * f["m_pi0_GeV"] / f["p_pi0_GeV"]

def frac_in(t_max_X0, E_GeV, p):
    """Fraction of photon shower energy in the first t_max_X0 (gamma-function profile, PDG)."""
    b = p["b_prof"]; tmax = math.log(E_GeV * 1000 / p["Ec_MeV"]) + 0.5; a = b * tmax + 1
    n = 400; h = 60.0 / n
    g = [((i + .5) * h) ** (a - 1) * math.exp(-b * (i + .5) * h) for i in range(n)]
    tot = sum(g); return sum(gi for i, gi in enumerate(g) if (i + .5) * h <= t_max_X0) / tot

def item_ok(p, f):
    E = f["E_GeV"]
    if p["max_field_T"] < f["field_T"] or p["rad_tol_Gy_yr"] < f["dose_Gy_yr"]: return False
    for X in (3, 4, 5, 6, 7, 8):                 # section depth setting (X0)
        if X * p["X0_cm"] > f["depth_free_cm"]: continue
        for pitch in (1.5, 2, 3, 4.5, 6):        # strip pitch setting (cm)
            if sep_cm(f) < f["k_sep"] * max(pitch, p["core_cm"]): continue
            fr = frac_in(X, E, p)
            stoch = math.sqrt(fr * p["a_pre_min"] ** 2 + (1 - fr) * f["a_ec"] ** 2) / math.sqrt(E)
            if math.hypot(stoch, p["c"]) <= f["res_req"]: return True
    return False

def alt_ok(p, f):
    E = f["E_GeV"]
    res = math.sqrt((p["a"] / math.sqrt(E)) ** 2 + (p["b_GeV"] / E) ** 2 + p["c"] ** 2)
    return (res <= f["res_req"] and p["X0_cm"] * p["n_X0"] <= f["depth_free_cm"]
            and sep_cm(f) >= f["k_sep"] * max(p["pitch_cm"], p["RM_cm"])
            and p["max_field_T"] >= f["field_T"] and p["rad_tol_Gy_yr"] >= f["dose_Gy_yr"])

def make(req):
    f = dict(FIXED); f["res_req"] = req
    return {"fixed": f, "props": PROPS, "unc": UNC}

def fails(inp): return not item_ok(inp["props"][ADOPTED], inp["fixed"])
def viable(inp): return [k for k, p in inp["props"].items() if k != ADOPTED and alt_ok(p, inp["fixed"])]

if __name__ == "__main__":
    f = make(0.03)["fixed"]; p = PROPS[ADOPTED]
    print(f"pi0 separation at 10 GeV/c: {sep_cm(f):.1f} cm")
    for X in (3, 5, 8):
        fr = frac_in(X, 2.0, p); s = math.sqrt(fr * p["a_pre_min"]**2 + (1-fr) * f["a_ec"]**2) / math.sqrt(2)
        print(f"item depth {X} X0: frac={fr:.2f} sigma/E(2 GeV)={100*math.hypot(s, p['c']):.2f}%")
    ok = check_base("BASE", make(0.10), fails)
    ok &= check_conf("CONF1", make(0.03), fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
