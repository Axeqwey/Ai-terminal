# -*- coding: utf-8 -*-
import platform

import psutil
from datetime import datetime

def get_time():
    """Возвращает текущее локальное время."""
    return f"Сейчас: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


def get_system_status():
    data = {}

    data["cpu_percent"] = psutil.cpu_percent(interval=1)
    data["ram_percent"] = psutil.virtual_memory().percent
    data["ram_used"] = psutil.virtual_memory().used
    data["ram_total"] = psutil.virtual_memory().total

    # Температура
    try:
        temps = psutil.sensors_temperatures()
        data["temperatures"] = {k: [t.current for t in v] for k, v in temps.items()}
    except:
        data["temperatures"] = "Не поддерживается"

    # Батарея
    try:
        batt = psutil.sensors_battery()
        if batt:
            data["battery"] = {
                "percent": batt.percent,
                "plugged": batt.power_plugged
            }
        else:
            data["battery"] = "Нет батареи"
    except:
        data["battery"] = "Не поддерживается"

    data["os"] = platform.platform()
    data["time"] = datetime.now().strftime("%H:%M:%S")

    return data
