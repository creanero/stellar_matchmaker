import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord, Angle



def main():
    pass

def generate_plot(obs, param, results, figsize=10):
    
    """Plot the outputs.

    This function simply plots the target star and the reference stars.

    Args:
        obs (object) : Object carrying information about class observation.
        params (object) : Object carrying information from class stellar_param has info about filters and mags.
        results(astropy tables): Object carrying information about Gaia query from the target star.
        
    """
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(figsize, figsize))
    bp_rp = np.array(results['bp_rp'])
    print(type(bp_rp))
    vmin=np.nanpercentile(bp_rp,10, method='nearest')
    vmax=np.nanpercentile(bp_rp,90, method='nearest')
    plt.scatter(param.ra.to(u.deg), param.dec.to(u.deg), color = "w", marker = "*", s=1000)

    plt.scatter(results['ra'], results['dec'], c=results['bp_rp'], cmap='RdYlBu_r',s=results['mag_size'], vmin=vmin, vmax=vmax)
    
    plt.xlabel('RA (deg)')
    plt.ylabel('DEC (deg)') 
    plt.xlim(345.62, 347.62)
    plt.colorbar(label='BP-RP (mag)')

    good_refs=results[results["good"] == True]
    print(good_refs)
    plt.scatter(good_refs['ra'], good_refs['dec'], color = "limegreen", marker="o", s=20, facecolors='none')

    plt.show()

if __name__ == "__main__":
    main()





