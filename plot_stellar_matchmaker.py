import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord, Angle



def main():
    pass

def generate_plot(obs, param, results, figsize=10):
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(figsize, figsize))
    plt.scatter(results['ra'], results['dec'], c=results['phot_bp_mean_mag'], cmap='RdYlBu',s=results['phot_g_mean_mag'])
    plt.xlabel('RA (deg)')
    plt.ylabel('DEC (deg)') 
    plt.colorbar(label='BP Magnitude')
    plt.show()

if __name__ == "__main__":
    main()





