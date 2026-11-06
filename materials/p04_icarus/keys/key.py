"""Key for p04_icarus (r1). Run: python -I key.py
Adopted item: one serial ADC per wire channel with synchronous sampling, replacing multiplexed ADCs.
r1: CONF1 (port-capacity lever) withdrawn after red team r1; no physics conflict found that makes
per-channel synchronous digitisation itself fail (see notes.md). Only BASE is checked.
The r0 key is kept in ../abandoned/key_r0.py.
"""
import sys, math
sys.path.insert(0, r"C:\Users\lyuho\Downloads\hindsight contamination\pilot\harness")
from keylib import check_base, _draws

def make():
    return {
        "fixed": {
            # exact stated facts
            "n_wires": 20000,          # stated: 20,000 wires (all recorded continuously)
            "snr_req": 6.0,            # stated: S/N >= 6 on induction planes (r1: was 10)
            "skew_req_ns": 50.0,       # stated: common time reference to better than 50 ns
            "drift_ms": 1.2,           # stated: maximum drift time ~1.2 ms
            "dead_req": 0.03,          # stated: dead time below "a few percent" (taken as 3%)
        },
        "props": {
            # MIP charge on a 4 mm induction wire: 2.1 MeV/cm / 23.6 eV x ~0.7 recombination survival x 0.4 cm
            # ~ 25,000 e; induction signal taken ~0.6 of that (author knowledge)
            "signal_e": 15000.0,
            "adopted": {
                "enc_e": 1200.0,       # warm front end, ~400 pF wire+cable load: ~1000-1500 e (author knowledge)
                "skew_ns": 5.0,        # common sampling clock: few-ns distribution skew
                "buffer_ms": 4.0,      # board memory covering several drift windows
                "dead_frac": 0.01,     # parallel serial readout
            },
        },
    }

def margins(inp):
    f, p = inp["fixed"], inp["props"]; o = p["adopted"]
    return {"snr": p["signal_e"] / o["enc_e"] / f["snr_req"],
            "skew": f["skew_req_ns"] / o["skew_ns"],
            "buffer": o["buffer_ms"] / f["drift_ms"],
            "dead": f["dead_req"] / o["dead_frac"]}

def fails(inp):
    return min(margins(inp).values()) < 1.0

if __name__ == "__main__":
    inp = make()
    ok = check_base("BASE", inp, fails)
    m = margins(inp)
    print("BASE nominal margins: " + ", ".join(f"{k}={v:.2f}x" for k, v in m.items())
          + f"  min={min(m.values()):.2f}x {'(>=2x)' if min(m.values()) >= 2 else '(<2x)'}")
    n = 2000; passes = sum(not fails(x) for x in _draws("BASE", inp, n))
    print(f"BASE adopted passes in {passes / n:.3f} of x0.5-2 draws (informational)")
    print("CONF1 withdrawn in r1: no honest physics conflict for the counted item (see notes.md)")
    sys.exit(0 if ok and min(m.values()) >= 2 else 1)
