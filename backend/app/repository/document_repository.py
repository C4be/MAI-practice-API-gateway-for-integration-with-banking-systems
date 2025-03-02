from app.repository.base_repository import BaseRepository
from sqlalchemy.orm import Session
from app.model.document import Document

# TODO: дописать необходимые методы
class DocumentRepository(BaseRepository):
    def __init__(self,  db_session: Session):
        super().__init__(db_session)
        self.model = Document