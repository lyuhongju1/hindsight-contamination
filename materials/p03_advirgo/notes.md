# Notes: p03_advirgo

## Design choices
- Adopted item: frequency-dependent squeezing via an external detuned high-finesse resonator (AdV+ Phase I). Descriptions avoid the forbidden terms and do not name or rule out any technology class.
- BASE: invented 3.6 km dual-recycled interferometer, 55 kg masses, quantum-noise crossover 55 Hz, 13 dB source, 85 % total efficiency, 400 m auxiliary evacuated path. Requirement: >= 3 dB quantum-noise reduction at 20 Hz and at 800 Hz.
- CONF1 (minimal edit, one number): auxiliary path 400 m -> 8 m. Mechanism: the resonator must have half-linewidth ~ f_SQL/sqrt(2) ~ 39 Hz; at 8 m this needs input transmission ~ 26 ppm, comparable to the round-trip loss, so the low-frequency squeezing is almost fully decohered (eps = 2 Lambda^2 / T, clamped at 1). Adopted reaches 0 dB at 20 Hz nominally, <= 1.8 dB even at the most favourable loss (7.5 ppm) and ideal angle; requirement is 3 dB.
- Fixed-angle squeezing fails in both BASE and CONF1 (any single angle anti-squeezes one of the two bands; best min over bands -8.8 dB).
- Survivor: EPR/conditional squeezing, which uses the 3.6 km interferometer itself as the frequency-dependent element for the detuned idler; needs no long auxiliary resonator. Conditional variance with 13 dB two-mode source, eta_signal 0.85, eta_idler 0.85*(1-delta): 3.66 dB nominal; ~3.2 dB at delta = 10 %.
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

## Doubts
- EPR survivor credibility: Ma et al. claim the interferometer gives near-ideal frequency dependence for km-scale detectors; the key does not model the residual mismatch of that effective filter or the extra 2nd-readout noise beyond the 5 % idler loss. At delta = 10 % margin is only ~0.2 dB over 3 dB; an added mismatch penalty of a few % of vacuum could make the survivor marginal. A red team may challenge this.
- EPR has only been demonstrated on tabletops, never in a km detector; a domain expert may view it as less mature (maturity is not a physics criterion, but credibility is judged).
- adoption_status "built and operated" is from author knowledge (AdV+ filter cavity used in O4) and was not verified with a fetched source.
- The vertex-space limit is a facility fact; a reviewer could argue it is "infrastructure" rather than physics. It is stated as plain fact and the failure itself is optical-loss physics.
