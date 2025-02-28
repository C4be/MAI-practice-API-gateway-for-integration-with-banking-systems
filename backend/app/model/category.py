from sqlalchemy import Column, Integer, String
from .base import Base

class Category(Base):    
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    
    # Тип документа - [кредитный договор, выписка из счета, ...]
    type = Column(String)