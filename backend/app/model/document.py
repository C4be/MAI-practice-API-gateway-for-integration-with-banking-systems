from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Document(Base):
    __tablename__ = 'document'
    
    id = Column(Integer, primary_key=True)
    
    # Ссылка из файловой BD
    link = Column(String)
    
    # Описание документа
    description = Column(String)
    
    # ID пользователя
    user_id = Column(Integer, ForeignKey('user.id'))
    
    # ID работника оформившего документ
    worker_id = Column(Integer, ForeignKey('user.id'))
    
    # ID Категория документа
    category_id = Column(Integer, ForeignKey('category.id'))
    
    # Дата с которой актуальна запись
    actual_date = Column(Date)
    
    # Дата с которой запись не актуальна
    actual_end_date = Column(Date)
    
    # Планавая дата закрытия/недействительности
    plan_maturity_date = Column(Date)
    
    # Фактическая дата закрытия/недействительности
    fact_maturity_date = Column(Date)
    
    user = relationship("User", foreign_keys=[user_id])
    worker = relationship("User", foreign_keys=[worker_id])
    category = relationship("Category")