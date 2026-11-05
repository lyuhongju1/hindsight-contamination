#!/usr/bin/env python3
"""Check the one-time setup (SETUP.md) without printing any secret. Usage: python -I setup_check.py"""
import json, os, shutil, subprocess, urllib.request

def ok(name, cond, note=""):
    print(f"[{'OK' if cond else '--'}] {name}{(' - ' + note) if note else ''}")
    return cond

def env(name):
    v = os.environ.get(name, "")
    return ok(f"env {name}", bool(v), f"set ({len(v)} chars)" if v else "missing")

def call(url, headers):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return None, str(e)

if env("ANTHROPIC_API_KEY"):
    s, _ = call("https://api.anthropic.com/v1/models",
                {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"})
    ok("Anthropic key accepted", s == 200, f"HTTP {s}")
if env("OPENROUTER_API_KEY"):
    s, _ = call("https://openrouter.ai/api/v1/key", {"Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"]})
    ok("OpenRouter key accepted", s == 200, f"HTTP {s}")
env("ZENODO_TOKEN")  # optional until first deposit

def run(cmd):
    try: return subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception: return ""
ok("git user.name", bool(run(["git", "config", "--global", "user.name"])))
ok("git user.email", bool(run(["git", "config", "--global", "user.email"])))
gh = shutil.which("gh")
if ok("gh installed", bool(gh)):
    st = subprocess.run([gh, "auth", "status"], capture_output=True, text=True)
    ok("gh authenticated", st.returncode == 0)
