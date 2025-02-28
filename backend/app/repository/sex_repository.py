from base_repository import BaseRepository
from model.sex import Sex

# TODO: дописать необходимые методы
class SexRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = Sex