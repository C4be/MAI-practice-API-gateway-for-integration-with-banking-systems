from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Contract(Base):
    __tablename__ = 'contract'
    
    id = Column(Integer, primary_key=True)
    
    # ID клиента
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # ID документа
    document_id = Column(Integer, ForeignKey('document.id'))
    
    # ID статуса операции
    oper_status_id = Column(Integer, ForeignKey('oper_status.id'))
    
    user = relationship("User")
    document = relationship("Document")
    oper_status = relationship("OperStatus")