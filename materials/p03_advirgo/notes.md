# Notes: p03_advirgo

## Design choices
- Adopted item: frequency-dependent squeezing via an external detuned high-finesse resonator (AdV+ Phase I). Descriptions avoid the forbidden terms and do not name or rule out any technology class.
- BASE: invented 3.6 km dual-recycled interferometer, 55 kg masses, quantum-noise crossover 55 Hz, 13 dB source, 90 % total efficiency (85 % before r1), 400 m auxiliary evacuated path. Requirement: >= 3 dB quantum-noise reduction at 20 Hz and at 800 Hz.
- CONF1 (minimal edit, one number): auxiliary path 400 m -> 8 m. Mechanism: the resonator must have half-linewidth ~ f_SQL/sqrt(2) ~ 39 Hz; at 8 m this needs input transmission ~ 26 ppm, comparable to the round-trip loss, so the low-frequency squeezing is almost fully decohered (eps = 2 Lambda^2 / T, clamped at 1). Adopted reaches 0 dB at 20 Hz nominally, <= 1.8 dB even at the most favourable loss (7.5 ppm) and ideal angle; requirement is 3 dB.
- Fixed-angle squeezing fails in both BASE and CONF1 (any single angle anti-squeezes one of the two bands; best min over bands -8.8 dB).
- Survivor: EPR/conditional squeezing, which uses the 3.6 km interferometer itself as the frequency-dependent element for the detuned idler; needs no long auxiliary resonator. Conditional variance with 13 dB two-mode source, eta_signal 0.90, eta_idler 0.90*(1-delta), plus mismatch excess (r1): 4.39 dB nominal; ~3.5 dB at worst corner.
- Workaround routes closed by plain fact: arm tubes carry only the main beams (no auxiliary resonator in the 3.6 km tubes); arm power and test-mass mass fixed as stated (no moving the crossover out of band). Folding the 8 m resonator does not help: round-trip loss grows ~ with the number of reflections as the path grows, so loss per unit path (the figure of merit) is unchanged or worse.
- Coherence (rule 7): the edited number only concerns the vertex auxiliary space; nothing else in the instrument depends on it. 8 m of straight vacuum at a vertex station is realistic.

## Survivors per CONF
- CONF1: 1 (epr_conditional_squeezing).

## Fixed inputs (inputs["fixed"]) and justification
- f_sql_Hz = 55, src_dB = 13, eta = 0.85, L_aux_m = 400 / 8, f_low = 20 Hz, f_high = 800 Hz, req_dB = 3: all are exact numbers stated in the description (instrument facts and the requirement), not cited properties.
- Varied x0.5-2: round-trip loss short (15 ppm nominal), long (60 ppm nominal), EPR extra idler loss (5 % nominal). No unc ranges used.

## Citations for varied properties (from author knowledge; not fetched in this task, 0 web fetches)
- Short-cavity round-trip loss ~10-20 ppm: Evans et al., PRD 88, 022002 (2013); Isogai et al., Opt. Express 21, 30114 (2013); Oelker et al., PRL 116, 041102 (2016).
- 300 m-class cavity loss ~50-80 ppm: McCuller et al., PRL 124, 171102 (2020); Zhao et al., PRL 124, 171101 (2020).
- EPR scheme / idler losses: Ma et al., Nat. Phys. 13, 776 (2017); Suedbeck et al., Nat. Photon. 14, 240 (2020); Yap et al., Nat. Photon. 14, 223 (2020).

## Model simplifications (all favour the adopted item or are neutral)
- Adopted: ideal squeeze angle assumed at 20 Hz; only resonator decoherence and stated efficiency included; dispersion/mode-mismatch/phase-noise ignored.
- K = (f_SQL/f)^2 (arm bandwidth >> 800 Hz assumed for the K scaling; neutral for the conclusion).

## Post-run change log
- Run 1 used n=400 draws and a 3600-step angle grid for speed; run 2 restored the keylib default n=2000 and a 720-step grid (fixed-angle option is far from threshold, grid resolution irrelevant). No stated numbers changed; result unchanged (PASS).
- Coordinator fix (updated brief v3, 'descriptions never ask a question'): removed the final 'Question: ...' line from NAME, ANON, BASE, CONF1. Requirement line rephrased as an instrument goal not tied to the squeezed-light subsystem: 'at the stated arm power and test-mass mass, the next phase must lower total quantum noise by at least 3 dB at 20 Hz and by at least 3 dB at 800 Hz, relative to the quantum noise of the interferometer with ordinary vacuum entering its output port' (NAME/ANON analogous, without numbers). No stated number changed; BASE and CONF1 still differ only in 400 m -> 8 m. kprobe.json rewritten to the required {"CONF1": {"question", "expected"}} format (same physics question). key.py re-run unchanged: BASE PASS, CONF1 PASS (survivor epr_conditional_squeezing). Forbidden-term check re-run: no adopted/identity matches outside NAME; no '?' in any description.
- Doubt added: with the subsystem no longer singled out, a reader could propose non-squeezing quantum-noise routes (e.g. variational/speed-meter readout); arm power and mass are stated as fixed, but such routes are not coded in the key as survivors or failures.
- Red team r1 fixes (2026-11-06), shared edits applied identically to BASE and CONF1 (still differ only in 400 m -> 8 m):
  - FIX 1: auxiliary-path sentence now absolute: "no longer path exists or can be added at the site". Folding is closed by the new hardware fact below (loss grows with the number of reflections, so loss per unit path is not improved).
  - FIX 2: "arm tubes carry only the main beams" -> "no auxiliary optics or separate auxiliary beam lines can be installed in the 3.6 km arm tubes" (does not exclude the EPR idler, which travels in the main beam).
  - FIX 3: stated total efficiency 85% -> 90% in BASE and CONF1 (logged reason: red team asked to restore EPR margin after adding mismatch). EPR model now adds varied props/epr/filter_mismatch_excess = 0.025 vacuum units (x0.5-2; Ma et al. 2017). EPR nominal 4.39 dB, about 3.5 dB at worst corner (delta 10%, mismatch 0.05).
  - FIX 4: closed the short-cavity low-loss route with a plain hardware fact: "The best attainable loss of any high-reflectivity mirror at this wavelength is 5 ppm per reflection (absorption plus scatter)" (fixed input mirror_loss_floor; exact stated fact). Short-cavity round-trip loss = 2 x 5 ppm + varied excess (5 ppm nominal: rear-mirror transmission, clipping, defects). No unc range used. The adopted-item model now uses the exact relation: total linewidth set by T_in + loss, T_in = 4L*gamma/c - loss (<= 0 means impossible), eps = 2*loss/(T_in + loss) (Kwee et al. 2014). At 8 m, 4L*gamma/c ~ 26 ppm, so eps >= ~0.77 even at the 12.5 ppm minimum; adopted fails in 100% of draws.
  - FIX 5: speed-meter/topology routes closed by "the main interferometer topology, arm power and test-mass mass are fixed as stated". Frequency-dependent (variational) output readout would need a similar long low-loss resonator and fails for the same reason; not coded.
  - FIX 6 (scoring definition): the adopted item is squeeze-angle rotation produced by an EXTERNAL detuned filter cavity; EPR/conditional squeezing is a distinct alternative, and a generic "frequency-dependent squeezing" answer without mechanism is ambiguous.
  - FIX 7: kprobe now uses 10-30 ppm round-trip loss and a < 30% criterion; format unchanged.
  - Oelker et al., PRL 116, 041102 (2016) cavity length corrected in key.py comment: 2 m (not 16 m), from author knowledge, not fetched (0 web fetches).
  - key.py re-run: BASE PASS (FD 6.5/8.4 dB), CONF1 PASS (adopted fails 1.000; EPR viable 1.000; 1 survivor). Forbidden-term check re-run: clean. NAME/ANON unchanged (they describe the real baseline).

## Doubts
- EPR mismatch excess is a single scalar; the real frequency dependence of the mismatch is not modelled.
- EPR survivor credibility: Ma et al. claim the interferometer gives near-ideal frequency dependence for km-scale detectors; the key does not model the residual mismatch of that effective filter or the extra 2nd-readout noise beyond the 5 % idler loss. At delta = 10 % margin is only ~0.2 dB over 3 dB; an added mismatch penalty of a few % of vacuum could make the survivor marginal. A red team may challenge this.
- EPR has only been demonstrated on tabletops, never in a km detector; a domain expert may view it as less mature (maturity is not a physics criterion, but credibility is judged).
- adoption_status "built and operated" is from author knowledge (AdV+ filter cavity used in O4) and was not verified with a fetched source.
- The vertex-space limit is a facility fact; a reviewer could argue it is "infrastructure" rather than physics. It is stated as plain fact and the failure itself is optical-loss physics.

## post-run changes (r2 fixes)
- (in progress) Red team r2 FIX 1, 3 and optional topology wording applied to descriptions; key rewrite pending.
