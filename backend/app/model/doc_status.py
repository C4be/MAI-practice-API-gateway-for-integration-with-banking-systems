from sqlalchemy import Column, Integer, String
from .base import Base

class DocStatus(Base):
    __tablename__ = 'doc_status'
    
    id = Column(Integer, primary_key=True)
    
    # Статус документа - [...]
    doc_status = Column(String)