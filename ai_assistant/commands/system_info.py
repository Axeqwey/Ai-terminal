# -*- coding: utf-8 -*-
import psutil
from datetime import datetime

def get_time():
    """Возвращает текущее локальное время."""
    return f"Сейчас: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def get_system_status():
    """Возвращает простую сводку по CPU и памяти."""
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    total_gb = mem.total / (1024**3)
    used_percent = mem.percent
    return (
        f"CPU загрузка: {cpu:.1f}%\n"
        f"RAM: {used_percent:.1f}% ({mem.used / (1024**3):.2f} GB / {total_gb:.2f} GB)\n"
        f"Процессов: {len(psutil.pids())}"
    )
