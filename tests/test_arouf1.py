import tkinter

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np


root = tkinter.Tk()
root.wm_title("s/o'lin")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  

canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

button = tkinter.Button(master=root, text="Quit", command=quit)
button.pack(side=tkinter.BOTTOM)

input_area = tkinter.Canvas(root,width = 500, height = 20)
input_area.pack()

input_box = tkinter.Entry(root)
input_box.place(x=100, y=400)

def get_entry():
    entry = input_box.get()
    print(entry)
    
submit = tkinter.Button(root, text="submit", command=get_entry).place(x=300, y=400)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
canvas.draw()
tkinter.mainloop()

# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.

#if __name__ == "__main__":
#    # execute only if run as a script
#    main()
