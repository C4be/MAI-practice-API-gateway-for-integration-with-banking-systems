from app.repository.document_repository import DocumentRepository
from sqlalchemy.orm import Session

class DocumentService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.document_repository = DocumentRepository(db_session)    
        
    def get_doc_by_id(self, doc_id: int):
        return self.document_repository.get_by_id(doc_id)