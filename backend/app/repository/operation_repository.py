from base_repository import BaseRepository
from model.operation import Operation

# TODO: дописать необходимые методы
class OperationRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = Operation