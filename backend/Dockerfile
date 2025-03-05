# Используем официальный Python-образ
FROM python:3.11-slim-bookworm

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости, необходимые для работы WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    gcc \
    libgirepository1.0-dev \
    gir1.2-pango-1.0 \
    libcairo2 \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libffi-dev \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*
    
# Копируем файл зависимостей (например, requirements.txt)
COPY . .

# Устанавливаем Python-зависимости
RUN pip install -r requirements.txt

# Открываем порт 8000 для приложения
EXPOSE 8000

# Запускаем приложение через Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]