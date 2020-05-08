# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:06:03 2020

@author: Thomas
"""
# Import necessary libraries
import data_scientist as ds
import data_vizualisation as dv
import pandas as pd

# Constant
GLOBAL_COUNTER = 1
    
def refresh():
    # Read the csv file
    df_bitcoin = pd.read_csv("bitcoin_value.csv")
    """
    global update_graph    
    if not update_graph:
        print("je m'arrete")
        return
    """
    global GLOBAL_COUNTER
    print("I'm refresh")
    dv.ax.lines.pop(0)  # detruit l'ancienne ligne
    GLOBAL_COUNTER += 1
    dv.ax.plot(df_bitcoin["date"][:GLOBAL_COUNTER], df_bitcoin["bitcoin_value"][:GLOBAL_COUNTER])  # créer une nouvelle ligne
    dv.canvas.draw()
    dv.app.after(2000, refresh) 


refresh()

dv.app.mainloop()