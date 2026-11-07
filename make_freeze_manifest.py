#!/usr/bin/env python3
"""Writes FREEZE_MANIFEST.md: SHA-256 of every file that fixes the confirmatory study. python -I make_freeze_manifest.py"""
import glob, hashlib, os, time
H = os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
pats = ["PREREGISTRATION.md", "search/pair_selection_rules.md", "search/AMENDMENT_A1.md", "search/SELECTED_PAIRS.md",
        "materials/AUTHOR_BRIEF.md", "materials/REDTEAM_BRIEF.md", "materials/scoring_regex.json", "materials/test_regex.py", "materials/gates.py",
        "pilot/templates.json", "pilot/harness/batch.py", "pilot/harness/score.py", "pilot/harness/keylib.py",
        "power/power_override.py", "power/power_small_J.py", "analysis_kpremise.py", "data/conf_kpremise/kpremise_gate.json"]
for p in ("p01_xenon1t", "p02_gerda", "p03_advirgo", "p05_sno", "p09_nemo3", "p10_borexino"):
    pats += [f"materials/{p}/RUBRIC.md", f"materials/{p}/kprobe.json", f"materials/{p}/keys/key.py", f"materials/{p}/descriptions/*.txt"]
files = sorted({f.replace("\\", "/") for pat in pats for f in glob.glob(pat)})
L = ["# Freeze manifest: confirmatory study (PREREGISTRATION v4.3)\n",
     f"Generated {time.strftime('%Y-%m-%d %H:%M:%S %Z')}. The study is frozen by the public commit that adds this file. No confirmatory upgrade or identification sample has been drawn. The only confirmatory-model calls so far are the K premise check (§2.4).\n",
     "| SHA-256 | file |", "|---|---|"]
for f in files: L.append(f"| `{hashlib.sha256(open(f, 'rb').read()).hexdigest()}` | {f} |")
open("FREEZE_MANIFEST.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n"); print(len(files), "files hashed")
