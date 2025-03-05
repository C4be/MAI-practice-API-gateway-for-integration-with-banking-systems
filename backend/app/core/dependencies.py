from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL, DATABASE_MONGO_URL, MONGO_DB_NAME
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket
from app.model.base import Base
from app.model.fin_pos import FinPos
from app.model.sex import Sex
from app.model.user_type import UserType
from app.model.systems import Systems
from app.model.category import Category
from app.model.doc_status import DocStatus
from app.model.oper_status import OperStatus

# === Postgres depencies ===

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)
    
def drop_tables():
    Base.metadata.drop_all(bind=engine)


def load_guide_tables():
    db = next(get_db())
    
    fin_pos = [
        FinPos(pos='bankrupt'),
        FinPos(pos='poor'),
        FinPos(pos='average earnings'),
        FinPos(pos='high earnings')
    ]
    
    sex = [
        Sex(sex='men'),
        Sex(sex='women')
    ]
    
    user_type = [
        UserType(type='client'),
        UserType(type='worker'),
        UserType(type='admin')        
    ]
    
    systems = [
        Systems(system_name='ДБО'),
        Systems(system_name='АБС'),
        Systems(system_name='СМ')
    ]
    
    category = [
        Category(type='credit'),
        Category(type='report')
    ]
    
    doc_stat = [
        DocStatus(doc_status='LOADED_FROM_USER'),
        DocStatus(doc_status='READY_TO_CONTRACT'),
        DocStatus(doc_status='LOADED_PROCESS_SUCCESS'),
        DocStatus(doc_status='ACTUAL'),
        DocStatus(doc_status='DEPRICATED'),
    ]
    
    oper_stat = [
        OperStatus(oper_status = 'SUCCESS'),
        OperStatus(oper_status = 'FALL'),
    ]
    
    db.add_all(fin_pos)
    db.add_all(sex)
    db.add_all(user_type)
    db.add_all(systems)
    db.add_all(category)
    db.add_all(doc_stat)
    db.add_all(oper_stat)
    db.commit()
    db.close()
    
    
    

# Функция для получения сессии с базой данных
# Эта функция будет использоваться в качестве генератора для работы с сессиями SQLAlchemy
# Все операции с базой данных будут выполняться в рамках одной сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# === Mongo depencies ===  

# Подключение к MongoDB (асинхронный клиент)
mongo_client = AsyncIOMotorClient(DATABASE_MONGO_URL)
mongo_db = mongo_client[MONGO_DB_NAME]
mongo_fs = AsyncIOMotorGridFSBucket(mongo_db)