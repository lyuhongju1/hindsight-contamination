# Red-team report r1, p04_icarus (returned as text; saved by the orchestrator, 2026-11-06)

**Verdicts:**

| Level | Verdict | Reason |
|---|---|---|
| BASE | OK (minor FIX) | Port margin 1.2×, checked at nominal only (~60% of draws pass) |
| CONF1 | FIX, or DROP under a strict reading of rule 1 | — |
| kprobe | FIX | Gives the 600 pairs/port figure the description withholds |

**Central problems with CONF1:**
1. **Infrastructure, not physics.** The lever is a port count (40 → 8), an allocation phrase ("8 assigned to wire signals" lets other ports be reassigned), and an unstated per-port density (~600 pairs, from author knowledge). High-density feedthroughs could plausibly carry ~2,500 pairs per port.
2. **Does not test the counted item.** CONF1 falsifies *analog transport through the wall* (warm digitisation). It does **not** falsify "one ADC per channel with synchronous sampling", the counted, dated item. It kills warm multiplexed readout too, and the survivor (cold digitisation) can itself use per-channel synchronous ADCs. A correct answer of "per-channel ADCs in the liquid" would be regex-matched as adopted.

**Other notes:**
- The survivor is credible (ProtoDUNE-SP, SBND cold FE + ADC); MicroBooNE is *not* a cold-digitisation precedent.
- The 6 → 8 port change loosened the conflict and was logged; it is not biased tuning.
- Identifiability: high (ICARUS T600 → SBN).

**Orchestrator decision (2026-11-06):** the red team's proposal to *redefine the adopted item* as "warm digitisation outside the vessel" is **rejected**. That item was not the one dated and verified at selection (the counted item is "serial ADC per channel replacing multiplexed ADCs", arXiv:1503.01520), and swapping it would bypass the selection verification. The author gets one more attempt at a **physics** conflict that makes per-channel synchronous digitisation itself fail while another option survives. If no honest one exists, p04 yields **no unit**, an allowed outcome under PREREGISTRATION §7.
