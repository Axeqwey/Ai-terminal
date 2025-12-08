# -*- coding: utf-8 -*-
import os
import json
import psutil
import subprocess
import signal
import webbrowser
from config.settings import PATHS_FILE

def _load_paths():
    if not os.path.exists(PATHS_FILE):
        return {}
    try:
        with open(PATHS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}



def open_program(path):
    # URL
    if path.startswith("http://") or path.startswith("https://"):
        webbrowser.open(path)
        return f"Открываю URL: {path}"

    # Файл/папка/EXE
    if os.path.exists(path):
        subprocess.Popen([path], shell=True)
        return f"Открываю: {path}"
    return "Путь не найден"

def close_program(name):
    closed = False

    for proc in psutil.process_iter(['pid', 'name']):
        if name.lower() in proc.info['name'].lower():
            try:
                proc.terminate()     # Мягкое завершение
                closed = True
            except:
                pass

    if not closed:
        # Пробуем kill -9
        for proc in psutil.process_iter(['pid', 'name']):
            if name.lower() in proc.info['name'].lower():
                os.kill(proc.pid, signal.SIGKILL)
                closed = True

    return "Закрыто" if closed else "Процесс не найден"

