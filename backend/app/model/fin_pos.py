from sqlalchemy import Column, Integer, String
from .base import Base

class FinPos(Base):
    __tablename__ = 'fin_pos'
    
    id = Column(Integer, primary_key=True)
    
    # Тип финансовой позиции - [банкрот, малоимущий, средний заработок, высокий заработок]
    pos = Column(String)