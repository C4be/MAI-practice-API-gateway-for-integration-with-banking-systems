from app.repository.base_repository import BaseRepository
from app.model.stat import Stat

# TODO: дописать необходимые методы
class StatRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = Stat