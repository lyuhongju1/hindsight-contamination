# Red team r3: p03_advirgo (2026-11-06). Verdict: CLEARED (no FIX)

**Blind answers:** they agree with the key. BASE: a ~400 m filter cavity, ~6 dB across the band. CONF1: EPR survives (~4 dB flat); an 8 m cavity fails (loss half-width ≥15 Hz against the ~39 Hz needed).

**Checks:**
- All r2 FIXes are OK.
- Independent sanity numbers match the key: loss half-width 1.79 Hz at 400 m/60 ppm and 22.4 Hz at 8 m/15 ppm; lossless 8.38 dB.
- The 5 ppm project fact is plain, identical in both levels and credible; it closes the author's 4 ppm doubt. That case clears 3 dB by only 0.07 dB even with zero excess loss, before mismatch or phase noise.

**Routes closed:**
- cascaded or coupled cavities: storage time × loss per unit path;
- folded, ring or delay-line cavities, and end stations: the 5 ppm fact plus the site sentence;
- in-arm beam lines;
- detuned signal recycling and speed meters: the operating-point sentence;
- mirrorless resonators: physics (Q ≈ 3.6e12 needed);
- arm-as-filter: this is the EPR survivor.

**kprobe:** consistent.

**Residual doubts (logged):** EPR is ~0.2 dB above 3 dB at the worst corner; EPR has not been demonstrated at km scale.
