from sqlalchemy import Column, Integer, String
from .base import Base

class Systems(Base):
    __tablename__ = 'systems'
    
    id = Column(Integer, primary_key=True)
    
    # Система в которой у пользователя есть права - [ДБО, АБС, СМ, нет]
    system_name = Column(String)