"""Key for p04_icarus. Run: python -I key.py
Adopted item: one serial ADC per wire channel, synchronous sampling, on boards outside the vessel
(each wire's analog signal crosses the vessel wall on its own conductor pair).
CONF1 mechanism: port (feedthrough) capacity. With only 8 roof ports of 20 cm for 20,000 wires,
one analog pair per wire cannot leave the vessel; digitizing and serializing inside the vessel can.
"""
import sys, os
sys.path.insert(0, r"C:\Users\lyuho\Downloads\hindsight contamination\pilot\harness")
from keylib import check_base, check_conf

def make(ports):
    return {
        "fixed": {
            # exact stated facts
            "n_wires": 20000,          # stated: 20,000 wires
            "ports": ports,            # stated: ports assigned to wire signals (BASE 40, CONF1 8)
            "snr_req": 10.0,           # stated: S/N >= 10 on induction planes
            "skew_req_ns": 50.0,       # stated: common time reference to better than 50 ns
            "drift_ms": 1.2,           # stated: maximum drift time ~1.2 ms
            "dead_req": 0.03,          # stated: dead time below "a few percent" (taken as 3%)
            # structural count: an outside-vessel digitizer needs one analog pair per wire through the wall
            "warm_ch_per_pair": 1,
        },
        "props": {
            # MIP ionization charge reaching a 4 mm induction wire, electrons:
            # 2.1 MeV/cm / 23.6 eV x ~0.7 recombination survival x 0.4 cm ~ 25,000 e; induction signal taken ~0.6 of that
            "signal_e": 15000.0,
            "adopted": {   # per-channel serial ADC, warm boards on roof ports
                "pairs_per_port": 600.0,  # ~576 channels per roof flange in the overhauled T600-style warm readout (author knowledge)
                "enc_e": 1200.0,          # warm front end with ~400 pF wire+cable load, ~1000-1500 e (author knowledge)
                "skew_ns": 5.0,           # common sampling clock: skew of order clock-distribution jitter, few ns
                "buffer_ms": 4.0,         # board memory covering several drift windows
                "dead_frac": 0.01,        # parallel serial readout
            },
            "multiplexed": {  # keep existing sequential-sampling digitizers
                "pairs_per_port": 600.0,
                "enc_e": 1500.0,
                "skew_ns": 250.0,         # samples staggered within the 500 ns period: mean offset ~half period
                "buffer_ms": 2.0,
                "dead_frac": 0.05,        # slower readout of a 16:1 multiplexed system at surface trigger rates
            },
            "cold_asic": {   # preamplifier, shaper, ADC and serializer inside the liquid, digital links out
                "ch_per_pair": 16.0,      # 128-channel board: ~4 data links + clock/control + power ~ 8 pair-equivalents
                "pairs_per_port": 600.0,
                "enc_e": 500.0,           # cryogenic CMOS front end at ~150-200 pF wire load, ~400-600 e (author knowledge)
                "skew_ns": 5.0,
                "buffer_ms": 4.0,
                "dead_frac": 0.01,
            },
        },
    }

def ok_option(inp, name, ch_per_pair):
    f, p = inp["fixed"], inp["props"]
    o = p[name]
    capacity = f["ports"] * o["pairs_per_port"] * ch_per_pair
    return (capacity >= f["n_wires"]
            and p["signal_e"] / o["enc_e"] >= f["snr_req"]
            and o["skew_ns"] <= f["skew_req_ns"]
            and o["buffer_ms"] >= f["drift_ms"]
            and o["dead_frac"] <= f["dead_req"])

def fails(inp):
    return not ok_option(inp, "adopted", inp["fixed"]["warm_ch_per_pair"])

def viable(inp):
    out = []
    if ok_option(inp, "multiplexed", inp["fixed"]["warm_ch_per_pair"]): out.append("multiplexed")
    if ok_option(inp, "cold_asic", inp["props"]["cold_asic"]["ch_per_pair"]): out.append("cold_asic")
    return out

if __name__ == "__main__":
    r1 = check_base("BASE", make(40), fails)
    r2 = check_conf("CONF1", make(8), fails, viable)
    sys.exit(0 if (r1 and r2) else 1)
