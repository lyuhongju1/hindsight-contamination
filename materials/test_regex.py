#!/usr/bin/env python3
"""Screen-regex sanity tests for the sampled pairs (the screen only flags candidates; adjudicators code from RUBRIC.md).
Note: p09's generic 'high-QE PMT' branch also matches the 3-in. survivor; the screen over-flags it by design."""
import json, os, re, sys
R = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "scoring_regex.json"), encoding="utf-8"))
T = {  # pair: ([texts that must match 'adopted'], [texts that must not])
 "p01_xenon1t": (["Add liquid-phase purification of the xenon", "a liquid xenon purifier in the cryostat", "LXe purification loop"],
                 ["Increase the hot getter flow", "add a second distillation column"]),
 "p02_gerda": (["Switch to underground argon", "UAr from an underground source", "argon extracted from underground wells", "42Ar-depleted argon"],
               ["encapsulate the detectors in a nylon mini-shroud", "improve the radon trap"]),
 "p03_advirgo": (["install a 300 m filter cavity", "frequency-dependent squeezing", "rotate the squeezing angle with frequency"],
                 ["EPR-entangled squeezing using the arms", "raise the arm power"]),
 "p05_sno": (["Fill the vessel with linear alkylbenzene", "a LAB-based liquid scintillator", "use LAB with PPO"],
             ["switch to PXE", "pseudocumene scintillator", "load tellurium into water"]),
 "p09_nemo3": (["8-inch high-QE PMTs coupled directly", "R5912 photomultipliers", "eight-inch photomultipliers"],
               ["3-inch PMTs on small cubes", "add a PVT layer"]),
 "p10_borexino": (["deploy a 144Ce-144Pr antineutrino generator", "a cerium source next to the detector", "Ce-144 source"],
                  ["use a 51Cr neutrino source", "an argon-37 source"]),
}
bad = 0; n = 0
for p, (yes, no) in T.items():
    for t in yes: n += 1; ok = bool(re.search(R[p]["adopted"], t, re.I)); bad += not ok; print(("ok  " if ok else "FAIL"), p, "MATCH   ", t) if not ok else None
    for t in no: n += 1; ok = not re.search(R[p]["adopted"], t, re.I); bad += not ok; print(("ok  " if ok else "FAIL"), p, "NO-MATCH", t) if not ok else None
print(f"{n - bad}/{n} regex tests pass"); sys.exit(1 if bad else 0)
