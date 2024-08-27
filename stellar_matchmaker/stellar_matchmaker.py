import astropy.units as u
from astropy.coordinates import SkyCoord, Angle
from astroquery.gaia import Gaia

import pandas as pd
import numpy as np

if __name__ == "__main__":
    from observation import Observation
    from stellar_param import Stellar_param
    from plot_stellar_matchmaker import generate_plot
    from organize import organize

else:
    from .observation import Observation
    from .stellar_param import Stellar_param
    from .plot_stellar_matchmaker import generate_plot
    from .organize import organize

class Stellar_matchmaker:
    def __init__(self, askinfo=True, ra='23:6:29.37', dec='-5:02:29.04', 
                G=15.62, bp=19.01, rp=14.10, 
                mag_limit=15, mag_diff_limit=1, col_diff_limit=5, ra_size=1, dec_size=1):
        
        """
        This function is used to get the inputs for the program.

        Args
        ------
        askinfo : bool
            If True, the user will be prompted to enter the values. If False, the default values will be used.
        ra : str
            RA (h:m:s) 
        dec : str
            Dec (h:m:s)
        G : float
            G magnitude
        bp : float
            BP magnitude
        rp : float
            RP magnitude
        mag_limit : float
            limiting magnitude of the detector
        mag_diff_limit : float
            maximum difference between target and reference
        col_diff_limit : float
            maximum difference between target and reference
        ra_size : float
            size of the region to search for reference stars in RA (deg)
        dec_size : float
            size of the region to search for reference stars in DEC (deg)
        

        Returns
        ------
        obs: object
            Observation class object, contains information about the observational parameters used to set mag limit etc.
        results: astropy.table
            astropy table object, as per the input but with colour and size term as new columns
        """

        self.obs = Observation()
        self.param = Stellar_param()
        self.results = None

        
        if askinfo:
            ra_input = input("Please enter the RA of the target. default) 23:6:29.37 ")
            if ra_input=='':
                ra=ra
            else:
                ra=ra_input
            dec_input = input("Please enter the DEC of the target. default) -5:02:29.04 ")
            if dec_input=='':
                dec=dec
            else:
                dec=dec_input
            G_input = input("Please enter the G magnitude of the target. default) 15.62 ")
            if G_input=='':
                G=G 
            else:
                G=float(G_input)
            bp_input = input("Please enter the BP magnitude of the target. default) 19.01 ")
            if bp_input=='':
                bp=bp
            else:
                bp=float(bp_input)
            rp_input = input("Please enter the RP magnitude of the target. default) 14.10 ")
            if rp_input=='':
                rp=rp
            else:
                rp=float(rp_input)
            mag_limit_input = input("Please enter the limiting magnitude of the detector. default) 15 ")
            if mag_limit_input=='':
                mag_limit=mag_limit
            else:
                mag_limit=float(mag_limit_input)
            mag_diff_limit_input = input("Please enter the maximum difference of the G magnitude from the target. default) 1 ")
            if mag_diff_limit_input=='':
                mag_diff_limit=mag_diff_limit
            else:
                mag_diff_limit=float(mag_diff_limit_input)
            col_diff_limit_input = input("Please enter the maximum difference of the BP-RP magnitude from the target. default) 5 ")
            if col_diff_limit_input=='':
                col_diff_limit=col_diff_limit
            else:
                col_diff_limit=float(col_diff_limit_input)
            ra_size_input = input("Please enter the size of the region to search for reference stars in RA deg. default) 1 ")
            if ra_size_input=='':
                ra_size=ra_size
            else:
                ra_size=float(ra_size_input)
            dec_size_input = input("Please enter the size of the region to search for reference stars in DEC deg. default) 1 ")
            if dec_size_input=='':
                dec_size=dec_size
            else:
                dec_size=float(dec_size_input)
            

        self.obs.set_mag_limit(mag_limit * u.mag)
        self.obs.set_mag_diff_limit(mag_diff_limit * u.mag)
        self.obs.set_col_diff_limit(col_diff_limit * u.mag)
        self.obs.set_ra_size(ra_size * u.deg)
        self.obs.set_dec_size(dec_size * u.deg)


        self.param.set_ra(Angle('%s hours'%ra))
        self.param.set_dec(Angle('%s degrees'%dec))
        self.param.set_G(G * u.mag)
        self.param.set_bp(bp * u.mag)
        self.param.set_rp(rp * u.mag)




    def _generate_limits_clause(self, target, size, name):
        """
        This function generates the clause for the query.

        args
        ------
        target : float
            The target value.
        size : float
            The range of the value.
        name : str
            The name of the value.
        

        return
        ------
        clause : str
            The clause for the query.
        """
        
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

    def generate_query(self):
        """
        This function generates the query for the Gaia database.

        args
        ------
        obs : object
            Observation class object, contains information about the observational parameters used to set mag limit etc.
        param : object
            Stellar parameter object, contains information about the target: position and 3 magnitudes, used to compare with references
        
        return
        ------
        query : str
            The query for the Gaia database.
        """
        ra_clause = self._generate_limits_clause(self.param.ra, self.obs.ra_size, "ra")
        dec_clause = self._generate_limits_clause(self.param.dec, self.obs.dec_size, "dec")
        box_clause = " CONTAINS(POINT('ICRS', ra, dec), BOX('ICRS', {}, {}, {}, {})) = 1 ".format(self.param.ra.to(u.deg).value,
                                                                                            self.param.dec.to(u.deg).value,
                                                                                            2*self.obs.ra_size.to(u.deg).value,
                                                                                            2*self.obs.dec_size.to(u.deg).value)

        mag_clause = " phot_g_mean_mag < {}".format(float(self.obs.mag_limit / u.mag))

        query = ("SELECT "
                "ra, dec, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag "
                "FROM gaiadr3.gaia_source "
                "WHERE " + box_clause +
                "AND " + mag_clause)
        # print(query)
        return query

    def run_query(self, file_name='~/results.csv'):

        query = self.generate_query()
        job = Gaia.launch_job_async(query)
        
        results = job.get_results()
        results.write(file_name, format='ascii', overwrite=True)  

        results = organize(self.obs, self.param, results)
        generate_plot(self.obs, self.param, results)



        return results
    
  


if __name__ == "__main__":
    stellar_matchmaker = Stellar_matchmaker()
    stellar_matchmaker.run_query()
