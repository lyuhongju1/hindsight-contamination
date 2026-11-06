"""Key for p07_meg. Run: python -I key.py
Mechanism (CONF1): magnetic mirror. The adopted on-axis tagger downstream of the target only sees low-energy
positrons that reach the downstream end. If the field rises downstream (B_down > B_target), only positrons
inside the loss cone sin^2(alpha) < B_target/B_down get through. The rest are reflected upstream.
"""
import copy, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

FIXED_COMMON = {
    # exact stated facts in BASE.txt / CONF1.txt (not varied; see notes.md)
    "B_target": 0.5,        # T, stated
    "B_up": 0.25,           # T, stated (upstream end)
    "R_beam": 5e7,          # mu+/s delivered, stated
    "R_stop": 4.5e7,        # mu+/s stopped, stated
    "degrader": 50.0,       # mg/cm2 Mylar that can be thinned to compensate added beam-path material, stated
    "tracker_rmin": 15.0,   # cm, stated: no option places material in the tracker volume
    "req_reduction": 0.10,  # stated requirement: accidental background reduced by >= 10%
    "max_loss": 0.02,       # stated requirement: signal efficiency loss <= 2%
}

PROPS = {
    # f_rmd: fraction of accidental high-energy photons from radiative muon decay ("about half", stated; varied anyway)
    "f_rmd": 0.5,
    "downstream": {
        "eps_det": 0.9,     # detection eff. of a scintillator+crystal tagger for 1-5 MeV e+ (MEG II design report, approx.)
        "window": 2e-9,     # s, tag coincidence window (~ +-1 ns, scintillator timing ~100 ps class)
        "f_michel": 0.03,   # fraction of Michel e+ reaching an on-axis end counter with a symmetric field (est.)
        "q_ecut": 0.2,      # fraction of those Michel e+ passing the low-energy deposit cut (est.)
        "k_beam": 0.1,      # tag-like hits per transmitted (non-stopped) muon reaching the counter (est.)
        "in_beam": 0.0,     # mg/cm2 added in the beam path upstream of the target (none)
        "r_max": 7.0,       # cm, outer radius needed: 2 r_g for 5 MeV/c e+ at 0.25 T is ~13 cm diameter
    },
    "upstream": {
        "eps_det": 0.9,     # same scintillator technology, thin fibre layer + downstream-of-beam crystals (est.)
        "window": 2e-9,     # s
        "f_michel": 0.03,   # as above
        "q_ecut": 0.2,      # as above
        "p_misid": 0.01,    # beam mu+ (0.5-1 MeV in 200 um fibre vs ~0.04 MeV for e+) misidentified as e+ (est.)
        "in_beam": 21.0,    # mg/cm2: 200 um polystyrene fibre layer (1.05 g/cm3)
        "r_max": 7.0,       # cm
    },
}

def reach(inp, side):
    """Fraction of isotropically emitted low-energy e+ that reach the end on `side` (adiabatic guiding centre)."""
    f = inp["fixed"]
    Bt = f["B_target"]
    Bs, Bo = (f["B_down"], f["B_up"]) if side == "downstream" else (f["B_up"], f["B_down"])
    own = 0.5 if Bs <= Bt else 0.5 * (1 - math.sqrt(1 - Bt / Bs))   # loss cone through own-side mirror
    back = 0.0 if Bo <= Bt else 0.5 * math.sqrt(1 - Bt / Bo)         # reflected from the other side's mirror
    if Bs > Bt and Bo > Bt:
        back = 0.0  # trapped between two mirrors; not counted
    return own + back

def passes(inp, side):
    f, p = inp["fixed"], inp["props"][side]
    r = reach(inp, side)
    red = min(inp["props"]["f_rmd"], 1.0) * r * min(p["eps_det"], 1.0)
    michel = f["R_stop"] * p["f_michel"] * (r / 0.5) * p["q_ecut"]
    if side == "downstream":
        beam = (f["R_beam"] - f["R_stop"]) * p["k_beam"]  # non-stopped muons continue downstream
    else:
        beam = f["R_beam"] * p["p_misid"]                 # full beam crosses the upstream layer
    loss = 1 - math.exp(-p["window"] * (michel + beam))
    ok_red = red >= f["req_reduction"]
    ok_loss = loss <= f["max_loss"]
    ok_beam = p["in_beam"] <= f["degrader"]               # degrader can be thinned by the same amount
    ok_geom = p["r_max"] < f["tracker_rmin"]              # fits inside the tracker's inner radius on the axis
    # calorimeter resolutions (stated) are unchanged by either option
    return ok_red and ok_loss and ok_beam and ok_geom

def make(B_down):
    return {"fixed": dict(FIXED_COMMON, B_down=B_down), "props": copy.deepcopy(PROPS)}

def fails(inp):
    return not passes(inp, "downstream")

def viable(inp):
    return [s for s in ("upstream",) if passes(inp, s)]

if __name__ == "__main__":
    base = make(0.25)   # BASE: field falls to 0.25 T at both ends
    conf1 = make(2.0)   # CONF1: field rises to 2.0 T downstream
    for name, inp in (("BASE", base), ("CONF1", conf1)):
        print(f"{name}: reach_down={reach(inp, 'downstream'):.3f} reach_up={reach(inp, 'upstream'):.3f}")
    ok = check_base("BASE", base, fails)
    ok &= check_conf("CONF1", conf1, fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
