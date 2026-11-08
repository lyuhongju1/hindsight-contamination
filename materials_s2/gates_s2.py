#!/usr/bin/env python3
"""Mechanical gates for a confirmatory pair (AUTHOR_BRIEF rules 4, 9).

  python -I gates.py p02_gerda

A  forbidden terms: no description matches the pair's 'adopted' pattern; none except NAME matches 'identity'.
B  keys: re-runs keys/key.py; BASE and every CONF* line must report PASS.
C  files: dossier.md, notes.md, kprobe.json present; every kprobe question ends with the VERDICT instruction.
"""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__)); pair = sys.argv[1]; pd = os.path.join(HERE, pair); RX = os.path.join(os.path.dirname(HERE), "materials", "scoring_regex.json")
R = json.load(open(RX, encoding="utf-8"))[pair]
ok = True
for f in sorted(glob.glob(os.path.join(pd, "descriptions", "*.txt"))):
    lvl = os.path.splitext(os.path.basename(f))[0]; t = open(f, encoding="utf-8").read()
    a = re.findall(R["adopted"], t, re.I); i = [] if lvl == "NAME" else re.findall(R["identity"], t, re.I)
    bad = bool(a or i); ok &= not bad
    print(f"[A] {lvl:6s} {'FAIL' if bad else 'ok'}  adopted={a or '-'} identity={i or '-'}")
kp = os.path.join(pd, "keys", "key.py")
if os.path.exists(kp):
    out = subprocess.run([sys.executable, "-I", kp], capture_output=True, text=True, cwd=os.path.dirname(kp), timeout=900)
    lines = [l for l in out.stdout.splitlines() if re.match(r"\s*(BASE|CONF\d)\b", l) and ("PASS" in l or "FAIL" in l)]
    if not any(l.strip().startswith("BASE") for l in lines): ok = False; print("[B] BASE result line missing")
    for l in lines:
        passed = "PASS" in l and "FAIL" not in l; ok &= passed
        print(f"[B] {'ok  ' if passed else 'FAIL'} {l.strip()[:120]}")
    if out.returncode != 0: ok = False; print("[B] key.py exited with an error:", out.stderr[-300:])
    nconf = sum(1 for l in lines if l.strip().startswith("CONF"))
else:
    ok = False; print("[B] keys/key.py missing")
for need in ("dossier.md", "notes.md", "kprobe.json"):
    if not os.path.exists(os.path.join(pd, need)): ok = False; print(f"[C] missing {need}")
if os.path.exists(os.path.join(pd, "kprobe.json")):
    for k, v in json.load(open(os.path.join(pd, "kprobe.json"), encoding="utf-8")).items():
        q = v.get("question", "") if isinstance(v, dict) else ""
        good = q.rstrip().endswith("VERDICT: YES or VERDICT: NO."); ok &= good
        print(f"[C] kprobe {k}: {'ok' if good else 'FAIL (missing VERDICT instruction)'}  expected={v.get('expected') if isinstance(v, dict) else '?'}")
if os.path.exists(kp) and ok and nconf == 0:
    print("GATES PASSED (BASE only): NO CONF, zero-unit pair, contributes no confirmatory unit")
else:
    print("GATES", "PASSED" if ok else "FAILED")
