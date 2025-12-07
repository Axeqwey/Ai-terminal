# -*- coding: utf-8 -*-
from core.parser import parse_command
from commands.system_info import get_time, get_system_status
from commands.exec_cmd import run_cmd
from commands.programs import open_program, close_program

def handle_command(text, config=None):
    parsed = parse_command(text)
    if parsed is None:
        return "Не понимаю команду. Попробуй 'время', 'система', 'открыть notepad', 'закрыть notepad', 'cmd ipconfig'."

    action, arg = parsed

    if action == "time":
        return get_time()

    if action == "status":
        return get_system_status()

    if action == "cmd":
        if not arg:
            return "Пустая CMD команда."
        return run_cmd(arg)

    if action == "open":
        if not arg:
            return "Кого/что открыть?"
        return open_program(arg)

    if action == "close":
        if not arg:
            return "Кого/что закрыть?"
        return close_program(arg)

    return "Действие не реализовано."
