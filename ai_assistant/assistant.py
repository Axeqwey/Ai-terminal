#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from core.router import handle_command
from config.settings import load_settings
from core.logger import log_action


def print_banner():
    print("╔════════════════════════════════════╗")
    print("║  Терминальный ИИ-ассистент (demo) ║")
    print("╚════════════════════════════════════╝")
    print(
        "Напиши команду (пример: 'время', 'система', 'открыть notepad', 'закрыть notepad', 'cmd ipconfig', 'выход')\n")


def main():
    cfg = load_settings()
    print_banner()

    while True:
        try:
            user = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nВыход. Пока.")
            log_action("Завершение по CTRL+C / EOF.")
            break

        if not user:
            continue

        log_action(f"Ввод: {user}")

        if user.lower() in ("выход", "exit", "quit"):
            print("До связи.")
            log_action("Завершение по команде пользователя.")
            break

        try:
            result = handle_command(user, cfg)
            if result:
                print(result)
            log_action(f"Результат: {result}")
        except Exception as e:
            log_action(f"Ошибка при обработке команды: {e}")
            print("При выполнении команды произошла ошибка:", e)


if __name__ == "__main__":
    main()
