"""Key script for pair 'auger'. Standard library only.

FoM = G * f_cov * MF^2   (composition-tagged exposure, relative units)
  MF    = Delta / sqrt(sig_p^2 + sig_Fe^2 + 2*sig_det^2)   per-event p/Fe merit factor
          on the muon-content estimator (shower fluctuations + detector resolution)
  f_cov = min(1, budget/cost, labour/labour_need)            fraction of array equipped
  G     = 1 if option (a) supplies a measurement complementary to the water
          signal in the required zenith band, (b) does not open/alter the sealed
          water volume when that is forbidden, (c) does not require lifting the
          stations when that is forbidden; else 0.
Gates are booleans and are NOT perturbed; every numeric input is.
"""
import math
import random

# ---------------------------------------------------------------- real options
# Shared shower physics (real levels)
REAL_PHYS = {
    # ln(N_mu Fe / N_mu p) ~ 0.33 (Fe/p ~1.4 in R_mu at 1e19 eV, models)
    # https://arxiv.org/abs/2102.07797 (Fig. 3)
    "delta": 0.33,
    # relative muon-number fluctuations, proton ~0.13, iron ~0.05 at 1e19 eV
    # https://arxiv.org/abs/2102.07797 (Fig. 2, model curves)
    "sig_p": 0.13,
    "sig_fe": 0.05,
}

REAL_OPTIONS = {
    "thin_panel_on_station (adopted, SSD)": {
        # 8.357 M$ (no infrastructure) / 1660 stations, PDR App. A.1 WBS 1.1
        # https://arxiv.org/abs/1604.03637
        "cost": 5.0,          # k$ per station
        # 2 persons x (1.5 h on site + 2 h driving shared over 3 sites), PDR sec. 9.2
        "labour": 4.3,        # person-hours per station
        # S_mu(800) resolution 22% (p) / 14% (Fe) at 10^19.8 eV, PDR sec. 3.5
        "sig_det": 0.18,
        "inside_volume": False, "needs_lift": False,
        # complementary only for more vertical showers; EM absorbed above ~65 deg
        # https://arxiv.org/abs/2305.10104
        "bands": {"vertical"},
    },
    "layered_tank (distractor, LSD)": {
        # one extra PMT (~0.8 k$: PDR WBS 1.1.2 1.33 M$/~1700 PMTs) + separator
        # (separator cost ~0.5 k$ is an ESTIMATE, no public number; see notes)
        "cost": 1.3,
        # open hatch, insert separator in liner, add PMT: ESTIMATE 8 person-h
        # (prototype 'Guapa Guerrera' built by modifying a liner, arXiv:1405.5699)
        "labour": 8.0,
        # muon size resolution 20% (p) / 16% (Fe) at 10 EeV, arXiv:1405.5699
        "sig_det": 0.18,
        "inside_volume": True, "needs_lift": False,
        "bands": {"vertical"},
    },
    "rpc_under_station (distractor, MARTA)": {
        # >7 m2 RPC + concrete base; no public cost; ESTIMATE 15 k$ (see notes)
        "cost": 15.0,
        # tank lift + precast base: ESTIMATE 24 person-h
        "labour": 24.0,
        # muon density at 1000 m resolution 10-20%, arXiv:1712.07685
        "sig_det": 0.15,
        "inside_volume": False, "needs_lift": True,
        "bands": {"vertical"},
    },
    "buried_counter (alternative, AMIGA/UMD)": {
        # 1.6 M$ to complete 54 of 61 stations (no infrastructure), PDR p. iii/sec. 1
        "cost": 29.6,
        # 'deployed in two days' with 3 technicians (+ retro-digger), PDR sec. 9.6
        "labour": 48.0,
        # counting resolution 1.12/sqrt(N_mu); ~100 mu in 30 m2 at 10^19.6 eV,
        # PDR sec. 3.4 Table 3.2 scaled -> ~0.12
        "sig_det": 0.12,
        "inside_volume": False, "needs_lift": False,
        "bands": {"vertical"},
    },
    "radio_antenna (alternative, AERA/RD)": {
        # no public per-unit cost; ESTIMATE 2.5 k$ (simple SALLA on mast, arXiv:2305.10104)
        "cost": 2.5,
        "labour": 3.0,        # ESTIMATE, mast on existing station frame
        # MF(p-Fe)=1.60 with WCD for 65-85 deg (arXiv:2305.10104) -> equivalent sig_det
        # solving 0.33/sqrt(0.13^2+0.05^2+2 s^2)=1.60 gives s~0.09
        "sig_det": 0.09,
        "inside_volume": False, "needs_lift": False,
        # footprint covers >=3 stations at 1.5 km spacing only above ~65-70 deg
        "bands": {"inclined"},
        "max_spacing_inclined": 3.0,    # km; inclined footprints illuminate "tens of km2" (arXiv:2305.10104)
    },
}

# ---------------------------------------------------------------- ABS options
# All values stated in descriptions/ABS.txt (invented catalog).
ABS_PHYS = {"delta": 0.30, "sig_p": 0.14, "sig_fe": 0.06}
ABS_OPTIONS = {
    "Veltrane sheet (adopted analogue)": {"cost": 2.2, "labour": 3.0, "sig_det": 0.19,
        "inside_volume": False, "needs_lift": False, "bands": {"vertical"}},
    "Duolith insert": {"cost": 1.1, "labour": 7.0, "sig_det": 0.17,
        "inside_volume": True, "needs_lift": False, "bands": {"vertical"}},
    "Korrin plate": {"cost": 6.5, "labour": 20.0, "sig_det": 0.14,
        "inside_volume": False, "needs_lift": True, "bands": {"vertical"}},
    "Tessaline mat": {"cost": 14.0, "labour": 40.0, "sig_det": 0.11,
        "inside_volume": False, "needs_lift": False, "bands": {"vertical"}},
    "Orvane loop": {"cost": 1.6, "labour": 2.5, "sig_det": 0.09,
        "inside_volume": False, "needs_lift": False, "bands": {"inclined"},
        "max_spacing_inclined": 3.0},
}

# ---------------------------------------------------------------- levels
# Mirrors descriptions/*.txt. budget in k$ (credits for ABS) per station,
# labour in person-hours per station available for the upgrade campaign.
LEVELS = {
    "NAME":  {"n": 1660, "spacing": 1.5, "budget": 6.2, "labour": 5.8, "band": "vertical",
              "lock_volume": True, "no_lift": True},
    "ANON":  {"n": 1660, "spacing": 1.5, "budget": 6.2, "labour": 5.8, "band": "vertical",
              "lock_volume": True, "no_lift": True},
    "EQ1":   {"n": 1200, "spacing": 1.6, "budget": 7.5, "labour": 4.8, "band": "vertical",
              "lock_volume": True, "no_lift": True},
    "EQ2":   {"n": 2100, "spacing": 1.3, "budget": 6.8, "labour": 4.4, "band": "vertical",
              "lock_volume": True, "no_lift": True},
    "EQ3":   {"n": 900, "spacing": 1.8, "budget": 9.0, "labour": 4.6, "band": "vertical",
              "lock_volume": True, "no_lift": True},
    "CONF1": {"n": 1400, "spacing": 1.0, "budget": 7.0, "labour": 5.5, "band": "inclined",
              "lock_volume": True, "no_lift": True},
    "ABS":   {"n": 1500, "spacing": 1.4, "budget": 3.0, "labour": 3.6, "band": "vertical",
              "lock_volume": True, "no_lift": True},
}
ADOPTED = {"real": "thin_panel_on_station (adopted, SSD)", "abs": "Veltrane sheet (adopted analogue)"}


def gate(opt, lv):
    if lv["band"] not in opt["bands"]:
        return 0.0
    if lv["band"] == "inclined" and "max_spacing_inclined" in opt and lv["spacing"] > opt["max_spacing_inclined"]:
        return 0.0
    if lv["lock_volume"] and opt["inside_volume"]:
        return 0.0
    if lv["no_lift"] and opt["needs_lift"]:
        return 0.0
    return 1.0


def fom(opt, lv, phys):
    g = gate(opt, lv)
    if g == 0.0:
        return 0.0
    cov = min(1.0, lv["budget"] / opt["cost"], lv["labour"] / opt["labour"])
    mf = phys["delta"] / math.sqrt(phys["sig_p"] ** 2 + phys["sig_fe"] ** 2 + 2 * opt["sig_det"] ** 2)
    return g * cov * mf * mf


def evaluate(lv, opts, phys):
    scores = {k: fom(o, lv, phys) for k, o in opts.items()}
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    (w, s1), (_, s2) = ranked[0], ranked[1]
    margin = float("inf") if s2 == 0 else s1 / s2
    return w, margin, scores


def numeric_keys(lv, opts, phys):
    keys = [("lv", k) for k in ("spacing", "budget", "labour")]
    keys += [("phys", k) for k in phys]
    for name, o in opts.items():
        for k, v in o.items():
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                keys.append(("opt", name, k))
    return keys


def perturbed(lv, opts, phys, factors):
    lv2 = dict(lv)
    ph2 = dict(phys)
    op2 = {n: dict(o) for n, o in opts.items()}
    for key, f in factors.items():
        if key[0] == "lv":
            lv2[key[1]] *= f
        elif key[0] == "phys":
            ph2[key[1]] *= f
        else:
            op2[key[1]][key[2]] *= f
    return lv2, op2, ph2


def main():
    rng = random.Random(20261105)
    rows = []
    for name, lv in LEVELS.items():
        isabs = name == "ABS"
        opts = ABS_OPTIONS if isabs else REAL_OPTIONS
        phys = ABS_PHYS if isabs else REAL_PHYS
        adopted = ADOPTED["abs" if isabs else "real"]
        w, m, scores = evaluate(lv, opts, phys)
        print(f"== {name} ==")
        for k, s in sorted(scores.items(), key=lambda kv: -kv[1]):
            print(f"   {k:42s} FoM={s:.4f}")
        print(f"   winner={w}  margin={m:.2f}")
        keys = numeric_keys(lv, opts, phys)
        # single-parameter x0.5 / x2
        single_keep = 0
        flips = []
        for key in keys:
            for f in (0.5, 2.0):
                w2, _, _ = evaluate(*perturbed(lv, opts, phys, {key: f}))
                if w2 == w:
                    single_keep += 1
                else:
                    flips.append(f"{key}x{f}->{w2}")
        print(f"   single-param: winner kept {single_keep}/{2*len(keys)}")
        for fl in flips:
            print(f"      flip: {fl}")
        # joint draws
        keep = 0
        adopted_wins = 0
        for _ in range(2000):
            fac = {k: math.exp(rng.uniform(math.log(0.5), math.log(2.0))) for k in keys}
            w2, _, _ = evaluate(*perturbed(lv, opts, phys, fac))
            keep += (w2 == w)
            adopted_wins += (w2 == adopted)
        rob = keep / 2000
        aw = adopted_wins / 2000
        print(f"   joint draws: keyed winner kept {rob:.3f}; adopted wins {aw:.3f}")
        if name.startswith("EQ") or isabs:
            ok = (w == adopted and m >= 3 and aw >= 0.95)
            verdict = "PASS" if ok else "FAIL"
        elif name.startswith("CONF"):
            ok = (w != adopted and m >= 3 and (1 - aw) >= 0.95)
            verdict = "PASS" if ok else "FAIL"
        else:
            verdict = "report"
        rows.append((name, w, m, rob, verdict))
    print()
    print(f"{'level':6s} | {'winner':42s} | {'margin':>7s} | {'robust':>6s} | result")
    for r in rows:
        ms = "inf" if r[2] == float("inf") else f"{r[2]:.2f}"
        print(f"{r[0]:6s} | {r[1]:42s} | {ms:>7s} | {r[3]:6.3f} | {r[4]}")


if __name__ == "__main__":
    main()
