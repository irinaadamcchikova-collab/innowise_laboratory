FROM python:3.12-slim

WORKDIR /code

# Сначала копируем только requirements для кэширования слоёв
COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Потом копируем код приложения
COPY main.py /code/main.py

# Запускаем приложение (порт 80 — стандарт для продакшена в контейнере)
CMD ["fastapi", "run", "main.py", "--port", "80"]