"""Thin timing-only disk route under 'rise at target' + acceptance >=40 deg (r1 scan follow-up).
Signal crossing a thin (~0.5 mm plastic) layer is NOT lost; the cost is the random veto from Michel e+ crossings."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r1_scan import run, PLANES, RADII
res = run("attarget", 40)
Rstop = 4.5e7
print("disks with reduction 0.5*0.9*fR >= 0.10 (fR>=0.222), sorted by Michel crossing fraction fM:")
rows = sorted([(v[2], k, v) for k, v in res.items() if 0.45 * v[0] >= 0.10])
for fm, k, v in rows[:8]:
    print(f"  z={k[0]*100:4.1f} cm R={k[1]*100:4.1f} cm fR={v[0]:.3f} red={0.45*v[0]:.3f} fM={fm:.3f} "
          f"veto_loss(1ns)={Rstop*fm*1e-9:.3f} (2ns)={Rstop*fm*2e-9:.3f} (4ns)={Rstop*fm*4e-9:.3f}")
