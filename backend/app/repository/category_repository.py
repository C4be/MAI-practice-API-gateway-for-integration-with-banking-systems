from base_repository import BaseRepository
from model.category import Category

# TODO: дописать необходимые методы
class CategoryRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
        self.model = Category