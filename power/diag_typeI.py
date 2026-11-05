"""Type-I diagnostic for power_sim.py: is the inflated false-positive rate due to the different
baseline-rate distributions of adopted and distractor units (floor/ceiling compression)?
Usage: python -I diag_typeI.py <aps_repo_root> <out_dir>"""
import sys
src = open(__file__.replace('diag_typeI.py', 'power_sim.py'), encoding='utf-8').read()
exec(src[:src.index("TAU = 0.5")])
import numpy as np
se = S_E['conservative (A-D)']
lines = ["# Type-I diagnostic (d_out = 0, 20 units, 5 templates x 3 twins, n = 20, 4000 sims)\n",
         "| scenario | false-positive rate, logit | pp |", "|---|---|---|"]
def run(label, LA_, LD_, d_rec):
    global LA, LD
    LA, LD = LA_, LD_
    r = sim(20, 20, 0.0, 0.5, se, 5, 3, d_rec=d_rec, B=4000)
    lines.append(f"| {label} | {p_onesided(r['did_logit']):.3f} | {p_onesided(r['did_pp']):.3f} |")
LA0, LD0 = LA.copy(), LD.copy()
mid = lambda L: L[(L > np.log(.1/.9)) & (L < np.log(.9/.1))]
run("empirical baselines, recognition effect 0.3", LA0, LD0, 0.3)
run("empirical baselines, no recognition effect", LA0, LD0, 0.0)
run("both drawn from adopted distribution, effect 0.3", LA0, LA0, 0.3)
run("both restricted to 10-90% baselines, effect 0.3", mid(LA0), mid(LD0), 0.3)
open(sys.argv[2] + '/typeI_diagnostic.md', 'w').write("\n".join(lines) + "\n"); print("\n".join(lines))

# --- balanced levels: ANON gets as many samples per template as the twins combined
def sim_bal(U, n, d_out, tau, s_e, n_t=5, n_tw=3, d_rec=0.3, B=4000):
    base_a = rng.choice(LA, size=(B, U)); base_d = rng.choice(LD, size=(B, U))
    eff_a = d_rec + d_out + rng.normal(0, tau, (B, U)); eff_d = d_rec + rng.normal(0, tau, (B, U))
    def contrast(base, eff):
        anon_mu = base[..., None] + rng.normal(0, s_d, (B, U, 1)) + rng.normal(0, s_e, (B, U, n_t))
        twin_mu = (base - eff)[..., None, None] + rng.normal(0, s_d, (B, U, n_tw, 1)) + rng.normal(0, s_e, (B, U, n_tw, n_t))
        ka = rng.binomial(n * n_tw, expit(anon_mu)).sum(-1); kt = rng.binomial(n, expit(twin_mu)).sum((-1, -2)); N = n * n_t * n_tw
        return np.log((ka + .5) / (N - ka + .5)) - np.log((kt + .5) / (N - kt + .5))
    return contrast(base_a, eff_a) - contrast(base_d, eff_d)
lines += ["", "Balanced levels (ANON sampled 3x per template so both levels have equal n):", "", "| scenario | false-positive rate, logit |", "|---|---|"]
for label, LA_, LD_, dr in (("empirical baselines, effect 0.3", LA0, LD0, 0.3), ("empirical baselines, no effect", LA0, LD0, 0.0),
                            ("both from adopted distribution, effect 0.3", LA0, LA0, 0.3)):
    LA, LD = LA_, LD_
    lines.append(f"| {label} | {p_onesided(sim_bal(20, 20, 0.0, 0.5, se, d_rec=dr)):.3f} |")
LA, LD = LA0, LD0
for d in (0.5, 1.0):
    lines.append(f"| power, balanced, empirical baselines, d_out={d} | {p_onesided(sim_bal(20, 20, d, 0.5, se)):.3f} |")
open(sys.argv[2] + '/typeI_diagnostic.md', 'w').write("\n".join(lines) + "\n"); print("\n".join(lines[-9:]))
