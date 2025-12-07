# -*- coding: utf-8 -*-
"""
Простой парсер команд на русском (и базово — на английском).
Возвращает кортеж (action, argument) или строку action или None.
"""

def parse_command(text: str):
    t = text.strip().lower()

    # точные команды
    if t in ("время", "time"):
        return ("time", None)

    if t in ("система", "статус", "status", "sys"):
        return ("status", None)

    # cmd <команда>
    if t.startswith("cmd "):
        return ("cmd", t[4:])

    # открыть / открой / open
    if t.startswith("открыть ") or t.startswith("открой ") or t.startswith("open "):
        # "открыть notepad" -> ("open","notepad")
        # удаляем ведущие слова
        for prefix in ("открыть ", "открой ", "open "):
            if t.startswith(prefix):
                return ("open", t[len(prefix):].strip())

    # закрыть / закрыть процесс / kill / close
    if t.startswith("закрыть ") or t.startswith("убить ") or t.startswith("kill ") or t.startswith("close "):
        for prefix in ("закрыть ", "убить ", "kill ", "close "):
            if t.startswith(prefix):
                return ("close", t[len(prefix):].strip())

    # если просто имя программы — попытаемся открыть
    # например: "notepad"
    if " " not in t and len(t) > 0:
        return ("open", t)

    return None
