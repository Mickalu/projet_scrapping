# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:04:40 2020

@author: Thomas
"""

# Import necessary libraries
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

app = tk.Tk()

# Changement of the title and the icon
#app.title("Bitcoin value BTC/EUR")
#app.iconphoto(False, tk.PhotoImage(file="icon.gif"))
#app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file="icon.gif")) //Autre méthode

# Creation of frames
frame_left = tk.Frame(app)
frame_left.pack(side="left", expand=True)
#frame_center = tk.Frame(app)
#frame_center.pack(side="left", expand=True)
frame_right = tk.Frame(app)
frame_right.pack(side="left", expand=True)

# Creation of widgets
fig = Figure()
ax = fig.add_subplot(1,1,1)
ax.plot([], [])
ax.set_title("Bitcoin Value BTC/EUR")
ax.set_xlabel("Date")
ax.set_ylabel("BTC/EUR")
canvas = FigureCanvasTkAgg(fig, master=frame_left)  
canvas.get_tk_widget().pack(fill="both", expand=True)

button_launch_scraping = tk.Button(frame_right, text="Launch Scraping")
button_launch_scraping.pack()