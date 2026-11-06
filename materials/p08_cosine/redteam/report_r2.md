# Red team r2: p08_cosine (2026-11-06). Verdict: BASE OK; CONF1 DROP (as scoped); kprobe OK

**Blind answers:**
- BASE: in-house growth is favoured and sound.
- CONF1: vendor low-altitude crystals are favoured; the adopted item is "probably not sound", and relocating the method rescues it.

## Findings
- **(c) Decisive.** "The collaboration's chemistry, crystal-growth and machining work can only be done at its home institute" is a logistics rule, not physics (rule 1). Without it, the in-house method at the portal (250 m) or underground gives ≤0.03 mBq/kg and passes. No physical fact can close relocation.
- **(d)2. Schedule.** The failure also depends on the stated "about five months", which is a schedule rather than a physical floor. A Kyropoulos process takes about 4–6 weeks at minimum: 42 d gives robustness 0.39 and 30 d passes.
- **(a) r1 fixes:**
  - the exposure clock is justified (COSINE-100 arXiv:1905.12861; ANAIS arXiv:1706.05818);
  - the 1.5 dru goal is OK in the narrow sense, but the notes should say the limits are necessary, not sufficient;
  - Alpha Spectra is not credible against the background goal, so the survivor count is 1 (RMD), with a demonstrated-scale caveat (3–5 kg units).
- **(b) R0:** ×0.37 is acceptable; ×0.37–2 also passes.
- **Option for a new CONF:** a per-crystal ^nat K limit below what recrystallisation demonstrably reaches, while Astro-Grade (~4 ppb) does. This needs a cited in-house K figure.

## Study decision (2026-11-06)
- The r1 "home-institute-only" fix, which the orchestrator approved, was an error: it closed a workaround with a logistics rule. It is withdrawn.
- The adopted item stays the METHOD (not narrowed), so the altitude CONF1 is **withdrawn**.
- **One final author attempt** at a CONF that defeats the method physically (e.g. a K or ²¹⁰Pb limit backed by cited demonstrated purification performance, robust under ×0.5–2). Otherwise **p08 becomes a zero-unit pair** under A2.
