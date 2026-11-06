"""Key for p01_xenon1t (BASE, CONF1). Run: python -I key.py
Adopted item: purification acting on the circulated liquid (any purifier at LXe temperature, ~170 K).
Model: well-mixed inventory M; each processing path i with mass flow F_i and single-pass removal efficiency eps_i.
  CH4 (CH3T) residual after T days: A * exp(-sum(eps_i F_i) T / M)
  steady-state O2-equivalent impurity: c[ppb] = Q / sum(eps_i F_i); electron lifetime tau = K / c
Every stated fact (M, flows, drift-time requirement, injected activity, limit, window) is checked on every option.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

FIXED = {  # exact stated facts in BASE/CONF1 (not varied; see notes.md)
    "M_kg": 4000.0,            # "The cryostat holds 4.0 t of xenon"
    "F_gas_kg_d": 50.0 * 24,   # "heated zirconium getters at 50 kg per hour" (existing hardware)
    "F_col_kg_d": 3.0 * 24,    # "distillation column processes 3 kg of xenon per hour"
    "tau_req_ms": 0.5,         # "electron lifetime must be at least 0.5 ms"
    "T_days": 90.0,            # CONF1: "within 90 days after each campaign"
    "limit_Bq": 1e-3,          # CONF1: "below 1 mBq"
}

PROPS = {
    # Hot (~400 C) Zr getter: chemisorbs CH4 (thermally activated); LUX removed CH3T via hot getter
    # (LUX, PRD 93 072009 (2016)). Single-pass CH4 efficiency at rated flow taken 0.95 (CH4 is the hardest
    # species for hot Zr getters). O2/H2O single-pass ~0.99 (SAES PS4-MT spec: outlet < 1 ppb).
    "gas_getter": {"eps_ch4": 0.95, "eps_o2": 0.99},
    # Purifier acting on liquid at ~170 K (Cu filter, cold NEG, zeolite): no thermally activated C-H
    # dissociation; physisorption sites saturated by the Xe solvent -> CH4 single-pass efficiency <= 1e-3
    # (conservative upper bound, see notes.md doubts). O2 removal ~0.99 (XENONnT liquid purification,
    # >10 ms lifetime reported, arXiv:2402.10446). Liquid flow ~2 L/min LXe = ~8.5 t/day.
    "liquid": {"eps_ch4": 1e-3, "eps_o2": 0.99, "F_kg_d": 8500.0},
    # Distillation column: CH4 (bp 112 K) and O2 (bp 90 K) leave with the light fraction; eps ~ 1 (taken 0.9).
    "column": {"eps_ch4": 0.9, "eps_o2": 0.9},
    # O2-equivalent outgassing load, ppb*kg/day: from XENON1T-like ~0.65 ms (c~0.46 ppb) at ~425 kg/day.
    "Q_ppb_kg_d": 200.0,
    # Attachment: tau[ms] ~ 0.3 / c[ppb O2-eq] (common rule of thumb from Bakale et al. 1976 rate constant).
    "K_ms_ppb": 0.3,
}

def clip(e): return min(e, 1.0)

def paths(inp, option):
    f, p = inp["fixed"], inp["props"]
    col = (clip(p["column"]["eps_ch4"]) * f["F_col_kg_d"], clip(p["column"]["eps_o2"]) * f["F_col_kg_d"])
    if option == "liquid_phase":       # adopted: main circulation through the liquid purifier, column kept
        main = (clip(p["liquid"]["eps_ch4"]) * p["liquid"]["F_kg_d"], clip(p["liquid"]["eps_o2"]) * p["liquid"]["F_kg_d"])
    elif option == "gas_phase_getters":  # existing heated getters at the stated 40 kg/h, column kept
        main = (clip(p["gas_getter"]["eps_ch4"]) * f["F_gas_kg_d"], clip(p["gas_getter"]["eps_o2"]) * f["F_gas_kg_d"])
    elif option == "column_only":        # distillation column alone as purifier (stated 3 kg/h)
        main = (0.0, 0.0)
    return main[0] + col[0], main[1] + col[1]

def passes(inp, option, conf):
    f, p = inp["fixed"], inp["props"]
    r_ch4, r_o2 = paths(inp, option)
    tau = p["K_ms_ppb"] / (p["Q_ppb_kg_d"] / r_o2)
    ok = tau >= f["tau_req_ms"]
    if conf:
        resid = f["A_Bq"] * math.exp(-r_ch4 * f["T_days"] / f["M_kg"])
        ok = ok and resid <= f["limit_Bq"]
    return ok

ALTS = ["gas_phase_getters", "column_only"]

def mk(conf):
    fx = dict(FIXED); fx["A_Bq"] = 10.0 if conf else 0.0  # CONF1: "10 Bq of tritiated methane"; BASE: none
    return {"fixed": fx, "props": PROPS}

base, conf1 = mk(False), mk(True)
check_base("BASE", base, lambda i: not passes(i, "liquid_phase", False))
for o in ["liquid_phase"] + ALTS:
    print(f"   BASE nominal {o:18s} passes={passes(base, o, False)}")
check_conf("CONF1", conf1, lambda i: not passes(i, "liquid_phase", True),
           lambda i: [o for o in ALTS if passes(i, o, True)])
for o in ["liquid_phase"] + ALTS:
    r_ch4, r_o2 = paths(conf1, o)
    print(f"   CONF1 nominal {o:18s} CH4_resid={10*math.exp(-r_ch4*90/4000):.3g} Bq  "
          f"tau={PROPS['K_ms_ppb']*r_o2/PROPS['Q_ppb_kg_d']:.2f} ms  passes={passes(conf1, o, True)}")
