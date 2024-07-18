import astropy.units as u
from astropy.coordinates import SkyCoord, Angle
from astroquery.gaia import Gaia
from .observation import observation
from .Stellar_param import stellar_param
from .plot_stellar_matchmaker import generate_plot
from .Organize import organize
import pandas as pd
import numpy as np


def get_inputs():
    obs = observation()
    # temporary values for testing and demo
    obs.set_mag_limit(15 * u.mag)
    obs.set_mag_diff_limit(1 * u.mag)
    obs.set_col_diff_limit(5 * u.mag)
    obs.set_ra_size(1 * u.deg)
    obs.set_dec_size(1 * u.deg)

    param = stellar_param()
    # values for trappist-1
    param.set_ra(Angle('23:6:29.37 hours'))
    param.set_dec(Angle('-5:02:29.04 degrees'))
    param.set_G(15.62 * u.mag)
    param.set_bp(19.01 * u.mag)
    param.set_rp(14.10 * u.mag)
    
    return obs, param



def generate_limits_clause(target, size, name):
    try: 
        hi = (target + size).to(u.deg)
    except:
        hi = (target + size)

    try:
        lo = (target - size).to(u.deg)
    except:
        lo = (target - size)

    clause = " {0} > {1} AND {0} < {2} ".format(name, lo.value, hi.value)

    return clause

def generate_query(obs, param):

    ra_clause = generate_limits_clause(param.ra, obs.ra_size, "ra")
    dec_clause = generate_limits_clause(param.dec, obs.dec_size, "dec")
    mag_clause = " phot_g_mean_mag < {}".format(float(obs.mag_limit / u.mag))

    query = ("SELECT "
             "ra, dec, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag "
             "FROM gaiadr3.gaia_source "
             "WHERE " + ra_clause +
             "AND " + dec_clause +
             "AND " + mag_clause)
    # print(query)
    return query

def run_query(obs, param):

    query = generate_query(obs, param)
    job = Gaia.launch_job_async(query)
    
    results = job.get_results()
    results.write('~/results.csv', format='ascii', overwrite=True)  


    return results


def organise_data():
    pass



def output_data(obs, param, results):
    generate_plot(obs, param, results)

    pass

def main():
    """
    This function is only called if this program is executed in standalone format.  
    
    If we import the functions, this will not be called.
    """

    # skeleton stucture of the code, will be changed in future version
    obs, param = get_inputs()
    result = run_query(obs, param)

    result = organize(obs, param, result)
    output_data(obs, param, result)
    

    

if __name__ == "__main__":
    main()
