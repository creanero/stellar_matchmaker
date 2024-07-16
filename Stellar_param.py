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
        
        

def main ():
    pass

if __name__ == "__main__":
    main()
