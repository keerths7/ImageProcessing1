from tkinter import *
from color_detection import *
from colortobnwng import *
from cart import *
from blacknwtocolor import *

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

window = Tk()
window.title("Userchoice")
window.geometry("690x469")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 469,
    width = 690,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = resource_path(f"background.png"))
background = canvas.create_image(
    345.0, 234.5,
    image=background_img)

img0 = PhotoImage(file = resource_path(f"img0.png"))
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = colortobnwng,
    relief = "flat")

b0.place(
    x = 378, y = 161,
    width = 268,
    height = 54)

img1 = PhotoImage(file = resource_path(f"img1.png"))
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = cartoonizze,
    relief = "flat")

b1.place(
    x = 378, y = 254,
    width = 268,
    height = 50)

img2 = PhotoImage(file = resource_path(f"img2.png"))
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = Detect,
    relief = "flat")

b2.place(
    x = 378, y = 72,
    width = 268,
    height = 51)

img3 = PhotoImage(file = resource_path(f"img3.png"))
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = bnwtocolor,
    relief = "flat")

b3.place(
    x = 378, y = 339,
    width = 268,
    height = 54)

window.resizable(False, False)
window.mainloop()
