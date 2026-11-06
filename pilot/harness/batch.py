#!/usr/bin/env python3
"""Pilot sampling harness (Anthropic Message Batches API, standard library only).

  python -I batch.py plan    --task upgrade|identify --pairs t2k_nd280,auger --models M1,M2 --n 10 --run RUN
  python -I batch.py submit  --run RUN          # submits the plan in chunks; state saved for resume
  python -I batch.py harvest --run RUN          # waits for batches, appends results (append-only JSONL)
  python -I batch.py status  --run RUN

Every request is recorded with a prompt hash, model, reasoning setting, stop reason and usage.
Settings follow the companion study: temperature 1.0, 16k output cap, minimum reasoning per model.
The API key is read from the user environment and never printed.
"""
import argparse, glob, hashlib, json, os, sys, time, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__)); PILOT = os.path.dirname(HERE)
API = "https://api.anthropic.com/v1"; CHUNK = 2000
THINK = {  # minimum reasoning each model allows (companion study, Amendment 10)
    "claude-haiku-5-5": {"thinking": {"type": "disabled"}},
    "claude-sonnet-5-5": {"thinking": {"type": "between_tools"}},
    "claude-opus-5-5": {"thinking": {"type": "adaptive"}, "output_config": {"effort": "low"}},
    "claude-fable-5-1": {"thinking": {"type": "adaptive"}, "output_config": {"effort": "low"}},
}
CAP = {"upgrade": 16000, "identify": 2000, "kprobe": 4000}


def key():
    k = os.environ.get("ANTHROPIC_API_KEY")
    if not k and os.name == "nt":
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as h: k = winreg.QueryValueEx(h, "ANTHROPIC_API_KEY")[0]
    if not k: sys.exit("ANTHROPIC_API_KEY not set")
    return k


def api(method, path, body=None, raw_url=None):
    req = urllib.request.Request(raw_url or API + path, data=json.dumps(body).encode() if body is not None else None, method=method,
                                 headers={"x-api-key": key(), "anthropic-version": "2023-06-01", "content-type": "application/json"})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(req, timeout=900) as r: payload = r.read(); break
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and attempt < 7: time.sleep(30 * (attempt + 1)); continue
            sys.exit(f"API {e.code}: {e.read().decode(errors='replace')[:800]}")
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if attempt < 7: time.sleep(30 * (attempt + 1)); continue
            raise
    if raw_url: return [json.loads(l) for l in payload.decode().splitlines() if l.strip()]
    return json.loads(payload)


def run_dir(run): d = os.path.join(PILOT, "data", run); os.makedirs(d, exist_ok=True); return d


def cmd_plan(a):
    reqs = []
    if a.task == "kprobe":  # physics-knowledge probe: the question is the whole prompt (design v2 section 4.5)
        for pair in a.pairs.split(","):
            Q = json.load(open(os.path.join(PILOT, "pairs", pair, "round2", "kprobe.json"), encoding="utf-8"))
            for level, q in Q.items():
                prompt = q["question"]; h = hashlib.sha256(prompt.encode()).hexdigest()[:16]
                for m in a.models.split(","):
                    for i in range(a.n):
                        reqs.append({"cid": f"{pair}__{level}__K__{i}__{m}".replace(".", "p"), "pair": pair, "level": level,
                                     "template": "K", "sample": i, "model": m, "prompt": prompt, "prompt_sha256": h})
        d = run_dir(a.run)
        json.dump({"task": a.task, "cap": CAP[a.task], "created": time.time(), "requests": reqs}, open(os.path.join(d, "plan.json"), "w"))
        print(f"planned {len(reqs)} requests (kprobe)"); return
    T = json.load(open(os.path.join(PILOT, "templates.json"), encoding="utf-8"))[a.task]
    for pair in a.pairs.split(","):
        for f in sorted(glob.glob(os.path.join(PILOT, "pairs", pair, *a.desc_dir.split("/"), "*.txt"))):
            level = os.path.splitext(os.path.basename(f))[0]
            desc = open(f, encoding="utf-8").read().strip()
            for tname, tpl in T.items():
                prompt = tpl.replace("{DESC}", desc); h = hashlib.sha256(prompt.encode()).hexdigest()[:16]
                for m in a.models.split(","):
                    for i in range(a.n):
                        reqs.append({"cid": f"{pair}__{level}__{tname}__{i}__{m}".replace(".", "p"), "pair": pair, "level": level,
                                     "template": tname, "sample": i, "model": m, "prompt": prompt, "prompt_sha256": h})
    d = run_dir(a.run)
    json.dump({"task": a.task, "cap": CAP[a.task], "created": time.time(), "requests": reqs}, open(os.path.join(d, "plan.json"), "w"))
    out_tok = {"upgrade": 2800, "identify": 120}[a.task]
    print(f"planned {len(reqs)} requests ({a.task}); approx output {len(reqs) * out_tok / 1e6:.1f}M tokens")


def cmd_submit(a):
    d = run_dir(a.run); plan = json.load(open(os.path.join(d, "plan.json")))
    sp = os.path.join(d, "state.json"); state = json.load(open(sp)) if os.path.exists(sp) else {"batches": []}
    reqs = plan["requests"]; chunks = [reqs[k:k + CHUNK] for k in range(0, len(reqs), CHUNK)]
    for n, ch in enumerate(chunks):
        if n < len(state["batches"]): continue
        body = {"requests": [{"custom_id": r["cid"], "params": {"model": r["model"], "max_tokens": plan["cap"], "temperature": 1.0,
                "messages": [{"role": "user", "content": r["prompt"]}], **THINK.get(r["model"], {})}} for r in ch]}
        b = api("POST", "/messages/batches", body); state["batches"].append(b["id"])
        json.dump(state, open(sp, "w")); print(f"submitted chunk {n + 1}/{len(chunks)} ({len(ch)} requests)")


def cmd_harvest(a):
    d = run_dir(a.run); plan = json.load(open(os.path.join(d, "plan.json")))
    meta = {r["cid"]: r for r in plan["requests"]}; state = json.load(open(os.path.join(d, "state.json")))
    raw = os.path.join(d, "raw.jsonl"); have = set()
    if os.path.exists(raw): have = {json.loads(l)["custom_id"] for l in open(raw, encoding="utf-8")}
    with open(raw, "a", encoding="utf-8") as out:
        for bid in state["batches"]:
            while True:
                b = api("GET", f"/messages/batches/{bid}")
                if b["processing_status"] == "ended": break
                time.sleep(60)
            n = bad = 0
            for row in api("GET", "", raw_url=b["results_url"]):
                cid = row["custom_id"]
                if cid in have: continue
                if row["result"]["type"] != "succeeded": bad += 1; continue
                msg = row["result"]["message"]; u = msg.get("usage") or {}; r = meta[cid]
                out.write(json.dumps({"custom_id": cid, **{k: r[k] for k in ("pair", "level", "template", "sample", "prompt_sha256")},
                    "model": msg.get("model"), "max_tokens": plan["cap"], "thinking_setting": THINK.get(r["model"], {}),
                    "response": "".join(x.get("text", "") for x in msg.get("content", []) if x.get("type") == "text"),
                    "thinking": "".join(x.get("thinking", "") for x in msg.get("content", []) if x.get("type") == "thinking") or None,
                    "stop_reason": msg.get("stop_reason"), "usage": u, "batch_id": bid, "ts": time.time()}) + "\n")
                have.add(cid); n += 1
            out.flush(); print(f"batch {bid[-8:]}: harvested {n}, non-success {bad}")


def cmd_status(a):
    d = run_dir(a.run); state = json.load(open(os.path.join(d, "state.json")))
    for bid in state["batches"]:
        b = api("GET", f"/messages/batches/{bid}"); print(bid[-8:], b["processing_status"], b["request_counts"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("plan"); p.add_argument("--task", required=True); p.add_argument("--pairs", required=True)
    p.add_argument("--models", required=True); p.add_argument("--n", type=int, required=True); p.add_argument("--run", required=True)
    p.add_argument("--desc-dir", default="descriptions", help="e.g. round2/descriptions")
    for c in ("submit", "harvest", "status"): sp.add_parser(c).add_argument("--run", required=True)
    a = ap.parse_args(); {"plan": cmd_plan, "submit": cmd_submit, "harvest": cmd_harvest, "status": cmd_status}[a.cmd](a)
