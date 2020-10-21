import Tkinter
from Tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

root = Tkinter.Tk()
root.wm_title("s/o'lin")

fig = Figure(figsize=(5, 4), dpi=100)

#Initialisation tableaux
t = np.arange(0, 3, .01)
y = t **2

#Affichage fonction par defaut f(t) = t^2
fig.add_subplot(1,1,1).plot(t, y)

canvas = FigureCanvasTkAgg(fig, master=root)  
canvas.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
canvas.draw()

label1 = Label(root, text="f(t)")
label1.pack( side = LEFT)
inputFctn = Entry(root, bd =5)
inputFctn.pack(side = RIGHT)

def on_key_press():
    value = inputFctn.get()
    y = eval(value)
    fig.clear()
    fig.add_subplot(1,1,1).plot(t, y)
    fig.canvas.draw_idle()


button1 = Tkinter.Button(text='Valider', command=on_key_press)
button1.pack()


Tkinter.mainloop()
