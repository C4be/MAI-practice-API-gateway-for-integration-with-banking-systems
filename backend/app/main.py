from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from app.controller import abc_controller, cm_controller, dbo_controller
from app.core.config import DATABASE_URL, DATABASE_MONGO_URL, MONGO_DB_NAME
from app.core.logger import setup_logger
import requests
import json
import os
from contextlib import asynccontextmanager
import asyncio
from weasyprint import HTML
from app.core.dependencies import get_db, create_tables, drop_tables, load_guide_tables


postgres = get_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Выполняется при запуске и завершении работы приложения"""

    create_tables()
    load_guide_tables()
    
    # Заполняем БД при запуске
    # with engine.begin() as connection:
    #     with open("app/resources/postgres/data.sql", "r", encoding="utf-8") as file:
    #         sql_script = file.read()
    #         for statement in sql_script.split(';'):
    #             if statement.strip():
    #                 connection.execute(text(statement))
    

    yield  # Дальше работает приложение

    # TODO: отключить при продашене
    drop_tables()
    # Очищаем БД при завершении работы
    # with engine.begin() as connection:
    #     with open("app/resources/postgres/clear.sql", "r", encoding="utf-8") as file:
    #         clear_script = file.read()
    #         for statement in clear_script.split(';'):
    #             if statement.strip():
    #                 connection.execute(text(statement))


def save_docs():
    """Сохраняет документацию OpenAPI в PDF"""

    docs_url = "http://127.0.0.1:8086/docs"  # URL Swagger UI
    save_path = "app/resources/openapi.pdf"

    try:
        response = requests.get(docs_url)
        response.raise_for_status()

        # Генерируем PDF из HTML
        HTML(string=response.text).write_pdf(save_path)

        print(f"✅ OpenAPI документация сохранена в {save_path} (PDF)")

    except requests.RequestException as e:
        print(f"❌ Ошибка при сохранении документации: {e}")


# Настройка логгера
logger = setup_logger()

# Создаем приложение с lifespan
app = FastAPI(lifespan=lifespan)

# Подключение роутеров
app.include_router(abc_controller.router)
app.include_router(dbo_controller.router)
app.include_router(cm_controller.router)


@app.get("/")
def read_root():
    # save_docs()  # TODO: не забыть вклчить
    return {"message": f"postgre = {DATABASE_URL}\nmongo = {DATABASE_MONGO_URL}"}
