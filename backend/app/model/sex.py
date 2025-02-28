from sqlalchemy import Column, Integer, String
from .base import Base

class Sex(Base):
    __tablename__ = 'sex'
    
    id = Column(Integer, primary_key=True)
    
    # пол - [муж, жен]
    sex = Column(String)