from astropy import units as u
from astropy.coordinates import SkyCoord

class Observation:
    """ 
    Set the observational parameters.
    Limit the magnitude of the detector, the maximum difference between target and reference, and the size of the region to search for reference stars.
    """
    def __init__(self):
        self.mag_diff_limit = 0 *u.mag
        self.col_diff_limit = 0 *u.mag
        self.ra_size = 0 *u.deg
        self.dec_size = 0 *u.deg

    # limiting magnitude of detector    
    def get_mag_limit(self):
        return self.mag_limit  

    def set_mag_limit(self, input_val):
        if (input_val <= (0 * u.mag) or input_val > (30 * u.mag)):
            raise ValueError("Magnitude limit value out of scope, range limited to 0 to 30 magnitudes.")
        else:
            self.mag_limit = input_val
    
    # limiting maximum difference between target and reference
    def get_mag_diff_limit(self):
        return self.mag_diff_limit  

    def set_mag_diff_limit(self, input_val):
        if (input_val <= (0 * u.mag) or input_val > (5 * u.mag)):
            raise ValueError("Magnitude difference limit value out of scope, range limited to 0 to 5 magnitudes.")
        else:
            self.mag_diff_limit = input_val
   
    # limiting color difference between target and reference
    def get_col_limit(self):
        return self.col_diff_limit
    
    def set_col_diff_limit(self, input_val):
        if (input_val <= (0 * u.mag) or input_val > (10 * u.mag)):
            raise ValueError("Color difference limit value out of scope, range limited to 0 to 10 magnitudes.")
        else:
            self.col_diff_limit = input_val
            
    # limiting size of region to search for reference stars
    def get_ra_size(self):
        return self.ra_size
    
    def set_ra_size(self, input_val):
        if (input_val <= (0 * u.deg) or input_val > (1 * u.deg)):
            raise ValueError("RA size limit value out of scope, range limited to 0 to 1 degrees.")
        else:
            self.ra_size = input_val
    def get_dec_size(self):
        return self.dec_size
    
    def set_dec_size(self, input_val):
        if (input_val <= (0 * u.deg) or input_val > (1 * u.deg)):
            raise ValueError("DEC size limit value out of scope, range limited to 0 to 1 degrees.")
        else:
            self.dec_size = input_val           
def main ():
    pass

if __name__ == "__main__":
    main()
