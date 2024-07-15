#!/usr/bin/env python3

import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia



def get_inputs():
    pass

def generate_limits_clause(target, size, name):
    hi = target + size
    lo = target - size
    clause = "{0} > {1} AND {0} < {2}".format(name, lo, hi)

    return clause

def generate_query():
    target_ra = 0.
    ra_size = 0.125
    ra_clause = generate_limits_clause(target_ra, ra_size, "ra")

    target_dec = 0.
    dec_size = 0.125
    dec_clause = generate_limits_clause(target_dec, dec_size, "dec")

    query = ("SELECT "
             "ra, dec, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag "
             "FROM gaiadr3.gaia_source "
             "WHERE " + ra_clause +
             "AND " + dec_clause)
    return query

def run_query():
    query = generate_query()
    job = Gaia.launch_job(query)
    results = job.get_results()
    print(results)


def organise_data():
    pass

def output_data():
    pass

def main():
    """
    This function is only called if this program is executed in standalone format.  
    
    If we import the functions, this will not be called.
    """

    # skeleton stucture of the code, will be changed in future version
    get_inputs()
    run_query()
    organise_data()
    output_data()

    pass

if __name__ == "__main__":
    main()
