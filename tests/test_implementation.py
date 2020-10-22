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
# TODO Eval : Handle eval() errors in update_graph(), maybe try/catch
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
        #self.tk.attributes('-zoomed', True) DEFAULT
        self.tk.attributes('-fullscreen', True) #Fix for Anaconda
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
def update_graph():
    # Get the fields value
    func = input_func.get()
    range_min = float(input_range_min.get())
    range_max = float(input_range_max.get())
    range_step = float(input_step.get())

    # Evaluate the expression and handle error, update the function and the variable
    x = np.arange(range_min, range_max, range_step)
    fx = eval(func)

    # Update the fields content
    input_func.delete(0, END)
    input_func.insert(0, func)

    input_range_min.delete(0, END)
    input_range_min.insert(0, range_min)

    input_range_max.delete(0, END)
    input_range_max.insert(0, range_max)

    input_step.delete(0, END)
    input_step.insert(0, range_step)

    # Clear and update the graph
    fig.clear()
    fig.add_subplot(1,1,1).plot(x, fx)
    fig.canvas.draw_idle()

# TODO Catch the errors in the follow functions to show proper error message
# TODO Cast the 'x' to the expected format for the math.* methods

# @Milan You can remove thos functions if you already handle them

# Define the available mathematical functions
def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def exp(x):
    return math.exp(x)

def fctr(x):
    return math.factorial(x)

# Initiate the window and set its title
windowHandler = WindowHandler()
window = windowHandler.tk
window.wm_title("Geogebruh")
plt.style.use('dark_background')

fig = Figure(figsize=(5, 4), dpi=100)

# Range, graph and expression initialization
range_min = 0
range_max = 10
range_step = .05

x = np.arange(range_min, range_max, range_step)
fx = x**2

# Default math expression is f(t) = t**2
fig.add_subplot(1,1,1).plot(x, fx)

# Draw the graph
canvas = FigureCanvasTkAgg(fig, master=window)  
canvas.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
canvas.draw()

# Add toolbar to the graph, allowing zoom/pan/reset
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

# Generate the submit button
submit = Tkinter.Button(window, text='Tracer', command=update_graph)#.place(x=300, y=400)
submit.pack(side=RIGHT)

# TODO Make the changes alter the real "np.arange(range_min, range_max, range_step)" ranges/step
# Define range/step fields and labels
input_range_min = Entry(window, bd=2, width=5)
input_range_min.insert(0, "0")
input_range_min.pack(side=RIGHT)

label_range_min = Label(window, text="MIN")
label_range_min.pack(side=RIGHT)

input_range_max = Entry(window, bd=2, width=5)
input_range_max.insert(0, "10")
input_range_max.pack(side=RIGHT)

label_range_max = Label(window, text="MAX")
label_range_max.pack(side=RIGHT)

input_step = Entry(window, bd=2, width=5)
input_step.insert(0, ".05")
input_step.pack(side=RIGHT)

label_step = Label(window, text="STEP")
label_step.pack(side=RIGHT)

# Define function input field and labels
input_func = Entry(window, bd=2)
input_func.insert(0, "x**2")
input_func.pack(side=RIGHT)

label_func = Label(window, text="f(x) = ")
label_func.pack(side=RIGHT)

# Maintains the window open
#Tkinter.mainloop()
window.tk.mainloop()

