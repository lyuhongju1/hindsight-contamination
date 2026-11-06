"""r1 scan for p07_meg (N3): can any field profile / acceptance close every downstream on-axis RDC placement?
Run: python -I r1_scan.py   (standard library only; paraxial solenoid field, Boris pusher)
For each scenario, for disks on the axis at plane z with radius R, compute
  fR = fraction of all RMD low-energy e+ (isotropic, p 1.4-5.5 MeV/c) whose FIRST crossing of plane z is at r<R,
  fS = fraction of ACCEPTED signal events whose e+ (52.8 MeV/c, traced) or photon (straight) crosses plane z at r<R,
  fM = fraction of all Michel e+ crossing plane z at r<R (random-veto rate for a thin timing-only disk).
Beam spot: gaussian sigma 1 cm (unstated in BASE; typical surface beam)."""
import math, random
C = 0.299792458  # GeV/c per T per m
def field(prof):
    def Bz(z):
        if prof == "conf1":      # 0.5 T to 5 cm, linear to 2.0 T at 20 cm
            return 0.5 if z < 0.05 else (2.0 if z > 0.20 else 0.5 + 1.5 * (z - 0.05) / 0.15)
        if prof == "attarget":   # rise starts at the target: 0.5 T at z=0, 2.0 T at 15 cm
            return 0.5 if z < 0 else (2.0 if z > 0.15 else 0.5 + 1.5 * z / 0.15)
    def dBz(z, h=1e-4): return (Bz(z + h) - Bz(z - h)) / (2 * h)
    return Bz, dBz
PLANES = [0.002, 0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12, 0.2, 0.4, 1.2]
RADII = [0.005, 0.01, 0.015, 0.02, 0.03, 0.04, 0.05, 0.07, 0.10, 0.15]
def trace(p, th, ph, x0, y0, prof, zmax=1.25, smax=3.0):
    """returns {plane: r at first crossing} for a positive particle of momentum p (GeV/c)."""
    Bz, dBz = field(prof)
    u = [math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)]
    x, y, z = x0, y0, 0.0; out = {}; s = 0.0
    while s < smax and -0.3 < z < zmax and len(out) < len(PLANES):
        b = Bz(z); k = C * b / p
        ds = min(0.002, 0.15 / max(k, 1e-6))
        g = dBz(z); bx, by, bz = -0.5 * x * g, -0.5 * y * g, b
        # rotate u about B by angle -(C|B|/p) ds  (positive charge)
        Bm = math.sqrt(bx * bx + by * by + bz * bz); a = -C * Bm / p * ds
        nx, ny, nz = bx / Bm, by / Bm, bz / Bm
        ca, sa = math.cos(a), math.sin(a); d = u[0] * nx + u[1] * ny + u[2] * nz
        cx, cy, cz = ny * u[2] - nz * u[1], nz * u[0] - nx * u[2], nx * u[1] - ny * u[0]
        u = [u[0] * ca + cx * sa + nx * d * (1 - ca), u[1] * ca + cy * sa + ny * d * (1 - ca), u[2] * ca + cz * sa + nz * d * (1 - ca)]
        zn = z + u[2] * ds
        for P in PLANES:
            if P not in out and z < P <= zn:
                out[P] = math.hypot(x + u[0] * ds, y + u[1] * ds)
        x += u[0] * ds; y += u[1] * ds; z = zn; s += ds
    return out
def iso(rng):
    return math.acos(rng.uniform(-1, 1)), rng.uniform(0, 2 * math.pi)
def spot(rng, sig): return rng.gauss(0, sig), rng.gauss(0, sig)
def michel_p(rng):
    while True:
        x = rng.random()
        if rng.random() * 1.0 < x * x * (3 - 2 * x): return 0.0528 * x
def run(prof, thmin_deg, n=1500, sig=0.01, seed=1):
    rng = random.Random(seed); thmin = math.radians(thmin_deg)
    R = {(P, r): 0 for P in PLANES for r in RADII}; S = dict.fromkeys(R, 0); M = dict.fromkeys(R, 0); ns = 0
    for i in range(n):
        th, ph = iso(rng); x0, y0 = spot(rng, sig)
        for P, rr in trace(rng.uniform(0.0014, 0.0055), th, ph, x0, y0, prof).items():
            for r in RADII: R[(P, r)] += rr < r
        th, ph = iso(rng); x0, y0 = spot(rng, sig)
        for P, rr in trace(michel_p(rng), th, ph, x0, y0, prof, smax=0.6).items():
            for r in RADII: M[(P, r)] += rr < r
        th = math.acos(rng.uniform(-math.cos(thmin), math.cos(thmin))); ph = rng.uniform(0, 2 * math.pi); x0, y0 = spot(rng, sig)
        ns += 1
        hit = {}
        for P, rr in trace(0.0528, th, ph, x0, y0, prof, smax=0.6).items(): hit[P] = rr
        tg, pg = math.pi - th, ph + math.pi   # photon, straight line
        for P in PLANES:
            rg = None
            if math.cos(tg) > 0:
                t = P / math.cos(tg); rg = math.hypot(x0 + t * math.sin(tg) * math.cos(pg), y0 + t * math.sin(tg) * math.sin(pg))
            for r in RADII:
                S[(P, r)] += (P in hit and hit[P] < r) or (rg is not None and rg < r)
    return {k: (R[k] / n, S[k] / ns, M[k] / n) for k in R}
if __name__ == "__main__":
    for prof, thm in (("conf1", 70), ("attarget", 70), ("attarget", 40), ("attarget", 30)):
        res = run(prof, thm)
        ok = [(k, v) for k, v in res.items() if v[1] <= 0.02]
        best = max(ok, key=lambda kv: kv[1][0])
        print(f"== field={prof} acceptance theta>={thm} deg: best signal-safe disk z={best[0][0]*100:.1f} cm R={best[0][1]*100:.1f} cm "
              f"fR={best[1][0]:.3f} fS={best[1][1]:.3f} fMichel={best[1][2]:.3f}  -> reduction 0.5*0.9*fR={0.45*best[1][0]:.3f}")
        for P in PLANES:
            row = [f"{res[(P, r)][0]:.2f}/{res[(P, r)][1]:.2f}" for r in RADII]
            print(f"  z={P*100:5.1f}cm fR/fS:", " ".join(row))
