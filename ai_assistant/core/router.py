# # -*- coding: utf-8 -*-
# from core.parser import parse_command
# from commands.system_info import get_time, get_system_status
# from commands.exec_cmd import run_cmd
# from commands.programs import open_program, close_program
#
# # словарь для статистики команд
# usage = {}
#
# def remember(cmd):
#     usage[cmd] = usage.get(cmd, 0) + 1
#
# def get_top_commands(n=3):
#     return sorted(usage, key=usage.get, reverse=True)[:n]
#
# def handle_command(text, config=None):
#     action, arg = parse_command(text)
#
#     # запоминаем команду
#     remember(action)
#
#     if action == "help":
#         return (
#             "📘 Доступные команды:\n"
#             "\n"
#             "• время — показывает текущее время\n"
#             "• система — загрузка CPU/RAM\n"
#             "• открыть <программа> — открывает приложение\n"
#             "• закрыть <программа> — закрывает приложение\n"
#             "• cmd <команда> — выполнить команду CMD\n"
#             "• выход — завершить работу\n"
#         )
#
#     if action == "time":
#         return get_time()
#
#     if action == "status":
#         return get_system_status()
#
#     if action == "cmd":
#         if not arg:
#             return "Пустая CMD команда."
#         result = run_cmd(arg)
#         return result if isinstance(result, str) else str(result)
#
#     if action == "open":
#         if not arg:
#             return "Кого/что открыть?"
#         return open_program(arg)
#
#     if action == "close":
#         if not arg:
#             return "Кого/что закрыть?"
#         return close_program(arg)
#
#     return "Действие не реализовано."
#
#
# from commands.system import system_commands
# from ui.terminal_ui import ui
#
# def route(user_input: str):
#     text = user_input.strip()
#
#     if not text:
#         return
#
#     cmd = text.split()[0]
#
#     if cmd in system_commands:
#         system_commands[cmd](text)
#     else:
#         handle_ai(text)
#
#
# def handle_ai(text: str):
#     # заглушка ИИ — пока
#     ui.ai("Я обрабатываю твой запрос…")
#     ui.ai(f"(пока думаю над: «{text}»)")


from commands.system import system_commands
from ai.applied import handle as handle_ai
from ui.terminal_ui import ui

def route(user_input: str):
    text = user_input.strip()
    if not text:
        return

    cmd = text.split()[0]

    if cmd in system_commands:
        system_commands[cmd](text)
    else:
        handle_ai(text)
