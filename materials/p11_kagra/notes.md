# p11_kagra notes: no honest physical conflict found (zero-unit outcome)

Decision taken early (brief lesson 5), before writing descriptions or a key. No descriptions, no key, kprobe.json = {}.

## Item
Optical-lever sensing of marionette pitch/yaw for damping, in any implementation (lesson 1): source/QPD on the floor, on an
isolated bench, on the suspended recoil cage, or fibre-fed inside the cryostat. Alternative: improved photo-sensors.

## Mechanisms screened (each must defeat every variant robustly under x0.5-2, without a routine add-on)
1. Ground-motion / ground-tilt coupling of the lever's reference. Fails lesson 1: the same lever mounted on the suspended
   recoil cage (the photo-sensors' own reference) or on an isolated bench shares the survivor's reference. Also lesson 4:
   below the damped resonances a high-pass in the damping filter removes floor tilt/wind injection.
2. Sensing noise vs an angular-noise requirement in the GW band. Fails lesson 4: damping-loop low-pass filtering above the
   pitch/yaw resonances is routine; inside the control band, oplev and photo-sensor noise floors (~1e-10 to 1e-9 rad/rtHz
   order, memory) overlap within x0.5-2, so no robust separation.
3. Short lever arm forced by cage-mounted geometry. Lever noise ~ spot noise / 2L is comparable to a photo-sensor pair's
   displacement noise / baseline for L ~ baseline; separation not robust under x0.5-2 and narrowing to one geometry.
4. Radiative heat load through shield apertures for the beam. Fails lessons 1 and 4: cold IR-absorbing windows, or an
   in-cryostat fibre-fed lever, remove it. Photo-reflective sensors themselves dissipate LED power inside the cryostat,
   so heat favours the item, not the alternative.
5. Absorbed lever-beam power / photon-pressure noise on the cold marionette: ~uW absorbed, force noise ~1e-16 N/rtHz;
   negligible against any credible budget, and lower than the alternative's LED dissipation.
6. Stray light of the lever wavelength into the main readout: dichroic filtering is routine (lesson 4).

## Conclusion
No physical requirement separates optical-lever sensing (as such) from improved photo-sensors robustly under x0.5-2
without either narrowing to one configuration (lesson 1) or being defeated by a routine filter/window (lesson 4).
Reported as an honest zero-unit pair (brief rule: acceptable outcome).

## Fixed inputs / unc ranges
None (no key written).

## Post-run change log
None.

## Doubts
- adoption_status is from memory (unverified); no web fetches used.
- A conflict might exist for a sub-kelvin payload where any optical access is excluded, but that leaves the instrument class
  and would still be met by in-cryostat variants; not pursued.
