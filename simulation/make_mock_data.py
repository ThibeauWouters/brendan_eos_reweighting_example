"""Make N mock M-R observations (noiseless, on the EOS curve) from medium.npz."""

import json
from pathlib import Path

import numpy as np

N = 100

here = Path(__file__).parent
d = np.load(here / "medium.npz")
m, r = d["masses_EOS"], d["radii_EOS"]
print(f"MTOV = {m.max():.3f}, EOS has {len(m)} points")

# Use the stable branch only (up to MTOV), sorted by mass
i_tov = np.argmax(m)
m, r = m[: i_tov + 1], r[: i_tov + 1]

masses = np.linspace(1.2, m.max(), N)
radii = np.interp(masses, m, r)

STD_MASS, STD_RADIUS, CORR = 0.1, 0.5, 0.0
obs = [
    dict(name=f"PSR{i}", mean_mass=float(mi), mean_radius=float(ri),
         std_mass=STD_MASS, std_radius=STD_RADIUS, correlation=CORR)
    for i, (mi, ri) in enumerate(zip(masses, radii))
]
with open(here / "mock_observations.json", "w") as f:
    json.dump(obs, f, indent=2)
print(f"Wrote {len(obs)} observations, M in [{masses.min():.3f}, {masses.max():.3f}]")
