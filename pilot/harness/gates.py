#!/usr/bin/env python3
"""Mechanical gates on a pair's authored materials (design v3 section 2, design v2 section 4.3).

  python -I gates.py --pair t2k_nd280

Gate A  leakage:  no description matches any adopted or distractor scoring regex for the pair.
Gate B  identity: no EQ/CONF/ABS description matches the pair's identity regex (names, sites).
Gate C  keys:     re-runs keys/key.py and checks that EQ1-3, ABS and CONF1 report PASS.
Gate D  is the identification probe on the study models (run separately with batch.py + score.py).
"""
import argparse, glob, json, os, re, subprocess, sys

PILOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser(); ap.add_argument("--pair", required=True); a = ap.parse_args()
pd = os.path.join(PILOT, "pairs", a.pair)
RX = json.load(open(os.path.join(PILOT, "scoring_regex.json"), encoding="utf-8"))[a.pair]
ID = json.load(open(os.path.join(PILOT, "identity_regex.json"), encoding="utf-8"))[a.pair]
pats = {**{f"adopted:{k}": v for k, v in RX["adopted"].items()}, **{f"distractor:{k}": v for k, v in RX["distractors"].items()}}
ok = True
for f in sorted(glob.glob(os.path.join(pd, "descriptions", "*.txt"))):
    lvl = os.path.splitext(os.path.basename(f))[0]; t = open(f, encoding="utf-8").read()
    hits = [n for n, rx in pats.items() if re.search(rx, t, re.I)]
    idh = re.findall(ID, t, re.I) if lvl not in ("NAME",) else []
    status = "ok" if not hits and not (idh and lvl != "ANON") else "FAIL"
    if lvl == "ANON" and idh: status = "FAIL"
    if status == "FAIL": ok = False
    print(f"[A/B] {lvl:6s} {status}  leakage={hits or '-'}  identity_terms={idh or '-'}")
kp = os.path.join(pd, "keys", "key.py")
if os.path.exists(kp):
    out = subprocess.run([sys.executable, "-I", kp], capture_output=True, text=True, cwd=os.path.dirname(kp), timeout=600).stdout
    for lvl in ("EQ1", "EQ2", "EQ3", "ABS", "CONF1"):
        line = next((l for l in out.splitlines() if re.match(rf"\s*\|?\s*{lvl}\b", l)), "")
        passed = "PASS" in line and "FAIL" not in line
        ok &= passed; print(f"[C]   {lvl:6s} {'ok' if passed else 'FAIL'}  {line.strip()[:110]}")
else:
    ok = False; print("[C] key.py missing")
print("GATES", "PASSED" if ok else "FAILED")
