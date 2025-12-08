import logging
import os

# Путь к директории логов
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Настройка логирования
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "assistant.log"),
    level=logging.INFO,
    format="%(asctime)s — %(message)s",
    encoding="utf-8"
)

def log_action(text):
    """Записать действие в лог."""
    logging.info(text)
