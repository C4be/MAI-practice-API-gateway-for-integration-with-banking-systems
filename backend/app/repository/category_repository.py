from app.repository.base_repository import BaseRepository
from app.model.category import Category

# TODO: дописать необходимые методы
class CategoryRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = Category