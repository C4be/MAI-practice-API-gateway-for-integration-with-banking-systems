# Используем официальный Python-образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости, необходимые для работы WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \    
    python3-dev \
    libpq-dev \
    gcc
    
# Копируем файл зависимостей (например, requirements.txt)
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install  -r requirements.txt

# Копируем код приложения в контейнер
COPY . .

# Открываем порт 8000 для приложения
EXPOSE 8000

# Запускаем приложение через Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
