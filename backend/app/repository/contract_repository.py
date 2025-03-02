from app.repository.base_repository import BaseRepository
from app.model.contract import Contract

# TODO: дописать необходимые методы
class ContractRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = Contract