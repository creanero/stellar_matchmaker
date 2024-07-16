import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
from observation import observation
from Stellar_param import stellar_param


def get_inputs():
    obs = observation()
    param = stellar_param()

    return obs, param



def generate_limits_clause(target, size, name):
    hi = target + size
    lo = target - size
    clause = " {0} > {1} AND {0} < {2} ".format(name, lo.value, hi.value)

    return clause

def generate_query(obs, param):

    ra_clause = generate_limits_clause(param.ra, obs.ra_size, "ra")
    dec_clause = generate_limits_clause(param.dec, obs.dec_size, "dec")

    query = ("SELECT "
             "ra, dec, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag "
             "FROM gaiadr3.gaia_source "
             "WHERE " + ra_clause +
             "AND " + dec_clause)
    return query

def run_query(obs, param):

    query = generate_query(obs, param)
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
    obs, param = get_inputs()
    run_query(obs, param)
    organise_data()
    output_data()

    pass

if __name__ == "__main__":
    main()
