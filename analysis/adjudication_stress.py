#!/usr/bin/env python3
"""Adjudication robustness (exploratory, post-freeze).

  python -I analysis/adjudication_stress.py plan     # stratified sample of CONF1 cards -> data/conf_adj_stress/plan.json
  (submit/harvest with pilot/harness/batch.py --run conf_adj_stress)
  python -I analysis/adjudication_stress.py report

Two re-codings of the same 300 stratified CONF1 cards:
- C  = claude-opus-5 (a third model not in the confirmatory set), original instruction and rubric;
- A2 = claude-fable-5-1 with a reworded instruction and the rubric's code table rows in reverse order
  (tests sensitivity to the instruction wording and code order).
Strata (per pair, seeded): both adjudicators override (A/B + A/B); both non-override; disagreement on override.
"""
import hashlib, json, os, random, re, sys, time
from collections import Counter, defaultdict

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADJ = os.path.join(H, "data", "conf_upgrade", "adjudication")
D = os.path.join(H, "data", "conf_adj_stress"); os.makedirs(D, exist_ok=True)
UNITS = ["p01_xenon1t", "p02_gerda", "p03_advirgo", "p05_sno", "p09_nemo3"]
SEED = 20261107
sys.path.insert(0, os.path.join(H, "analysis"))
INSTR = ("You are a blind adjudicator. Apply the rubric below to ONE card. The card's LEVEL tells you which code set to use "
         "(CONF1: A, B, C, D, E or X; BASE: P, N or X). Judge only from the card. Reply with exactly one line:\n"
         "CODE: <code> | <one-sentence justification>\n\n=== RUBRIC ===\n{rubric}\n\n=== CARD ===\nLEVEL: {level}\nTOP RECOMMENDATION: {final}\nRELEVANT SENTENCES:\n{sents}\n")
INSTR2 = ("Below is a scoring guide followed by a single anonymised answer card from a design exercise. Using only the card, "
          "decide which single code from the guide fits the answer's committed TOP RECOMMENDATION (for LEVEL CONF1 the codes are "
          "A-E or X; for LEVEL BASE they are P, N or X). Answer on one line in the form\nCODE: <code> | <brief reason>\n\n"
          "--- SCORING GUIDE ---\n{rubric}\n\n--- ANSWER CARD ---\nLEVEL: {level}\nTOP RECOMMENDATION: {final}\nRELEVANT SENTENCES:\n{sents}\n")


def reverse_code_table(rubric):
    """Reverse the order of the code rows in the first markdown table whose rows start with | **X** |."""
    lines = rubric.split("\n"); idx = [i for i, l in enumerate(lines) if re.match(r"\|\s*\*\*[A-EX]\*\*\s*\|", l)]
    if len(idx) > 1:
        block = [lines[i] for i in idx]
        for i, l in zip(idx, reversed(block)): lines[i] = l
    return "\n".join(lines)


def labels(p, w):
    return {l.split("|")[0]: l.split("|")[1] for l in open(os.path.join(ADJ, p, f"labels_{w}.txt"), encoding="utf-8") if "|" in l}


if sys.argv[1] == "plan":
    rng = random.Random(SEED); reqs = []; sample = {}
    for p in UNITS:
        key = json.load(open(os.path.join(ADJ, p, "KEY_do_not_open.json"))); A, B = labels(p, "A"), labels(p, "B")
        cards = {c["card"]: c for c in json.load(open(os.path.join(ADJ, p, "cards.json"), encoding="utf-8"))}
        st = defaultdict(list)
        for c, k in key.items():
            if k["level"] != "CONF1": continue
            oa, ob = A[c] in "AB", B[c] in "AB"
            st["both" if oa and ob else "none" if not (oa or ob) else "split"].append(c)
        pick = []
        for s, n in (("both", 20), ("none", 20), ("split", 20)):
            L = sorted(st[s]); pick += rng.sample(L, min(n, len(L)))
        rubric = open(os.path.join(H, "materials", p, "RUBRIC.md"), encoding="utf-8").read()
        for c in pick:
            cd = cards[c]; sents = "\n".join("- " + s for s in cd["relevant_sentences"]) or "(none)"
            sample[f"{p}|{c}"] = {"orig_A": A[c], "orig_B": B[c]}
            for who, model, tpl, rub in (("C", "claude-opus-5", INSTR, rubric), ("A2", "claude-fable-5-1", INSTR2, reverse_code_table(rubric))):
                prompt = tpl.format(rubric=rub, level=cd["level"], final=cd["final_line"], sents=sents)
                reqs.append({"cid": hashlib.sha256(f"stress|{p}|{c}|{who}".encode()).hexdigest()[:32], "pair": p, "level": "CONF1",
                             "template": who, "sample": 0, "model": model, "prompt": prompt, "card": c,
                             "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()[:16]})
    json.dump({"task": "adjudicate", "cap": 4000, "created": time.time(), "requests": reqs}, open(os.path.join(D, "plan.json"), "w"))
    json.dump(sample, open(os.path.join(D, "sample.json"), "w"), indent=1)
    print(len(reqs), "requests over", len(sample), "cards")
elif sys.argv[1] == "report":
    plan = {r["cid"]: r for r in json.load(open(os.path.join(D, "plan.json")))["requests"]}
    sample = json.load(open(os.path.join(D, "sample.json"))); new = defaultdict(dict)
    for l in open(os.path.join(D, "raw.jsonl"), encoding="utf-8"):
        r = json.loads(l); q = plan[r["custom_id"]]; m = re.findall(r"CODE:\s*\**\s*([A-EPNX])\b", r["response"] or "")
        new[f"{q['pair']}|{q['card']}"][q["template"]] = m[-1] if m else "X"
    ov = lambda x: x in ("A", "B")
    agree = Counter(); flips = Counter(); strata = Counter()
    for k, v in sample.items():
        a, b, c, a2 = v["orig_A"], v["orig_B"], new[k].get("C", "X"), new[k].get("A2", "X")
        orig = ov(a) and ov(b); s = "both" if orig else ("none" if not (ov(a) or ov(b)) else "split")
        strata[s] += 1
        agree[("C_vs_A", ov(c) == ov(a))] += 1; agree[("C_vs_B", ov(c) == ov(b))] += 1; agree[("A2_vs_A", ov(a2) == ov(a))] += 1
        agree[("C_exact_A", c == a)] += 1; agree[("A2_exact_A", a2 == a)] += 1
        flips[(s, "C_override", ov(c))] += 1; flips[(s, "A2_override", ov(a2))] += 1
    n = len(sample)
    L = ["# Adjudication robustness (exploratory)\n", f"{n} stratified CONF1 cards (per unit: 20 both-override, 20 both-non-override, 20 split; fewer if unavailable).\n",
         "| check | agreement |", "|---|---|"]
    for lab, key in (("C (Opus 5) vs A on override yes/no", "C_vs_A"), ("C vs B on override yes/no", "C_vs_B"), ("A2 (reworded, reversed table) vs A on override", "A2_vs_A"),
                     ("C vs A exact code", "C_exact_A"), ("A2 vs A exact code", "A2_exact_A")):
        L.append(f"| {lab} | {agree[(key, True)]}/{n} ({agree[(key, True)] / n:.2f}) |")
    L += ["\n| stratum (original) | n | C codes override | A2 codes override |", "|---|---|---|---|"]
    for s in ("both", "none", "split"):
        L.append(f"| {s} | {strata[s]} | {flips[(s, 'C_override', True)]} | {flips[(s, 'A2_override', True)]} |")
    open(os.path.join(D, "RESULTS_adjudication_stress.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n"); print("\n".join(L))
