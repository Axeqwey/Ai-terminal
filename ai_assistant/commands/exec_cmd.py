# -*- coding: utf-8 -*-
import subprocess
import shlex
import platform

def run_cmd(command):
    """
    Выполняет команду в оболочке и возвращает stdout или stderr.
    Будь осторожен: команда выполняется локально.
    """
    # на Windows лучше запускать через shell=True для команд типа dir
    is_windows = platform.system().lower().startswith("win")

    try:
        if is_windows:
            # используем shell=True, чтобы команды типа dir/cls работали
            proc = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        else:
            # на Unix безопаснее парсить
            parts = shlex.split(command)
            proc = subprocess.run(parts, capture_output=True, text=True, encoding="utf-8")

        out = proc.stdout.strip()
        err = proc.stderr.strip()
        if out:
            return out
        if err:
            return "Ошибка:\n" + err
        return "Команда выполнена (без вывода)."
    except Exception as e:
        return f"Не удалось выполнить команду: {e}"
