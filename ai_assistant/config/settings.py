# -*- coding: utf-8 -*-
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PATHS_FILE = os.path.join(BASE_DIR, "config", "paths.json")

def load_settings():
    """
    Возвращает словарь путей и настроек из paths.json (или пустой dict).
    """
    try:
        with open(PATHS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {"paths": data}
    except Exception:
        return {"paths": {}}
