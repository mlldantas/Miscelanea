import numpy as np
import os
import pysynphot as s
import pandas as pd
import matplotlib.pyplot as plt


def photometry(filters_path, filters_list, specs_path, specs_list, telescope_area, results_path, confidence=0.6,
               plot=False, save=False):
    """

    :param filters_path: add the path to your filters response files -- e.g '/home/user/Documents/Filters'
    :param filters_list: add the path and name of your filters' list
    -- e.g '/home/user/Documents/filters_list.txt'
    Inside this list you should have all the filters' response files that you are going to use
    -- e.g.:
    uSDSS.txt
    gSDSS.txt
    rSDSS,txt
    iSDSS.txt
    zSDSS.txt
    You can create it in your command line by doing the following command:
    $ ls /home/user/Documents/Filters >> /home/user/Documents/filters_list.txt
    :param specs_path: add the path to your spectra files -- e.g '/home/user/Documents/Specs'
    :param specs_list: similar to the filters_list
    :param telescope_area: the default parameter is 4400 which is the J-PAS T80 M1 effective area in cm^2.
    Set it as you wish given your telescope.
    :param results_path: add the path where you would like to save your results. It is only obligatory if you set
    plot=True
    :param confidence: the confidence that you would like to add in order to calculate a simulated photometry.
    This is important for the photometry of the borders of the spectra. This will limit the calculation of the
    photometry in terms of the wavelength range. If the filter occupies less than X% of your spectrum wavelength range,
    it will generate an error value (-999), but if it occupies more than X% it will do the convolution the filter with
    the spectrum. The default value is 60% (0.6), but you can change this at your will.
    :param plot: if you want to plot the results and save them, please set 'plot=True'. If not, please set 'plot=False'.
    The default is false.
    :param save: if you want to save the results, please set 'save=True'. If not, please set 'save=False'.
    The default is False.
    is false.
    :return: The returned parameters are:
    1) photometry: your simulated photometry. This is your main result.
    2) lambda_eff: effective wavelengths of your filters.
    3) photometry_flam: the simulated photometry in terms of flux_lambda
    4) photometry_fnu: the simulated photometry in terms of flux_fnu
    5) filter_name: the name of the filters you used in each round. This is not very important, you can ignore this.
    """

    # Setting the telescope area; the default parameter is the T80 M1 effective area in cm^2 ---------------------------
    if telescope_area==None:
        s.setref(area=4400)
    else:
        s.setref(area=telescope_area)

    # Reading your files -----------------------------------------------------------------------------------------------
    filters_list = np.loadtxt(filters_list, dtype=str)
    specs_list   = np.loadtxt(specs_list, dtype=str)

    # Simulating photometry for your spectra using the selected survey filters -----------------------------------------
    count = 0
    for each_spectrum in specs_list:
        print each_spectrum
        filter_name     = []
        photometry      = []
        photometry_flam = []
        lambda_eff      = []
        for filters in filters_list:
            # saving an array with the filters names -------------------------------------------------------------------
            filter_name_i          = filters.split('.')[0]
            filter_name.append(filter_name_i)

            # convolution ----------------------------------------------------------------------------------------------
            filter_bandpass = s.FileBandpass(os.path.join(filters_path, filters))
            spectrum         = s.FileSpectrum(os.path.join(specs_path, each_spectrum))             # the entire spectrum
            index            = np.where(spectrum.flux > 0)            # selecting only the positive part of the spectrum
            spectrum2        = s.ArraySpectrum(wave=spectrum.wave[index], flux=spectrum.flux[index],
                                                    fluxunits=spectrum.fluxunits, waveunits=spectrum.waveunits)
            binset = filter_bandpass.wave                        # this is very very important! don't change this unless
                                                                        # you are absolutely sure of what you are doing!
            ## convolved photometry ------------------------------------------------------------------------------------
            photometry_i = s.Observation(spectrum2, filter_bandpass, binset=binset, force='extrap')

            ## effective wavelength ------------------------------------------------------------------------------------
            lambda_eff_i = photometry_i.efflam()
            lambda_eff.append(lambda_eff_i)

            ## checking if the simulated photometry is "virtual" and letting those away --------------------------------
            if filter_bandpass.wave.min() < spectrum2.wave.min():
                if filter_bandpass.wave.max() - spectrum2.wave.min() > confidence * (filter_bandpass.wave.max() -
                                                                                  filter_bandpass.wave.min()):
                    photometry.append(photometry_i.effstim('abmag'))
                    photometry_flam_i = photometry_i.effstim('flam')
                    photometry_flam.append(photometry_flam_i)

                else:
                    new_photometry_i = -999
                    photometry.append(new_photometry_i)
                    photometry_flam.append(new_photometry_i)

            elif filter_bandpass.wave.max() > spectrum2.wave.max():
                if spectrum2.wave.max() - filter_bandpass.wave.min() > confidence * (filter_bandpass.wave.max() -
                                                                                  filter_bandpass.wave.min()):
                    photometry.append(photometry_i.effstim('abmag'))
                    photometry_flam_i = photometry_i.effstim('flam')
                    photometry_flam.append(photometry_flam_i)

                else:
                    new_photometry_i = -999
                    photometry.append(new_photometry_i)
                    photometry_flam.append(new_photometry_i)

            else:
                photometry.append(photometry_i.effstim('abmag'))
                photometry_flam_i = photometry_i.effstim('flam')
                photometry_flam.append(photometry_flam_i)

        count = count+1

        # putting the iterated items into arrays -----------------------------------------------------------------------
        filter_name       = np.array(filter_name)            # name of each filter
        photometry        = np.array(photometry)             # in magnitudes
        lambda_eff        = np.array(lambda_eff)             # effective wavelengths of the filters
        photometry_flam   = np.array(photometry_flam)        # in flux of lambda
        photometry_fnu    = 10**(-0.4*(photometry + 48.60))  # in flux of nu

        if (plot==False)*(save==False):
            continue

        elif (plot==False)*(save==True):
            # saving the newley calculated photometry ------------------------------------------------------------------
            galaxy_simulation_abmag = np.vstack((filter_name, photometry))
            galaxy_simulation_abmag = pd.DataFrame(galaxy_simulation_abmag)
            galaxy_simulation_abmag.to_csv(os.path.join(results_path, str(count)+'_abmag.csv'), sep=',', header=None,
                                           index=False)
            galaxy_simulation_fnu = np.vstack((filter_name, photometry_fnu))
            galaxy_simulation_fnu = pd.DataFrame(galaxy_simulation_fnu)
            galaxy_simulation_fnu.to_csv(os.path.join(results_path, str(count)+'_fnu.csv'), sep=',', header=None,
                                         index=False)

        elif (plot==True) * (save==False):
            # plots ----------------------------------------------------------------------------------------------------
            plt.plot(spectrum2.wave, spectrum2.flux, '-')
            plt.plot(lambda_eff[[photometry_flam!=-999]], photometry_flam[[photometry_flam!=-999]], 'o')
            plt.title(r"%s" % each_spectrum, size='15')
            plt.savefig(os.path.join(results_path, 'object_'+str(count)+'.png'), dpi = 100)
            plt.show()

        elif (plot==True) * (save==True):
            # plots ----------------------------------------------------------------------------------------------------
            plt.plot(spectrum2.wave, spectrum2.flux, '-')
            plt.plot(lambda_eff[[photometry_flam!=-999]], photometry_flam[[photometry_flam!=-999]], 'o')
            plt.title(r"%s" % each_spectrum, size='15')
            plt.savefig(os.path.join(results_path, 'object_'+str(count)+'.png'), dpi = 100)
            plt.show()

            # saving the newley calculated photometry ------------------------------------------------------------------
            galaxy_simulation_abmag = np.vstack((filter_name, photometry))
            galaxy_simulation_abmag = pd.DataFrame(galaxy_simulation_abmag)
            galaxy_simulation_abmag.to_csv(os.path.join(results_path, 'object_'+str(count)+'_abmag.csv'), sep=',',
                                           header=None, index=False)
            galaxy_simulation_fnu = np.vstack((filter_name, photometry_fnu))
            galaxy_simulation_fnu = pd.DataFrame(galaxy_simulation_fnu)
            galaxy_simulation_fnu.to_csv(os.path.join(results_path, 'object_'+str(count)+'_fnu.csv'), sep=',',
                                         header=None, index=False)

    return photometry, lambda_eff, photometry_flam, photometry_fnu, filter_name

