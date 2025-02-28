from base_repository import BaseRepository
from model.document import Document

# TODO: дописать необходимые методы
class DocumentRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = Document