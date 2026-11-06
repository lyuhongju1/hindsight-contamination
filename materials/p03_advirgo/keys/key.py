"""Key for p03_advirgo. Run: python -I key.py
Adopted item: squeezed light whose squeezed quadrature follows the frequency-dependent optomechanical
response, produced by reflection off a detuned high-finesse auxiliary resonator (external, length <= stated
available path). Alternatives: fixed-angle squeezing; EPR/conditional squeezing using the interferometer
itself as the frequency-dependent element.
"""
import math, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                "..", "..", "..", "pilot", "harness")))
from keylib import check_base, check_conf

C = 299792458.0

def base_inputs(L_aux):
    return {
        "fixed": {  # exact stated facts (description), not varied; justified in notes.md
            "f_sql_Hz": 55.0,          # stated crossover (RP noise = shot noise)
            "src_dB": 13.0,            # stated source quadrature noise reduction
            "eta": 0.90,               # stated total efficiency source -> photodetector (r1: 0.85 -> 0.90)
            "mirror_loss_floor": 5e-6, # stated: best attainable loss per reflection (absorption + scatter)
            "L_aux_m": L_aux,          # stated longest straight evacuated auxiliary path
            "f_low_Hz": 20.0, "f_high_Hz": 800.0, "req_dB": 3.0,   # stated requirement
        },
        "props": {
            # Short (<~50 m) two-mirror cavity: round-trip loss = 2 x stated per-reflection floor (fixed)
            # + excess from rear-mirror transmission, clipping and point defects. Measured totals ~10-20 ppm
            # (Isogai et al., Opt. Express 21, 30114 (2013), ~10 ppm at ~2 m; Oelker et al., PRL 116, 041102
            # (2016), 2 m cavity; Evans et al., PRD 88, 022002 (2013)). Excess nominal 5 ppm (total 15 ppm).
            "fd_cavity": {"rt_loss_short_excess": 5e-6,
            # Hundreds-of-m cavities: ~50-80 ppm (AdV+/LIGO ~300 m filter-cavity designs and measurements,
            # e.g. McCuller et al., PRL 124, 171102 (2020); Zhao et al., PRL 124, 171101 (2020)). Nominal 60 ppm.
                          "rt_loss_long": 60e-6},
            # EPR scheme: extra loss on the idler path (frequency-separating optics, second homodyne readout)
            # beyond the stated signal-path efficiency; few % (Suedbeck et al., Nat. Photon. 14, 240 (2020);
            # Yap et al., Nat. Photon. 14, 223 (2020); Ma et al., Nat. Phys. 13, 776 (2017)). Nominal 5 %.
            # Residual mismatch between the interferometer's effective filter for the idler and the ideal
            # frequency dependence, as excess noise in vacuum units: ~0.02-0.03 (Ma et al., Nat. Phys. 13,
            # 776 (2017)). Nominal 0.025.
            "epr": {"idler_extra_loss": 0.05, "filter_mismatch_excess": 0.025},
        },
    }

def dB(V): return -10.0 * math.log10(V)

def fd_improvement(inp):
    fx, p = inp["fixed"], inp["props"]["fd_cavity"]
    e2r = 10 ** (fx["src_dB"] / 10.0)
    L = fx["L_aux_m"]
    loss = (2 * fx["mirror_loss_floor"] + p["rt_loss_short_excess"]) if L < 50 else p["rt_loss_long"]
    gamma = 2 * math.pi * fx["f_sql_Hz"] / math.sqrt(2)      # required resonator half-linewidth (rad/s)
    T_tot = 4 * L * gamma / C                                 # total round-trip coupling+loss giving that linewidth
    T_in = T_tot - loss                                       # input transmission (exact; <= 0 means impossible)
    eps = 1.0 if T_in <= 0 else min(1.0, 2 * loss / (T_in + loss))   # Kwee et al., PRD 90, 062006 (2014)
    eta_lo = fx["eta"] * (1 - eps)
    V_lo = eta_lo / e2r + 1 - eta_lo                          # ideal angle assumed (optimistic for adopted)
    V_hi = fx["eta"] / e2r + 1 - fx["eta"]                    # resonator transparent at high frequency
    return dB(V_lo), dB(V_hi)

def fi_improvement(inp):
    """Best single fixed squeeze angle; output quadrature b2 = a2 - K a1, K = (f_sql/f)^2."""
    fx = inp["fixed"]; e2r = 10 ** (fx["src_dB"] / 10.0); eta = fx["eta"]
    Vs, Va = eta / e2r + 1 - eta, eta * e2r + 1 - eta
    best = (-99, -99)
    for i in range(720):
        phi = math.pi * i / 720
        n, m = (math.cos(phi), math.sin(phi)), (-math.sin(phi), math.cos(phi))
        res = []
        for f in (fx["f_low_Hz"], fx["f_high_Hz"]):
            K = (fx["f_sql_Hz"] / f) ** 2; u = (-K, 1.0)
            S = Vs * (u[0]*n[0] + u[1]*n[1]) ** 2 + Va * (u[0]*m[0] + u[1]*m[1]) ** 2
            res.append(dB(S / (1 + K * K)))
        if min(res) > min(best): best = tuple(res)
    return best

def epr_improvement(inp):
    fx = inp["fixed"]; d = min(0.99, inp["props"]["epr"]["idler_extra_loss"])
    e2r = 10 ** (fx["src_dB"] / 10.0)
    ch, sh = (e2r + 1 / e2r) / 2, (e2r - 1 / e2r) / 2          # two-mode squeezed vacuum, same total squeezing
    es, ei = fx["eta"], fx["eta"] * (1 - d)
    Vs, Vi, Cc = es * ch + 1 - es, ei * ch + 1 - ei, math.sqrt(es * ei) * sh
    V = Vs - Cc * Cc / Vi + inp["props"]["epr"]["filter_mismatch_excess"]   # conditional variance + mismatch
    return dB(V), dB(V)

def meets(imp, fx): return min(imp) >= fx["req_dB"]

def fails(inp): return not meets(fd_improvement(inp), inp["fixed"])

def viable(inp):
    fx = inp["fixed"]; out = []
    if meets(fi_improvement(inp), fx): out.append("fixed_angle_squeezing")
    if meets(epr_improvement(inp), fx): out.append("epr_conditional_squeezing")
    return out

if __name__ == "__main__":
    b, c1 = base_inputs(400.0), base_inputs(8.0)
    for lvl, x in (("BASE", b), ("CONF1", c1)):
        print(f"# {lvl}: FD (lo,hi) dB = {tuple(round(v,2) for v in fd_improvement(x))}; "
              f"FI best = {tuple(round(v,2) for v in fi_improvement(x))}; "
              f"EPR = {tuple(round(v,2) for v in epr_improvement(x))}")
    ok = check_base("BASE", b, fails)
    ok &= check_conf("CONF1", c1, fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
