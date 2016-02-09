# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:14:19 2016

@author: Michy

Threephase unbalanced circuit solver

### Description ###
This short snippet of code is aimed at solving canonical threephase circuits.
It is useful for doing a quick check if calculating everything by hand.

Note that a mutual inductor can be included in the circuit. The mutual
inductor is taken into account by transformating it in the equivalent Y circuit.
If you do not wish to include a mutual inductor in the simulation just set to
0 self and  mutual inductances (l11,l22 and lm)

"""

import numpy as np

# Angular speed (rad/s)
w = 1000

# Self and mutual inductance for the mutual inductor (Henry)
l11 = 0
l22 = 0
lm = 0

# Inductances of the equivalent Y circuit (Henry)
l1 = l11 - lm
l2 = l22 - lm
l3 = lm

# Load impedences (Ohm)
z1 = 20 - 2j + l1 * w *1j
z2 = 20 + 20j + 8j + l2 * w *1j
z3 = 10 - 20j + 12j + lm * w *1j

# Threephase source (Volt)
vs1 = 200
vs2 = 200*np.exp(-2j*np.pi/3)
vs3 = 200*np.exp(-4j*np.pi/3)

# Votage across the whole line
Vo = (vs1/z1 + vs2/z2 + vs3/z3)/(1/z1 + 1/z2 + 1/z3)

# Phase currents
I1 = (vs1 - Vo)/z1
I2 = (vs2 - Vo)/z2
I3 = (vs3 - Vo)/z3

# Phase voltage (Volt)
V1 = z1 * I1
V2 = z2 * I2
V3 = z3 * I3

# Apparent power (VA)
Svs = vs1 * np.conj(I1) + vs2 * np.conj(I2) + vs3 * np.conj(I3)

# Real power (Watt)
P = np.real(z1) * I1 * np.conj(I1) + np.real(z2) * I2 * np.conj(I2)+ np.real(z3) * I3 * np.conj(I3)

print(P)
print(Svs)
print("...done!")