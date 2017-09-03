# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:52:18 2015

@author: Michy
@description:
    Simple function to solve linear systems

        Y = A X

    by appling

        X = A^(-1) Y

    where
        Y: column vector of known terms
        A: coefficient matrix (squared non singular matrix)
        X: unknown terms vector

@example:

    A = np.matrix('1 2; 3 4')
    y = np.matrix('2; 4')
    print(solveSystem(y,A))

"""

import numpy as np

# Solver function
def solveSystem(y,A):

    if np.linalg.det(A) == 0:
        print("Warning: determinant of A is 0. Returning NaN")
        return np.nan
    else:
        if A.shape[1] == y.shape[0]: 
            return np.linalg.inv(A) * y
        else:
            raise ValueError("Number of columns of A must be equal to the number of rows of y!")

if __name__ == '__main__':
    A = np.matrix('1 2; 3 4')
    y = np.matrix('2; 4')
    print(solveSystem(y,A))
    
