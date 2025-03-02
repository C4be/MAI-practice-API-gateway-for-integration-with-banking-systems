from app.repository.base_repository import BaseRepository
from app.model.user_type import UserType

# TODO: дописать необходимые методы
class UserTypeRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = UserType