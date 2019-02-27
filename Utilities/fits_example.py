#!/usr/bin/env python
# coding: utf-8

# # Libraries

# In[1]:


import astropy.io.fits   as pf  # previously pyfits
import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt


# # File & spectrum

# In[2]:


spec       = './t05750_g+4.5_p00p00_hrplc.fits'
ftfile     = pf.open(spec)
flux       = pf.getdata(spec)
wl_i       = ftfile[0].header['CRVAL1']
wl_step    = ftfile[0].header['CDELT1']
wavelength = np.arange(flux.size)*wl_step+wl_i      # wavelength


# # Saving in a csv file
# for other formats please see: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

# In[3]:


data = np.column_stack((wavelength, flux))
data = pd.DataFrame(data)
header = ['wavelength', 'flux']
data.columns = header
data.to_csv('./my_spec.csv', index=False)


# # Checking the spectrum

# In[4]:


plt.plot(wavelength, flux, '-')
plt.show()

