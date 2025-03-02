from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    
    # Имя
    first_name = Column(String)
    
    # Фамилия
    last_name = Column(String)
    
    # Отчество
    middle_name = Column(String)
    
    # День рождения
    birthday = Column(Date)
    
    # ID финансовой позиции
    fin_position_id = Column(Integer, ForeignKey('fin_pos.id'))
    
    # Адресс места жительства
    address = Column(String)
    
    # ИНН - Идентификационный Номер Налогоплательщика
    inn = Column(Integer)
    
    # ID пола
    sex_id = Column(Integer, ForeignKey('sex.id'))
    
    # ID пользователя
    user_type_id = Column(Integer, ForeignKey('user_type.id'))
    
    fin_position = relationship("FinPos")
    user_type = relationship("UserType")
    sex = relationship("Sex")