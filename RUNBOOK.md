# RUNBOOK — hindsight contamination study (solo operation)

*The operating log. Any Claude session resuming this project reads this file first, then `hindsight_contamination_study_design_v3.md`. Update the status column and the log at the end of every work session.*

Status key: ☐ not started · ◐ in progress · ☑ done · ⛔ blocked on PI.

---

## PI actions (only Hong Joo can do these)

| # | Action | Needed for | Status |
|---|---|---|---|
| P0 | Follow `SETUP.md` (about 30 min), then say "setup done" | Everything below | ☑ (OpenRouter skipped, Zenodo later) |
| P1 ☑ | Anthropic API key with a budget (set as env var `ANTHROPIC_API_KEY`; **never paste it in chat**). Rotate the old APS key first | All sampling | ⛔ |
| P2 | Multi-vendor gateway key (e.g. OpenRouter) as env var `OPENROUTER_API_KEY` | Second frontier vendor (design v3 §4), open-weight models (Arm 2a) | ⛔ (strongly recommended) |
| P3 ☑ | Approve creating a public GitHub repository for freezes and deposits (proposed name: `hindsight-contamination`), and approve each push | Credible timestamped freezes | ⛔ |
| P4 | Decide on GPU access for the causal arm (yes / no) | Arm 2b, claim rung 4 | ⛔ |
| P5 | Check the target journal's AI-use policy and choose the venue | Stage 1 | ⛔ |
| P6 | Read and sign off the Stage 1 manuscript; submit it | Stage 1 | later |
| P7 | Approve Zenodo deposits (needs your account token) | Freezes, registry | later |

---

## Pipeline

| Stage | Step | Who | Gate to pass | Status |
|---|---|---|---|---|
| **0 Setup** | Repository skeleton, `agents/` folders, role briefs | Claude | — | ☐ |
| | Freeze the selection rules + search script (hash, commit) | Claude, push with P3 | Public commit | ⛔ P3 |
| **1 Pilot** | Pilot pairs: T2K ND280 → SuperFGD, AugerPrime (from `candidate_pairs_PILOT.md`) | Claude | — | ☐ |
| | Twin ladder for the pilot pairs; key scripts; robustness check; red team | Author, key and red-team agents | §2 rules | ☐ |
| | Identification probes on all study models | Claude, needs P1/P2 | ID ≤ 10% | ⛔ P1 |
| | Pilot sampling: templates, output cap, truncation check, variance components (τ, description SD, template × level) | Claude | < 1% truncated | ⛔ P1 |
| | Re-run the power simulation with pilot variances and a GLMM; verify false-positive rate ≤ 0.05 | Claude | Power ≥ 0.8 on H1 | ☐ |
| **2 Pair selection** | Run the INSPIRE frame (`search/`) | Claude | Logged | ☐ (after the Stage 0 freeze) |
| | Two screening agents apply I1–I6; disagreements excluded | Agents | Evidence quotes | ☐ |
| | Dating: two dating agents plus the verifier script | Agents + script | Verified quotes and dates | ☐ |
| | Leakage audit (regex + content agent) | Script + agent | Clean | ☐ |
| | Seeded draw → ≥ 14 pairs, ≥ 28 post-baseline units; negative-control items | Script | Target met or shortfall logged | ☐ |
| **3 Materials** | Twin sets authored by Claude agents **and** by a second-vendor model | Agents / API | §2 keys, red team, ID gate | ☐ (second set ⛔ P2) |
| | Availability-matched distractors (pilot templates only) | Claude | Matched bands | ☐ |
| **4 Stage 1** | Analysis script frozen on simulated data; manuscript | Claude | P6 sign-off | ☐ |
| **5 Confirmatory** | Sampling inside a 4-week window, snapshot IDs pinned | Claude | Stop reasons, QC | ☐ |
| | Run the frozen analysis; specification curve; adjudication agents | Claude | — | ☐ |
| **6 Stage 2** | Manuscript, release, deposit | Claude, P7 | P6 | ☐ |
| **Registry** | Verify the candidates in `registry/`; freeze Wave 1; sample; deposit | Claude, P1, P3/P7 | Dated status checks | ☐ |
| **Arm 2b** | Causal injection | Needs P4 | — | ⛔ P4 |

---

## Log

- **2026-11-05.** Setup complete: Anthropic key verified (stored at user scope; load it from the user environment until Claude Code is restarted). GitHub logged in as lyuhongju1. Public repo https://github.com/lyuhongju1/hindsight-contamination created by Claude with PI approval; initial commit 020491c pushed. OpenRouter skipped: the second-vendor check is not possible until a key is added. Line-ending conversion disabled for byte-stable hashes.
- **2026-11-05.** Setup: git identity set and GitHub CLI 2.103.3 installed by Claude; gh is not logged in, and no API keys exist yet.
- **2026-11-05.** Switched to solo operation (no recruitment); design v3 written. `experts/` moved to `_obsolete/`. No sampling done; no keys on this machine. The machine has no GPU.
