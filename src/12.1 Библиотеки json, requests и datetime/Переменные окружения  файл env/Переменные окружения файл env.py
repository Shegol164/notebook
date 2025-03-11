"""Использование .env-файла"""

import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
# Получение значения переменной GITHUB_TOKEN из .env-файла
github_token = os.getenv("GITHUB_TOKEN")
# Создание заголовка с токеном доступа API
headers = {"Authorization": f"token {github_token}"}
# Отправка GET-запроса к API
response = requests.get("https://api.github.com/user", headers=headers)
# Обработка ответа
print(response.json())

"""Шаблон файла .env"""
"""Чтобы все разработчики в команде имели представление о том, какие переменные окружения необходимы для работы проекта и как они должны быть организованы, создание шаблона .env -файла (часто называемого .env.example или .env.sample) является важной частью работы над проектом. Такой файл должен быть включен в отслеживаемые Git файлы для облегчения настройки проекта."""
# Создайте файл .env из копии этого файла и замените значения переменных реальными данными
# Конфигурация базы данных
DATABASE_HOST = localhost  # Хост для базы данных
DATABASE_USER = username  # Имя пользователя базы данных
DATABASE_PASSWORD = password  # Пароль базы данных
DATABASE_NAME = mydatabase  # Имя базы данных

# API-ключи
API_KEY = your_api_key_here
GITHUB_TOKEN = your_github_token_here
