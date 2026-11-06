"""Key for p15_aligo. Run: python -I key.py
Adopted item: separate-reference-beam (balanced) readout. Survivor candidate: DC readout.
Mechanism tested: phase noise between the reference beam and the antisymmetric-port beam (they travel
different routes), which beats against the static quadrature-orthogonal carrier from arm loss mismatch.
Fake displacement x = L_eff * (2*pi/lambda) * dx / G, with L_eff = offset_ref * sqrt(P_cd / P_ref)
(field-amplitude equivalent offset of the orthogonal static carrier) and G the phase-loop gain at 10 Hz.
DC readout: the reference field co-propagates with the signal, so path motion is common mode; its
residual couplings are laser intensity noise x = offset*RIN/2 and beam jitter on the mode cleaner
x = offset * a_static * dx / w.
"""
import sys, math
sys.path.insert(0, r"C:\Users\lyuho\Downloads\hindsight contamination\pilot\harness")
from keylib import check_base, check_conf

LAM = 1.064e-6  # m, stated laser wavelength (fixed)

def model(inp):
    s, p = inp["stated"], inp["props"]
    lim = s["target_m"] / s["tech_margin"]                      # each technical noise <= target/10
    L_eff = s["offset_m"] * math.sqrt(s["P_cd_W"] / s["P_off_W"])
    ref = p["separate_reference"]
    x_ref = L_eff * (2 * math.pi / LAM) * s["dx_m"] / ref["loop_gain_10Hz"]
    dc = p["dc_readout"]
    x_dc_rin = s["offset_m"] * s["rin"] / 2
    x_dc_jit = s["offset_m"] * dc["static_miscentre_w"] * s["dx_m"] / dc["waist_m"]
    return lim, x_ref, max(x_dc_rin, x_dc_jit)

def fails(inp):
    lim, x_ref, _ = model(inp); return x_ref > lim

def viable(inp):
    lim, _, x_dc = model(inp); return ["dc_readout"] if x_dc <= lim else []

base_stated = {"target_m": 4e-19, "tech_margin": 10, "offset_m": 8e-12, "P_off_W": 12e-3,
               "P_cd_W": 0.1e-3, "dx_m": 2e-15, "rin": 3e-10}
props_suspended = {
    # gain of a reference-phase servo actuating on suspended optics at 10 Hz; UGF of tens of Hz (property, x0.5-2)
    "separate_reference": {"loop_gain_10Hz": 30.0},
    # static mis-centring on the output mode cleaner ~1% of waist; waist ~0.5 mm (typical OMC values)
    "dc_readout": {"static_miscentre_w": 0.01, "waist_m": 5e-4},
}
BASE = {"stated": base_stated, "props": props_suspended}
check_base("BASE", BASE, fails)

# Attempted CONF1: optics beyond the antisymmetric port rigidly mounted (not suspended) on their platform,
# relative motion 3e-12 m/rtHz at 10 Hz. Rigid mounts permit piezo actuation (UGF ~ several kHz), so the
# phase servo gain at 10 Hz is ~1e3 or more -> honest loop_gain_10Hz = 1e3.
conf1 = {"stated": dict(base_stated, dx_m=3e-12),
         "props": {"separate_reference": {"loop_gain_10Hz": 1e3},
                   "dc_readout": props_suspended["dc_readout"]}}
check_conf("CONF1", conf1, fails, viable)

# Same CONF1 if one (dishonestly) kept the slow suspended-optic servo gain:
conf1_slow = {"stated": dict(base_stated, dx_m=3e-12), "props": props_suspended}
check_conf("CONF1slow", conf1_slow, fails, viable)
for name, inp in [("BASE", BASE), ("CONF1", conf1), ("CONF1slow", conf1_slow)]:
    lim, xr, xd = model(inp)
    print(f"{name:9s} limit={lim:.2e} x_separate_reference={xr:.2e} x_dc_readout={xd:.2e}")
