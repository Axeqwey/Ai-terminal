# -*- coding: utf-8 -*-
import os
import json
import psutil
import platform
from config.settings import PATHS_FILE

def _load_paths():
    if not os.path.exists(PATHS_FILE):
        return {}
    try:
        with open(PATHS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def open_program(name_or_path):
    """
    Открывает программу: либо по ключу из paths.json, либо по прямому пути.
    Возвращает строку статуса.
    """
    paths = _load_paths()
    target = name_or_path.strip()

    # если имя есть в paths.json
    if target in paths:
        target_path = paths[target]
    else:
        target_path = target  # считаем, что это путь или имя исполняемого файла

    # Windows: os.startfile, unix: subprocess
    try:
        if platform.system().lower().startswith("win"):
            # os.startfile работает с путём или ассоциацией
            os.startfile(target_path)
        else:
            # попытаемся выполнить в фоне
            import subprocess
            subprocess.Popen([target_path])
        return f"Открываю: {target_path}"
    except Exception as e:
        return f"Не получилось открыть '{target}': {e}"

def close_program(name_or_pid):
    """
    Закрывает процесс по имени или pid.
    Если передано число — интерпретируется как PID.
    Иначе — имя процесса (частичное совпадение допускается).
    """
    target = str(name_or_pid).strip()

    # если PID
    if target.isdigit():
        pid = int(target)
        try:
            p = psutil.Process(pid)
            p.terminate()
            return f"Отправлен сигнал завершения процессу PID={pid}."
        except Exception as e:
            return f"Не удалось завершить PID={pid}: {e}"

    # иначе ищем по имени (частичное совпадение)
    matched = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if target.lower() in (proc.info.get('name') or '').lower():
                matched.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not matched:
        return f"Процессы с именем, содержащим '{target}', не найдены."

    results = []
    for p in matched:
        try:
            p.terminate()
            results.append(f"{p.info.get('name')} (PID={p.info.get('pid')}) — завершён.")
        except Exception as e:
            results.append(f"{p.info.get('name')} (PID={p.info.get('pid')}) — не завершён: {e}")

    return "\n".join(results)
