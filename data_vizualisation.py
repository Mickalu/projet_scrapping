# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:04:40 2020

@author: Thomas
"""

### LIBRARIES #################################################################
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from threading import Thread
import data_scientist as ds

### CLOBAL VARIABLES ##########################################################
GLOBAL_COUNTER = 1

### FLAG ###
update_scrap = False
   

### FUNCTIONS BINDED ##########################################################    
def on_click_launch_update_plot(event):
    global update_scrap
    global thread_scraping
    
    if update_scrap:
        
        update_scrap = False
        thread_scraping.join()
        button_updating_scrap_var.set("Launch scrap")
        return 
        
    else:
        update_scrap = True
        refresh()
        button_updating_scrap_var.set("Stop scrap")
        
        #global thread_scraping
        
        thread_scraping = Thread(target = scrap_thread)
        thread_scraping.start()

def on_closing():
    global update_scrap
    global thread_scraping
    update_scrap = False
    thread_scraping.join()
    app.destroy()


### FUNCTIONS #################################################################
def refresh():
    global update_scrap
    global GLOBAL_COUNTER
    
    df_bitcoin = pd.read_csv("bitcoin_value.csv", sep=";")
    
    if update_scrap:
        print("I'm refresh")
        ax.lines.pop(0)  # detruit l'ancienne ligne
        
        GLOBAL_COUNTER += 1
        ax.plot(df_bitcoin["date"][:GLOBAL_COUNTER], df_bitcoin["bitcoin_value"][:GLOBAL_COUNTER], color="r")  # créer une nouvelle ligne
        
        ax.set_xticklabels(df_bitcoin["date"][:GLOBAL_COUNTER], rotation=45)
        
        canvas.draw()
        statistic_information()
        app.after(1000, refresh) 
    
    else:
        print("je m'arrête")
        return
        
        
def scrap_thread():
    print("je lance mon thread")
    while True:
        global update_scrap
        
        if update_scrap:
            ds.scraping()
        else:
            break
    print("j'ai fini mon thread")

def statistic_information():
    df_bitcoin = pd.read_csv("bitcoin_value.csv", sep=";")
    if len(df_bitcoin) != 0:
        label_text_last_value_var.set("Last value : " + str(df_bitcoin["bitcoin_value"][len(df_bitcoin)-1]) + " EUR")
        label_text_mean_var.set("Mean : " + str(df_bitcoin["bitcoin_value"].mean())[:7] + " EUR")
        label_text_min_var.set("Min : " + str(df_bitcoin["bitcoin_value"].min()) + " EUR")
        label_text_max_var.set("Max : " + str(df_bitcoin["bitcoin_value"].max()) + " EUR")


###############################################################################    
app = tk.Tk()
app["bg"] = "#71BDFF"

### TITLE AND ICON CHANGEMENT ###
app.title("Bitcoin value BTC/EUR")
app.iconphoto(False, tk.PhotoImage(file="icon.gif"))

### FRAMES ####################################################################
frame_left = tk.Frame(app, background="#71BDFF")
frame_left.pack(side="left", expand=True)

frame_center = tk.Frame(app, background="#71BDFF", borderwidth=5, relief="ridge", padx=20)
frame_center.pack(side="left", expand=True)

frame_center_last_value = tk.Frame(frame_center, background="#71BDFF")
frame_center_last_value.pack(side="top")

frame_center_mean = tk.Frame(frame_center, background="#71BDFF")
frame_center_mean.pack(side="top")

frame_center_min = tk.Frame(frame_center, background="#71BDFF")
frame_center_min.pack(side="top")

frame_center_max = tk.Frame(frame_center, background="#71BDFF")
frame_center_max.pack(side="top")

frame_right = tk.Frame(app, background="#71BDFF")
frame_right.pack(side="left", expand=True)

### WIDGETS ###################################################################

### GRAPH WITH MATPLOTLIB ####
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

### LABELS FOR STATISTIC INFORMATION ###
label_text_last_value_var = tk.StringVar()
label_text_last_value = tk.Label(frame_center_last_value, textvariable = label_text_last_value_var, background="#71BDFF", anchor="w")
label_text_last_value.pack(side="left")
label_text_last_value_var.set("Last value : ... EUR")

label_text_mean_var = tk.StringVar()
label_text_mean = tk.Label(frame_center_mean, textvariable = label_text_mean_var, background="#71BDFF", anchor="w")
label_text_mean.pack(side="left")
label_text_mean_var.set("Mean : ... EUR")

label_text_min_var = tk.StringVar()
label_text_min = tk.Label(frame_center_min, textvariable = label_text_min_var, background="#71BDFF", anchor="w")
label_text_min.pack(side="left")
label_text_min_var.set("Min : ... EUR")

label_text_max_var = tk.StringVar()
label_text_max = tk.Label(frame_center_max, textvariable = label_text_max_var, background="#71BDFF", anchor="w")
label_text_max.pack(side="left")
label_text_max_var.set("Max : ... EUR")

### BUTTON ###
button_updating_scrap_var = tk.StringVar()
button_launch_scraping = tk.Button(frame_right, textvariable = button_updating_scrap_var)
button_launch_scraping.pack()
button_updating_scrap_var.set("Launch scrap")

### BINDING ###################################################################
button_launch_scraping.bind("<ButtonRelease-1>", on_click_launch_update_plot)
app.protocol("WM_DELETE_WINDOW", on_closing)


### LAUNCH APP ################################################################
app.mainloop()
ds.delete_data()


