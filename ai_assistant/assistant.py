#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.router import route
from config.settings import load_settings
from core.logger import log_action
from ui.terminal_ui import ui


def print_banner():
    ui.system("╔════════════════════════════════════╗")
    ui.system("║      Wayk :: TERMINAL AI         ║")
    ui.system("╚════════════════════════════════════╝")
    ui.system("Введите команду или вопрос\n")


def main():
    load_settings()  # загружаем, даже если пока не используем
    print_banner()

    while True:
        try:
            user = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            ui.system("Выход. Пока.")
            log_action("Завершение по CTRL+C / EOF.")
            break

        if not user:
            continue

        log_action(f"Ввод: {user}")

        try:
            route(user)
            log_action("Команда обработана.")
        except Exception as e:
            log_action(f"Ошибка: {e}")
            ui.error(f"Ошибка при выполнении: {e}")


if __name__ == "__main__":
    main()
