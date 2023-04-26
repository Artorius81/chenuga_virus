import tkinter as tk
from ctypes import *
from tkinter import ttk
from tkinter.messagebox import showerror

# while True:

window = tk.Tk()


def open_error():
    showerror(title="Пиздец", message="Бля ну вот даже не пробуй")


def disable_alt_f4():
    open_error()
    pass


window.attributes('-fullscreen', True)
window.configure(background="red")
window.title("Chenuga")

label = tk.Label(window, text="Chenuga")
label.pack()
window.protocol("WM_DELETE_WINDOW", disable_alt_f4)
# windll.user32.BlockInput(True)
window.mainloop()
