"""Key for p10_borexino. Run: python -I key.py
Adopted item: 144Ce-144Pr electron-antineutrino emitter in the access chamber.
CONF1 mechanism: fully deuterated target (99.8% D). Inverse beta decay needs free protons (hydrogen-1); the
residual hydrogen-1 gives ~1e1 events. Antineutrino charged-current on deuterium (nu_bar + d -> n n e+) has a
threshold of 4.03 MeV, above the 144Pr endpoint of 2.996 MeV, so it gives zero events. The remaining channels
(elastic scattering on electrons, neutral-current deuteron breakup) carry no event-by-event neutrino energy
from a continuous spectrum, so they fail the "80% within 10%" energy requirement.
Survivors: line-energy electron-neutrino emitters seen by elastic scattering (51Cr, 37Ar).
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf

DAY = 86400.0

def geom(D_cm, R_cm, n=400):
    """Volume average of 1/(4 pi r^2) over a sphere of radius R whose centre is a distance D > R from a point source."""
    tot = 0.0
    for i in range(n):
        s = (i + 0.5) * R_cm / n
        shell = math.log((D_cm + s) / (D_cm - s)) / (2 * s * D_cm)   # shell average of 1/r^2
        tot += 4 * math.pi * s * s * shell * (R_cm / n)
    return tot / (4.0 / 3.0 * math.pi * R_cm ** 3) / (4 * math.pi)

# --- fixed: exact stated facts (see notes.md) ---
FIXED = {
    "D_cm": 750.0,            # stated: chamber centre 7.5 m from detector centre
    "R_fid_cm": 340.0,        # stated: fiducial radius 3.4 m
    "V_fid_m3": 165.0,        # stated: fiducial volume 165 m3
    "T_run_d": 540.0,         # stated: 18 months of data
    "N_req": 1500.0,          # stated requirement: >= 1500 source-induced interactions
    "outside_max": 0.20,      # stated requirement: >= 80% of interactions with energy known to within 10%
    "SB_min": 1.0,            # stated requirement: signal outnumbers background
    "bkg_es_per_d": 100.0,    # stated: 100 background events/day in 0.25-0.6 MeV in fiducial volume
    "n_e_m3": 2.9e29,         # stated: electrons per m3
}

PROPS = {
    # 144Ce-144Pr: 100 kCi (SOX plan 100-150 kCi, arXiv:1304.7721); 144Ce half-life 284.9 d -> mean life 411 d.
    # IBD cross section per 144Ce decay, averaged over the 144Pr spectrum above the 1.806 MeV threshold (estimate,
    # order of SOX numbers). IBD positron energy known from detector resolution 5.5%/sqrt(E): about 3% of events
    # outside +-10%. IBD background (accidentals, geo- and reactor-antineutrinos): about 0.5/day in the fiducial volume.
    "ce": {"A_Bq": 3.7e15, "tau_d": 411.0, "sig_ibd_cm2": 4.0e-44, "eff": 0.9,
           "ibd_outside": 0.03, "bkg_ibd_per_d": 0.5,
           # untagged channels (nu_bar-e elastic scattering, NC deuteron breakup): the continuous 0-3 MeV spectrum
           # gives no per-event neutrino energy; about 80% of events lie outside +-10% of any assumed energy
           "untag_outside": 0.8},
    # 51Cr: 10 MCi (SOX phase A plan); half-life 27.7 d -> mean life 40.0 d; 0.75 MeV lines 90%, 0.43 MeV 10%.
    # Elastic-scattering cross section per decay with recoil in the 0.25-0.56 MeV window ~2.6e-45 cm2, from the standard
    # tree-level formula dsig/dT = (2 G_F^2 m_e / pi) [gL^2 + gR^2 (1-T/E)^2 - gL gR m_e T / E^2], nu_e: gL = 1/2 + sin2thW,
    # gR = sin2thW ('t Hooft 1971; Bahcall, Kamionkowski & Sirlin, PRD 51 (1995) 6146), times the 0.75 MeV branch (~90%).
    # Fraction of ES events from the 0.43 MeV line (outside +-10% of 0.75 MeV): about 6%.
    "cr51": {"A_Bq": 3.7e17, "tau_d": 40.0, "sig_es_cm2": 2.6e-45, "eff": 0.9, "outside": 0.06},
    # 37Ar: 5 MCi (proposed level, unverified); half-life 35.0 d -> mean life 50.5 d; 0.811/0.813 MeV lines (~100%).
    # ES cross section per decay with recoil in the 0.25-0.6 MeV window ~3.1e-45 cm2 (same standard formula). Outside ~1%.
    "ar37": {"A_Bq": 1.85e17, "tau_d": 50.5, "sig_es_cm2": 3.1e-45, "eff": 0.9, "outside": 0.01},
}

def teff_s(tau_d, T_d):
    return tau_d * (1 - math.exp(-T_d / tau_d)) * DAY

def ce_passes(inp):
    f, s, c = inp["fixed"], inp["stated"], inp["props"]["ce"]
    G = geom(f["D_cm"], f["R_fid_cm"])
    # tagged channel: IBD on hydrogen-1
    n_H = s["n_H1_m3"] * f["V_fid_m3"]
    N_ibd = c["A_Bq"] * teff_s(c["tau_d"], f["T_run_d"]) * G * c["sig_ibd_cm2"] * n_H * c["eff"]
    B_ibd = c["bkg_ibd_per_d"] * f["T_run_d"]
    ibd_ok = N_ibd >= f["N_req"] and c["ibd_outside"] <= f["outside_max"] and N_ibd >= f["SB_min"] * B_ibd
    # nu_bar + d charged current: threshold 4.03 MeV > 144Pr endpoint 2.996 MeV -> zero events (kinematic, exact)
    # untagged channels: fail the energy requirement whatever their count
    untag_ok = c["untag_outside"] <= f["outside_max"]
    return ibd_ok or untag_ok

def fails(inp):
    return not ce_passes(inp)

def es_line_ok(inp, name):
    f, c = inp["fixed"], inp["props"][name]
    G = geom(f["D_cm"], f["R_fid_cm"])
    n_e = f["n_e_m3"] * f["V_fid_m3"]
    # "counting period chosen for the analysis" (stated wording): the analyst picks a window starting at deployment
    # of length w = k*tau, k in [1, 3] (red-team r1 FIX 1). Within that window, the window count must meet N_req
    # and signal must outnumber background.
    if c["outside"] > f["outside_max"]:
        return False
    for i in range(21):
        w = min(c["tau_d"] * (1 + 0.1 * i), f["T_run_d"])
        S = c["A_Bq"] * teff_s(c["tau_d"], w) * G * c["sig_es_cm2"] * n_e * c["eff"]
        B = f["bkg_es_per_d"] * w
        if S >= f["N_req"] and S >= f["SB_min"] * B:
            return True
    return False

def viable(inp):
    return [k for k in ("cr51", "ar37") if es_line_ok(inp, k)]

if __name__ == "__main__":
    import copy
    base = {"fixed": dict(FIXED), "stated": {"n_H1_m3": 6.0e28}, "props": copy.deepcopy(PROPS)}
    conf1 = {"fixed": dict(FIXED), "stated": {"n_H1_m3": 1.2e26}, "props": copy.deepcopy(PROPS)}
    G = geom(FIXED["D_cm"], FIXED["R_fid_cm"])
    for lvl, d in (("BASE", base), ("CONF1", conf1)):
        c = d["props"]["ce"]
        N = c["A_Bq"] * teff_s(c["tau_d"], FIXED["T_run_d"]) * G * c["sig_ibd_cm2"] * d["stated"]["n_H1_m3"] * FIXED["V_fid_m3"] * c["eff"]
        print(f"# {lvl}: Ce IBD events in 18 months = {N:.1f}")
    for k in ("cr51", "ar37"):
        c = PROPS[k]; n_e = FIXED["n_e_m3"] * FIXED["V_fid_m3"]
        S = c["A_Bq"] * teff_s(c["tau_d"], c["tau_d"]) * G * c["sig_es_cm2"] * n_e * c["eff"]
        print(f"# {k}: ES events in first mean life = {S:.0f}, background = {FIXED['bkg_es_per_d'] * c['tau_d']:.0f}")
        S3 = c["A_Bq"] * teff_s(c["tau_d"], 3 * c["tau_d"]) * G * c["sig_es_cm2"] * n_e * c["eff"]
        print(f"# {k}: ES events in 3 mean lives = {S3:.0f}, background = {FIXED['bkg_es_per_d'] * 3 * c['tau_d']:.0f}")
    ok = check_base("BASE", base, fails)
    ok &= check_conf("CONF1", conf1, fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
