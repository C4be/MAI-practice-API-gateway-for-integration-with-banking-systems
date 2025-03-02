from app.repository.base_repository import BaseRepository
from sqlalchemy.orm import Session
from app.model.document import Document
from app.model.user import User
import logging

logger = logging.getLogger(__name__)

class DocumentRepository(BaseRepository):
    def __init__(self,  db_session: Session):
        super().__init__(db_session)
        self.model = Document
        
    def get_doc_by_FIO(self, first_name: str, last_name: str, middle_name: str):
        user = self.session.query(User).filter(
            User.first_name == first_name,
            User.last_name == last_name,
            User.middle_name == middle_name
        ).first()
        
        logger.warning(user)

        return self.session.query(self.model).filter(self.model.user_id == user.id).all() if user else []