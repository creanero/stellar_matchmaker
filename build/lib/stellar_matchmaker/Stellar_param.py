#get target star information from user 
from astropy import units as u
from astropy.coordinates import SkyCoord

class stellar_param:

    def __init__(self):
        self.ra = 0 *u.deg
        self.dec = 0 *u.deg
        self.G = 0      #filter G from https://www.cosmos.esa.int/web/gaia/dr3-passbands
        self.bp=0.0     #filter bp 
        self.rp=0.0     #fileter rp 
        
    def get_ra(self):
        return self.ra  

    def set_ra(self, input_val):
        if (input_val < (0 * u.deg) or input_val >= (360 * u.deg)):
            raise ValueError("RA value out of scope, range limited to 0 to 360 degrees.")
        else:
            self.ra = input_val
        
    def get_dec(self):
        return self.dec  

    def set_dec(self, input_val):
        if (input_val < (-90 * u.deg) or input_val > (90 * u.deg)):
            raise ValueError("Dec value out of scope, range limited to -90 to +90 degrees.")
        else:
            self.dec = input_val
        
    def get_G(self):
        return self.G  

    def set_G(self, input_val):
        if (input_val < (-1.5 * u.mag) or input_val >= (21 * u.mag)):
            # https://www.aanda.org/articles/aa/full_html/2021/08/aa40735-21/aa40735-21.htm Gaia DR paper
            raise ValueError("Gaia G magnitude value out of scope, range limited by Gaia limiting magnitude.")
        else:
            self.G = input_val
        
    def get_bp(self):
        return self.bp  

    def set_bp(self, input_val):
        if (input_val < (-1.5 * u.mag) or input_val >= (21 * u.mag)):
            # https://www.aanda.org/articles/aa/full_html/2021/08/aa40735-21/aa40735-21.htm Gaia DR paper
            raise ValueError("Gaia bp magnitude value out of scope, range limited by Gaia limiting magnitude.")
        else:
            self.bp = input_val
        
    def get_rp(self):
        return self.rp  

    def set_rp(self, input_val):
        if (input_val < (-1.5 * u.mag) or input_val >= (21 * u.mag)):
            # https://www.aanda.org/articles/aa/full_html/2021/08/aa40735-21/aa40735-21.htm Gaia DR paper
            raise ValueError("Gaia rp magnitude value out of scope, range limited by Gaia limiting magnitude.")
        else:
            self.rp = input_val
                
    

def main ():
    pass

if __name__ == "__main__":
    main()
