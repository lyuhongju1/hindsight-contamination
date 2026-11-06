#!/usr/bin/env python3
"""Answer key for pair t2k_nd280 (standard library only).

Figure of merit (FoM): expected number of *kinematically complete* charged-current
events per unit exposure -- events in which BOTH the outgoing charged lepton (muon)
AND the leading recoil proton are reconstructed -- produced in the volume that is
available for a new active target:

    FoM = V * rho * w_req * eps_mu * eps_p * F(p_th)

  V        available target volume [m^3]                        (level input)
  rho      mean density of the target option [g/cm^3]           (option property)
  w_req    mass fraction of the target in the required material (1 if any material
           is acceptable; the water mass fraction if interactions must be on water)
  eps_mu   muon reconstruction efficiency averaged over the stated angular split:
           eps_fwd*(1-f_mu_ha) + eps_ha*f_mu_ha  (f_mu_ha = fraction above 50 deg)
  eps_p    same for the leading proton with f_p_ha
  F(p_th)  fraction of leading protons above the option's proton tracking threshold.
           Spectrum model: survival function F(p) = 0.5 ** ((p/p_med)**k), a Weibull
           form fixed by the two stated numbers (median p_med and the fraction
           frac_hi of protons above 2*p_med):  k = log2(log2(1/frac_hi)).

Higher FoM is better. Margin = best / runner-up.
The product structure is the standard counting estimate used in near-detector
acceptance studies (target mass x acceptance x threshold efficiency); it is a
simplification -- see notes.md.
"""
import math
import random

# ---------------------------------------------------------------------------
# 1. Candidate options (real levels: NAME, ANON, EQ1-3, CONF1)
# ---------------------------------------------------------------------------
# Densities:
#   polystyrene 1.06 g/cm^3 -- PDG Atomic & Nuclear Properties, polystyrene:
#     https://pdg.lbl.gov/2024/AtomicNuclearProperties/HTML/polystyrene.html
#   water 1.000 g/cm^3 -- PDG: https://pdg.lbl.gov/2024/AtomicNuclearProperties/HTML/water_liquid.html
#   argon gas 1.662e-3 g/cm^3 at 1 atm, 20 C -- PDG:
#     https://pdg.lbl.gov/2024/AtomicNuclearProperties/HTML/argon_gas_Ar.html
#     x10 for 10 atm (ideal gas), operating pressure of ND-GAr style HPgTPC,
#     arXiv:2203.06281 https://arxiv.org/abs/2203.06281
RHO_PS = 1.06
RHO_H2O = 1.00
RHO_AR_10ATM = 1.662e-3 * 10.0


def mix_density(w_water, rho_solid=RHO_PS):
    """Density of a water/plastic mixture with water mass fraction w_water."""
    return 1.0 / (w_water / RHO_H2O + (1.0 - w_water) / rho_solid)


OPTIONS = {
    # ADOPTED: optically isolated ~1 cm cells read in three orthogonal views.
    #   eps >0.90 at all angles; proton threshold ~300 MeV/c (three views)
    #   -- ND280 Upgrade TDR, arXiv:1901.03750, Sect. 6.4.1 https://arxiv.org/abs/1901.03750
    #   material polystyrene (TDR Sect. 2.2.1) -> rho 1.06 (PDG, above)
    "cube_3view": dict(rho=RHO_PS, w_water=0.0, eps_fwd=0.90, eps_ha=0.90, p_th=300.0,
                       label="3-view fine-cell plastic target (adopted)"),
    # BASELINE-LIKE: planar x/y bars perpendicular to beam (FGD1 design).
    #   bars 9.61 mm, perpendicular to beam -- NIM A 659 (2011) 106, arXiv:1106.1238
    #     https://arxiv.org/abs/1106.1238
    #   forward efficiency excellent (take 0.90, same as cubes -- generous), high angle
    #   (>~50 deg) selection efficiency ~20% -- TDR arXiv:1901.03750 Sect. 6.1
    #   proton threshold ~450 MeV/c -- arXiv:1610.06367 Sect. 1 https://arxiv.org/abs/1610.06367
    #     and PoS(EPS-HEP2017)518 https://pos.sissa.it/314/518/pdf
    "planar_xy": dict(rho=RHO_PS, w_water=0.0, eps_fwd=0.90, eps_ha=0.20, p_th=450.0,
                      label="planar x/y bars transverse to beam"),
    # ALTERNATIVE: planar bars interleaved with water layers (FGD2 design).
    #   7 XY modules + 6 x 2.5 cm water -- arXiv:1106.1238 Sect. 4.3.4;
    #   water mass fraction ~0.5 ("oxygen target, as in FGD2 (~50%)") -- T2K ND upgrade
    #   task-force talk, July 2016 https://indico.ipmu.jp/event/94/contributions/2149/attachments/1710/2013/T2K-upgrade-HK-july2016.pdf
    #   computed: 15 cm water vs 14 x 0.961 cm x 1.06 g/cm^3 = 14.3 g/cm^2 plastic -> 0.51
    #   efficiencies / threshold as planar_xy (threshold taken equal -- generous)
    "planar_xy_water": dict(rho=mix_density(0.51), w_water=0.51, eps_fwd=0.90, eps_ha=0.20,
                            p_th=450.0, label="planar x/y bars + water layers"),
    # ALTERNATIVE: two-view bar target re-oriented for high angles ("FGDXY"/horizontal).
    #   two-view: ~20% lower efficiency forward/backward (0.9*0.8=0.72), comparable at
    #   high angle (0.90); proton threshold ~500 MeV/c -- TDR arXiv:1901.03750 Sect. 6.4.1, 6.5.4
    "twoview_bars": dict(rho=RHO_PS, w_water=0.0, eps_fwd=0.72, eps_ha=0.90, p_th=500.0,
                         label="two-view bar target"),
    # DISTRACTOR (and real 2016 reference option): water-filled 3D scintillator grid
    #   (WAGASCI-like, water-in). 70% H2O / 30% CH by mass, 2.5 cm cells; >70% muon
    #   efficiency incl. large angles; cannot reconstruct protons below ~450 MeV/c
    #   -- arXiv:1610.06367 Sect. 2-3 https://arxiv.org/abs/1610.06367
    "water_grid": dict(rho=mix_density(0.70), w_water=0.70, eps_fwd=0.70, eps_ha=0.70,
                       p_th=450.0, label="water-filled scintillator grid"),
    # ALTERNATIVE: the same grid without water ("empty WAGASCI").
    #   proton threshold 200-250 MeV/c (take 225) -- arXiv:1610.06367 Sect. 3;
    #   ~250 MeV/c -- July 2016 task-force talk (URL above)
    #   density: plastic volume fraction of the water-in grid = (0.30/1.06)*rho_mix
    #   = 0.288 -> rho = 0.288*1.06 = 0.305 g/cm^3 (derived from the 70/30 mass split)
    #   efficiency assumed equal to water-in grid (0.70; arXiv:1610.06367)
    "dry_grid": dict(rho=(0.30 / RHO_PS) * mix_density(0.70) * RHO_PS, w_water=0.0,
                     eps_fwd=0.70, eps_ha=0.70, p_th=225.0, label="empty scintillator grid"),
    # DISTRACTOR: high-pressure gaseous argon TPC as target (EOI-era second option,
    #   arXiv:1609.04111 Sect. VI https://arxiv.org/abs/1609.04111 : "low momentum threshold
    #   with 4pi acceptance"). 10 atm Ar; ~80% proton efficiency at 10 MeV kinetic energy
    #   -> p_th = sqrt(T^2+2 M T) = 137 MeV/c -- arXiv:2203.06281 https://arxiv.org/abs/2203.06281
    #   efficiency taken 0.90 at all angles (near-4pi; generous). Vessel wall mass ignored
    #   (generous).
    "hp_gas_tpc": dict(rho=RHO_AR_10ATM, w_water=0.0, eps_fwd=0.90, eps_ha=0.90,
                       p_th=math.sqrt(10.0 ** 2 + 2 * 938.272 * 10.0),
                       label="pressurised gas TPC target"),
}
ADOPTED = "cube_3view"

# ---------------------------------------------------------------------------
# 1b. ABS options -- invented families; every value is stated in ABS.txt (source:
#     descriptions/ABS.txt catalog). Analogue mapping in notes.md.
# ---------------------------------------------------------------------------
ABS_OPTIONS = {
    "korrin_array":   dict(rho=0.74, w_water=0.0, eps_fwd=0.88, eps_ha=0.88, p_th=270.0,
                           label="Korrin array (analogue of adopted)"),
    "lathe_stack":    dict(rho=0.75, w_water=0.0, eps_fwd=0.86, eps_ha=0.24, p_th=430.0,
                           label="Lathe stack"),
    "quessel_stack":  dict(rho=0.75, w_water=0.0, eps_fwd=0.70, eps_ha=0.86, p_th=480.0,
                           label="Quessel twin-view stack"),
    "ossine_mesh":    dict(rho=0.72, w_water=0.0, eps_fwd=0.66, eps_ha=0.66, p_th=440.0,
                           label="Ossine-flooded Brindle mesh"),
    "dry_brindle":    dict(rho=0.21, w_water=0.0, eps_fwd=0.66, eps_ha=0.66, p_th=210.0,
                           label="dry Brindle mesh"),
    "pellow_chamber": dict(rho=0.013, w_water=0.0, eps_fwd=0.92, eps_ha=0.92, p_th=120.0,
                           label="Pellow vapour chamber"),
}
ABS_ADOPTED = "korrin_array"

# ---------------------------------------------------------------------------
# 2. Level inputs -- mirror descriptions/*.txt (keep in sync)
# ---------------------------------------------------------------------------
LEVELS = {
    "NAME":  dict(L=2.0, W=1.9, H=0.6, p_med=450.0, frac_hi=0.06, f_mu_ha=0.25,
                  f_p_ha=0.35, need_water=False),
    "ANON":  dict(L=2.0, W=1.9, H=0.6, p_med=450.0, frac_hi=0.06, f_mu_ha=0.25,
                  f_p_ha=0.35, need_water=False),
    "EQ1":   dict(L=1.6, W=1.6, H=0.8, p_med=300.0, frac_hi=0.06, f_mu_ha=0.55,
                  f_p_ha=0.65, need_water=False),
    "EQ2":   dict(L=2.4, W=2.2, H=0.5, p_med=320.0, frac_hi=0.05, f_mu_ha=0.60,
                  f_p_ha=0.60, need_water=False),
    "EQ3":   dict(L=1.8, W=2.0, H=0.7, p_med=290.0, frac_hi=0.07, f_mu_ha=0.60,
                  f_p_ha=0.70, need_water=False),
    "CONF1": dict(L=2.1, W=1.7, H=0.65, p_med=300.0, frac_hi=0.06, f_mu_ha=0.60,
                  f_p_ha=0.70, need_water=True),
    "ABS":   dict(L=1.5, W=1.5, H=0.9, p_med=280.0, frac_hi=0.06, f_mu_ha=0.55,
                  f_p_ha=0.65, need_water=False),
}
VARIED = ["L", "W", "H", "p_med", "frac_hi", "f_mu_ha", "f_p_ha"]


# ---------------------------------------------------------------------------
# 3. FoM
# ---------------------------------------------------------------------------
def clamp_inputs(x):
    y = dict(x)
    for k in ("f_mu_ha", "f_p_ha"):
        y[k] = min(max(y[k], 0.0), 0.95)
    y["frac_hi"] = min(max(y["frac_hi"], 1e-4), 0.45)
    return y


def survival(p, p_med, frac_hi):
    k = math.log2(math.log2(1.0 / frac_hi))
    return 0.5 ** ((p / p_med) ** k)


def fom(opt, x):
    x = clamp_inputs(x)
    vol = x["L"] * x["W"] * x["H"]
    w = opt["w_water"] if x["need_water"] else 1.0
    e_mu = opt["eps_fwd"] * (1 - x["f_mu_ha"]) + opt["eps_ha"] * x["f_mu_ha"]
    e_p = opt["eps_fwd"] * (1 - x["f_p_ha"]) + opt["eps_ha"] * x["f_p_ha"]
    return vol * opt["rho"] * w * e_mu * e_p * survival(opt["p_th"], x["p_med"], x["frac_hi"])


def rank(opts, x):
    vals = {k: fom(o, x) for k, o in opts.items()}
    order = sorted(vals, key=vals.get, reverse=True)
    best, second = order[0], order[1]
    margin = vals[best] / vals[second] if vals[second] > 0 else float("inf")
    return vals, best, margin


# ---------------------------------------------------------------------------
# 4. Robustness
# ---------------------------------------------------------------------------
def robustness(opts, x, keyed, conf):
    """Return (single-factor table, joint fraction). Success = keyed wins (EQ/ABS/
    NAME/ANON) or adopted loses (CONF)."""
    def ok(y):
        _, best, _ = rank(opts, y)
        return (best != keyed) if conf else (best == keyed)

    singles = []
    for p in VARIED:
        for f in (0.5, 2.0):
            y = dict(x)
            y[p] = x[p] * f
            singles.append((p, f, ok(y)))
    rng = random.Random(20261105)
    n, good = 2000, 0
    for _ in range(n):
        y = dict(x)
        for p in VARIED:
            y[p] = x[p] * math.exp(rng.uniform(math.log(0.5), math.log(2.0)))
        good += ok(y)
    return singles, good / n


# ---------------------------------------------------------------------------
# 5./6. Run and report
# ---------------------------------------------------------------------------
def main():
    rows = []
    for lvl, x in LEVELS.items():
        opts, keyed = (ABS_OPTIONS, ABS_ADOPTED) if lvl == "ABS" else (OPTIONS, ADOPTED)
        conf = lvl.startswith("CONF")
        vals, best, margin = rank(opts, x)
        print("=" * 72)
        print(f"Level {lvl}: inputs {x}")
        for k in sorted(vals, key=vals.get, reverse=True):
            print(f"   {opts[k]['label']:<45s} FoM = {vals[k]:9.4f}")
        print(f"   winner: {best}   margin: {margin:.2f}")
        singles, frac = robustness(opts, x, keyed, conf)
        fails = [(p, f) for p, f, good in singles if not good]
        print(f"   single-factor x0.5/x2 failures: {fails if fails else 'none'}")
        what = "adopted loses" if conf else "keyed winner keeps winning"
        print(f"   joint log-uniform [0.5,2] draws (2000, seed 20261105): {what} in {frac:.1%}")
        if lvl in ("NAME", "ANON"):
            verdict = "report"
        elif conf:
            verdict = "PASS" if (best != keyed and margin >= 3 and frac >= 0.95) else "FAIL"
        else:
            verdict = "PASS" if (best == keyed and margin >= 3 and frac >= 0.95) else "FAIL"
        rows.append((lvl, best, margin, frac, verdict))
    print("=" * 72)
    print(f"{'Level':<7}{'Winner':<17}{'Margin':>8}{'Robust':>9}  Result")
    for lvl, best, margin, frac, verdict in rows:
        print(f"{lvl:<7}{best:<17}{margin:>8.2f}{frac:>9.1%}  {verdict}")


if __name__ == "__main__":
    main()
