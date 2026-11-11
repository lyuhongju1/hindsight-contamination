#!/usr/bin/env python3
"""Assemble paper_package/: everything needed to read, check and reproduce the study.   python -I make_package.py"""
import glob, hashlib, os, shutil, subprocess, sys

H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "paper_package")
if os.path.exists(P): shutil.rmtree(P)
os.makedirs(P)
IGN = shutil.ignore_patterns("__pycache__", "*.pyc", "verify_cache", "patch_*.py", "_tmp_*", "key_r0_backup.py")


def cp(src, dst):
    s, d = os.path.join(H, src), os.path.join(P, dst)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    (shutil.copytree(s, d, ignore=IGN) if os.path.isdir(s) else shutil.copy2(s, d))


# paper
cp("paper/draft.md", "paper/draft.md"); cp("paper/references.md", "paper/references.md")
# data (all confirmatory, exploratory, negative-control and stress-test runs) and the pilot
cp("data", "data"); cp("pilot", "pilot")
# materials: Study 1 (all 21 pairs incl. zero-unit), Study 2, negative control
cp("materials", "materials"); cp("materials_s2", "materials_s2"); cp("negative_control", "negative_control")
# pre-registrations, amendments, freeze manifests, design history
for f in ("PREREGISTRATION.md", "PREREGISTRATION_S2.md", "FREEZE_MANIFEST.md", "pair_selection_rules.md",
          "hindsight_contamination_study_design.md", "hindsight_contamination_study_design_v2.md",
          "hindsight_contamination_study_design_v3.md", "hindsight_contamination_study_design_v4_amendment.md"):
    cp(f, "preregistration/" + f)
cp("search/AMENDMENT_A1.md", "preregistration/AMENDMENT_A1_A2_A3.md")
# item selection (frame, queue, dater claims and verdicts, verifier); the arXiv PDF cache is excluded
cp("search", "selection")
# code
cp("analysis", "code")
for f in ("analysis_kpremise.py", "make_freeze_manifest.py", "make_package.py"): cp(f, "code/" + f)
cp("power", "power")
# logs and summaries
for f in ("RUNBOOK.md", "RESULTS_SUMMARY.md", "SETUP.md"): cp(f, "docs/" + f)

# regenerate tables and figures from the packaged data only
r = subprocess.run([sys.executable, "-I", os.path.join(P, "code", "make_figures_tables.py")], cwd=P, capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-600:])
shutil.copy2(os.path.join(H, "paper_package_README.md"), os.path.join(P, "README.md"))

# checksum manifest
lines = []
for f in sorted(glob.glob(os.path.join(P, "**", "*"), recursive=True)):
    if os.path.isfile(f):
        lines.append(f"{hashlib.sha256(open(f, 'rb').read()).hexdigest()}  {os.path.relpath(f, P).replace(os.sep, '/')}")
open(os.path.join(P, "MANIFEST_SHA256.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
sz = sum(os.path.getsize(f) for f in glob.glob(os.path.join(P, "**", "*"), recursive=True) if os.path.isfile(f))
print(f"{len(lines)} files, {sz / 1e6:.1f} MB")
