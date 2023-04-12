FastHR
======

FastHR is a Python function efficiently and accurately calculating hardness ratios for X-ray sources using a Bayesian approach.

Quick example
-------------

	from fasthr import *
	import numpy as np
	
	# setup your priors
	psi1_S, psi2_S = 1., 0. # soft-band prior
	psi1_H, psi2_H = 1., 0. # hard-band prior
	
	# Step 0, prepare some external tables
	ygrid = np.linspace(0., 1., 1000)
	lnI = tabul_lnI(100, 100, ygrid, psi1_S, psi1_H)
	np.save("ygrid.npy"), ygrid)
	np.save("lnI.npy", lnI)
	
	# 