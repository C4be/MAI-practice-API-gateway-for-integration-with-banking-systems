from sqlalchemy import Column, Integer, String
from .base import Base

class OperStatus(Base):
    __tablename__ = 'oper_status'
    
    id = Column(Integer, primary_key=True)
    
    # Статус операции - [...]
    oper_status = Column(String)