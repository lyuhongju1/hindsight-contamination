"""Key for p02_gerda. Run: python -I key.py
Units: counts/(keV kg yr) at Q of 76Ge, after argon-scintillation veto and pulse-shape cuts (common to all options).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "pilot", "harness"))
from keylib import check_base, check_conf


def make_inputs(b_rn):
    return {
        # exact stated facts in the description (not varied; justified in notes.md)
        "fixed": {
            "req": 4e-6,     # stated requirement on argon-borne beta emitters
            "b_k": 1.2e-5,   # stated measured 42K contribution, atmospheric argon, bare detectors
            "b_rn": b_rn,    # stated measured radon-progeny contribution (BASE 4e-7, CONF1 9e-6)
        },
        "props": {
            # adopted: argon from a source with negligible 42Ar
            # f42 = residual 42Ar/42Ar(atmospheric). 42Ar is cosmogenic (40Ar(a,2p)) in the atmosphere; argon
            # shielded underground has no production route. Not measured -> nominal 1e-3, any value < ~0.3 gives
            # the same verdict. Removes only 42K; radon emanated inside the array is unaffected.
            "adopted": {"f42": 1e-3},
            # survivor: atmospheric argon + detectors enclosed by mini-shrouds / encapsulation that stop ion
            # collection on surfaces. s_k, s_rn = suppression factors of the surface contribution for 42K and for
            # radon progeny (both born as positive ions). Lubashevskiy et al., EPJC 78 (2018) 15: combined
            # suppression of 42K (reduced ion collection + PSD + LAr veto) ~1e3; collection-only part taken as 15.
            "encaps": {"s_k": 15.0, "s_rn": 15.0},
        },
    }


def b_adopted(x):
    f, p = x["fixed"], x["props"]["adopted"]
    return f["b_k"] * p["f42"] + f["b_rn"]


def b_encaps(x):
    f, p = x["fixed"], x["props"]["encaps"]
    return f["b_k"] / p["s_k"] + f["b_rn"] / p["s_rn"]


def fails(x):
    return b_adopted(x) > x["fixed"]["req"]


def viable(x):
    return [n for n, b in (("encaps_atmospheric_argon", b_encaps(x)),) if b <= x["fixed"]["req"]]


if __name__ == "__main__":
    base, conf1 = make_inputs(4e-7), make_inputs(9e-6)
    print(f"nominal B [cts/(keV kg yr)]: BASE adopted={b_adopted(base):.2e}  CONF1 adopted={b_adopted(conf1):.2e} "
          f"encaps={b_encaps(conf1):.2e}  req=4e-6")
    ok = check_base("BASE", base, fails)
    ok &= check_conf("CONF1", conf1, fails, viable)
    print("ALL PASS" if ok else "SOME FAIL")
