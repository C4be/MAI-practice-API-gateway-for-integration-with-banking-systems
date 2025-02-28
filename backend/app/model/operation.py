from sqlalchemy import Column, Integer, String
from .base import Base

class Operation(Base):
    __tablename__ = 'operation'
    
    id = Column(Integer, primary_key=True)
    
    # Статус операции - [...]
    status = Column(String)