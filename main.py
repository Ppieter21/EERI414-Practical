import tkinter as tk
import os
import time
#import numpy as np
#from PIL import Image, ImageTk
#from numpy.fft import fftshift
from matplotlib.image import imread
import matplotlib.pyplot as plt

import cmath

import matplotlib
import matplotlib.backends.backend_agg as agg


WIDTH, HEIGHT = 1000,562
SAMPLINGRATE = 128
AMOUNT = 2
ImageSize = 256
root = tk.Tk()
root.minsize(WIDTH, HEIGHT)
root.title("EERI 414 Practical:  IIR Digital high-pass filter")
BG = tk.PhotoImage(file = os.path.join("Images", "background.png"))
lblBG = tk.Label(root, image = BG)
lblBG.place(x = 0, y = 0)
root.configure(background = "navy")

def btnGenerateClick():
    pass

def btnAnalogClick():
    pass


def btnDigitalClick():
    pass


def btnRealizeClick():
    pass


def btnCompareClick():
    pass



       
btngenerate = tk.Button(root, text = "Generate signal",command=btnGenerateClick)
btngenerate.place(x=WIDTH*0.2,y=HEIGHT*0.1)

btnAnalog = tk.Button(root, text = "Analog domain",command=btnAnalogClick)
btnAnalog.place(x=WIDTH*0.2,y=HEIGHT*0.2)

btnDigital = tk.Button(root, text = "Digital domain",command=btnDigitalClick)
btnDigital.place(x=WIDTH*0.2,y=HEIGHT*0.3)

btnRealize = tk.Button(root, text = "Realize filter",command=btnRealizeClick)
btnRealize.place(x=WIDTH*0.2,y=HEIGHT*0.4)

btnCompare = tk.Button(root, text = "Input vs output of filter",command=btnCompareClick)
btnCompare.place(x=WIDTH*0.2,y=HEIGHT*0.5)



root.mainloop()
