import numpy as np
import astropy.units as u

def organize(obs, param, results):
    results["bp_rp"]=results["phot_bp_mean_mag"]- results["phot_rp_mean_mag"] #subract the mags
    results['mag_size']=(obs.mag_limit-results['phot_g_mean_mag'])**2
    np.where(results['mag_size']<1,1,results['mag_size'])
    return results

        
    
def main():
    pass

if __name__ == "__main__":
    main()
