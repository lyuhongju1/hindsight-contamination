# p03_advirgo: negative-control notes (NC1)

*2026-11-07. Outcome: **NC-zero**. No NC_CONF.txt, nc_key.py or nc_kprobe.json was written. The reasons follow. 0 web fetches.*

## alt(u)
**EPR / conditional squeezing.** A two-mode (signal + idler) entangled squeezed source is used. The idler is offset in frequency so that the 3.6 km interferometer itself acts as the detuned frequency-dependent element. Signal and idler are read out separately, and the signal readout is conditioned on the idler readout.
- It is the documented non-adopted alternative (dossier/notes; RUBRIC code D lists it first).
- It is the only coded survivor of the main CONF1. The main key gives 4.39 dB flat at nominal and ~3.5 dB at the worst corner, against a 3 dB requirement. The external detuned resonator gives -0.28 dB at 8 m and 15 ppm.

## What an NC edit must do (keylib)
One added sentence or set of numbers must:
- make EPR fail in >= 95% of x0.5-2 draws;
- keep the external resonator failing (it does, because the 8 m / 5 ppm facts are untouched);
- leave a third option meeting >= 3 dB at every frequency from 20 to 800 Hz in >= 95% of draws.

## Killing EPR is easy
The main key's EPR model shows EPR has little margin. Values below are the band-flat improvement in dB:

| idler extra loss | mismatch 0.025 | mismatch 0.075 |
|---|---|---|
| 0.05 | 4.39 | 3.83 |
| 0.10 | 3.78 | 3.29 |
| 0.20 | 2.61 | 2.23 |
| 0.30 | 1.49 | 1.20 |
| 0.40 | 0.39 | 0.16 |

At a stated total efficiency of 0.80, EPR gives 2.62 dB, and at 0.70 it gives 1.38 dB.

So a plain fact would kill EPR robustly. Examples: a stated idler-path or second-readout efficiency of <= ~70%; a stated limit on the interferometer's response at the idler offset; a stated total efficiency of ~0.70.

## No third option survives (the blocking problem)
CONF1 fixes the topology, operating point, arm power and test-mass mass. It also limits the auxiliary path to 8 m with >= 5 ppm loss per reflection, and it forbids optics in the arm tubes. Under these facts, a reduction of >= 3 dB at every frequency from 20 to 800 Hz needs a quadrature (squeeze angle or readout angle) that rotates by ~80 deg between 20 Hz (K = 7.6) and 800 Hz (K ~ 0.005). Only two things can supply that rotation:
- (a) a long, low-loss auxiliary resonator, either on the input (the adopted item) or on the output. This is closed by 8 m x 5 ppm: the loss per unit length is fixed, and folding does not help.
- (b) the 3.6 km interferometer itself, reached through an entangled idler. This is alt(u).

Candidates checked:
1. **Fixed-angle squeezing.** Key result: -8.97 dB. Analytic bound: a single pure ellipse cannot give V <= 0.5 in two quadratures ~82 deg apart (best is ~0.99 at the 41/41 split, at any squeeze level). It fails for every source level and every efficiency.
2. **Frequency-independent variational readout plus fixed squeezing.** Key result: -2.07 dB. It fails.
3. **Frequency-dependent variational readout.** It needs an output resonator of the same kind (route a). It is closed by 8 m x 5 ppm, and it is worse than the input side because loss after the signal degrades the signal itself.
4. **Speed meter, detuned signal recycling / optical spring, more arm power or heavier masses.** All are closed by "the main interferometer topology and its operating point, arm power and test-mass mass are fixed as stated".
5. **Resonator in the arm tubes, longer vertex path, or a folded 8 m path.** All are closed by stated facts. Folding does not change the loss per length.
6. **Negative-mass (atomic spin) back-action cancellation.** These schemes (Khalili & Polzik 2018; Zeuthen et al. 2019) use entangled two-colour light with a second, conditional readout, so any edit that kills EPR through the idler/second readout also kills them. They are also not credible at 20-55 Hz for a km detector: they have been demonstrated only at kHz-MHz, and wavelength conversion to the atomic line would be needed. They fail the "credible third option" bar.

Any EPR-killing fact therefore leaves zero survivors. Reopening a third option would need a second edit that relaxes a CONF1 fact: a longer path, lower mirror loss, or freedom in topology or operating point. That breaks the "one minimal edit" rule. It would also revive the adopted item (path/loss) or add a non-historical option by construction.

An edit that targets something specific to EPR (e.g. the offset-frequency response of the interferometer) does not change this. It still leaves only options 1-6, all of which fail.

## Fixed inputs used (from the main key, unchanged)
- f_SQL = 55 Hz; source 13 dB; eta = 0.90; 5 ppm per reflection; L_aux = 8 m; band 20-800 Hz; requirement 3 dB.
- EPR props: idler_extra_loss 0.05 and filter_mismatch_excess 0.025 (both nominal).
- Numbers come from the functions of materials/p03_advirgo/keys/key.py, imported via python -I (fi, vr and epr only; key.py's main was not run).

## Doubts
- A reader could invent an option not covered here (e.g. a quantum-nondemolition or intracavity scheme needing new optics inside the main interferometer). These are closed by the fixed-topology clause.
- If the study accepted relaxing a CONF1 fact as part of the NC edit, an NC_CONF could be built. A possible design: kill EPR with a stated idler-path efficiency of ~0.6, and allow an ~80-100 m auxiliary path while keeping the adopted item failing. That fails, though, because a longer path revives the adopted item itself. So NC-zero is the honest outcome.

## DIFF
None (NC-zero): CONF1 -> no NC_CONF.
