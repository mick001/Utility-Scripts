# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 01:40:51 2016

@author: Michy

Given a two sided magnetic circuit, calculate the mutual inductor 
parameters. The mutual inductor is assumed to be connected in series
with a current source.

"""

import numpy as np

# Magnetic reluctances
r1 = 3*10**6/(4*np.pi)
r2 = 10**6/(2*np.pi)
r3 = 10**6/(4*np.pi)

# Windings
N1 =100
N2 = 200

# Magnetic permeances
g1 = 1/r1
g2 = 1/r2
g3 = 1/r3

# Sum of permeances
gsum = g1+g2+g3

# Self and mutual permeances
g11 = g1*(g2+g3)/gsum
g22 = g2*(g1+g3)/gsum
gm = -(g2*g1)/gsum

# Self and mutual inductances
l11 = g11*N1**2
l22 = g22*N2**2
lm = gm*N1*N2

# Equivalent inductances
print(l11 + l22 - 2*lm)
print(l11 + l22 + 2*lm)