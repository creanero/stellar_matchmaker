import astropy.units as u
from astropy.coordinates import SkyCoord, Angle
from astroquery.gaia import Gaia
from observation import observation
from Stellar_param import stellar_param
from plot_stellar_matchmaker import generate_plot
from Organize import organize


def get_inputs(ra='23:6:29.37', dec='-5:02:29.04', G=15.62, bp=19.01, rp=14.10, mag_limit=15, mag_diff_limit=1, col_diff_limit=5, ra_size=1, dec_size=1):
    """
    This function is used to get the inputs for the program.

    Args:
        obs (Observation): Observation class object, contains information about the observational parameters used to set mag limit etc.
        param (Setllar_param): Stellar parameter object, contains information about the target: position and 3 magnitudes, used to compare with references
        results (astropy.table): astropy table object, with columns for reference star position and magnitudes, used to calculate size to plot and colour
    
    Returns:
        results (astropy.table): astropy table object, as per the input but with colour and size term as new columns
    """
    obs = observation()
    # temporary values for testing and demo
    obs.set_mag_limit(mag_limit * u.mag)
    obs.set_mag_diff_limit(mag_diff_limit * u.mag)
    obs.set_col_diff_limit(col_diff_limit * u.mag)
    obs.set_ra_size(ra_size * u.deg)
    obs.set_dec_size(dec_size * u.deg)

    param = stellar_param()
    # values for trappist-1
    param.set_ra(Angle('%s hours'%ra))
    param.set_dec(Angle('%s degrees'%dec))
    param.set_G(G * u.mag)
    param.set_bp(bp * u.mag)
    param.set_rp(rp * u.mag)
    
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
    # print(results)

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
