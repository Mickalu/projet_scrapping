# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:04:40 2020

@author: Thomas
"""

# Import necessary libraries
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from threading import Thread
import data_scientist as ds
from statistics import mean

# Constant
GLOBAL_COUNTER = 1
update_scrap = False
    
def refresh():
    global update_scrap
    global GLOBAL_COUNTER
    
    df_bitcoin = pd.read_csv("bitcoin_value.csv", sep=";")
    """
    global update_graph    
    if not update_graph:
        print("je m'arrete")
        return
    """
    if update_scrap:
        print("I'm refresh")
        ax.lines.pop(0)  # detruit l'ancienne ligne
        
        GLOBAL_COUNTER += 1
        ax.plot(df_bitcoin["date"][:GLOBAL_COUNTER], df_bitcoin["bitcoin_value"][:GLOBAL_COUNTER])  # créer une nouvelle ligne
        
        ax.set_xticklabels(df_bitcoin["date"][:GLOBAL_COUNTER], rotation=90)
        
        canvas.draw()
        statistic_information()
        app.after(1000, refresh) 
    
    else:
        return
        
def on_click_launch_update_plot(event):
    global update_scrap
    
    if update_scrap:
        
        update_scrap = False
        
        button_updating_scrap_var.set("Launch scrap")
        return 
        
    else:
        update_scrap = True
        refresh()
        button_updating_scrap_var.set("Stop scrap")
        
        global thread_scraping
        
        thread_scraping = Thread(target = scrap_thread)
        thread_scraping.start()
        
def scrap_thread():
    while True:
        global update_scrap
        
        if update_scrap:
            ds.scraping()
        else:
            break

def statistic_information():
    df_bitcoin = pd.read_csv("bitcoin_value.csv", sep=";")
    #df = df_bitcoin.apply(pd.to_numeric, errors='coerce')
    if len(df_bitcoin) != 0:
        label_text_last_value_var.set("Last value : " + str(df_bitcoin["bitcoin_value"][len(df_bitcoin)-1]))
        label_text_mean_var.set("Mean : " + str(df_bitcoin["bitcoin_value"].mean())[:7])
        label_text_min_var.set("Min : " + str(df_bitcoin["bitcoin_value"].min()))
        label_text_max_var.set("Max : " + str(df_bitcoin["bitcoin_value"].max()))
    else:
        label_text_last_value_var.set("Last value : ")
        label_text_mean_var.set("Mean : ")
        label_text_min_var.set("Min : ")
        label_text_max_var.set("Max : ")
        
app = tk.Tk()

# Changement of the title and the icon
app.title("Bitcoin value BTC/EUR")
app.iconphoto(False, tk.PhotoImage(file="icon.gif"))
# app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file="icon.gif")) //Autre méthode

# Creation of frames
frame_left = tk.Frame(app)
frame_left.pack(side="left", expand=True)

frame_center = tk.Frame(app)

frame_center.pack(side="left", expand=True)

frame_center_last_value = tk.Frame(frame_center)
frame_center_last_value.pack(side="top")

frame_center_mean = tk.Frame(frame_center)
frame_center_mean.pack(side="top")

frame_center_min = tk.Frame(frame_center)
frame_center_min.pack(side="top")

frame_center_max = tk.Frame(frame_center)
frame_center_max.pack(side="top")

frame_right = tk.Frame(app)
frame_right.pack(side="left", expand=True)

# Creation of widgets
# Graph
fig = Figure()
fig.autolayout : True
fig.set_figheight(7)
fig.set_figwidth(9)

ax = fig.add_subplot(1,1,1)


ax.plot([], [])
ax.set_title("Bitcoin Value BTC/EUR")

ax.set_xlabel("Date")
ax.set_ylabel("BTC/EUR")


canvas = FigureCanvasTkAgg(fig, master=frame_left)  
canvas.get_tk_widget().pack(fill="both", expand=True)

label_text_last_value_var = tk.StringVar()
label_text_mean_var = tk.StringVar()
label_text_min_var = tk.StringVar()
label_text_max_var = tk.StringVar()

# Statistic
label_text_last_value = tk.Label(frame_center_last_value, textvariable = label_text_last_value_var )
label_text_last_value.pack(side="left")

label_text_mean = tk.Label(frame_center_mean, textvariable = label_text_mean_var)
label_text_mean.pack(side="left")

label_text_min = tk.Label(frame_center_min, textvariable = label_text_min_var)
label_text_min.pack(side="left")

label_text_max = tk.Label(frame_center_max, textvariable = label_text_max_var)
label_text_max.pack(side="left")

statistic_information()

# Button
button_updating_scrap_var = tk.StringVar()

button_launch_scraping = tk.Button(frame_right, textvariable = button_updating_scrap_var)

button_updating_scrap_var.set("Launch scrap")

button_launch_scraping.pack()
button_launch_scraping.bind("<ButtonRelease-1>", on_click_launch_update_plot)

app.mainloop()


