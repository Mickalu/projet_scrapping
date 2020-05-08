# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:06:03 2020

@author: Thomas
"""
# Import necessary libraries
import data_scientist as ds
import data_vizualisation as dv
import pandas as pd 
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Constant
GLOBAL_COUNTER = 1

# Read the csv file
df_bitcoin = pd.read_csv("bitcoin_value.csv")
date_list = df_bitcoin["date"]
bitcoin_list = df_bitcoin["bitcoin_value"]

def update_plot():
    global GLOBAL_COUNTER
    dv.fig.delaxes(dv.fig.get_axes()[0])
    subplot_1 = dv.fig.add_subplot(1,1,1)
    date_list = df['Date'][:GLOBAL_COUNTER].to_list()

    for column in column_list:
        value_list = df[column][:GLOBAL_COUNTER].to_list()
        line = subplot_1.plot_date([date_list],[value_list])
    canvas.draw()


def refresh():
    global GLOBAL_COUNTER
    print("refresh")
    dv.app.after(500, refresh)
    update_plot()
    GLOBAL_COUNTER+=1

