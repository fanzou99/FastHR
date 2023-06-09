FastHR
======

FastHR is a Python tool that efficiently estimates hardness ratios for X-ray sources using a Bayesian approach.

Install
-------
FastHR can be installed using pip.
	
    pip install fasthr

Usage
-----

> Below is a quick example.

    from fasthr.main import *
    import numpy as np
    
    # setup the priors
    psi1_S, psi2_S = 1., 0. # soft-band prior
    psi1_H, psi2_H = 1., 0. # hard-band prior
    
    # Step 0, prepare some external tables.
    ygrid = np.linspace(0., 1., 100)
    lnI = tabul_lnI(100, 100, ygrid, psi1_S, psi1_H)
    
    # set up the data
    S = 10 # total soft-band counts in the source region
    H = 10 # total hard-band counts in the source region
    e_S = 1. # soft-band exposure time
    e_H = 1. # hard-band exposure time
    xi_S = 5 # the expected soft-band background count rate in the source region
    xi_H = 5 # the expected hard-band background count rate in the source region
    
    # calculate the cumulative posterior of HR.
    # In this example, I assume the background intensity to be exactly known.
    # If you don't want to adopt this assumption, see the examples folder for more details.
    myhr = fasthr(S, H, e_S, e_H, psi1_S, psi2_S, psi1_H, psi2_H, xi_S = xi_S, xi_H = xi_H)
    myhr.init_hrcdf("fixed")
    hrgrid, cdfgrid = myhr.calc_hrcdf(ygrid, lnI)
    
    # obtain characteristic point estimators.
    lower_err, median, upper_err = np.interp([0.16, 0.5, 0.84], cdfgrid, hrgrid)

Further usages could be found under the *examples* folder.

The algorithm is explained in Appendix A of [Zou et al. (2023)](https://arxiv.org/abs/2304.09904). Please consider citing this publication if you use FastHR in your research.

Contact
-------
If you have any queries or feedback, feel free to contact Fan Zou (Penn State University; fuz64@psu.edu).
