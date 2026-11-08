"""Key for s2_q60_danss (red-team r1 FIX round). Run: python -I key.py
Adopted item: neutron (delayed) tagging by gadolinium capture, in any form (coating, film or loaded plastic).
Settings of the item (threshold x topology x coincidence window x distance cut, 336 in all); the item fails only if ALL fail.
Every stated fact is checked on every option:
  - volume V and outer polyethylene layer (escape model calibrated on SANDD, which has a PE layer),
  - reactor power P and distance L (IBD rate),
  - ambient singles rate per m2 of outer surface above 1 MeV (site fact),
  - delayed (neutron-tag) efficiency >= EFF_REQ,
  - accidental coincidence rate <= ACC_REQ x detected IBD signal rate.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

def fixed(V_L):
    return {  # exact stated facts, or physical constants
        "V_L": V_L,                  # stated scintillator volume (BASE 900 L, CONF1 30 L), treated as a cube
        "P_th_W": 3.0e9,             # stated thermal power
        "L_cm": 1000.0,              # stated distance from core centre, 10 m
        "amb_Hz_per_m2": 80.0,       # stated site fact: ambient single deposits above 1 MeV per m2 of outer surface
        "EFF_REQ": 0.30,             # stated: neutron capture signal recorded for >= 30% of IBD events in the volume
        "ACC_REQ": 1.0,              # stated: accidental coincidences below the IBD signal rate
        "nH_per_cm3": 4.86e22,       # H atoms per cm3 of polystyrene-class plastic (C8H8, 1.05 g/cm3), exact
        "E_fis_J": 200.0 * 1.602e-13,  # energy per fission, ~200 MeV (physical constant to ~2%)
        "Gd_casc_MeV": 7.9,          # 157Gd(n,g) Q = 7.94 MeV (155Gd 8.54 MeV); capture is >80% on 157Gd
        "Gd_mult": 4,                # mean cascade multiplicity ~4 (integer structural count; 3 and 5 checked in notes)
        "Tl_MeV": 2.614,             # 208Tl line, the end of the natural gamma spectrum
        "prompt_thr_MeV": 1.0,       # stated: the positron spectrum is recorded from 1 MeV upward (fixes the prompt cut)
    }

COMMON = {  # shared physics, varied once per draw
    "sigma_f_cm2": 5.8e-43,          # IBD yield per fission (Huber-Mueller-class flux x cross section), few % precision
    "eps_prompt": 0.80,              # positron (prompt) efficiency, SANDD 80.2% at 9 L (arXiv:2105.00083)
    "lam_gamma_cm": 19.7,            # 2 MeV gamma attenuation length in polystyrene, NIST XCOM mu/rho = 0.0484 cm2/g
    "frac_above_2p0": 0.25,          # fraction of ambient singles (>1 MeV) above 2.0 MeV (208Tl, n-H 2.2 MeV); estimate
    "frac_above_2p7": 0.01,          # fraction above 2.7 MeV (only capture gammas, cosmogenic); estimate
    "n_amb_Hz_per_m2": 0.6,          # ambient (cosmogenic) neutron captures per m2 of outer surface; estimate
    "lam_n_window_frac": 1.0,        # gamma singles in a 0.4-0.65 MeVee window relative to the >1 MeV rate; estimate
}

GD = {  # physical properties of the item, shared by all its settings (varied once per draw)
    "ell_n_cm": 9.0,                 # effective neutron travel; SANDD-calibrated 10.2 cm, shorter for Gd (tau ~24-30 us)
    "loss_capture_H": 0.14,          # captures on H instead of Gd; PANDA Geant4, 85.7% on Gd for 6 cm bars
    "tau_us": 24.0,                  # capture time, DANSS Gd-coated strips 24 us (arXiv:1606.02896); PANDA 29.6 us
    "dist_x0_sigma": 2.8,            # nominal V_local radius in units of the 3D displacement sigma (chi3 CDF 0.95); estimate
    "V_local_L": 8.0,                # coincidence region; Gd cascade centroid smeared over 10-20 cm (Route B)
    "amb_multi_frac": 0.4,           # fraction of ambient >1 MeV singles that hit >= 2 separated segments; estimate
}

# Settings of the item (reader's choices; exact, not varied): delayed threshold x topology cut (>= 2 gamma clusters)
# x coincidence window n*tau x distance-cut scale s on V_local (red-team FIX 5).
# Efficiency costs, relative to the reference setting (n = 3, s = 1) to which the cited calibrations (SANDD, PANDA)
# already correspond: window (1 - exp(-n)) / (1 - exp(-3)) (exponential capture-time distribution);
# distance cut chi3_cdf(x0 * s^(1/3)) / chi3_cdf(x0) (3D Gaussian prompt-delayed displacement, radius ~ V^(1/3)).
WINDOWS = (1.0, 1.5, 2.0, 3.0)
DSCALES = (1.0, 0.5, 0.25)
GD_SETTINGS = [(round(t, 2), topo, n, s) for t in [1.0 + 0.2 * i for i in range(14)] for topo in (0, 1)
               for n in WINDOWS for s in DSCALES]  # 1.0-3.6 MeV

PROPS = {
    "common": COMMON,
    "gd": GD,
    # Survivor 1: 6Li-doped PSD plastic (SANDD type, arXiv:2105.00083)
    "li6_psd_plastic": {
        "ell_n_cm": 10.2,            # derived from SANDD 51.9% escape at 9 L with PE layer (see notes)
        "loss_capture_H": 0.128,     # SANDD: 12.8% of captures on H
        "loss_E_cut": 0.043,         # SANDD energy-cut efficiency 95.7%
        "loss_PSD": 0.082,           # SANDD total 34.8% / (45.4% x 87.2% x 95.7%) -> PSD-cut eff 0.918 (Table 3)
        "loss_PSD_fibre": 0.25,      # FIX 6: WLS-fibre readout (SANDD is directly coupled); ~4x less light, PSD FoM ~halved
        "gamma_leak": 0.01,          # SANDD: gammas rejected at the 99% level
        "tau_us": 37.2,              # SANDD mean capture time
        "V_local_L": 3.0,            # alpha+triton deposit local to the capture point, neighbouring segments
    },
    # Survivor 2: 6LiF:ZnS sheets between plastic segments (SoLid type); estimates, see notes
    "li6f_zns_sheets": {
        "ell_n_cm": 10.2,
        "loss_capture_H": 0.30,      # thinner capture layer than loaded plastic; estimate
        "loss_E_cut": 0.05,
        "loss_PSD": 0.20,            # ZnS signal identification efficiency ~80%; estimate
        "gamma_leak": 0.001,         # ZnS microsecond pulse; gamma misID ~1e-3 or less; estimate
        "tau_us": 65.0,              # SoLid-class capture time
        "V_local_L": 3.0,
    },
    # Non-survivor: present state, capture on hydrogen only (2.2 MeV gamma), threshold 1.0 MeV
    "h_capture": {
        "ell_n_cm": 12.0, "loss_capture_H": 0.0, "tau_us": 200.0, "V_local_L": 8.0, "thr_MeV": 1.0,
    },
}

UNC = {
    "props/common/sigma_f_cm2": [0.8, 1.25],   # reactor IBD yield per fission known to a few %
    "props/common/lam_gamma_cm": [0.8, 1.25],  # NIST XCOM attenuation coefficient
    "props/li6_psd_plastic/loss_PSD": [0.8, 1.25],  # SANDD Table 4: PSP relative systematic 1.0% (clamped to the floor)
}

ADOPTED = "gd"

def geom(f):
    a = (f["V_L"] * 1000.0) ** (1.0 / 3.0)   # cube side, cm
    S_m2 = 6 * a * a / 1e4
    return a, S_m2

def f_stay(ell, a):
    return math.exp(-ell * 1.5 / a)          # 1 - escape; escape = 1 - exp(-ell*S/(4V)), S/(4V) = 1.5/a

def irwin_hall_sf(x, k):
    """P(sum of k U[0,1] > x)."""
    if x <= 0: return 1.0
    if x >= k: return 0.0
    c = sum((-1) ** j * math.comb(k, j) * (x - j) ** k for j in range(int(math.floor(x)) + 1)) / math.factorial(k)
    return 1.0 - c

def p_cascade_above(thr, Ec, n, lam, a, kmin=1):
    """Gd cascade: n gammas of Ec/n; each interacts with p = 1-exp(-d/lam), d = a/3 (mean path to surface);
    an interacting gamma deposits U[0, Eg] (Compton continuum up to full absorption: optimistic for Gd)."""
    Eg = Ec / n
    p = 1.0 - math.exp(-(a / 3.0) / lam)
    return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) * irwin_hall_sf(thr / Eg, k) for k in range(kmin, n + 1))

def chi3_cdf(x):
    """P(|r| < x sigma) for a 3D isotropic Gaussian displacement."""
    return math.erf(x / math.sqrt(2.0)) - math.sqrt(2.0 / math.pi) * x * math.exp(-x * x / 2.0)

def ibd_rate(f, c):
    Np = f["nH_per_cm3"] * f["V_L"] * 1000.0
    fis = f["P_th_W"] / f["E_fis_J"]
    return fis * c["sigma_f_cm2"] * Np / (4 * math.pi * f["L_cm"] ** 2)

def amb_above(thr, f, c, S):
    """Ambient singles above thr (Hz): piecewise log-linear in the integral spectrum through 1.0, 2.0, 2.7 MeV."""
    R1 = f["amb_Hz_per_m2"] * S
    pts = [(1.0, 1.0), (2.0, min(1.0, c["frac_above_2p0"])), (2.7, min(1.0, c["frac_above_2p7"]))]
    if thr <= 1.0: return R1
    if thr >= 2.7: return R1 * pts[2][1]
    for (e0, y0), (e1, y1) in zip(pts, pts[1:]):
        if e0 <= thr <= e1:
            t = (thr - e0) / (e1 - e0)
            return R1 * math.exp(math.log(y0) + t * (math.log(y1) - math.log(y0)))

def evaluate(name, inp, setting=None):
    f, c, p = inp["fixed"], inp["props"]["common"], inp["props"][name]
    a, S = geom(f)
    R_ibd = ibd_rate(f, c)
    stay = f_stay(p["ell_n_cm"], a)
    cap = max(0.0, 1.0 - p["loss_capture_H"])
    R_prompt = amb_above(f["prompt_thr_MeV"], f, c, S)  # prompt singles above the stated 1 MeV
    R_namb = c["n_amb_Hz_per_m2"] * S
    n_win, s_dist = (setting[2], setting[3]) if setting else (3.0, 1.0)
    dt = n_win * p["tau_us"] * 1e-6                      # coincidence window n*tau, a setting
    w_eff = (1.0 - math.exp(-n_win)) / (1.0 - math.exp(-3.0))
    x0 = p.get("dist_x0_sigma", 2.8)
    d_eff = chi3_cdf(x0 * s_dist ** (1.0 / 3.0)) / chi3_cdf(x0)
    if name in ("gd", "h_capture"):
        if name == "h_capture":
            thr, topo = p["thr_MeV"], 0
            pcont = p_cascade_above(thr, 2.2, 1, c["lam_gamma_cm"], a)
        else:
            thr, topo = setting[0], setting[1]
            pcont = p_cascade_above(thr, f["Gd_casc_MeV"], f["Gd_mult"], c["lam_gamma_cm"], a, kmin=1 + topo)
        eff = min(1.0, stay * cap * pcont * w_eff * d_eff)
        rej = min(1.0, p.get("amb_multi_frac", 1.0)) if topo else 1.0
        R_delayed = amb_above(thr, f, c, S) * rej + R_namb * pcont
    else:
        eff = min(1.0, stay * cap * max(0.0, 1 - p["loss_E_cut"]) * max(0.0, 1 - p["loss_PSD"])
                  * max(0.0, 1 - p.get("loss_PSD_fibre", 0.0)))
        R_delayed = p["gamma_leak"] * c["lam_n_window_frac"] * R_prompt + R_namb * cap
    f_sp = min(1.0, p["V_local_L"] * s_dist / f["V_L"])
    signal = R_ibd * c["eps_prompt"] * eff
    acc = R_prompt * R_delayed * dt * f_sp
    ratio = acc / signal if signal > 0 else float("inf")
    return eff, ratio, R_ibd, signal

def passes(name, inp, setting=None):
    eff, ratio, _, _ = evaluate(name, inp, setting)
    return eff >= inp["fixed"]["EFF_REQ"] and ratio <= inp["fixed"]["ACC_REQ"]

def gd_passing(inp):
    return [st for st in GD_SETTINGS if passes("gd", inp, st)]

def gd_any_pass(inp):
    return any(passes("gd", inp, st) for st in GD_SETTINGS)

def make(V_L):
    return {"fixed": fixed(V_L), "props": PROPS, "unc": UNC}

def fails(inp):  # the item fails only if EVERY setting (threshold x topology) fails
    return not gd_any_pass(inp)

def viable(inp):
    return [n for n in inp["props"] if n not in ("common", ADOPTED) and passes(n, inp)]

def table(level, inp):
    print(f"--- {level} (V = {inp['fixed']['V_L']} L) nominal ---")
    for n in inp["props"]:
        if n == "common": continue
        sts = GD_SETTINGS if n == ADOPTED else [None]
        for st in sts:
            if n == ADOPTED and (st[0] not in (1.0, 1.6, 2.0, 2.6, 3.0, 3.6) or st[2:] != (3.0, 1.0)): continue
            eff, ratio, R, sg = evaluate(n, inp, st)
            lab = f"gd thr={st[0]:.1f} topo={st[1]}" if st else n
            print(f"  {lab:20s} delayed_eff={eff:.3f} acc/signal={ratio:8.3f} IBD/day={R*86400:6.0f} "
                  f"detected/day={sg*86400:6.0f} {'pass' if passes(n, inp, st) else 'fail'}")
    gp = gd_passing(inp)
    print(f"  gd settings passing in {level}: {len(gp)} of {len(GD_SETTINGS)}")
    ok30 = [(evaluate("gd", inp, st)[1], st) for st in GD_SETTINGS if evaluate("gd", inp, st)[0] >= inp["fixed"]["EFF_REQ"]]
    if ok30:
        r, st = min(ok30)
        print(f"  best gd setting with eff >= 30% (thr, topo, n_win, s_dist) = {st}: acc/signal = {r:.3f}")
    else:
        print("  no gd setting reaches eff >= 30%")

if __name__ == "__main__":
    # model check against PANDA36 (360 L, 3 MeV threshold): the model must not UNDER-estimate Gd (35.5% measured/MC)
    pf = fixed(360.0); a, _ = geom(pf)
    panda = f_stay(9.0, a) * 0.86 * p_cascade_above(3.0, 7.9, 4, 19.7, a)
    print(f"PANDA36 check: model Gd delayed eff at 360 L, 3 MeV = {panda:.3f} (published 0.355)")
    b, c1 = make(900.0), make(30.0)
    table("BASE", b); table("CONF1", c1)
    ok = check_base("BASE", b, fails)
    ok &= check_conf("CONF1", c1, fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
    # sensitivity (not part of the keylib check): Gd-loaded plastic with a short capture time (~10 us)
    GD["tau_us"] = 10.0
    check_conf("CONF1_tau10", make(30.0), fails, viable)
    GD["tau_us"] = 24.0
    # sensitivity (not part of the keylib check): cascade multiplicity 3 and 5
    for m in (3, 5):
        x = make(30.0); x["fixed"]["Gd_mult"] = m
        print(f"sensitivity Gd_mult={m}: CONF1 nominal Gd settings passing = {gd_passing(x)}")
