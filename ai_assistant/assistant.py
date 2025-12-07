#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.router import handle_command
from config.settings import load_settings
import logging
import os

# Инициализация логов
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "assistant.log"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    encoding="utf-8"
)

def print_banner():
    print("╔════════════════════════════════════╗")
    print("║  Терминальный ИИ-ассистент (demo) ║")
    print("╚════════════════════════════════════╝")
    print("Напиши команду (пример: 'время', 'система', 'открыть notepad', 'закрыть notepad', 'cmd ipconfig', 'выход')\n")

def main():
    cfg = load_settings()  # загружает config/paths.json и т.п.
    print_banner()

    while True:
        try:
            user = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nВыход. Пока.")
            break

        if not user:
            continue

        logging.info("Ввод: %s", user)

        if user.lower() in ("выход", "exit", "quit"):
            print("До связи.")
            logging.info("Завершение по команде пользователя.")
            break

        try:
            result = handle_command(user, cfg)
            if result:
                # если результат многострочный — печатаем как есть
                print(result)
            logging.info("Результат: %s", str(result))
        except Exception as e:
            logging.exception("Ошибка при обработке команды")
            print("При выполнении команды произошла ошибка:", e)

if __name__ == "__main__":
    main()
