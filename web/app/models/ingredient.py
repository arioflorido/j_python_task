from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database.session import Base
from datetime import date

class Ingredient(Base):
    """Defines the ingredients model"""

    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    best_before = Column(Date)
    use_by = Column(Date)

    def __init__(self, name: str, best_before: date, use_by: date):
        self.name = name
        self.best_before = best_before
        self.use_by = use_by

    def __repr__(self) -> str:
        return f'<Ingredient {self.name}>'

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {
            'name': self.name
            }
