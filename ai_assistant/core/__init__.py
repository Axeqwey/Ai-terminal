from ui.terminal_ui import ui

def help_cmd(_):
    ui.system("Доступные команды:")
    ui.system("• help — помощь")
    ui.system("• exit — выход")
    ui.system("• clear — очистка экрана")

def exit_cmd(_):
    ui.system("Сеанс завершён.")
    exit(0)

def clear_cmd(_):
    import os
    os.system("cls" if os.name == "nt" else "clear")

system_commands = {
    "help": help_cmd,
    "exit": exit_cmd,
    "clear": clear_cmd,
}
