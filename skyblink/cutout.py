from astropy.wcs import WCS
from astropy.nddata import Cutout2D
from astropy.coordinates import SkyCoord
import astropy.units as u

def make_cutout(image, header, ra_deg, dec_deg, size_arcmin):
    wcs = WCS(header)
    center =SkyCoord(ra=ra_deg * u.deg, dec=dec_deg * u.deg, frame="icrs")
    size = size_arcmin * u.arcmin
    cutout = Cutout2D(image, position=center, size=size, wcs=wcs)
    return cutout