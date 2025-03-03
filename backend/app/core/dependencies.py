from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import DATABASE_URL
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorGridFSBucket  # ✅ Асинхронный GridFS
import gridfs
from app.core.config import *


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# Подключение к MongoDB (асинхронный клиент)
mongo_client = AsyncIOMotorClient(DATABASE_MONGO_URL)
mongo_db = mongo_client[MONGO_DB_NAME]

# ✅ Асинхронный GridFS
mongo_fs = AsyncIOMotorGridFSBucket(mongo_db)