
# Import system library (used to test python version)
import sys

# Import our own library (tokenization and evaluation)
import lib_fct as Lf

# Import Tkinter methods (Window interface)
if sys.version_info[0] == 3:
    # Python3 (lowercase 't')
    import tkinter as Tk
    from tkinter import messagebox
else:
    # Python2 (uppercase 't')
    import Tkinter as Tk
    from Tkinter import messagebox

# Import Numpy (math mathods) and Matplotlib (Graph generation)
import numpy as np

# FONCTION: INTERFACE GRAPHIQUE
# Create the window handler class (allowing fullscreen, and ESC to escape)
class WindowHandler:

    def __init__(self):
        self.tk = Tk.Tk()
	# This just maximizes it so we can see the window, it is not fullscreen.
        #self.tk.attributes('-zoomed', True)
        self.tk.attributes('-fullscreen', True) # Fix for Jupiter/Anaconda
        self.frame = Tk.Frame(self.tk)
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

# FONCTION: INTERFACE GRAPHIQUE + EVALUATEUR
# Function getting input field value
def UpdateGraph(fig, input_func, input_range_min, input_range_max, input_step):
    # Get the fields value
    func_input = input_func.get()
    range_min = float(input_range_min.get())
    range_max = float(input_range_max.get())
    range_step = float(input_step.get())

    # Analyse the inputed expression
    func_token = Lf.LexicalAnalysis(func_input)

    # Return parsed and evaluated function string
    func_parsed = Lf.VerifToken(func_token)

    # DEBUG
    #print(func_parsed)
    #print(type(func_parsed))

    # Update the new interval and step
    x = np.arange(range_min, range_max, range_step)

    # Evaluate the expression and handle error, update the function and the variable
    try:
        fx = eval(func_parsed)

        # Update the fields content
        func_expr = func_parsed
        input_func.delete(0, Tk.END)
        input_func.insert(0, func_expr.replace("np.", ''))

        input_range_min.delete(0, Tk.END)
        input_range_min.insert(0, range_min)

        input_range_max.delete(0, Tk.END)
        input_range_max.insert(0, range_max)

        input_step.delete(0, Tk.END)
        input_step.insert(0, range_step)

        # Clear and update the graph
        fig.clear()
        fig.add_subplot(1,1,1).plot(x, fx)
        fig.canvas.draw_idle()
    except:
        #print("[DEBUG] Your input is wrong!")
        messagebox.showwarning("Warning", "Your input(s) are incorrect")
        pass

