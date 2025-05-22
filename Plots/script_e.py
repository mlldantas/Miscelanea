#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Violin Plot Using Seaborn Package in Python
    @author:  Maria Luiza L. Dantas
    @date:    2015.23.10
    @version: 0.0.1

"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ======================================================================================================================
# Main thread
if __name__ == '__main__':

    # Reading the files which contain the data -------------------------------------------------------------------------
    
    sns.set(style="whitegrid", palette="pastel", color_codes=True, font_scale=0.8)
    
    # Load the example tips dataset
    agn_logit = pd.read_csv('full_E.csv', index_col=0)

    # Draw a nested violinplot and split the violins for easier comparison ---------------------------------------------
    # Commands: bw == smoothness of the curve; cut == hight of the middle axis; 
    # linewidth modifies all lines of the plot.

    # Plot 01 ----------------------------------------------------------------------------------------------------------
    sns.factorplot(x="type", y="lgm_tot_p50", hue="Seyfert", data=agn_logit, split=True,
                   inner="quart", palette={"No": "#de2d26", "Yes": "#fcbba1"}, bw=.3, cut=1, linewidth=1.,
                   x_order=['Before PSM','After PSM'], kind="violin", legend_out=False)
    plt.ylabel(r"$\rm{\log \, M_{*}}$", fontsize=20, fontweight='bold')
    plt.xlabel(r"", fontsize=30)
    plt.ylim([-2., 4])
    plt.xlim([-0.5, 1.5])
    plt.tick_params('both', labelsize='15')
    plt.subplots_adjust(left=0.25, bottom=0.2, right=0.9, top=0.75)
    sns.despine(left=True)
    plt.savefig('stellarmass_e.pdf', format='pdf')
    plt.show()

    # Plot 02 ----------------------------------------------------------------------------------------------------------
    sns.factorplot(x="type", y="sfr_tot_p50", hue="Seyfert", data=agn_logit, split=True,
                   inner="quart", palette={"No": "#de2d26", "Yes": "#fcbba1"}, bw=.3, cut=1, linewidth=1.,
                   x_order=['Before PSM','After PSM'], kind="violin", legend=False)
    plt.ylabel(r"$\rm{\log \, SFR}$", fontsize=20, fontweight='bold' )
    plt.xlabel(r"", fontsize=30)
    plt.ylim([-2.0, 0.5])
    #plt.xlim([-0.5, 1.5])
    plt.tick_params('both', labelsize='15')
    plt.subplots_adjust(left=0.25, bottom=0.2, right=0.9, top=0.75)
    sns.despine(left=True)
    plt.savefig('sfr_e.pdf', format='pdf')
    plt.show()

    # Plot 03 ----------------------------------------------------------------------------------------------------------
    sns.factorplot(x="type", y="color_gr", hue="Seyfert", data=agn_logit, split=True,
                  inner="quart", palette={"No": "#de2d26", "Yes": "#fcbba1"}, bw=.3, cut=1, linewidth=1.,
                  x_order=['Before PSM','After PSM'], kind="violin", legend=False)
    plt.ylabel(r"$\rm{g-r}$", fontsize=20, fontweight='bold')
    plt.xlabel(r"", fontsize=30)
    plt.ylim([-0.2, 1.5])
    #plt.xlim([-1, 2])
    plt.tick_params('both', labelsize='15')
    plt.subplots_adjust(left=0.25, bottom=0.2, right=0.9, top=0.75)
    sns.despine(left=True)
    plt.savefig('color_e.pdf', format='pdf')
    plt.show()