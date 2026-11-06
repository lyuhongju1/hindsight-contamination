# Pilot summary and go/no-go recommendation

*2026-11-05. Covers everything in `pilot/` (findings F1–F11). Written by Claude for the PI.*

## What was tested

| Item | Detail |
|---|---|
| Pairs | 2 real instruments: T2K ND280 → 3D-cube target; Auger → surface scintillator panels |
| Models | 3: Sonnet 4.5, Sonnet 4.6, Opus 5.5 |
| Materials | 4 author rounds and 6 red-team rounds |
| Probes | ~1,900 identification and constraint-knowledge (K) probe responses |
| Sampling | ~2,700 upgrade responses, all templates and models |
| Adjudication | 144 blind cards, κ = 0.97 |

## Main results

1. **Disguise fails (F1, F2, F4).** Twins of famous instruments are recognized at 50–100%, Auger at 100%, including abstract twins. Opus 5.5 even names the real upgrade unprompted. Recognition must be **measured, not gated**. This is a reportable result on its own.
2. **Override is real and model-dependent, and it replicates across both pairs (F8, F11):**

   | Model | T2K CONF2 override | Auger CONF1 override | Knows the physics (K) |
   |---|---|---|---|
   | Sonnet 4.5 | **26%** | **22%** | yes |
   | Sonnet 4.6 | 8% | 6% | yes |
   | Opus 5.5 | 0% | 0% | yes |

3. **The strongest evidence is qualitative and striking.**
   - Sonnet 4.5 misstates physics it gets right in isolation, so that the historical answer fits ("plastic ≈ 1.5% hydrogen").
   - It falls back to the historical technology when its own preferred option is ruled out.
4. **The model that recognizes famous instruments best (Opus 5.5) never overrides.** Recognition is not sufficient for contamination; compliance with stated physics matters more.

## What the pilot taught about the method

- **The forced final line plus blind five-category adjudication works** (κ ≈ 0.97). Sentence-level regex scoring does not (F5).
- **Honest conflict twins are scarce.** Each real instrument yielded about **one** usable conflict after 3–4 author/red-team rounds. Equivalent twins with computable keys are fragile (F3, F6).
- **The K-probe doubles as a check on the key's physics.** It caught a wrong premise (F9). It needs a forced verdict line (F10).
- **Operational costs:**
  - agent stalls are frequent, so work should be split small with no web access by default;
  - API spend for the whole pilot was roughly $70–100 (to be confirmed from logged usage).

## Recommendation: **GO**, with these changes before the Stage 1 freeze

1. **Restate H1 on the absolute override rate O** (K-gated), with R descriptive (F11). Rerun the power simulation for this estimand. The pilot effects (≈ 25% against a 10% threshold for Sonnet 4.5, ≈ 0% for Opus) suggest **~10–14 pairs** may suffice, not the 28 units planned. To be verified.
2. **Add more models.** The effect is model-dependent, so the paper's question becomes *which* models override and why. This is cheap with the existing key:
   - Haiku 4.5/5.5, Sonnet 5/5.5, Opus 4.5 (scale and generation axes, as in the APS paper);
   - **at least one non-Anthropic model (OpenRouter key)**, which is now essential: without it, a reviewer can say "this is a Claude 4.5 quirk".
3. **Freeze the v4.1/v4.2 protocol:**
   - ≥ 1 credible survivor;
   - fixed exact facts;
   - forced final lines for upgrade and K prompts;
   - frozen rubrics;
   - the K-premise check (F9);
   - closure of workaround routes.
4. **Item supply is the bottleneck.** Budget ~3–4 agent rounds per pair. Run the INSPIRE frame and the dating pipeline next.
5. **A human spot-check of the conflict keys** by the PI (about 1 hour) would materially strengthen the paper. All judgement so far is model judgement.

## What would change the recommendation

If the effect vanishes on new pairs, or exists only on Sonnet 4.5, the paper becomes a narrower but still publishable report: "override of stated physics by recalled history is model-specific and absent in the newest frontier model". The registered design makes that outcome credible too.
