import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord, Angle



def main():
    pass

def generate_plot(obs, param, results, figsize=10):
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(figsize, figsize))
    vmin=np.nanpercentile(results['bp_rp'],10)
    vmax=np.nanpercentile(results['bp_rp'],90)
    plt.scatter(results['ra'], results['dec'], c=results['bp_rp'], cmap='RdYlBu',s=results['mag_size'], vmin=vmin, vmax=vmax)
    plt.xlabel('RA (deg)')
    plt.ylabel('DEC (deg)') 
    plt.colorbar(label='BP Magnitude')
    plt.show()

if __name__ == "__main__":
    main()





