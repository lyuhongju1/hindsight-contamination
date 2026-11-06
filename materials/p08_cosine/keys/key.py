"""Key for p08_cosine. Run: python -I key.py"""
import copy, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

# Stated facts (descriptions): requirements and the altitude of the home institute.
FIXED = {
    "K_max_ppb": 40.0,        # stated: natK <= 40 ppb per crystal
    "Pb210_max_mBq": 1.5,     # stated: 210Pb <= 1.5 mBq/kg
    "H3_max_mBq": 0.1,        # stated: tritium <= 0.1 mBq/kg at start of data taking
    "lab_portal_m": 250.0,    # stated: tunnel portal altitude (enters via F_portal below)
    "t_home_d": 150.0,        # stated (r1): "about five months" from final drying to sealed crystal at the home institute
}

COMMON = {
    # Sea-level cosmogenic 3H production rate in NaI: 83 +- 27 /kg/d measured (Amare et al., ANAIS, Astropart. Phys. 97 (2018) 96).
    # Calculated estimates are lower: ACTIVIA-type ~26 /kg/d and Mei et al.-type ~36 /kg/d (as compared in the same paper).
    # r1 fix: range widened to x0.3-1.5 (25-125 /kg/d) to cover them (see unc below).
    "R0_per_kg_d": 83.0,
    # 3H half-life 12.32 y
    "T12_d": 12.32 * 365.25,
    # neutron-flux factor near the 250 m tunnel portal relative to sea level (JESD89A altitude scaling, ~1.2)
    "F_portal": 1.2,
}

OPTIONS = {
    # Adopted: in-house growth from recrystallisation-purified powder at the home institute.
    # natK ~20 ppb, 210Pb ~0.4 mBq/kg in CUP-grown crystals (Lee et al., COSINE-200 R&D; unverified, see notes).
    # Exposure at the home site from final drying of purified powder to sealed crystal: ~150 d
    # (stated in the descriptions as 'about five months'; still varied x0.5-2 as an approximate figure).
    # Transport to the lab: ~10 d near ground level.
    "adopted_inhouse": {"K_ppb": 20.0, "Pb210_mBq": 0.4, "t_ship_d": 10.0},
    # Commercial, Alpha Spectra (Grand Junction CO, ~1,400 m): best COSINE-100 crystals natK ~17 ppb,
    # 210Pb ~0.8 mBq/kg (COSINE-100 EPJC 78 (2018) 107). Neutron-flux factor at 1,400 m ~2.7 (JESD89A).
    # Exposure ~150 d at the vendor (same stated 'about five months'), ~40 d sea/ground shipping (air not modelled).
    "alpha_spectra": {"K_ppb": 17.0, "Pb210_mBq": 0.8, "F_site": 2.7, "t_site_d": 150.0, "t_ship_d": 40.0},
    # Commercial, RMD (Watertown MA, near sea level) from Astro-Grade powder: SABRE NaI-33 natK ~4.3 ppb,
    # 210Pb ~0.41 mBq/kg (SABRE, EPJC 79 (2019) 363). F ~1.0 at sea level.
    "rmd_astrograde": {"K_ppb": 4.3, "Pb210_mBq": 0.41, "F_site": 1.0, "t_site_d": 150.0, "t_ship_d": 40.0},
}

# Neutron-flux factor at the home institute relative to sea level (JESD89A; Leadville 3,100 m ~12.9).
F_HOME = {"BASE": 1.0, "CONF1": 17.0}   # 30 m -> ~1.0 ; 3,600 m -> ~17


def h3_mBq(inp, o):
    c, p = inp["common"], inp["props"][o]
    tau = c["T12_d"] / math.log(2)
    home = o == "adopted_inhouse"
    F_site = inp["home"]["F_home"] if home else p["F_site"]
    t_site = inp["fixed"]["t_home_d"] if home else p["t_site_d"]
    # atoms/kg = R0 * sum_i F_i * tau * (1 - exp(-t_i/tau)); activity = N/tau  [per kg per day]
    a = c["R0_per_kg_d"] * (F_site * (1 - math.exp(-t_site / tau))
                            + c["F_portal"] * (1 - math.exp(-p["t_ship_d"] / tau)))
    return a / 86400.0 * 1e3  # mBq/kg


def ok(inp, o):
    f, p = inp["fixed"], inp["props"][o]
    return (p["K_ppb"] <= f["K_max_ppb"] and p["Pb210_mBq"] <= f["Pb210_max_mBq"]
            and h3_mBq(inp, o) <= f["H3_max_mBq"])


def fails(inp):
    return not ok(inp, "adopted_inhouse")


def viable(inp):
    return [o for o in inp["props"] if o != "adopted_inhouse" and ok(inp, o)]


def make(level):
    return {"fixed": copy.deepcopy(FIXED), "common": copy.deepcopy(COMMON), "props": copy.deepcopy(OPTIONS),
            "home": {"F_home": F_HOME[level]},
            # R0: x0.3-1.5 spans calculated (ACTIVIA ~26, Mei ~36) to measured+1sigma (ANAIS 83+-27) values;
            # half-life known to <1% -> clamp at minimum allowed range
            "unc": {"common/R0_per_kg_d": [0.3, 1.5], "common/T12_d": [0.8, 1.25]}}


if __name__ == "__main__":
    for lvl in ("BASE", "CONF1"):
        inp = make(lvl)
        print(f"# {lvl}: 3H mBq/kg nominal: " + ", ".join(f"{o}={h3_mBq(inp, o):.3f}" for o in OPTIONS))
    ok_b = check_base("BASE", make("BASE"), fails)
    ok_c = check_conf("CONF1", make("CONF1"), fails, viable)
    sys.exit(0 if (ok_b and ok_c) else 1)
