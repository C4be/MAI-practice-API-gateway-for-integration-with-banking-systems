from sqlalchemy import Column, Integer, String
from .base import Base

class UserType(Base):
    __tablename__ = 'user_type'
    
    id = Column(Integer, primary_key=True)
    
    # Тип пользователя - [клиент, рабочий, администратор]
    type = Column(String)