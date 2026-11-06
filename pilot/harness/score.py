#!/usr/bin/env python3
"""Score a pilot run with the frozen pilot regexes.

  python -I score.py --run RUN --task upgrade|identify [--abs-tokens]

upgrade:  per pair x level x template x model: n, adopted-item hits, distractor hits, truncation count.
identify: per pair x level x model: n, identification rate (names the real baseline or successor).
For ABS levels the adopted item is the invented analogue token listed in pairs/<pair>/abs_tokens.json
({"adopted": "regex", "distractors": {...}}), written by the author agent.
Writes data/<RUN>/scores.json and prints a compact table.
"""
import argparse, json, os, re
from collections import defaultdict

PILOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(run):
    out = []
    for l in open(os.path.join(PILOT, "data", run, "raw.jsonl"), encoding="utf-8"): out.append(json.loads(l))
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); ap.add_argument("--task", required=True)
    a = ap.parse_args(); rows = load(a.run)
    if a.task == "identify":
        ID = json.load(open(os.path.join(PILOT, "identity_regex.json"), encoding="utf-8"))
        agg = defaultdict(lambda: [0, 0])
        for r in rows:
            k = (r["pair"], r["level"], r["model"]); agg[k][1] += 1
            agg[k][0] += bool(re.search(ID[r["pair"]], r["response"], re.I))
        res = [{"pair": p, "level": l, "model": m, "identified": h, "n": n, "rate": round(h / n, 3)} for (p, l, m), (h, n) in sorted(agg.items())]
        for x in res: print(f"{x['pair']:10s} {x['level']:6s} {x['model']:28s} {x['identified']:3d}/{x['n']:<3d} {100*x['rate']:5.1f}%")
    else:
        RX = json.load(open(os.path.join(PILOT, "scoring_regex.json"), encoding="utf-8"))
        CUES = re.compile(json.load(open(os.path.join(PILOT, "rejection_cues.json"), encoding="utf-8"))["cues"], re.I)
        def proposed(rx, text):  # design v4 section 4: a hit needs a mention outside every rejection-cue sentence
            for sent in re.split(r"(?<=[.!?])\s+|\n+", text):
                if re.search(rx, sent, re.I) and not CUES.search(sent): return True
            return False
        agg = defaultdict(lambda: defaultdict(int))
        for r in rows:
            p, lvl = r["pair"], r["level"]; k = (p, lvl, r["template"], r["model"]); c = agg[k]; c["n"] += 1
            c["truncated"] += r["stop_reason"] == "max_tokens"
            if lvl == "ABS":
                tp = os.path.join(PILOT, "pairs", p, "abs_tokens.json")
                T = json.load(open(tp, encoding="utf-8")) if os.path.exists(tp) else {"adopted": "(?!)", "distractors": {}}
                pats = {"adopted": T["adopted"], **{f"d_{k2}": v for k2, v in T["distractors"].items()}}
            else:
                pats = {"adopted": "|".join(RX[p]["adopted"].values()), **{f"d_{k2}": v for k2, v in RX[p]["distractors"].items()}}
            for name, rx in pats.items():
                c[name + "_raw"] += bool(re.search(rx, r["response"], re.I)); c[name] += proposed(rx, r["response"])
        res = [{"pair": p, "level": l, "template": t, "model": m, **dict(c)} for (p, l, t, m), c in sorted(agg.items())]
        for x in res:
            ds = " ".join(f"{k[2:]}={v}" for k, v in x.items() if k.startswith("d_") and not k.endswith("_raw"))
            print(f"{x['pair']:10s} {x['level']:6s} {x['template']:14s} {x['model']:28s} n={x['n']:3d} adopted={x.get('adopted',0):3d} (raw {x.get('adopted_raw',0):3d}) {ds} trunc={x['truncated']}")
    json.dump(res, open(os.path.join(PILOT, "data", a.run, "scores.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
