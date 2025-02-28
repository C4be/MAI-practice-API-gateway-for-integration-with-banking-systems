from sqlalchemy.orm import Session

class BaseRepository:
    """
    Базовый класс который описывает логику репозитория
    """
    
    def __init__(self, session: Session):
        self.session = session
        self.model = None  # TODO: проверить, перезапишется ои при наследовании

    def get_by_id(self, id: int):
        return self.session.query(self.model).get(id)

    def get_all(self):
        return self.session.query(self.model).all()

    def create(self, entity):
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self, entity):
        self.session.commit()
        return entity

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()