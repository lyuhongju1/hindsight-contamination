# Notes: p03_advirgo

## Design choices
- Adopted item: frequency-dependent squeezing via an external detuned high-finesse resonator (AdV+ Phase I). Descriptions avoid the forbidden terms and do not name or rule out any technology class.
- BASE: invented 3.6 km dual-recycled interferometer, 55 kg masses, quantum-noise crossover 55 Hz, 13 dB source, 90 % total efficiency (85 % before r1), 400 m auxiliary evacuated path. Requirement (r2): >= 3 dB quantum-noise reduction at every frequency from 20 Hz to 800 Hz (key: 25 log-spaced points).
- CONF1 (minimal edit, one number): auxiliary path 400 m -> 8 m. Mechanism: the resonator must have half-linewidth ~ f_SQL/sqrt(2) ~ 39 Hz; at 8 m this needs input transmission ~ 26 ppm, comparable to the round-trip loss, so the low-frequency squeezing is largely decohered. r2 key: sideband model with half-linewidth, detuning and injection angle optimised against the band minimum; best band minimum ~0.5 dB at the 10 ppm floor and -0.3 dB at nominal 15 ppm; requirement is 3 dB.
- Fixed-angle squeezing fails in both BASE and CONF1 (any single angle anti-squeezes one of the two bands; best band minimum ~ -9 dB).
- Survivor: EPR/conditional squeezing, which uses the 3.6 km interferometer itself as the frequency-dependent element for the detuned idler; needs no long auxiliary resonator. Conditional variance with 13 dB two-mode source, eta_signal 0.90, eta_idler 0.90*(1-delta), plus mismatch excess (r1): 4.39 dB nominal; ~3.5 dB at worst corner.
- Workaround routes closed by plain fact: no auxiliary optics or separate auxiliary beam lines can be installed in the 3.6 km arm tubes; arm power and test-mass mass fixed as stated (no moving the crossover out of band). Folding the 8 m resonator does not help: round-trip loss grows ~ with the number of reflections as the path grows, so loss per unit path (the figure of merit) is unchanged or worse.
- Coherence (rule 7): the edited number only concerns the vertex auxiliary space; nothing else in the instrument depends on it. 8 m of straight vacuum at a vertex station is realistic.

## Survivors per CONF
- CONF1: 1 (epr_conditional_squeezing).

## Fixed inputs (inputs["fixed"]) and justification
- f_sql_Hz = 55, src_dB = 13, eta = 0.90, mirror_loss_floor = 5 ppm, L_aux_m = 400 / 8, f_low = 20 Hz, f_high = 800 Hz, req_dB = 3: all are exact numbers stated in the description (instrument/project facts and the requirement), not cited properties.
- Varied x0.5-2: short-cavity excess round-trip loss (5 ppm nominal, on top of the fixed 2 x 5 ppm), long-cavity round-trip loss (60 ppm nominal), EPR extra idler loss (5 % nominal). unc range (r2): props/epr/filter_mismatch_excess varied x0.5-3 (WIDER than default, conservative; Ma et al. 2017; Brown et al., PRD 96, 062003 (2017), from author knowledge, not fetched).

## Citations for varied properties (from author knowledge; not fetched in this task, 0 web fetches)
- Short-cavity round-trip loss ~10-20 ppm: Evans et al., PRD 88, 022002 (2013); Isogai et al., Opt. Express 21, 30114 (2013); Oelker et al., PRL 116, 041102 (2016).
- 300 m-class cavity loss ~50-80 ppm: McCuller et al., PRL 124, 171102 (2020); Zhao et al., PRL 124, 171101 (2020).
- EPR scheme / idler losses: Ma et al., Nat. Phys. 13, 776 (2017); Suedbeck et al., Nat. Photon. 14, 240 (2020); Yap et al., Nat. Photon. 14, 223 (2020).

## Model simplifications (all favour the adopted item or are neutral)
- Adopted (r2): two-photon sideband model of a lossy detuned two-mirror resonator; half-linewidth, detuning and injection angle optimised per draw for the band minimum; only resonator loss and the stated efficiency included; mode mismatch, phase noise and length noise ignored (all favour the adopted item).
- K = (f_SQL/f)^2 (arm bandwidth >> 800 Hz assumed for the K scaling; neutral for the conclusion).

## Post-run change log
- Run 1 used n=400 draws and a 3600-step angle grid for speed; run 2 restored the keylib default n=2000 and a 720-step grid (fixed-angle option is far from threshold, grid resolution irrelevant). No stated numbers changed; result unchanged (PASS).
- Coordinator fix (updated brief v3, 'descriptions never ask a question'): removed the final 'Question: ...' line from NAME, ANON, BASE, CONF1. Requirement line rephrased as an instrument goal not tied to the squeezed-light subsystem: 'at the stated arm power and test-mass mass, the next phase must lower total quantum noise by at least 3 dB at 20 Hz and by at least 3 dB at 800 Hz, relative to the quantum noise of the interferometer with ordinary vacuum entering its output port' (NAME/ANON analogous, without numbers). No stated number changed; BASE and CONF1 still differ only in 400 m -> 8 m. kprobe.json rewritten to the required {"CONF1": {"question", "expected"}} format (same physics question). key.py re-run unchanged: BASE PASS, CONF1 PASS (survivor epr_conditional_squeezing). Forbidden-term check re-run: no adopted/identity matches outside NAME; no '?' in any description.
- Doubt added: with the subsystem no longer singled out, a reader could propose non-squeezing quantum-noise routes (e.g. variational/speed-meter readout); arm power and mass are stated as fixed, but such routes are not coded in the key as survivors or failures.
- Red team r1 fixes (2026-11-06), shared edits applied identically to BASE and CONF1 (still differ only in 400 m -> 8 m):
  - FIX 1: auxiliary-path sentence now absolute: "no longer path exists or can be added at the site". Folding is closed by the new hardware fact below (loss grows with the number of reflections, so loss per unit path is not improved).
  - FIX 2: "arm tubes carry only the main beams" -> "no auxiliary optics or separate auxiliary beam lines can be installed in the 3.6 km arm tubes" (does not exclude the EPR idler, which travels in the main beam).
  - FIX 3: stated total efficiency 85% -> 90% in BASE and CONF1 (logged reason: red team asked to restore EPR margin after adding mismatch). EPR model now adds varied props/epr/filter_mismatch_excess = 0.025 vacuum units (x0.5-2; Ma et al. 2017). EPR nominal 4.39 dB, about 3.5 dB at worst corner (delta 10%, mismatch 0.05).
  - FIX 4: closed the short-cavity low-loss route with a plain hardware fact: "The best attainable loss of any high-reflectivity mirror at this wavelength is 5 ppm per reflection (absorption plus scatter)" (fixed input mirror_loss_floor; exact stated fact). Short-cavity round-trip loss = 2 x 5 ppm + varied excess (5 ppm nominal: rear-mirror transmission, clipping, defects). No unc range used. The adopted-item model now uses the exact relation: total linewidth set by T_in + loss, T_in = 4L*gamma/c - loss (<= 0 means impossible), eps = 2*loss/(T_in + loss) (Kwee et al. 2014). At 8 m, 4L*gamma/c ~ 26 ppm, so eps ~0.96 at the 12.5 ppm draw minimum (0.77 is the value at 10 ppm) [corrected in r2]; adopted fails in 100% of draws.
  - FIX 5: speed-meter/topology routes closed by "the main interferometer topology, arm power and test-mass mass are fixed as stated". Frequency-dependent (variational) output readout would need a similar long low-loss resonator and fails for the same reason; not coded.
  - FIX 6 (scoring definition): the adopted item is squeeze-angle rotation produced by an EXTERNAL detuned filter cavity; EPR/conditional squeezing is a distinct alternative, and a generic "frequency-dependent squeezing" answer without mechanism is ambiguous.
  - FIX 7: kprobe now uses 10-30 ppm round-trip loss and a < 30% criterion; format unchanged.
  - Oelker et al., PRL 116, 041102 (2016) cavity length corrected in key.py comment: 2 m (not 16 m), from author knowledge, not fetched (0 web fetches).
  - key.py re-run: BASE PASS (FD 6.5/8.4 dB), CONF1 PASS (adopted fails 1.000; EPR viable 1.000; 1 survivor). Forbidden-term check re-run: clean. NAME/ANON unchanged (they describe the real baseline).

## Doubts
- (r2) The CONF1 failure rests on the stated project mirror-loss fact. A short cavity with a total round-trip loss of ~4 ppm (2 ppm/reflection, no excess) would marginally meet the band requirement (3.07 dB). A reader who disbelieves the project fact could argue for it, but the stated fact makes the round-trip loss >= 10 ppm.
- (r2) The key places all of the stated efficiency after the resonator. Splitting injection loss before it changes BASE by ~0.2 dB (red team 5.85 vs key 6.08) but does not change any verdict.
- EPR mismatch excess is a single scalar; the real frequency dependence of the mismatch is not modelled.
- EPR survivor credibility: Ma et al. claim the interferometer gives near-ideal frequency dependence for km-scale detectors; the key does not model the residual mismatch of that effective filter or the extra 2nd-readout noise beyond the 5 % idler loss. At delta = 10 % margin is only ~0.2 dB over 3 dB; an added mismatch penalty of a few % of vacuum could make the survivor marginal. A red team may challenge this.
- EPR has only been demonstrated on tabletops, never in a km detector; a domain expert may view it as less mature (maturity is not a physics criterion, but credibility is judged).
- adoption_status "built and operated" is from author knowledge (AdV+ filter cavity used in O4) and was not verified with a fetched source.
- The vertex-space limit is a facility fact; a reviewer could argue it is "infrastructure" rather than physics. It is stated as plain fact and the failure itself is optical-loss physics.

## post-run changes (r2 fixes)
- FIX 1 (decisive; reason: the two-point requirement could be met by a narrowband-tuned 8 m cavity that is 5-11 dB worse than vacuum between 45 and 400 Hz): the requirement in NAME, ANON, BASE and CONF1 now reads "lower total quantum noise by at least 3 dB at every frequency from 20 Hz to 800 Hz, relative to the quantum noise of the interferometer with ordinary vacuum entering its output port". NAME/ANON had the qualitative "below/above the crossover" wording; they now carry the same band requirement. No other stated number changed. BASE and CONF1 still differ only in 400 m -> 8 m (diff checked).
- FIX 2 (reason: the scalar Kwee shortcut fixed gamma = f_SQL/sqrt(2) and checked only two points): key.py rewritten.
  - meets() now uses the band minimum over 25 log-spaced points, 20-800 Hz.
  - fd_improvement uses a two-photon sideband model of a lossy detuned two-mirror resonator. It includes the complex reflection per sideband r(w) = (g_in - g_loss + i(w - Delta)) / (g - i(w - Delta)), the loss vacuum (I - M M^H) and then the stated efficiency 0.90, with readout b2 = c2 - K c1 and K = (f_SQL/f)^2.
  - For every draw it optimises the input-coupling half-width (hence gamma), the detuning and the injection squeeze angle to maximise the band minimum. The search is a coarse vectorised grid (24 x 33 x 36), then multi-start local refinement of the 4 best points (14 rounds of 7x7x7 grids).
  - Lossless check: 8.38 dB flat at gamma = Delta = 39 Hz, equal to the flat source limit. This validates the model.
  - Fixed-angle squeezing and EPR are evaluated against the same band criterion. Fixed-angle and fixed-homodyne results depend only on fixed inputs and are cached.
  - numpy is now used.
  - n = 2000 draws kept (not reduced). The first r2 version (36 x 49 x 72 grid, 6 starts) took ~6 min standalone and timed out under gates.py (900 s limit) on a loaded machine. Speed-up: worst-frequency noise ratio taken before the log, smaller coarse grid, 4 starts. Results agree with the first version within 0.05 dB (e.g. 0.53 -> 0.48 dB at 8 m/10 ppm; a finer brute-force grid gives 0.46). The gates now pass in ~100 s.
- Sanity checks (key_output.txt), compared with the red-team numbers:
  - 400 m at 60 ppm: 6.08 dB band minimum (red team ~5.85);
  - 8 m at the 10 ppm floor: 0.48 dB (red team ~0.41; FAILS);
  - EPR: 4.39 dB flat (matches);
  - fixed angle: -8.97 dB (FAILS).
  - Nominal CONF1 (15 ppm): -0.28 dB.
  - The small differences from the red team probably come from where the loss sits (here all of the stated efficiency is applied after the resonator) and from optimiser resolution.
- FIX 3 (reason: as a world claim the floor is ~2x pessimistic; as a project fact it is exact): in BASE and CONF1, "The best attainable loss of any high-reflectivity mirror at this wavelength is 5 ppm per reflection (absorption plus scatter)." -> "The lowest-loss high-reflectivity mirrors available to this project have 5 ppm loss per reflection (absorption plus scatter)." The change is identical in both. NAME and ANON never had this sentence. The key value is unchanged (fixed mirror_loss_floor = 5 ppm).
  - Robustness note: the red team says a hypothetical 2 ppm/reflection floor still fails. With the 5 ppm excess this key gives 0.78 dB (fails). With 2 ppm/reflection and zero excess (4 ppm round trip) the band minimum is 3.07 dB, marginally passing. The stated project fact (5 ppm) makes the round-trip loss >= 10 ppm, so this is not reachable in CONF1.
- FIX 4 (stale text): corrected in place in the sections above. The design-choices and fixed-inputs entries now give eta = 0.90 (the stale 0.85 is replaced). The workaround text now quotes the r1 arm-tube wording instead of "arm tubes carry only the main beams". In the r1 FIX 4 entry, eps at 12.5 ppm is ~0.96 (0.77 is the value at 10 ppm). The CONF1 mechanism text now quotes the r2 band results.
- Optional fixes, all applied:
  - (a) BASE/CONF1: "the main interferometer topology and its operating point, arm power and test-mass mass are fixed as stated". Reason: this closes detuned signal recycling (operating-point change).
  - (b) EPR filter_mismatch_excess range widened to x0.5-3 via inputs["unc"]. Brown et al., PRD 96, 062003 (2017) is cited in a key comment (author knowledge, not fetched; 0 web fetches). EPR still viable in 1.000 of draws.
  - (c) Added "fixed_homodyne_variational_readout" as a coded alternative: frequency-independent homodyne angle plus fixed squeeze angle, both optimised. Best band minimum is -2.07 dB, so it FAILS in all draws. Variational readout with a frequency-dependent homodyne angle would need an output resonator with the same loss-per-length problem; it is not coded.
- key.py re-run with python -I: BASE PASS (FD 6.08 dB; FI -8.97; fixed-homodyne VR -2.07; EPR 4.39); CONF1 PASS (adopted fails 1.000; >=1 viable 1.000; survivor epr_conditional_squeezing). kprobe.json is unchanged: its question concerns resonator loss/linewidth physics and its 10-30 ppm range is consistent with the project-fact floor (round trip >= 10 ppm). It needs no edit for the new requirement wording.
- gates.py p03_advirgo: GATES PASSED (A forbidden terms ok for all four descriptions; B BASE and CONF1 PASS; C kprobe ok, expected NO).
