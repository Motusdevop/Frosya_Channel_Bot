# syntax=docker/dockerfile:1

FROM python:3.11-alpine

# Рабочая директория внутри контейнера
WORKDIR /app

# Устанавливаем зависимости (только pip + зависимости для сборки колёс)
RUN pip install --no-cache-dir --upgrade pip

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Переменные окружения
ENV PYTHONUNBUFFERED=1 \
    TZ=UTC

# Запускаем бота
CMD ["python", "src/main.py"]