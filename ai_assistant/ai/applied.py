from core.old_handler import handle_command
from ui.terminal_ui import ui

def handle(text):
    result = handle_command(text)

    if result:
        ui.ai(result)
