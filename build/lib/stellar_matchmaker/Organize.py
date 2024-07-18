import numpy as np
import astropy.units as u

def organize(obs, param, results):
    """ Organise the data for plotting
    
    Runs calculations on the results based on the observation and star parameters to allow it to be plotted clearly.

    Args:
        obs (Observation): Observation class object, contains information about the observational parameters used to set mag limit etc.
        param (Setllar_param): Stellar parameter object, contains information about the target: position and 3 magnitudes, used to compare with references
        results (astropy.table): astropy table object, with columns for reference star position and magnitudes, used to calculate size to plot and colour
    
    Returns:
        results (astropy.table): astropy table object, as per the input but with colour and size term as new columns
    """
    results["bp_rp"]=results["phot_bp_mean_mag"]- results["phot_rp_mean_mag"] #subract the mags
    results['mag_size']=(obs.mag_limit-results['phot_g_mean_mag'])**2
    np.where(results['mag_size']<1,1,results['mag_size'])

    results = good_ref(obs, param, results)
    print(results)
    return results

def good_ref(obs, param, results):
    mag_diff=abs(param.G - results["phot_g_mean_mag"])
    target_col = (param.bp-param.rp)
    col_diff=abs(target_col - results["bp_rp"]*u.mag)
    good_mag=mag_diff <= obs.mag_diff_limit
    good_col=col_diff <= obs.col_diff_limit
    results["good"]=np.logical_and(good_mag, good_col)

    return results
    
def main():
    pass

if __name__ == "__main__":
    main()
