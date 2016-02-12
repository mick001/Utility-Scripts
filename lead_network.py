# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:37:11 2016

@author: Michy
@Description: Phase margin increase using a lead network 
	(for control systems) as a function of alpha.
	
	
	1 + T * s
	------------------
	1 + alpha * T * s
	
	Phase margin icrease has the following expression:
	
	arctan(1/sqrt(alpha)) - arctan(sqrt(alpha))
	
	For alpha -> 0 deltaphm -> 90 degrees
	For alpha -> 1 deltaphm -> 0 degrees
	
	Note that 0 < alpha < 1
	
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np

# Alpha parameter
alpha = np.linspace(0.001,1,50)

# Phase margin increase (in radians)
deltaphm = np.arctan(1/np.sqrt(alpha))-np.arctan(np.sqrt(alpha))

# Phase margin increase (in degrees)
deltaphm_d = (deltaphm)/np.pi*180

# Plot
plt.plot(alpha,deltaphm_d)
plt.show()