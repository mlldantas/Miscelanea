import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u

from dustmaps.bayestar import BayestarQuery
from dustmaps.edenhofer2023 import Edenhofer2023Query

# Create a grid of Galactic coordinates
l = np.linspace(0, 60, 200)  # Galactic longitude [deg]
b = np.linspace(-10, 10, 200)  # Galactic latitude [deg]
l2d, b2d = np.meshgrid(l, b)
coords = SkyCoord(l2d * u.deg, b2d * u.deg, distance=1 * u.kpc, frame='galactic')

# Query Bayestar map (median cumulative E(B–V) to 1 kpc)
bayestar = BayestarQuery(version='bayestar2019', max_samples=1)
ebv = bayestar(coords, mode='median')

# Query Edenhofer map (mean integrated E(B–V) to 1 kpc)
edenhofer = Edenhofer2023Query(integrated=True)
ebv_ed = edenhofer(coords, mode='mean')

# Determine unified color scale
vmin = 0
vmax = max(np.nanmax(ebv), np.nanmax(ebv_ed))

# Plotting parameters
fig, axs = plt.subplots(1, 2, figsize=(12, 5), dpi=150)
f = 0.02        # colorbar size fraction
fsize = 15      # font size for titles and axis labels
cbsize = 12     # colorbar font size
ticksize = 12   # tick marker (axis label) font size

# Bayestar plot
im0 = axs[0].imshow(ebv, origin='lower',
                    extent=[l.min(), l.max(), b.min(), b.max()],
                    vmin=vmin, vmax=vmax)
axs[0].set_title('Bayestar (1 kpc)', fontsize=fsize)
axs[0].set_xlabel('Galactic l [deg]', fontsize=fsize)
axs[0].set_ylabel('Galactic b [deg]', fontsize=fsize)
axs[0].tick_params(labelsize=ticksize)
cb0 = fig.colorbar(im0, ax=axs[0], fraction=f)
cb0.ax.tick_params(labelsize=cbsize)
cb0.set_label('E(B–V) [mag]', fontsize=cbsize)

# Edenhofer plot
im1 = axs[1].imshow(ebv_ed, origin='lower',
                    extent=[l.min(), l.max(), b.min(), b.max()],
                    vmin=vmin, vmax=vmax)
axs[1].set_title('Edenhofer (integrated)', fontsize=fsize)
axs[1].set_xlabel('Galactic l [deg]', fontsize=fsize)
axs[1].set_ylabel('Galactic b [deg]', fontsize=fsize)
axs[1].tick_params(labelsize=ticksize)
cb1 = fig.colorbar(im1, ax=axs[1], fraction=f)
cb1.ax.tick_params(labelsize=cbsize)
cb1.set_label('E(B–V) [mag]', fontsize=cbsize)

plt.tight_layout()
plt.show()

