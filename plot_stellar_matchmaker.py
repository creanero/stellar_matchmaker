import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord, Angle



def main():
    pass

def generate_plot(obs, param, results, figsize=10):
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(figsize, figsize))
    bp_rp = np.array(results['bp_rp'])
    print(type(bp_rp))
    vmin=np.nanpercentile(bp_rp,10, method='nearest')
    vmax=np.nanpercentile(bp_rp,90, method='nearest')
    plt.scatter(results['ra'], results['dec'], c=results['bp_rp'], cmap='RdYlBu_r',s=results['mag_size'], vmin=vmin, vmax=vmax)
    plt.xlabel('RA (deg)')
    plt.ylabel('DEC (deg)') 
    plt.xlim(345.62, 347.62)
    plt.colorbar(label='BP-RP (mag)')
    plt.show()

if __name__ == "__main__":
    main()





