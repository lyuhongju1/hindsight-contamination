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
  - >= 2 alternatives are viable at nominal values and in >= 95% of draws;
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
    paths = list(_leaves(inputs))
    for _ in range(n):
        x = copy.deepcopy(inputs)
        for p in paths: _set(x, p, _get(inputs, p) * math.exp(rng.uniform(math.log(0.5), math.log(2))))
        yield x

def check_conf(level, inputs, fails, viable, n=2000):
    nom_fail, nom_viable = fails(inputs), viable(inputs)
    f = v = 0
    for x in _draws(level, inputs, n):
        f += bool(fails(x)); v += len(viable(x)) >= 2
    ok = nom_fail and len(nom_viable) >= 2 and f / n >= 0.95 and v / n >= 0.95
    print(f"{level:8s} adopted_fails_nominal={nom_fail} viable_nominal={nom_viable} "
          f"adopted_fails={f / n:.3f} >=2_viable={v / n:.3f} {'PASS' if ok else 'FAIL'}")
    return ok

def check_base(level, inputs, fails):
    ok = not fails(inputs)
    print(f"{level:8s} adopted_passes_nominal={ok} {'PASS' if ok else 'FAIL'}")
    return ok
