import os

# Таким решением можно полностью устранить возможность запуска калькулятора или диспетчера задач
# Банально мы переименовываем .exe диспетчера и калькулятора и т.к винда не может найти оригинальные .exe, то процесс
# просто не запускается

def block_task_manager():
    path1 = "C:\Windows\System32\Taskmgr.exe"
    path2 = "C:\Windows\System32\Taskmgr(копия).exe"

    # получем полный доступ к файлу диспетчера задач
    os.system("takeown /f C:\Windows\System32\Taskmgr.exe")
    os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l")
    os.system(
        "icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l")  # убиваем диспетчер задач если он запущен

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
