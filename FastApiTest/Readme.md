1. Пишем в `requirements.txt` все необходимые зависимости
2. Устанавливаем их `pip install -r requirements.txt` 
3. Запуск сервера `uvicorn app.main:app --reload --host 0.0.0.0 --port 8080` в режиме разработки