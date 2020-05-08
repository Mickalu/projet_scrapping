# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:02:20 2020

@author: lucas
"""


import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("bitcoin_value.csv")

plt.plot(dataFrame['date'], dataFrame['bitcoin value'])