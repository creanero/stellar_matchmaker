from astropy import units as u
from astropy.coordinates import SkyCoord

class observation:

    def __init__(self):
        self.mag_limit = 0 *u.mag
        self.col_limit = 0 *u.mag
        self.ra_size = 0 *u.deg
        self.dec_size = 0 *u.deg

def main ():
    pass

if __name__ == "__main__":
    main()
