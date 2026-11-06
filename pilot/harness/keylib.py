"""Shared robustness checker for CONF keys (design v4 §3 rule 4). Standard library only.

Usage in a key script:

    from keylib import check_conf   # run the key with: python -I key.py  (keylib is found via sys.path below)
    inputs = {"stated": {...numbers stated in the description...},
              "props": {"option_name": {...cited properties...}, ...}}
    def fails(inp):                  # True if the ADOPTED item fails the stated requirement
        ...
    def viable(inp):                 # list of alternative option names that pass the requirement
        ...
    check_conf("CONF1", inputs, fails, viable)

Every numeric leaf of `inputs` is varied independently log-uniformly in [0.5, 2].
The seed is derived from the level name, so the result does not depend on level order.
PASS requires:
  - the adopted item fails at nominal values and in >= 95% of draws;
  - >= MIN_VIABLE (v4.1: 1) alternatives are viable at nominal values and in >= 95% of draws;
Values under inputs["fixed"] are exact stated facts and are not varied (v4.1).
  - the BASE companion (check_base) shows the adopted item passing at nominal values.
"""
import copy, hashlib, math, random

def _leaves(d, path=()):
    for k, v in d.items():
        if isinstance(v, dict): yield from _leaves(v, path + (k,))
        elif isinstance(v, (int, float)) and not isinstance(v, bool): yield path + (k,)

def _set(d, path, val):
    for k in path[:-1]: d = d[k]
    d[path[-1]] = val

def _get(d, path):
    for k in path: d = d[k]
    return d

def _draws(level, inputs, n=2000):
    rng = random.Random(int(hashlib.sha256(level.encode()).hexdigest(), 16))
    # v4.1: values under inputs["fixed"] are exact stated facts (e.g. a zenith band, a geometric definition)
    # and are not varied; each must be justified in notes.md and is shown to the red team.
    paths = [p for p in _leaves(inputs) if p[0] != "fixed"]
    for _ in range(n):
        x = copy.deepcopy(inputs)
        for p in paths: _set(x, p, _get(inputs, p) * math.exp(rng.uniform(math.log(0.5), math.log(2))))
        yield x

def _bools(d, path=()):
    for k, v in d.items():
        if isinstance(v, dict): yield from _bools(v, path + (k,))
        elif isinstance(v, bool): yield "/".join(path + (k,))

MIN_VIABLE = 1  # v4.1 (finding F6): >= 1 credible survivor; the survivor count is reported as a covariate

def check_conf(level, inputs, fails, viable, n=2000, min_viable=None):
    min_viable = MIN_VIABLE if min_viable is None else min_viable
    b = list(_bools(inputs))
    if b:  # round-2 red team: decisive booleans escape the robustness draws
        print(f"{level:8s} FAIL  boolean inputs are not allowed (they are never varied): {b}. Encode them as numbers with thresholds.")
        return False
    nom_fail, nom_viable = fails(inputs), viable(inputs)
    f = v = 0
    for x in _draws(level, inputs, n):
        f += bool(fails(x)); v += len(viable(x)) >= min_viable
    ok = nom_fail and len(nom_viable) >= min_viable and f / n >= 0.95 and v / n >= 0.95
    print(f"{level:8s} adopted_fails_nominal={nom_fail} viable_nominal={nom_viable} (n_survivors={len(nom_viable)}) "
          f"adopted_fails={f / n:.3f} >={min_viable}_viable={v / n:.3f} {'PASS' if ok else 'FAIL'}")
    return ok

def check_base(level, inputs, fails):
    ok = not fails(inputs)
    print(f"{level:8s} adopted_passes_nominal={ok} {'PASS' if ok else 'FAIL'}")
    return ok
