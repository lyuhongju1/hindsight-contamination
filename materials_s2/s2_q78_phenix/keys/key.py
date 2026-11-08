"""Key for s2_q78_phenix. Run with: python -I key.py
All resolutions are sigma (not FWHM). Units: cm, GeV, Gy, T, ns, fractions.
Adopted item: compact W-powder/epoxy + scintillating-fibre sampling EM calorimeter, coded in
every sampling configuration (W volume fraction scaled down, fibre fraction up; fibre diameter
0.25-1.0 mm). Survivor: PbWO4 crystals with APD readout (PHOS-like). Other alternatives: PbSc
(shashlik), PbGl, Pb/LAr accordion.
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

# Item settings (not varied: they are the design choices an expert could make within the item)
SCALES = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]      # W(+binder) volume scaled by s; fibres fill the rest
FIBRE_D = [0.25, 0.35, 0.47, 0.6, 1.0]                  # mm

def base_inputs(req):
    return {
        "fixed": {
            "E_ref": 2.0,            # GeV, energy at which the requirement is stated
            "req_sigma": req,        # sigma_E/E required at E_ref (fraction)
            "gap": 32.0,             # cm radial space for the calorimeter incl. readout
            "B": 1.4,                # T solenoid field at the calorimeter
            "dose": 20.0,            # Gy total over the programme at the calorimeter
            "crossing": 100.0,       # ns between bunch crossings
            "n_X0": 18.0,            # stated longitudinal containment, radiation lengths
            "rm_max": 2.5,           # cm, stated radius containing 90% of a photon shower (= Moliere radius)
        },
        "unc": {},
        "props": {
            # PDG material constants
            "pdg": {"X0_W": 0.3504, "RM_W": 0.9327, "dEdx_W": 22.10, "X0_poly": 41.0, "RM_poly": 9.4,
                    "dEdx_scint": 2.00, "dEdx_epoxy": 2.3},
            # W/SciFi item, nominal sPHENIX-like block; resolution from 2D projective prototype (TNS 68 (2021) 173)
            "wsf": {"X0_nom": 0.70, "vf0": 0.20, "e0": 0.30, "b": 0.133, "c": 0.035, "d0": 0.47,
                    "readout": 4.0, "Bmax": 5.0, "t_sig": 15.0, "dose_tol": 1.0e4},
            # PbWO4 + APD (PHOS NIM A550 (2005) 169; PDG for X0, RM)
            "pwo": {"X0": 0.8903, "RM": 1.959, "a": 0.0130, "b": 0.0358, "c": 0.0112, "dLY_dT": 0.02,
                    "dT": 0.1, "readout": 5.0, "Bmax": 4.0, "t_sig": 10.0, "dose_tol": 500.0},
            # PHENIX PbSc and PbGl (NIM A499 (2003) 521); PDG/ATLAS for LAr accordion
            "pbsc": {"X0": 2.02, "RM": 3.0, "b": 0.081, "c": 0.021, "readout": 8.0, "Bmax": 0.01, "t_sig": 10.0, "dose_tol": 1.0e3},
            "pbgl": {"X0": 2.8, "RM": 3.7, "b": 0.059, "c": 0.008, "readout": 8.0, "Bmax": 0.01, "t_sig": 5.0, "dose_tol": 50.0},
            "lar": {"X0": 1.9, "RM": 4.0, "b": 0.10, "c": 0.007, "readout": 15.0, "Bmax": 5.0, "t_sig": 450.0, "dose_tol": 1.0e5},
        },
    }

def wsf_configs(x):
    p, w = x["props"]["pdg"], x["props"]["wsf"]
    # nominal W volume fraction from the nominal X0: 1/X0 = fW/X0_W + (1-fW)/X0_poly
    fW0 = (1 / w["X0_nom"] - 1 / p["X0_poly"]) / (1 / p["X0_W"] - 1 / p["X0_poly"])
    def fmip(fW, fe, vf):
        return vf * p["dEdx_scint"] / (vf * p["dEdx_scint"] + fW * p["dEdx_W"] + fe * p["dEdx_epoxy"])
    vf0 = min(w["vf0"], 1 - fW0 - 0.01)
    e0 = max(0.0, 1 - fW0 - vf0)
    f_nom = fmip(fW0, e0, vf0)
    out = []
    for s in SCALES:
        fW, fe = fW0 * s, e0 * s
        vf = 1 - fW - fe
        X0 = 1 / (fW / p["X0_W"] + (1 - fW) / p["X0_poly"])
        RM = 1 / (fW / p["RM_W"] + (1 - fW) / p["RM_poly"])
        f = fmip(fW, fe, vf)
        for d in FIBRE_D:
            b = w["b"] * math.sqrt((f_nom / f) * (d / w["d0"]))   # sampling term ~ sqrt(d / f_samp)
            out.append({"X0": X0, "RM": RM, "b": b, "c": w["c"], "a": 0.0, "readout": w["readout"],
                        "Bmax": w["Bmax"], "t_sig": w["t_sig"], "dose_tol": w["dose_tol"], "tag": (s, d)})
    return out

def sigma(o, E):
    return math.sqrt((o.get("a", 0.0) / E) ** 2 + o["b"] ** 2 / E + o["c"] ** 2)

def passes(o, x):
    st, fx = x["fixed"], x["fixed"]
    return (sigma(o, st["E_ref"]) <= st["req_sigma"]
            and fx["n_X0"] * o["X0"] + o["readout"] <= st["gap"]
            and o["RM"] <= fx["rm_max"]
            and o["Bmax"] >= st["B"]
            and o["t_sig"] <= st["crossing"]
            and o["dose_tol"] >= st["dose"])

def pwo_opt(x):
    o = dict(x["props"]["pwo"])
    o["c"] = math.hypot(o["c"], o["dLY_dT"] * o["dT"])   # temperature-stabilisation residual adds to constant term
    return o

def fails(x):
    return not any(passes(o, x) for o in wsf_configs(x))

def viable(x):
    opts = {"PbWO4_APD": pwo_opt(x), "PbSc": x["props"]["pbsc"], "PbGl": x["props"]["pbgl"], "LAr_accordion": x["props"]["lar"]}
    return [k for k, o in opts.items() if passes(o, x)]

def best_wsf(x):
    cs = wsf_configs(x)
    ok_geo = [o for o in cs if x["fixed"]["n_X0"] * o["X0"] + o["readout"] <= x["fixed"]["gap"] and o["RM"] <= x["fixed"]["rm_max"]]
    o = min(ok_geo, key=lambda o: sigma(o, x["fixed"]["E_ref"]))
    return o["tag"], sigma(o, x["fixed"]["E_ref"]), o["RM"], o["X0"]

if __name__ == "__main__":
    base = base_inputs(0.12)
    conf = base_inputs(0.04)
    UNC = {"props/wsf/b": [0.8, 1.25], "props/wsf/c": [0.8, 1.25], "props/wsf/X0_nom": [0.8, 1.25],
           "props/pwo/X0": [0.8, 1.25], "props/pwo/RM": [0.8, 1.25], "props/pwo/b": [0.8, 1.25],
           "props/pdg/X0_W": [0.8, 1.25], "props/pdg/RM_W": [0.8, 1.25], "props/pdg/dEdx_W": [0.8, 1.25],
           "props/pdg/dEdx_scint": [0.8, 1.25], "props/pdg/X0_poly": [0.8, 1.25], "props/pdg/RM_poly": [0.8, 1.25]}
    base["unc"] = dict(UNC); conf["unc"] = dict(UNC)
    print("nominal best W/SciFi config (scale, fibre mm), sigma/E at 2 GeV, RM cm, X0 cm:", best_wsf(conf))
    print("nominal PbWO4 sigma/E at 2 GeV: %.4f" % sigma(pwo_opt(conf), 2.0))
    check_base("BASE", base, fails)
    check_conf("CONF1", conf, fails, viable)
    # Sensitivity (decisive for the verdict): the item's constant term is partly a uniformity/calibration
    # setting (the same prototype gives 3.0% or 3.5% depending on the correction). Halve it:
    conf_c = base_inputs(0.04); conf_c["unc"] = dict(UNC); conf_c["props"]["wsf"]["c"] *= 0.5
    print("sensitivity c_wsf x0.5: best W/SciFi", best_wsf(conf_c))
    check_conf("CONF1_c/2", conf_c, fails, viable)
    # Stochastic-only comparison: item with c = 1% (an optimistic but routine calibration target)
    conf_s = base_inputs(0.04); conf_s["unc"] = dict(UNC); conf_s["props"]["wsf"]["c"] = 0.01
    print("sensitivity c_wsf = 1%: best W/SciFi", best_wsf(conf_s))
    check_conf("CONF1_c1", conf_s, fails, viable)
