from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Contract(Base):
    __tablename__ = 'contract'
    
    id = Column(Integer, primary_key=True)
    
    # ID клиента
    user_id = Column(Integer, ForeignKey('user.id'))
    
    # ID документа
    document_id = Column(Integer, ForeignKey('document.id'))
    
    # ID статуса операции
    operation_status_id = Column(Integer, ForeignKey('operation.id'))
    
    user = relationship("User")
    document = relationship("Document")
    operation_status = relationship("Operation")