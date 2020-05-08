# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:02:20 2020

@author: lucas
"""


import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("bitcoin_value.csv")

dataframe_date = dataFrame['date']
dataframe_bitcoin_value = dataFrame['bitcoin_value']

plt.plot(dataframe_date, dataframe_bitcoin_value)
plt.show()