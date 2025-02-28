from fastapi import FastAPI
from app.controller import abc_controller, cm_controller, dbo_controller

# Создаем приложение
app = FastAPI()

# Подключение роутеров
app.include_router(abc_controller.router)
app.include_router(dbo_controller.router)
app.include_router(cm_controller.router)
