from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from app.controller import abc_controller, cm_controller, dbo_controller
from app.core.config import DATABASE_URL

# Движок соединения с Postgres
engine = create_engine(DATABASE_URL)

async def lifespan(app: FastAPI):
    # Код, который выполняется при запуске приложения (startup)
    with engine.begin() as connection:
        with open("app/resources/postgres/data.sql", "r", encoding="utf-8") as file:
            sql_script = file.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    connection.execute(text(statement))

    yield

    # Код, который выполняется при завершении работы приложения (shutdown)
    with engine.begin() as connection:
        with open("app/resources/postgres/clear.sql", "r", encoding="utf-8") as file:
            clear_script = file.read()
            for statement in clear_script.split(';'):
                if statement.strip():
                    connection.execute(text(statement))

# Создаем приложение
app = FastAPI(lifespan=lifespan)
    
# Подключение роутеров
app.include_router(abc_controller.router)
app.include_router(dbo_controller.router)
app.include_router(cm_controller.router)
