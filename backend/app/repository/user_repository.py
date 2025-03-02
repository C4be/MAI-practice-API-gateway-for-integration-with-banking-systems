from app.repository.base_repository import BaseRepository
from app.model.user import User

# TODO: дописать необходимые методы
class UserRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = User