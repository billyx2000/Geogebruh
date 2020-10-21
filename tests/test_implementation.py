#!/usr/bin/python3

# Initial @Milan
# Modified @Grraahaam
#
# Dynamic user entry + Graph design and maybe more
#
# Tkinter documentation : https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm
# MatPlotLib documentation : https://matplotlib.org/3.3.2/py-modindex.html
#
# TODO Improve layout : toolbar Increase left-margin + Decrease top-margin
# TODO Improve layout : Label/Input/Button Increase right-margin + Increase top-margin
# TODO Improve layout : Maybe put the interaction bar at the top?
# TODO Eval : Handle eval() errors in get_input(), maybe try/catch
# TODO Eval : Sanitize and verify user input before sending to eval()
#	Do we need the lexical_analysis then?


# Import Tkinter methods (Window interface)
import Tkinter
from Tkinter import *

# Import Numpy (math mathods) and Matplotlib (Graph generation)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# Import the math native library
import math

# Create the window handler class (allowing fullscreen, and ESC to escape)
class WindowHandler:

    def __init__(self):
        self.tk = Tk()
	# This just maximizes it so we can see the window, it is not fullscreen.
        self.tk.attributes('-zoomed', True)
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
	# Just switch the state
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

# Function getting input field value
def get_input():
    value = inputFctn.get()
    # Evaluate the expression and handle error
    y = eval(value)
    inputFctn.delete(0, END)
    inputFctn.insert(0, value)
    fig.clear()
    fig.add_subplot(1,1,1).plot(t, y)
    fig.canvas.draw_idle()

# TODO Catch the errors in the follow functions to show proper error message
# TODO Cast the 'x' to the expected format for the math.* methods
# Define the available mathematical functions
def sqrt(x):
    return math.sqrt(x)

def sin(x):
    #x = str(x)
    #print(type(x))
    return math.sin(float(str(x)))

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def exp(x):
    return math.exp(x)

def fctr(x):
    return math.factorial(x)

# Initiate the window and set its title
#window = Tkinter.Tk()
windowHandler = WindowHandler()
window = windowHandler.tk
window.wm_title("Geogebruh")
plt.style.use('dark_background')

fig = Figure(figsize=(5, 4), dpi=100)

# Graph and expression initialization
t = np.arange(0, 3, .01)
y = t**2

# Default math expression is f(t) = t**2
fig.add_subplot(1,1,1).plot(t, y)

# Draw the graph
canvas = FigureCanvasTkAgg(fig, master=window)  
canvas.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
canvas.draw()

# Add toolbar to the graph, allowing zoom/pan/reset
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

# Generate the submit button
submit = Tkinter.Button(window, text='Valider', command=get_input)#.place(x=300, y=400)
submit.pack(side=RIGHT)

# Define input field
inputFctn = Entry(window, bd=2)
inputFctn.insert(0, "t**2")
inputFctn.pack(side=RIGHT)
#inputFctn.place(x=100, y=400)

# Set window label
label1 = Label(window, text="f(t) = ")
label1.pack(side=RIGHT)

# Maintains the window open
#Tkinter.mainloop()
window.tk.mainloop()

