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
| **1 Pilot** | Pilot pairs: T2K ND280 → SuperFGD, AugerPrime (from `candidate_pairs_PILOT.md`) | Claude | — | ◐ author agents running |
| | Pilot scaffold: scoring and identity regexes, five templates, briefs (author, red team), harness (`batch.py`, `score.py`, `gates.py`) | Claude | Regex unit tests; API smoke test | ☑ |
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

- **2026-11-06 (selection complete).** 14 pairs selected after 3 rounds (25 baselines assessed by two daters each, 25/25 eligibility agreement; every counted item double-verified). See `search/SELECTED_PAIRS.md`. A1 addendum 3 ("adopted" = the collaboration's chosen plan, not one of several options; build status recorded as an exploratory covariate) was committed before round-3 selection. Next: phase 3, materials for the 14 pairs.
- **2026-11-06 (round 2).** 10 of 14 detectors selected (round 1: XENON1T, GERDA→LEGEND, Advanced Virgo, ICARUS, SNO→SNO+, AGATA, MEG; round 2: COSINE-100, NEMO-3→SuperNEMO, Borexino→SOX). Verifier fixed for pypdf spacing and hyphenation false negatives; all 33 claims re-verified (no round-1 change; the paraphrase and fabricated controls still fail). Lineage rule (A1 addendum 2) committed before round 2. Round 3 running: astroparticle (FACT, KASCADE), collider (NA62, BESIII), grav_waves (KAGRA, aLIGO), nu_accel (MiniBooNE, OPERA). The first eligible in queue order per field is selected.
- **2026-11-06 (later).** Phase 2 progress: selection rules frozen (commit 721e55f); INSPIRE frame run (539 records); two-screener I1 screening (537/539 agree, 83 included, 81 after removing pilot pairs); upgrade-document search (2,130 documents for 65 baselines); Amendment A1 (sequential seeded draw) and I6 boundary 2023-06-30 committed before assessment; dating verifier built and self-tested. **Round 1 eligibility running** (q01–q09, one per field; daters D1 and D2 independent, three baselines per agent). Next: run the verifier on both daters' claims → I2 needs both claims verified with the same class (Post-primary) → select per round-robin until 14. Note: commits no longer carry Claude attribution lines (user memory); old commits are left as they are to preserve the freeze references.
- **2026-11-06. FULL STUDY STARTED** (PI: go; minimal PI involvement). Decision: public GitHub pre-registration, not a Registered Report. Phase 1: H1 power rerun (`power/power_override.py`; an empirical-logit test was rejected for inflated type I; the raw-proportion marginal test is conservative); target 14 pairs (minimum 10). `PREREGISTRATION.md` v4.2 drafted (H1 per model with Holm; H2 model differences; everything else exploratory; 7 Claude models plus a non-Anthropic model if a key is provided). Next: phase 2, running the INSPIRE frame.
- **2026-11-05. PILOT COMPLETE.** See `pilot/PILOT_SUMMARY.md`. Override replicates across T2K and Auger (Sonnet 4.5 26% / 22%; Sonnet 4.6 8% / 6%; Opus 5.5 0% / 0%), with blind adjudication κ ≈ 0.97. Recommendation: GO with changes (H1 on absolute O, more models incl. non-Anthropic, freeze v4.1/v4.2, item supply is the bottleneck). Awaiting PI decision.
- **2026-11-05.** T2K: round 2 red team (CONF1 DROP, CONF2 FIX); keylib now rejects booleans; brief rules 8–10. Round 3: BASE OK, CONF2 OK, CONF1 FIX (survivors are one technology at two pressures; 4.5 kg). Round-2 probes: recognition 55–100% even for generic twins; K 75–100% (F4). **First pilot sampling submitted** (`up_t2k_p1`: BASE, CONF2, ANON, NAME × 5 templates × 3 models × n=10 = 600). Fixed two harness bugs before any charge (stray .txt picked up as a description; custom_id > 64 characters → hashed). Round-4 CONF1 author running; Auger round-2 author still running.
- **2026-11-05.** Red teams: every level FIX for both pairs (findings F3: computable keys fragile for equivalent twins; cost/labour deciding Auger; giveaway exclusions; Auger CONF1 key bug). **PI approved the override-primary redesign** → `hindsight_contamination_study_design_v4_amendment.md`. Built `keylib.py` (all-inputs robustness, per-level seeds), K-probe task, rejection-aware scoring (`rejection_cues.json`), author brief v2, and a no-workaround rule in briefs. Round-2 author agents launched for both pairs (BASE + 2 CONF each). Next: gates → red team → ID + K probes → pilot sampling on BASE/CONF/ANON/NAME.
- **2026-11-05.** Pilot authoring done for both pairs (gates A–C passed; author agents stalled once each, then resumed). Identification probes run (840 requests, all succeeded). **Both pairs fail the ≤ 10% ID gate badly** (T2K 50–100% on EQ and CONF; Auger ~100% everywhere; Opus 5.5 names the adopted upgrade unprompted). See `pilot/findings.md` F1–F2 and the proposed redesign: the primary estimand becomes the override test with recognition measured rather than gated. Red teams running.
- **2026-11-05.** Pilot started. Push rule added to `.claude/settings.local.json` (exact `git push origin main` only; verified). Models reachable: Haiku 4.5 to Opus 5.5 and Fable 5.1. Pilot models: Sonnet 4.5, Sonnet 4.6, Opus 5.5 (adaptive, low effort); smoke test passed. Scoring and identity regexes and templates written before any pilot material. Two author agents launched (t2k_nd280, auger). Next: gates → red team → identification probes (n=20) → upgrade sampling (n=10 per cell).
- **2026-11-05.** Setup complete: Anthropic key verified (stored at user scope; load it from the user environment until Claude Code is restarted). GitHub logged in as lyuhongju1. Public repo https://github.com/lyuhongju1/hindsight-contamination created by Claude with PI approval; initial commit 020491c pushed. OpenRouter skipped: the second-vendor check is not possible until a key is added. Line-ending conversion disabled for byte-stable hashes.
- **2026-11-05.** Setup: git identity set and GitHub CLI 2.103.3 installed by Claude; gh is not logged in, and no API keys exist yet.
- **2026-11-05.** Switched to solo operation (no recruitment); design v3 written. `experts/` moved to `_obsolete/`. No sampling done; no keys on this machine. The machine has no GPU.
