# -*- coding: utf-8 -*-
"""
Парсер команд. Возвращает (action, argument)
"""

def parse_command(text):
    text = text.lower().strip()

    aliases = {
        "open": ["открой", "запусти", "открыть"],
        "close": ["закрой", "закрыть", "останови"],
        "time": ["время", "который час"],
        "status": ["система", "пк", "нагрузка", "cpu", "ram"],
        "disk": ["диск", "место", "память"],
        "net": ["сеть", "интернет", "ип", "ip"],
        "cmd": ["команда", "выполни", "cmd"],
        "help": ["помощь", "что ты умеешь", "команды", "help", "хелп"],

    }

    # --- 1) CMD-команда (особый случай) ---
    # Пример: "cmd ipconfig"
    if text.startswith("cmd "):
        return ("cmd", text[4:].strip())

    # --- 2) Общие команды ---
    for action, keys in aliases.items():
        for k in keys:
            if text.startswith(k):
                arg = text[len(k):].strip()
                return (action, arg)

    return ("unknown", "")
