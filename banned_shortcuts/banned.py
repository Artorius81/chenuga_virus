import ctypes, sys


def is_admin():
    try:
        # Если админ вернет True
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    sys.coinit_flags = 2
    # Если админ продолжаем скрипт дальше
    pass
else:
    sys.coinit_flags = 2
    # Перезапускаем скрипт с правами админа
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit(0)  # выходим из старой версии скрипта
