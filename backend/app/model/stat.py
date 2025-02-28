from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Stat(Base):
    __tablename__ = 'stat'
    
    id = Column(Integer, primary_key=True)
    
    # ID пользователя
    user_id = Column(Integer, ForeignKey('user.id'))
    
    # Дата загрузки
    date = Column(Date)
    
    # ID Документа
    document_id = Column(Integer, ForeignKey('document.id'))
    
    # ID статуса операции
    operation_status_id = Column(Integer, ForeignKey('operation.id'))
    
    user = relationship("User")
    document = relationship("Document")
    operation_status = relationship("Operation")