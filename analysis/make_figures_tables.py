#!/usr/bin/env python3
"""Regenerate every summary table (CSV) and figure (PNG + PDF) from the released data.

  python -I code/make_figures_tables.py        (run from the package root, or from the project root)

Reads only data/ (and materials/ for the K-probe expectations). Writes tables/ and figures/.
Override = both blind adjudicators code A or B (PREREGISTRATION §5). Palette: validated reference
instance (blue sequential; categorical blue/orange), light surface, thin marks, recessive axes.
"""
import csv, json, math, os, re
from collections import defaultdict, Counter
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

ROOT = os.getcwd()
D = lambda *p: os.path.join(ROOT, "data", *p)
TAB = os.path.join(ROOT, "tables"); FIG = os.path.join(ROOT, "figures")
os.makedirs(TAB, exist_ok=True); os.makedirs(FIG, exist_ok=True)

ORDER = ["claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001", "claude-opus-4-5-20251101", "claude-sonnet-4-6",
         "claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"]
SHORT = {"claude-sonnet-4-5-20250929": "Sonnet 4.5", "claude-haiku-4-5-20251001": "Haiku 4.5", "claude-opus-4-5-20251101": "Opus 4.5",
         "claude-sonnet-4-6": "Sonnet 4.6", "claude-haiku-5-5": "Haiku 5.5", "claude-sonnet-5-5": "Sonnet 5.5", "claude-opus-5-5": "Opus 5.5"}
UNITS = ["p01_xenon1t", "p02_gerda", "p03_advirgo", "p05_sno", "p09_nemo3", "p10_borexino"]
UNAME = {"p01_xenon1t": "XENON1T", "p02_gerda": "GERDA", "p03_advirgo": "Adv. Virgo", "p05_sno": "SNO", "p09_nemo3": "NEMO-3", "p10_borexino": "Borexino*"}

# palette (reference instance, light mode)
INK, INK2, MUTED, GRID, BASEL, SURF = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7", "#fcfcfb"
BLUE, ORANGE = "#2a78d6", "#eb6834"
SEQ = LinearSegmentedColormap.from_list("blue", ["#f0efec", "#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])
plt.rcParams.update({"font.size": 9, "axes.edgecolor": BASEL, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "axes.facecolor": SURF, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": False, "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(FIG, name + ".png"), dpi=200, bbox_inches="tight")
    fig.savefig(os.path.join(FIG, name + ".pdf"), bbox_inches="tight"); plt.close(fig)


def write_csv(name, header, rows):
    with open(os.path.join(TAB, name + ".csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)


def load_run(run):
    plan = {r["cid"]: r for r in json.load(open(D(run, "plan.json")))["requests"]}
    rows = [json.loads(l) for l in open(D(run, "raw.jsonl"), encoding="utf-8")]
    return rows, plan


# ---------- main upgrade data (with the 32k resample replacing its cells) ----------
rows, plan = load_run("conf_upgrade")
rrows, rplan = load_run("conf_upgrade_resample")
rcells = {(r["pair"], r["level"], r["model"]) for r in rplan.values()}
rows = [r for r in rows if (r["pair"], r["level"], plan[r["custom_id"]]["model"]) not in rcells] + rrows
plan.update(rplan)


def labels(p, w):
    return {l.split("|")[0]: l.split("|")[1] for l in open(D("conf_upgrade", "adjudication", p, f"labels_{w}.txt"), encoding="utf-8") if "|" in l}


ovr, basep, codes = {}, {}, Counter()
for p in UNITS:
    key = json.load(open(D("conf_upgrade", "adjudication", p, "KEY_do_not_open.json")))
    A, B = labels(p, "A"), labels(p, "B")
    for c, k in key.items():
        if k["level"] == "CONF1":
            ovr[k["custom_id"]] = A[c] in "AB" and B[c] in "AB"
            if A[c] == B[c]: codes[(p, A[c])] += 1
        if k["level"] == "BASE":
            basep[k["custom_id"]] = A[c] == "P" and B[c] == "P"
cnt = defaultdict(lambda: [0, 0]); bcnt = defaultdict(lambda: [0, 0]); tcnt = defaultdict(lambda: [0, 0])
gate = json.load(open(D("conf_kpremise", "kpremise_gate.json")))
incl = lambda p, m: gate[f"{p}/CONF1"]["status"] == "PASS" and gate[f"{p}/CONF1"]["model_majority_correct"][m]
for r in rows:
    m = plan[r["custom_id"]]["model"]; k = (r["pair"], m)
    if r["level"] == "CONF1":
        cnt[k][1] += 1; cnt[k][0] += ovr.get(r["custom_id"], False)
        if incl(r["pair"], m): tcnt[r["template"]][1] += 1; tcnt[r["template"]][0] += ovr.get(r["custom_id"], False)
    if r["level"] == "BASE":
        bcnt[k][1] += 1; bcnt[k][0] += basep.get(r["custom_id"], False)

# K premise
kplan = {r["cid"]: r for r in json.load(open(D("conf_kpremise", "plan.json")))["requests"]}
kc = defaultdict(lambda: [0, 0])
for l in open(D("conf_kpremise", "raw.jsonl"), encoding="utf-8"):
    r = json.loads(l); m = kplan[r["custom_id"]]["model"]
    v = re.findall(r"VERDICT:\s*\**\s*(YES|NO)\b", r["response"] or "", re.I)
    kc[(r["pair"], m)][1] += 1; kc[(r["pair"], m)][0] += bool(v) and v[-1].upper() == "NO"

# recognition
rec = json.load(open(D("conf_identify", "recognition.json")))

# ---------- tables ----------
T = []
for p in UNITS:
    for m in ORDER:
        rv = rec.get(f"{p}|CONF1|{m}", [0, 0])
        T.append([p, SHORT[m], m, cnt[(p, m)][0], cnt[(p, m)][1], round(cnt[(p, m)][0] / max(cnt[(p, m)][1], 1), 3),
                  bcnt[(p, m)][0], bcnt[(p, m)][1], kc[(p, m)][0], kc[(p, m)][1], rv[0], rv[1],
                  "yes" if incl(p, m) else "no"])
write_csv("table_cells_model_x_unit", ["unit", "model", "model_id", "override_CONF1", "n_CONF1", "O", "BASE_adopt", "n_BASE",
                                       "K_correct", "n_K", "recognized_CONF1", "n_identify", "included_confirmatory"], T)
write_csv("table_override_by_template", ["template", "override", "n", "rate"],
          [[t, v[0], v[1], round(v[0] / v[1], 3)] for t, v in sorted(tcnt.items())])
write_csv("table_adjudication_codes_agreed", ["unit", "code", "n_cards_both_agree"], sorted([[p, c, n] for (p, c), n in codes.items()]))
FUN1 = [["Study 1", "pairs taken through authoring", 21], ["Study 1", "admitted honest physics-only conflict", 6],
        ["Study 1", "passed K premise (confirmatory units)", 5],
        ["Study 2", "queue entries", 33], ["Study 2", "eligible (both daters)", 15], ["Study 2", "physics-decidable units", 0]]
write_csv("table_funnel", ["study", "stage", "count"], FUN1)
txt = open(D("conf_upgrade", "RESULTS_confirmatory.md"), encoding="utf-8").read()
fe = re.findall(r"(claude-[a-z0-9.-]+) (-?[0-9.]+) \(([0-9.]+)\)", txt.split("Model fixed effects")[1])
write_csv("table_glmm_model_effects", ["model", "logit_at_median_unit", "probability_at_median_unit"],
          [[SHORT.get(m, m), float(b), float(p)] for m, b, p in fe])

# ---------- figures ----------
# F1 funnel
fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.4), sharex=False)
for ax, st in zip(axes, ("Study 1", "Study 2")):
    rs = [r for r in FUN1 if r[0] == st]; y = np.arange(len(rs))[::-1]
    ax.barh(y, [r[2] for r in rs], height=0.55, color=BLUE)
    for yi, r in zip(y, rs): ax.text(r[2] + 0.4, yi, str(r[2]), va="center", color=INK, fontsize=9)
    ax.set_yticks(y); ax.set_yticklabels([r[1] for r in rs], color=INK2); ax.set_title(st, color=INK, loc="left", fontsize=10)
    ax.set_xticks([]); ax.spines["bottom"].set_visible(False); ax.set_xlim(0, max(r[2] for r in rs) * 1.2)
fig.suptitle("Few real upgrade decisions admit an honest physics-only conflict", x=0.01, ha="left", color=INK, fontsize=11)
fig.tight_layout(); save(fig, "fig1_funnel")

# F2 override heatmap
M = np.array([[cnt[(p, m)][0] / max(cnt[(p, m)][1], 1) for p in UNITS] for m in ORDER])
fig, ax = plt.subplots(figsize=(6.6, 3.4))
im = ax.imshow(M, cmap=SEQ, vmin=0, vmax=1, aspect="auto")
for i, m in enumerate(ORDER):
    for j, p in enumerate(UNITS):
        v = cnt[(p, m)][0]; c = "#ffffff" if M[i, j] > 0.55 else INK
        ax.text(j, i, f"{v}" + ("" if incl(p, m) else "†"), ha="center", va="center", color=c, fontsize=8)
ax.set_xticks(range(len(UNITS))); ax.set_xticklabels([UNAME[p] for p in UNITS]); ax.set_yticks(range(len(ORDER)))
ax.set_yticklabels([SHORT[m] for m in ORDER]); ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
cb = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02); cb.set_label("override rate (of 50)", color=INK2); cb.outline.set_visible(False)
ax.set_title("Override of the historically adopted item under conflict (CONF1)", loc="left", color=INK, fontsize=10)
fig.text(0.01, -0.03, "Cell = overrides out of 50 (both adjudicators A/B). † excluded from confirmatory tests "
         "(K gate). *Borexino suspended by the K premise check.", fontsize=7, color=MUTED, ha="left")
save(fig, "fig2_override_heatmap")

# F3 knowledge vs override dissociation
fig, ax = plt.subplots(figsize=(4.6, 3.6))
ax.axvspan(15, 20.6, ymin=0, ymax=1, color="#f0efec", zorder=0)
ax.axhline(10, color=GRID, lw=1, zorder=1)
xs = [kc[(p, m)][0] for p in UNITS[:5] for m in ORDER]; ys = [cnt[(p, m)][0] for p in UNITS[:5] for m in ORDER]
jit = [((i * 7) % 5 - 2) * 0.09 for i in range(len(xs))]  # deterministic jitter so stacked cells stay visible
ax.scatter([x + j for x, j in zip(xs, jit)], ys, s=36, color=BLUE, edgecolor=SURF, linewidth=1.5, zorder=3)
nd = sum(1 for x, y in zip(xs, ys) if x >= 15 and y >= 10)
ax.text(9.3, 30, f"Shaded: knows the physics\n(K ≥ 15/20). Above the line:\noverrides (≥ 10/50).\nBoth: {nd} of {len(xs)} cells.", fontsize=8, color=INK2, va="top")
ax.text(9.3, -1.5, "points jittered horizontally by < 0.2 for visibility", fontsize=6.5, color=MUTED)
ax.set_xlabel("K-probe correct (of 20), physics asked in isolation"); ax.set_ylabel("overrides under conflict (of 50)")
ax.set_xlim(9, 20.6); ax.set_ylim(-2, 52)
ax.set_title("Knowing the physics does not prevent override", loc="left", color=INK, fontsize=10)
save(fig, "fig3_knowledge_vs_override")

# F4 BASE adoption vs CONF override, small multiples
fig, axes = plt.subplots(1, 5, figsize=(9.6, 2.9), sharey=True)
for ax, p in zip(axes, UNITS[:5]):
    y = np.arange(len(ORDER))[::-1]
    for yi, m in zip(y, ORDER):
        b, o = bcnt[(p, m)][0], cnt[(p, m)][0]
        ax.plot([b, o], [yi, yi], color=GRID, lw=2, zorder=1)
        ax.scatter([b], [yi], s=28, color=BLUE, zorder=3, edgecolor=SURF, linewidth=1)
        ax.scatter([o], [yi], s=28, color=ORANGE, zorder=3, edgecolor=SURF, linewidth=1)
    ax.set_title(UNAME[p], color=INK, fontsize=9, loc="left"); ax.set_xlim(-3, 53); ax.set_xticks([0, 25, 50])
    ax.set_yticks(y); ax.set_yticklabels([SHORT[m] for m in ORDER])
axes[0].scatter([], [], color=BLUE, label="adopts item at BASE (sound)"); axes[0].scatter([], [], color=ORANGE, label="overrides at CONF1 (item fails)")
fig.legend(loc="lower left", bbox_to_anchor=(0.01, -0.08), ncol=2, frameon=False, fontsize=8)
fig.suptitle("Override tracks a prior preference for the historical item (counts of 50)", x=0.01, ha="left", color=INK, fontsize=10)
fig.tight_layout(); save(fig, "fig4_base_vs_conf")

# F5 GLMM model effects
fe_sorted = sorted([(SHORT.get(m, m), float(p)) for m, b, p in fe], key=lambda x: x[1])
fig, ax = plt.subplots(figsize=(4.6, 2.8))
y = np.arange(len(fe_sorted))
ax.hlines(y, 0, [v for _, v in fe_sorted], color=GRID, lw=2)
ax.scatter([v for _, v in fe_sorted], y, s=40, color=BLUE, zorder=3, edgecolor=SURF, linewidth=1.5)
for yi, (_, v) in zip(y, fe_sorted): ax.text(v + 0.02, yi, f"{v:.3f}", va="center", fontsize=8, color=INK)
ax.axvline(0.10, color=MUTED, lw=1, ls=(0, (3, 3))); ax.text(0.107, len(y) - 1.5, "H1 null (0.10)", fontsize=7, color=MUTED, va="center")
ax.set_yticks(y); ax.set_yticklabels([n for n, _ in fe_sorted]); ax.set_xlim(0, 0.65)
ax.set_xlabel("estimated override probability at the median unit (GLMM)")
ax.set_title("Models differ sharply (H2: LR = 300, df = 6)", loc="left", color=INK, fontsize=10)
save(fig, "fig5_model_effects")

# F6 templates
tt = sorted(tcnt.items())
fig, ax = plt.subplots(figsize=(4.6, 2.4))
x = np.arange(len(tt)); v = [a[0] / a[1] for _, a in tt]
ax.bar(x, v, width=0.55, color=BLUE)
for xi, vi in zip(x, v): ax.text(xi, vi + 0.006, f"{vi:.2f}", ha="center", fontsize=8, color=INK)
ax.set_xticks(x); ax.set_xticklabels([t.split("_", 1)[1] for t, _ in tt]); ax.set_ylim(0, 0.32)
ax.set_ylabel("override rate"); ax.set_title("Override is stable across prompt templates", loc="left", color=INK, fontsize=10)
save(fig, "fig6_templates")

# F7 adjudication robustness
st = open(D("conf_adj_stress", "RESULTS_adjudication_stress.md"), encoding="utf-8").read()
ag = re.findall(r"\| ([^|]+) \| (\d+)/(\d+) \(([0-9.]+)\) \|", st)
fig, ax = plt.subplots(figsize=(5.6, 2.4))
y = np.arange(len(ag))[::-1]
ax.barh(y, [float(a[3]) for a in ag], height=0.55, color=BLUE)
for yi, a in zip(y, ag): ax.text(float(a[3]) + 0.01, yi, f"{a[1]}/{a[2]}", va="center", fontsize=8, color=INK)
ax.set_yticks(y); ax.set_yticklabels([a[0] for a in ag], fontsize=8); ax.set_xlim(0, 1.12); ax.set_xticks([0, 0.5, 1])
ax.set_xlabel("agreement on 216 stratified CONF1 cards")
ax.set_title("Adjudication is stable to a third model and reworded rubric", loc="left", color=INK, fontsize=10)
save(fig, "fig7_adjudication_robustness")
write_csv("table_adjudication_stress", ["check", "agree", "n", "rate"], [[a[0], a[1], a[2], a[3]] for a in ag])

print("tables:", sorted(os.listdir(TAB))); print("figures:", sorted(f for f in os.listdir(FIG) if f.endswith(".png")))
