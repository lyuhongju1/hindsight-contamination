"""Key for p03_advirgo. Run: python -I key.py
Adopted item: squeezed light whose squeezed quadrature follows the frequency-dependent optomechanical
response, produced by reflection off a detuned high-finesse auxiliary resonator (external, length <= stated
available path). Alternatives coded: fixed-angle squeezing; frequency-independent variational readout
(fixed homodyne angle) combined with fixed-angle squeezing; EPR/conditional squeezing using the
interferometer itself as the frequency-dependent element.

r2: the requirement is evaluated on 25 log-spaced frequencies over 20-800 Hz (band minimum >= 3 dB).
The adopted item is modelled with a two-photon sideband model of a lossy detuned two-mirror resonator
(complex reflection per sideband, loss vacuum added, then the stated total efficiency); for every draw the
half-linewidth, detuning and injection squeeze angle are OPTIMISED to maximise the band-minimum improvement
(coarse vectorised grid 24 x 33 x 36, then multi-start local refinement).
"""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                "..", "..", "..", "pilot", "harness")))
from keylib import check_base, check_conf

C = 299792458.0
N_FREQ = 25

def base_inputs(L_aux):
    return {
        "fixed": {  # exact stated facts (description), not varied; justified in notes.md
            "f_sql_Hz": 55.0,          # stated crossover (RP noise = shot noise)
            "src_dB": 13.0,            # stated source quadrature noise reduction
            "eta": 0.90,               # stated total efficiency source -> photodetector
            "mirror_loss_floor": 5e-6, # stated project fact: lowest loss per reflection of available HR mirrors
            "L_aux_m": L_aux,          # stated longest straight evacuated auxiliary path
            "f_low_Hz": 20.0, "f_high_Hz": 800.0, "req_dB": 3.0,   # stated requirement band and level
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
            # 776 (2017); Brown et al., PRD 96, 062003 (2017)). Nominal 0.025; range widened to x0.5-3 (r2).
            "epr": {"idler_extra_loss": 0.05, "filter_mismatch_excess": 0.025},
        },
        "unc": {"props/epr/filter_mismatch_excess": [0.5, 3.0]},   # wider than default (r2, conservative)
    }

def dB(V): return -10.0 * math.log10(V)

def _band(fx):
    f = np.geomspace(fx["f_low_Hz"], fx["f_high_Hz"], N_FREQ)
    K = (fx["f_sql_Hz"] / f) ** 2       # K = (f_SQL/f)^2 (arm bandwidth >> 800 Hz assumed; neutral)
    return f, K

def _rt_loss(inp):
    fx, p = inp["fixed"], inp["props"]["fd_cavity"]
    return (2 * fx["mirror_loss_floor"] + p["rt_loss_short_excess"]) if fx["L_aux_m"] < 50 else p["rt_loss_long"]

def _fc_grid(fx, loss, g_in, D, th):
    """Noise ratio (vs vacuum readout) for grids of input-coupling half-width g_in [Hz], detuning ratio
    D = Delta/gamma, and injection squeeze angle th. Returns array (..., N_FREQ) broadcast over inputs."""
    f, K = _band(fx)
    e2r = 10 ** (fx["src_dB"] / 10.0); s, a = 1.0 / e2r, e2r; eta = fx["eta"]
    g_l = C * loss / (4 * fx["L_aux_m"]) / (2 * math.pi)     # loss half-width [Hz]
    g = g_in + g_l; Dl = D * g
    def r(w):  # amplitude reflection of a lossy two-mirror cavity at sideband offset w from the carrier [Hz]
        d = w - Dl
        return (g_in - g_l + 1j * d) / (g - 1j * d)
    rp_, rm_ = r(f), r(-f)
    rp = (rp_ + np.conj(rm_)) / 2; rm = (rp_ - np.conj(rm_)) / 2j   # two-photon quadrature matrix entries
    u0, u1 = -K, 1.0                                                  # readout b2 = c2 - K c1
    v0 = np.conj(rp) * u0 + np.conj(rm) * u1                          # v = M^H u
    v1 = -np.conj(rm) * u0 + np.conj(rp) * u1
    q = np.abs(v0) ** 2 + np.abs(v1) ** 2; uu = 1 + K * K
    N0 = eta * ((s + a) / 2 * q + uu - q) + (1 - eta) * uu        # cavity loss vacuum + stated efficiency
    Nc = eta * (s - a) / 2 * (np.abs(v0) ** 2 - np.abs(v1) ** 2)
    Ns = eta * (s - a) / 2 * 2 * np.real(np.conj(v0) * v1)
    N = N0 + Nc * np.cos(2 * th) + Ns * np.sin(2 * th)
    return N / uu        # noise ratio vs vacuum per frequency (improvement dB = -10 log10 of this)

def fd_opt(inp, loss=None):
    """Optimise (g_in, Delta/gamma, theta) for the band-minimum improvement. Returns (bandmin_dB, params)."""
    fx = inp["fixed"]; loss = _rt_loss(inp) if loss is None else loss
    lg = np.linspace(math.log(0.01), math.log(5000.0), 24)[:, None, None, None]
    D = np.linspace(-4, 4, 33)[None, :, None, None]
    th = np.linspace(0, math.pi, 36, endpoint=False)[None, None, :, None]
    m = -_fc_grid(fx, loss, np.exp(lg), D, th).max(axis=-1)   # maximise minus the worst-frequency noise ratio
    step0 = np.array([lg[1, 0, 0, 0] - lg[0, 0, 0, 0], D[0, 1, 0, 0] - D[0, 0, 0, 0], th[0, 0, 1, 0] - th[0, 0, 0, 0]])
    o = np.linspace(-1, 1, 7); best, x = -1e9, None
    for flat in np.argsort(m, axis=None)[::-1][:4]:   # multi-start: refine the 4 best coarse points
        i, j, k = np.unravel_index(flat, m.shape)
        xs = np.array([lg[i, 0, 0, 0], D[0, j, 0, 0], th[0, 0, k, 0]]); bs = m[i, j, k]; step = step0.copy()
        for _ in range(14):   # local refinement: 7x7x7 grid of +-step, recentre, shrink x0.6
            a_ = (xs[0] + o * step[0])[:, None, None, None]
            b_ = (xs[1] + o * step[1])[None, :, None, None]
            c_ = (xs[2] + o * step[2])[None, None, :, None]
            mm = -_fc_grid(fx, loss, np.exp(a_), b_, c_).max(axis=-1)
            i2, j2, k2 = np.unravel_index(np.argmax(mm), mm.shape)
            if mm[i2, j2, k2] >= bs:
                bs = mm[i2, j2, k2]; xs = np.array([a_[i2, 0, 0, 0], b_[0, j2, 0, 0], c_[0, 0, k2, 0]])
            step = step * 0.6
        if bs > best: best, x = bs, xs
    g_l = C * loss / (4 * fx["L_aux_m"]) / (2 * math.pi)
    return dB(-float(best)), {"gamma_Hz": round(math.exp(x[0]) + g_l, 1), "Delta_over_gamma": round(float(x[1]), 2),
                         "theta_deg": round(math.degrees(x[2]) % 180, 1), "gamma_loss_Hz": round(g_l, 2)}

def fd_improvement(inp): return (fd_opt(inp)[0],)

def _fixed_readout(fx, t, th):
    """Fixed squeeze angle th, homodyne readout b2 + t*b1 (t = tan of a frequency-independent homodyne
    angle; t = 0 is ordinary phase readout). Signal normalised; improvement (dB) vs vacuum with t = 0."""
    f, K = _band(fx)
    e2r = 10 ** (fx["src_dB"] / 10.0); eta = fx["eta"]
    Vs, Va = eta / e2r + 1 - eta, eta * e2r + 1 - eta
    u0, u1 = t - K, 1.0
    S = (Vs * (u0 * np.cos(th) + u1 * np.sin(th)) ** 2 + Va * (-u0 * np.sin(th) + u1 * np.cos(th)) ** 2)
    return -10 * np.log10(S / (1 + K * K))

_CACHE = {}   # fixed-angle and fixed-homodyne options depend only on inputs["fixed"] (never varied)

def _cached(name, fx, fn):
    key = (name,) + tuple(sorted(fx.items()))
    if key not in _CACHE: _CACHE[key] = fn()
    return _CACHE[key]

def fi_improvement(inp): return _cached("fi", inp["fixed"], lambda: _fi(inp))

def vr_improvement(inp): return _cached("vr", inp["fixed"], lambda: _vr(inp))

def _fi(inp):
    th = np.linspace(0, math.pi, 3600, endpoint=False)[:, None]
    return (float(_fixed_readout(inp["fixed"], 0.0, th).min(axis=-1).max()),)

def _vr(inp):
    """Frequency-independent variational readout (fixed homodyne angle) + fixed squeeze angle, both optimised."""
    t = np.tan(np.linspace(-math.pi / 2 + 1e-3, math.pi / 2 - 1e-3, 721))[:, None, None]
    th = np.linspace(0, math.pi, 360, endpoint=False)[None, :, None]
    return (float(_fixed_readout(inp["fixed"], t, th).min(axis=-1).max()),)

def epr_improvement(inp):
    fx = inp["fixed"]; d = min(0.99, inp["props"]["epr"]["idler_extra_loss"])
    e2r = 10 ** (fx["src_dB"] / 10.0)
    ch, sh = (e2r + 1 / e2r) / 2, (e2r - 1 / e2r) / 2          # two-mode squeezed vacuum, same total squeezing
    es, ei = fx["eta"], fx["eta"] * (1 - d)
    Vs, Vi, Cc = es * ch + 1 - es, ei * ch + 1 - ei, math.sqrt(es * ei) * sh
    V = Vs - Cc * Cc / Vi + inp["props"]["epr"]["filter_mismatch_excess"]   # conditional variance + mismatch
    return (dB(V),)   # frequency-flat over the band (ideal effective filter assumed apart from the mismatch)

def meets(imp, fx): return min(imp) >= fx["req_dB"]   # imp = band minimum over 25 log-spaced 20-800 Hz points

def fails(inp): return not meets(fd_improvement(inp), inp["fixed"])

def viable(inp):
    fx = inp["fixed"]; out = []
    if meets(fi_improvement(inp), fx): out.append("fixed_angle_squeezing")
    if meets(vr_improvement(inp), fx): out.append("fixed_homodyne_variational_readout")
    if meets(epr_improvement(inp), fx): out.append("epr_conditional_squeezing")
    return out

if __name__ == "__main__":
    b, c1 = base_inputs(400.0), base_inputs(8.0)
    print(f"# band: {N_FREQ} log-spaced points 20-800 Hz; values are band-minimum improvement in dB")
    for lvl, x in (("BASE", b), ("CONF1", c1)):
        v, prm = fd_opt(x)
        print(f"# {lvl}: FD band-min = {v:.2f} dB (rt loss {_rt_loss(x)*1e6:.1f} ppm; optimum {prm}); "
              f"FI = {fi_improvement(x)[0]:.2f}; VR(fixed homodyne) = {vr_improvement(x)[0]:.2f}; "
              f"EPR = {epr_improvement(x)[0]:.2f}")
    print("# sanity:")
    for lab, inp, loss in (("400 m @ 60 ppm", b, 60e-6), ("8 m @ 10 ppm (floor, zero excess)", c1, 10e-6),
                           ("8 m @ 9 ppm (hypothetical 2 ppm/reflection + 5 ppm excess)", c1, 9e-6),
                           ("8 m @ 4 ppm (hypothetical 2 ppm/reflection, zero excess)", c1, 4e-6)):
        v, prm = fd_opt(inp, loss)
        print(f"#   FD {lab}: band-min {v:.2f} dB {prm}")
    ok = check_base("BASE", b, fails)
    ok &= check_conf("CONF1", c1, fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
