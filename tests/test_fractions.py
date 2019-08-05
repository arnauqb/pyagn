import pytest
import pyagn.sed as sed
from pyagn import constants
from scipy import integrate
import numpy as np
from numpy import testing
from astropy import units as u

M_range = np.geomspace(1e6,1e10,2)
mdot_range = np.geomspace(0.05,1,2)

def test_fraction():
    """
    Tests whether integrating all the fractions of UV times the local luminosity returns the global UV luminosity.
    """
    distance = 1e26
    for M in M_range:
        for mdot in mdot_range:
            print("%e %.2f"%(M,mdot))
            bh = sed.SED(M = M, mdot = mdot, reprocessing = False)
            fraction_list, total_uv_flux, total_flux = bh.compute_uv_fractions(distance, return_flux = True, include_corona = True)
            uvf = total_uv_flux / total_flux
            testing.assert_approx_equal(uvf, bh.uv_fraction, significant = 2)

    

