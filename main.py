# import os
# import json
#
# PROJECT = "ai_assistant"
#
# # Структура (папки → список файлов)
# structure = {
#     PROJECT: {
#         "assistant.py": """\
# from core.router import handle_command
#
# def main():
#     print("ИИ-ассистент запущен. Пиши команду...")
#
#     while True:
#         user = input("> ").strip()
#
#         if user.lower() in ("выход", "exit", "quit"):
#             print("До связи.")
#             break
#
#         result = handle_command(user)
#         if result:
#             print(result)
#
# if __name__ == "__main__":
#     main()
# """,
#
#         "commands": {
#             "__init__.py": "",
#             "system_info.py": """\
# import psutil
# from datetime import datetime
#
# def get_time():
#     return f"Сейчас {datetime.now().strftime('%H:%M:%S')}"
#
# def get_system_status():
#     cpu = psutil.cpu_percent()
#     ram = psutil.virtual_memory().percent
#     return f"CPU: {cpu}%, RAM: {ram}%"
# """,
#
#             "exec_cmd.py": """\
# import subprocess
#
# def run_cmd(command):
#     result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     if result.stdout:
#         return result.stdout
#     if result.stderr:
#         return "Ошибка: " + result.stderr
#     return "Команда выполнена."
# """,
#
#             "programs.py": """\
# import os
# import json
# from config.settings import PATHS_FILE
#
# def open_program(name):
#     if not os.path.exists(PATHS_FILE):
#         return "Файл paths.json не найден."
#
#     with open(PATHS_FILE, "r", encoding="utf-8") as f:
#         data = json.load(f)
#
#     if name not in data:
#         return "Не знаю такой программы."
#
#     path = data[name]
#
#     try:
#         os.startfile(path)
#         return f"Открываю: {path}"
#     except Exception as e:
#         return f"Ошибка: {e}"
# """
#         },
#
#         "core": {
#             "__init__.py": "",
#             "parser.py": """\
# def parse_command(text):
#     text = text.lower()
#
#     if "время" in text:
#         return "time"
#     if "загрузка" in text or "система" in text:
#         return "status"
#     if text.startswith("cmd "):
#         return ("cmd", text[4:])
#     if text.startswith("открой "):
#         return ("open", text.replace("открой ", ""))
#
#     return None
# """,
#
#             "router.py": """\
# from commands.system_info import get_time, get_system_status
# from commands.exec_cmd import run_cmd
# from commands.programs import open_program
# from core.parser import parse_command
#
# def handle_command(text):
#     parsed = parse_command(text)
#
#     if parsed is None:
#         return "Не понимаю команду."
#
#     if parsed == "time":
#         return get_time()
#
#     if parsed == "status":
#         return get_system_status()
#
#     if isinstance(parsed, tuple):
#         cmd, arg = parsed
#
#         if cmd == "cmd":
#             return run_cmd(arg)
#         if cmd == "open":
#             return open_program(arg)
#
#     return "Не понимаю команду."
# """
#         },
#
#         "ai": {
#             "__init__.py": "",
#             "llm_engine.py": """\
# # Здесь потом подключим LLM (OpenAI, Ollama)
# # Пока заглушка.
#
# def ask_ai(prompt):
#     return "ИИ пока спит. Скоро проснётся."
# """
#         },
#
#         "config": {
#             "__init__.py": "",
#             "settings.py": """\
# import os
#
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# PATHS_FILE = os.path.join(BASE_DIR, "config", "paths.json")
# """,
#
#             "paths.json": """\
# {
#     "notepad": "C:/Windows/notepad.exe",
#     "calc": "C:/Windows/system32/calc.exe"
# }
# """
#         },
#
#         "logs": {
#             "assistant.log": ""
#         },
#
#         "requirements.txt": """\
# psutil
# """
#     }
# }
#
#
# # -------------------------------------------
# # Создание структуры
# # -------------------------------------------
#
# def create(path, data):
#     """Создание файлов и папок рекурсивно."""
#     if isinstance(data, str):
#         # создаём файл
#         with open(path, "w", encoding="utf-8") as f:
#             f.write(data)
#         return
#
#     if isinstance(data, dict):
#         # создаём папку
#         os.makedirs(path, exist_ok=True)
#         for name, content in data.items():
#             create(os.path.join(path, name), content)
#
#
# def main():
#     print("Создаю проектную структуру...")
#
#     for root, content in structure.items():
#         create(root, content)
#
#     print("Готово! Проект создан:", PROJECT)
#
#
# if __name__ == "__main__":
#     main()
