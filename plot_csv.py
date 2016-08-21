# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:02:49 2016

@author: Michy
@name: Quick .csv plot
@description: Plot a csv as quickly as possible from cmd line
@example: example of use from terminal (or cmd): python plot_csv.py file1.csv x y
@notes:
    1. Default path is current working directory
    2. Default file encoding is utf-16
    3. By default header parameter in pd.read_csv is set to 0. Note that the
    .csv may have an arbitrary number of columns (variables).

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

# Default path is cwd. Comment out if you don't need it.
path = os.getcwd()

# Remember to add .csv extension to the file name.
fileName = sys.argv[1]
# x label name
x_ = sys.argv[2]
# y label name
y_ = sys.argv[3]

# Print name of file plotted and other info
print("""

Plotting %s \n
variables plotted:
x \t %s
y \t %s

""" % (fileName, x_, y_))

# Plot file
try:
    df = pd.read_csv(fileName, header = 0, encoding = "utf-16")
    x = df[x_]
    y = df[y_]
    plt.plot(x, y)
    plt.show()
except Exception as e:
    print("Exception triggered:")
    print(str(e))
    print("\n")
