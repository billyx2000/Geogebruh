import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
x=np.linspace(-19,14,100000)
plt.plot(x,8*np.sin(x))  # on utilise la fonction sinus de Numpy
plt.ylabel('fonction 8*sinus')
plt.xlabel("l'axe des abcisses")
plt.show()