# Candidate pending decisions for the prospective registry (design v2 §7)

> **Read first.**
> - This list was compiled on 2026-11-05 by a language model (Claude Opus 5.5) from web search results. That model is also a **study model**, so the list carries the selection bias described in `pair_selection_rules.md` §0.
> - **A human must verify every entry** against primary collaboration sources before registration.
> - The **final registry list must be chosen by a frozen rule** (search sources, inclusion criteria, random draw where needed), not taken from this list alone.
> - The search summaries used here were produced by a fetch model and can misread documents. Treat the quoted statuses as leads to check.
> - **Status key:**
>   - **Confirmed pending:** a dated source from late 2025 or 2026 describes the decision as open.
>   - **Status unverified:** the newest dated source found is older than that, or is ambiguous.
> - **Type key:**
>   - **H:** hardware or technology choice (preferred for the hindsight design).
>   - **P:** programmatic (site, geometry or funding). Useful for a forecasting registry but not a technology answer key.

## Confirmed pending (7)

| # | Decision | Type | Publicly listed options | Expected decision | Status evidence (dated) |
|---|---|---|---|---|---|
| 1 | **Einstein Telescope geometry** | P/H | Single 10 km triangle vs two 15 km L-shaped detectors ("2L") | Second half of 2027 (INFN); one press piece says early 2027 | Geometry Comparison Report submitted to the ET Board of Governmental Representatives on 2026-10-07, with **no preferred geometry** (https://www.infn.it/en/triangle-or-2l-for-einstein-telescope-comparative-report-on-configurations-submitted/ ; https://www.einstein-telescope.it/en/2026/10/09/triangular-or-double-l-configuration-for-einstein-telescope-geometry-comparison-report-submitted/ ; https://www.ifae.es/news/2026/10/14/over-200-experts-contribute-to-einstein-telescope-geometry-comparison-report/) |
| 2 | **Einstein Telescope site** | P | Euregio Meuse-Rhine (BE/NL/DE); Sardinia (Sos Enattos); Saxony (Lusatia). Under 2L, two of the three | 2027; bid books due by end of 2026 | June 2026 report on the Euregio bid (https://newmobility.news/en/2026/06/09/belgian-rail-site-puts-euregios-einstein-telescope-bid-on-track/); FAQ (https://www.einsteintelescope-emr.eu/en/faq/); 2026-11-03 press item still calls it upcoming (https://www.techtimes.com/articles/329997/20261103/einstein-telescope-report-two-nation-design-locates-gravitational-wave-sources-100x-more-precisely.htm) |
| 3 | **DUNE FD3 charge readout** | H | Reference: vertical-drift LArTPC with strip charge-readout planes (as FD2). Option: pixel readout (LArPix/Q-Pix family) | "FD3 (decision 2027)" on a DUNE slide | DUNE overview talk, autumn 2026 (https://indico.cern.ch/event/1712218/contributions/7202023/attachments/3346160/5998562/NFPT_DUNE_BBilki_v2.pdf); Phase II paper arXiv:2503.23293 (2025-03). Check the talk date on Indico |
| 4 | **LIGO A♯ test-mass coating** | H | Titania-doped tantala (improved deposition); crystalline GaAs/AlGaAs; amorphous silicon (possibly hydrogenated); target about 2× below A+ | Not stated | arXiv:2608.11673 (2026-08), "LIGO A♯: Detector Design and Science Prospects Beyond A+", treats the reduction as a design assumption with several candidates (https://arxiv.org/pdf/2608.11673) |
| 5 | **Cosmic Explorer site** | P | Long list of about 26 candidate US locations for a 40 km detector | Long-list report to NSF in autumn 2026; short list about 2028; NSF makes the final choice | arXiv:2509.05430 (2025-09) (https://arxiv.org/html/2509.05430v1); CE DCC P2500002 |
| 6 | **FCC-ee detector concepts** | H | CLD, IDEA, ALLEGRO, ILD, ALFA, AGORA (six concepts) | Target of ≥ 4 expressions of interest by Q1–Q2 2028; approval about 2030 | IHEP talk, 2026-09-21 (https://indico.ihep.ac.cn/event/30546/contributions/231189/attachments/106963/144939/20260921-AGORA_at_FCC-ee_CEPC-day.pdf); FCC Feasibility Study Vol. 1, arXiv:2505.00272 |
| 7 | **nEXO 2.0 go-ahead at SNOLAB** | P | Canadian-led nEXO 2.0 at SNOLAB vs no near-term construction (DOE stepped back in December 2024) | Not stated; an older SNOLAB goal was construction start 2026–27 | Canadian NP long-range plan arXiv:2602.22464 (2026-02) recommends it as not yet realized (https://arxiv.org/pdf/2602.22464) |

## Status unverified (7)

| # | Decision | Type | Listed options | Newest dated evidence | What to check |
|---|---|---|---|---|---|
| 8 | **DUNE FD4 technology** | H | Vertical-drift LArTPC variant (reference); Theia water-based liquid scintillator (alternative); pixel / Q-Pix readout | ESPPU input, arXiv:2503.23291 and 2503.23293 (2025-03): decisions "no later than" 2027 (FD3) and 2028 (FD4) | Newer DUNE Phase II statements |
| 9 | **XLZD photosensor** | H | 3-inch PMTs (Design Book baseline, 1182 PMTs) vs SiPMs (R&D, e.g. Xenoscope) | XLZD Design Book, EPJC 2025 (arXiv:2410.17137) gives a PMT **baseline**. A 2024 talk lists the photosensor choice as open | Whether the baseline is final. If the PMT baseline is treated as committed, drop this entry |
| 10 | **LHCb Upgrade II RICH photodetector** | H | SiPMs (cooled), LAPPD / MCP-PMTs, CMOS SPADs; MaPMTs as low-occupancy backup | 2025 talks: R&D ongoing, with a TDR deadline of Q2 2026 that R&D may overrun | Whether a RICH TDR has appeared on CDS / LHCC |
| 11 | **LHCb Upgrade II Mighty Tracker and PicoCal readout** | H | Mighty Tracker: DMAPS inner, SciFi outer (layout and sensor details open). PicoCal: SpaCal + Shashlik, readout ASIC under development | Scoping document says all TDRs by end of 2026; JINST 21 C04057 (2026) says the readout is still in development | Whether the TDRs were submitted before freeze. Register before they appear, or drop |
| 12 | **IceCube-Gen2 optical module** | H | LOM-16, LOM-18, mEgg (multi-PMT designs) | 2025 Münster PhD thesis says Gen2 is "less clear"; 2025 WIPAC LOM-16 prototype tests | Gen2 TDR or collaboration statement |
| 13 | **ET low-frequency interferometer test mass and wavelength** | H | Silicon at 1550 nm (baseline since the 2020 design report) vs about 2 µm; sapphire mentioned | Design Report Update 2020; Glasgow facility proceedings (date unclear) | Whether the ET technical design treats Si/1550 nm as settled. If so, drop |
| 14 | **Hyper-K second tank in Korea** | P | Korea (about 1100 km baseline) vs a second tank in Japan vs none | 2018 PTEP studies; no recent decision found | Current Hyper-K and Korean funding statements |

## Checked and excluded (decision already made or effectively made)

| Decision | Reason for exclusion |
|---|---|
| CUPID light-detector technology | Neganov–Trofimov–Luke Ge light detectors adopted as baseline. A Neutrino 2026 poster calls them "the baseline technology"; the crystal choice (Li₂¹⁰⁰MoO₄) was made in 2018 |
| LEGEND-1000 site | LNGS Hall C is the construction plan (a 2025 proceedings paper puts the construction start in early 2027), and the DOE CD-1 review passed in November 2025. SNOLAB was formally carried as an alternative through CD-1, so check whether final CD-1 approval names the site. If it remains formally open, it could move to "unverified" |

## Notes for the frozen selection rule

- **Prefer H-type decisions.** The hindsight design scores technology choices against a later answer key. P-type decisions (sites, geometry) suit a general forecasting registry but are not upgrade proposals.
- **Decisions due soonest are the most valuable**, because they score first: LHCb Upgrade II TDRs (late 2026), DUNE FD3 (2027), ET geometry and site (2027).
- **Register LHCb entries immediately or not at all.** They are near-term, so verify that no TDR is public at the registration timestamp.
- **For each entry, freeze before sampling:**
  - the option set;
  - the scoring rule, i.e. which public document counts as the decision (collaboration paper, TDR, or funding-agency record);
  - a "no decision by date X" outcome.
