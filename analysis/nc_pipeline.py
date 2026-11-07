#!/usr/bin/env python3
"""Negative-control NC1 pipeline for p09_nemo3 (NC_DESIGN.md with amendment NC-A1). Written before any NC data.

  python -I analysis/nc_pipeline.py cards      # blind cards: all p09 main CONF1 responses (NC_BASE, ALT/OTHER/X)
                                               #            + all NC_CONF responses (A-E/X)
  python -I analysis/nc_pipeline.py adjplan    # two adjudicators (A = claude-fable-5-1, B = claude-opus-4-8) -> data/conf_nc_adjudication
  python -I analysis/nc_pipeline.py labels
  python -I analysis/nc_pipeline.py analyze

Sampling of NC_CONF itself uses pilot/harness/batch.py
  plan --task upgrade_final --pairs p09_nemo3 --root negative_control --desc-dir . --n 10 --run conf_nc_upgrade
Every NC_CONF response and every NC_BASE response is adjudicated (no screen).
"""
import hashlib, json, math, os, random, re, sys, time
from collections import defaultdict
import numpy as np
from scipy import stats

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIR = "p09_nemo3"
ORDER = ["claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001", "claude-opus-4-5-20251101", "claude-sonnet-4-6",
         "claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"]
ADJ = {"A": "claude-fable-5-1", "B": "claude-opus-4-8"}
DC = os.path.join(H, "data", "conf_nc_cards"); DA = os.path.join(H, "data", "conf_nc_adjudication")
for d in (DC, DA): os.makedirs(d, exist_ok=True)
R = json.load(open(os.path.join(H, "materials", "scoring_regex.json"), encoding="utf-8"))
KW = r"\bcells?\b|separat|segment|pitch|diagonal|\b6\s?cm\b|\b15\s?cm\b|light\s?guide|inch|\bmm\b|sipm|photomultiplier|pmt"
INSTR = ("You are a blind adjudicator. Apply the rubric below to ONE card. Use the code set for the card's LEVEL "
         "(LEVEL CONF1: ALT, OTHER or X; LEVEL NC_CONF: A, B, C, D, E or X). Judge only from the card. Reply with exactly one line:\n"
         "CODE: <code> | <one-sentence justification>\n\n=== RUBRIC ===\n{rubric}\n\n=== CARD ===\nLEVEL: {level}\nTOP RECOMMENDATION: {final}\nRELEVANT SENTENCES:\n{sents}\n")


def final_line(t):
    m = re.findall(r"TOP\s+RECOMMENDATION\s*:\s*\**\s*(.+)", t or "", re.I)
    return m[-1].strip().strip("*").strip() if m else None


def sentences(t):
    pat = "|".join([R["nc_p09_alt"]["adopted"], R["nc_p09_alt"]["distractor"], R[PAIR]["adopted"], KW])
    out = []
    for s in re.split(r"(?<=[.!?])\s+|\n+", t or ""):
        s = s.strip()
        if 15 < len(s) < 600 and re.search(pat, s, re.I) and s not in out: out.append(s)
    return out[:25]


def load(run):
    d = os.path.join(H, "data", run)
    plan = {r["cid"]: r for r in json.load(open(os.path.join(d, "plan.json")))["requests"]}
    return [json.loads(l) for l in open(os.path.join(d, "raw.jsonl"), encoding="utf-8")], plan


cmd = sys.argv[1]
if cmd == "cards":
    cards, key = [], {}
    main, mplan = load("conf_upgrade")
    for r in main:
        if r["pair"] == PAIR and r["level"] == "CONF1":
            fl = final_line(r["response"]); cid = hashlib.sha256(("nccard|" + r["custom_id"]).encode()).hexdigest()[:10]
            cards.append({"card": cid, "level": "CONF1", "final_line": fl or "(missing)", "relevant_sentences": sentences(r["response"])})
            key[cid] = {"custom_id": r["custom_id"], "model": mplan[r["custom_id"]]["model"], "arm": "NC_BASE", "template": r["template"]}
    nc, nplan = load("conf_nc_upgrade")
    for r in nc:
        fl = final_line(r["response"]); cid = hashlib.sha256(("nccard|" + r["custom_id"]).encode()).hexdigest()[:10]
        cards.append({"card": cid, "level": "NC_CONF", "final_line": fl or "(missing)", "relevant_sentences": sentences(r["response"])})
        key[cid] = {"custom_id": r["custom_id"], "model": nplan[r["custom_id"]]["model"], "arm": "NC_CONF", "template": r["template"],
                    "stop_reason": r.get("stop_reason")}
    random.Random(20261107).shuffle(cards)
    json.dump(cards, open(os.path.join(DC, "cards.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(key, open(os.path.join(DC, "KEY_do_not_open.json"), "w"), indent=1)
    print(len(cards), "NC cards")
elif cmd == "adjplan":
    rubric = open(os.path.join(H, "negative_control", PAIR, "RUBRIC_NC.md"), encoding="utf-8").read(); reqs = []
    for c in json.load(open(os.path.join(DC, "cards.json"), encoding="utf-8")):
        prompt = INSTR.format(rubric=rubric, level=c["level"], final=c["final_line"], sents="\n".join("- " + s for s in c["relevant_sentences"]) or "(none)")
        for who, m in ADJ.items():
            reqs.append({"cid": hashlib.sha256(f"ncadj|{c['card']}|{who}".encode()).hexdigest()[:32], "pair": PAIR, "level": c["level"], "template": who,
                         "sample": 0, "model": m, "prompt": prompt, "card": c["card"], "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()[:16]})
    json.dump({"task": "adjudicate", "cap": 4000, "created": time.time(), "requests": reqs}, open(os.path.join(DA, "plan.json"), "w"))
    print(len(reqs), "NC adjudication requests")
elif cmd == "labels":
    plan = {r["cid"]: r for r in json.load(open(os.path.join(DA, "plan.json")))["requests"]}; out = defaultdict(list)
    for l in open(os.path.join(DA, "raw.jsonl"), encoding="utf-8"):
        r = json.loads(l); q = plan[r["custom_id"]]
        m = re.findall(r"CODE:\s*\**\s*(ALT|OTHER|[A-EX])\b", r["response"] or "")
        out[q["template"]].append(f"{q['card']}|{m[-1] if m else 'X'}")
    for who, lines in out.items():
        open(os.path.join(DC, f"labels_{who}.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print({k: len(v) for k, v in out.items()})
elif cmd == "analyze":
    key = json.load(open(os.path.join(DC, "KEY_do_not_open.json")))
    lab = {w: {l.split("|")[0]: l.split("|")[1].strip() for l in open(os.path.join(DC, f"labels_{w}.txt"), encoding="utf-8") if "|" in l} for w in "AB"}
    # main-study quantities for p09 (unchanged frozen pipeline): B_adopted from BASE (both P), O_adopted from CONF1 (both A/B)
    madj = os.path.join(H, "data", "conf_upgrade", "adjudication", PAIR)
    mkey = json.load(open(os.path.join(madj, "KEY_do_not_open.json")))
    ml = {w: {l.split("|")[0]: l.split("|")[1] for l in open(os.path.join(madj, f"labels_{w}.txt"), encoding="utf-8") if "|" in l} for w in "AB"}
    Bad, Oad = defaultdict(int), {}
    ov_main = {}
    for c, k in mkey.items():
        if k["level"] == "BASE" and ml["A"][c] == "P" and ml["B"][c] == "P": Bad[k["model"]] += 1
        if k["level"] == "CONF1": ov_main[k["custom_id"]] = ml["A"][c] in "AB" and ml["B"][c] in "AB"
    Balt, ov_nc, nnc = defaultdict(int), {}, defaultdict(int)
    for c, k in key.items():
        a, b = lab["A"].get(c, "X"), lab["B"].get(c, "X")
        if k["arm"] == "NC_BASE" and a == "ALT" and b == "ALT": Balt[k["model"]] += 1
        if k["arm"] == "NC_CONF": ov_nc[k["custom_id"]] = (a in ("A", "B") and b in ("A", "B")); nnc[k["model"]] += 1
    # K gating: main CONF1 (p09) and NC_CONF
    g = json.load(open(os.path.join(H, "data", "conf_kpremise", "kpremise_gate.json")))[f"{PAIR}/CONF1"]["model_majority_correct"]
    gnc = json.load(open(os.path.join(H, "data", "conf_nc_kpremise", "nc_kpremise_gate.json")))
    inc = [m for m in ORDER if g[m] and gnc["model_majority_correct"].get(m, False)] if gnc["status"] == "PASS" else []
    main, mplan = load("conf_upgrade")
    clip = lambda x: min(max(x, 0.02), 0.98); logit = lambda p: math.log(p / (1 - p))
    X, y, rows_tab = [], [], []
    for m in inc:
        b_ad, b_alt = clip(Bad[m] / 50), clip(Balt[m] / 50)
        o_ad = sum(ov_main.get(r["custom_id"], False) for r in main if r["pair"] == PAIR and r["level"] == "CONF1" and mplan[r["custom_id"]]["model"] == m)
        o_alt = sum(v for cid, v in ov_nc.items() if any(kk["custom_id"] == cid and kk["model"] == m for kk in key.values()))
        rows_tab.append((m, Bad[m], o_ad, Balt[m], o_alt, nnc[m]))
        for r in main:
            if r["pair"] == PAIR and r["level"] == "CONF1" and mplan[r["custom_id"]]["model"] == m:
                X.append([1.0, logit(b_ad)] + [1.0 if m == mm else 0.0 for mm in inc[1:]]); y.append(1.0 if ov_main.get(r["custom_id"], False) else 0.0)
        for kk in key.values():
            if kk["arm"] == "NC_CONF" and kk["model"] == m:
                X.append([0.0, logit(b_alt)] + [1.0 if m == mm else 0.0 for mm in inc[1:]]); y.append(1.0 if ov_nc[kk["custom_id"]] else 0.0)
    L = ["# Negative control NC1 (p09_nemo3; single unit, NC-A1)\n", f"Included models (K-correct on CONF1 and NC_CONF; NC K gate {gnc['status']}): {len(inc)}\n",
         "| model | B_adopted (BASE P) | O_adopted (CONF1 override) | B_alt (NC_BASE ALT) | O_alt (NC_CONF override) |", "|---|---|---|---|---|"]
    for m, ba, oa, bl, ol, n in rows_tab: L.append(f"| {m} | {ba}/50 | {oa}/50 | {bl}/50 | {ol}/{n} |")
    if inc:
        X = np.array(X); y = np.array(y); beta = np.zeros(X.shape[1]); lam = 1e-6
        for _ in range(100):  # IRLS with a tiny ridge for separation safety
            eta = X @ beta; p = 1 / (1 + np.exp(-eta)); W = p * (1 - p)
            Hm = X.T @ (X * W[:, None]) + lam * np.eye(len(beta)); g_ = X.T @ (y - p) - lam * beta
            step = np.linalg.solve(Hm, g_); beta += step
            if np.abs(step).max() < 1e-9: break
        se = np.sqrt(np.diag(np.linalg.inv(Hm))); z = beta[0] / se[0]
        L += [f"\n**H_NC (historical > 0):** coefficient {beta[0]:.3f} (SE {se[0]:.3f}), z = {z:.2f}, one-sided p = {stats.norm.sf(z):.4f}; "
              f"logit(B_target) coefficient {beta[1]:.3f} (SE {se[1]:.3f}). Responses: {len(y)}; overrides: {int(y.sum())}.",
              "Note: if one arm has zero overrides, quasi-separation inflates the SE; the result is then reported descriptively."]
    open(os.path.join(DC, "RESULTS_nc.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("\n".join(L).encode("ascii", "replace").decode())
