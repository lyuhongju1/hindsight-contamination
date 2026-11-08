# Feasibility q60: DANSS upgrade (arXiv:2112.04973), feasibility check only (lesson 5)

Source check: the arXiv abstract confirms a 1 m3 plastic detector, a new strip design, a goal of 12% at 1 MeV (sigma, as quoted), more than twice the light output, and timing along the strip. It gives no Gd or 6Li details. The film and strip specifications come from the candidate row and have not been checked here.

## Item 2 (Gd in a separate Gd2O3 film; the item is read as Gd capture tagging in ANY implementation)

- Route A, containment plus ambient-gamma accidentals: WINDOW (conditional; this is the only viable route). Mechanism: the compact segmented plastic volume is a stated instrument fact under `fixed` (about 20-30 cm per side, roughly 10-30 L, which is coherent for a near-field monitor at about 10 m from a GW-scale core: about 100+ IBD/day before efficiency). Gd capture gives an 8 MeV cascade of 3-4 gammas of about 1-3 MeV each. The interaction length for 2 MeV gammas in plastic is about 22 cm, so most of the cascade escapes, and the deposited delayed energy falls mostly below 2.5-3 MeV, the same range as 40K (1.46 MeV), n-H (2.2 MeV) and 208Tl (2.6 MeV; Compton edge 2.38 MeV). Gd therefore has two options:
  - (i) Threshold above about 2.6 MeV: estimated efficiency is about 10-20% (upper bound about 25-30% if every cited property is set to x2), against a stated requirement of 40% or more.
  - (ii) Threshold of about 1 MeV: efficiency is about 50%, but the delayed singles rate equals the ambient gamma rate (stated, about 10^2 Hz). Accidentals are R_p * R_d * dt with dt about 50-100 us. That is roughly 10^2 times the 6Li case, against a stated accidental/signal limit.

  The factor of about 10^2 should survive x0.5-2 on the gamma rate, the singles rate, the capture time and the gamma attenuation together (at worst x8). Multiplicity and topology cuts (settings) cut efficiency further in a small volume.

  Survivor: 6Li-doped PSD plastic (LLNL/SANDD type), or 6LiF:ZnS sheets (SoLid type) read through the same WLS fibres and SiPMs. Q = 4.78 MeV goes to alpha+triton, deposited in about 10 um, so it is fully contained and position-local. It gives about 0.4-0.6 MeVee in PSD plastic, and the ZnS pulse is microseconds long. Both are identified by pulse shape on waveform digitizers the baseline already has (DANSS uses flash ADCs), so PSD is a setting, not an add-on. The neutron-like singles rate stays about 1-10 Hz, even with a capture time of about 40-80 us.

  Why Gd settings fail: the threshold, windows and topology cuts are all settings within the item, and every one of them either loses efficiency or admits gamma singles. Extra shielding is a separate add-on (C1: it scores C and the conflict stands). It also leaves internal and n-H gammas in place. A no-space rule must NOT be used.

  Risks:
  - The Gd efficiency at a 2.6 MeV threshold in a 25 cm cube needs a quick MC or literature figure before authoring (the main open number).
  - The 6Li neutron escape from a small volume also hits the survivor's efficiency, so the requirement must be set at a level 6Li meets (about 40-50% overall is plausible).
  - Recognition: small 6Li reactor monitors are well known.
- Route B, delayed vertex localization (6Li capture point within a few cm; the Gd cascade centroid is smeared over about 10-20 cm): NO WINDOW alone. A resolution requirement is a narrow performance spec and fragile under x0.5-2, because neutron diffusion of about 5-10 cm dominates both. Usable only as a supporting fact.
- Route C, capture time: NO WINDOW. Gd is faster (about 10-30 us in Gd plastic vs 40-80 us for 6Li), so this favours the item.
- Route D, pulse-shape ID of alpha+triton: NO WINDOW as a standalone requirement (stating it would narrow the choice to a method). It is the mechanism that lets the survivor pass Route A.
- Route E, containment versus a stated tagging efficiency with no background statement: NO WINDOW. A 1 MeV threshold (a setting) gives Gd about 50%, which is not robustly below a requirement 6Li also meets.
- Route F, correlated background (fast-neutron recoil plus capture): NO WINDOW. It hits both captures equally; only the prompt-side PSD differs, and that is independent of the delayed capture nucleus.

Verdict, item 2: WINDOW. Route A only (compact stated volume, Gd cascade escape, ambient gamma singles, accidental-rate limit plus delayed-efficiency limit). It is conditional on an MC check of Gd efficiency above 2.6 MeV in about 25 cm of plastic.

## Item 1 (2 cm x 5 cm strips, 8 WLS fibres, two-sided SiPM readout)

- Route, granularity or topology requirement (stated maximum segment size, or annihilation-gamma topology): NO WINDOW. The requirement would be a design fiat on segment size, and fibre count and readout are settings that restore resolution.
- Route, light yield or energy resolution: NO WINDOW. The item improves it (more than 2x light, goal 12% sigma at 1 MeV).
- Route, dead material or pile-up: NO WINDOW. The effects are small and shared with the alternatives.

Verdict, item 1: NO WINDOW.
