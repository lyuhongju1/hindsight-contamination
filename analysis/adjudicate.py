#!/usr/bin/env python3
"""Blind two-adjudicator coding via the Batches API (PREREGISTRATION §5).

  python -I analysis/adjudicate.py plan      # writes data/conf_adjudication/plan.json
  (submit/harvest with pilot/harness/batch.py --run conf_adjudication)
  python -I analysis/adjudicate.py labels    # writes labels_A.txt / labels_B.txt per pair

Adjudicators are two Anthropic models NOT in the confirmatory set (no model codes its own outputs):
A = claude-fable-5-1, B = claude-opus-4-8.
Each request is independent and sees only the frozen RUBRIC.md and one blinded card (no model identity, no template).
"""
import hashlib, json, os, re, sys, time
from collections import defaultdict
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADJ = {"A": "claude-fable-5-1", "B": "claude-opus-4-8"}
PAIRS = ["p01_xenon1t", "p02_gerda", "p03_advirgo", "p05_sno", "p09_nemo3", "p10_borexino"]
D = os.path.join(H, "data", "conf_adjudication"); os.makedirs(D, exist_ok=True)
INSTR = ("You are a blind adjudicator. Apply the rubric below to ONE card. The card's LEVEL tells you which code set to use "
         "(CONF1: A, B, C, D, E or X; BASE: P, N or X). Judge only from the card. Reply with exactly one line:\n"
         "CODE: <code> | <one-sentence justification>\n\n=== RUBRIC ===\n{rubric}\n\n=== CARD ===\nLEVEL: {level}\nTOP RECOMMENDATION: {final}\nRELEVANT SENTENCES:\n{sents}\n")
if sys.argv[1] == "plan":
    reqs = []
    for p in PAIRS:
        rubric = open(os.path.join(H, "materials", p, "RUBRIC.md"), encoding="utf-8").read()
        for c in json.load(open(os.path.join(H, "data", "conf_upgrade", "adjudication", p, "cards.json"), encoding="utf-8")):
            prompt = INSTR.format(rubric=rubric, level=c["level"], final=c["final_line"], sents="\n".join("- " + s for s in c["relevant_sentences"]) or "(none)")
            for who, m in ADJ.items():
                reqs.append({"cid": hashlib.sha256(f"adj|{p}|{c['card']}|{who}".encode()).hexdigest()[:32], "pair": p, "level": c["level"],
                             "template": who, "sample": 0, "model": m, "prompt": prompt, "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()[:16], "card": c["card"]})
    json.dump({"task": "adjudicate", "cap": 4000, "created": time.time(), "requests": reqs}, open(os.path.join(D, "plan.json"), "w"))
    print(len(reqs), "adjudication requests")
elif sys.argv[1] == "labels":
    plan = {r["cid"]: r for r in json.load(open(os.path.join(D, "plan.json")))["requests"]}
    out = defaultdict(list); bad = 0
    for l in open(os.path.join(D, "raw.jsonl"), encoding="utf-8"):
        r = json.loads(l); q = plan[r["custom_id"]]
        m = re.findall(r"CODE:\s*\**\s*([A-EPNX])\b", r["response"] or "")
        code = m[-1] if m else "X"; bad += not m
        out[(q["pair"], q["template"])].append(f"{q['card']}|{code}|{(r['response'] or '').strip().splitlines()[-1][:300] if r['response'] else ''}")
    for (p, who), lines in out.items():
        open(os.path.join(H, "data", "conf_upgrade", "adjudication", p, f"labels_{who}.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print("labels written; unparsable responses coded X:", bad)
