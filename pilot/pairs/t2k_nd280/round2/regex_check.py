import json, re, glob, os
d = os.path.dirname(os.path.abspath(__file__))
pat = json.load(open(os.path.join(d, r"..\..\..\scoring_regex.json")))["t2k_nd280"]
pats = {**pat["adopted"], **pat["distractors"]}
for f in sorted(glob.glob(os.path.join(d, "descriptions", "*.txt"))):
    t = open(f).read()
    hits = [k for k, p in pats.items() if re.search(p, t, re.I)]
    print(os.path.basename(f), "lines=%d" % len(t.strip().splitlines()), "hits=", hits or "none")
