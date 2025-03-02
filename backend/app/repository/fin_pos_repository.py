from app.repository.base_repository import BaseRepository
from app.model.fin_pos import FinPos

# TODO: дописать необходимые методы
class FinPosRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = FinPos