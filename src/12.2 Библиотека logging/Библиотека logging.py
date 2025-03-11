import logging

name = "Alice"
age = 30

# Выводим сообщение в лог
logging.info (f"Имя: {name}, возраст: {age}")
"""Уровни логирования"""
# app_logger.debug("Это сообщение уровня DEBUG")
# app_logger.info("Это сообщение уровня INFO")
# app_logger.warning("Это сообщение уровня WARNING")
# app_logger.error("Это сообщение уровня ERROR")
# app_logger.critical("Это сообщение уровня CRITICAL")
"""Создание и получение логеров"""
import logging
# Получение корневого логера
root_logger = logging.getLogger()
# Создание и получение именованного логера
app_logger = logging.getLogger("my_application")
"Установка уровня логирования"
app_logger = logging.getLogger("my_application")
app_logger.setLevel(logging.DEBUG)
