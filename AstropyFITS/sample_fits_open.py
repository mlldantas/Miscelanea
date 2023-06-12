# coding: utf-8
import matplotlib.pyplot as plt
from astropy.utils.data import get_pkg_data_filename
from astropy.visualization import astropy_mpl_style
from astropy.io import fits
plt.style.use(astropy_mpl_style)
image_file = get_pkg_data_filename('/home/mlldantas/Downloads/lixo/ADP.2018-03-26T10 12 41.337.fits')
image_data = fits.getdata(image_file, ext=2)
plt.imshow(image_data, cmap='gray', norm=LogNorm())
from matplotlib.colors import LogNorm
plt.imshow(image_data, cmap='gray', norm=LogNorm())
plt.show()
