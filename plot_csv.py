# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:02:49 2016

@author: Michy
@name: Quick .csv plot
@description: Plot a csv as quickly as possible from cmd line
@example of cmd line command: python .\plot_csv.py file1.csv
@note: Remember to set path before running or comment path out and pass it as an argument

"""

path = "C://users//michy//desktop//"

import sys
import pandas as pd
import matplotlib.pyplot as plt

# Remember to add .csv extension
fileName = sys.argv[1]

# Print name of file plotted
print(""" 

Plotting %s

""" %(fileName))

# Plot file
try:
	path = path + fileName
	y = pd.read_csv(path)
	plt.plot(range(len(y)),y)
	plt.show()
except Exception as e:
	print("Exception triggered:")
	print(str(e))
	print("\n")
