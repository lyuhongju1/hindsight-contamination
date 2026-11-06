# Screening brief: baseline papers (pair_selection_rules.md, criterion I1 and field)

You screen INSPIRE records for whether each is a **baseline instrument paper**. Decide from the metadata only (title, collaboration, journal, report numbers, date). Do not search the web.

**I1 = Y** if the record is a paper describing a **constructed detector or instrument as built**: its design, construction, commissioning, or performance as a whole system. Typical titles: "The X detector", "The X experiment" (instrument description), "Design and performance of the X detector", "The X observatory".

**I1 = N** if it is any of:
- a physics-results paper;
- a subsystem-only paper (one calorimeter, one readout chip, one electronics board), unless the subsystem is itself the whole instrument;
- an R&D or prototype study;
- a software, simulation or calibration paper;
- a review;
- a design report for something not yet built;
- an upgrade proposal.

**Field**, for I1 = Y only, one of:
- `collider` (collider and fixed-target HEP)
- `nu_accel` (accelerator and reactor neutrino)
- `nu_natural` (natural-source neutrino: solar, atmospheric, astrophysical)
- `dark_matter`
- `double_beta`
- `grav_waves`
- `astroparticle` (cosmic-ray and gamma-ray)
- `precision` (precision and low-energy)
- `other`

**Output.** Text only, one line per record, in the order given:

`recid | Y or N | field (or -) | <=10-word reason`

At the end, give the counts. Do not write files. Do not open any other project file. If a tool is denied, do not work around it; report it.
