from sqlalchemy import Column, Integer, String, Date, Boolean
from app.database.session import Base
from datetime import date, datetime

today = date.today()

class Ingredient(Base):
    """Defines the ingredients model"""

    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    best_before = Column(Date)
    use_by = Column(Date)
    is_expired = Column(Boolean)

    def __init__(self, name: str, best_before: str, use_by: str):
        self.name = name
        self.best_before = best_before
        self.use_by = use_by
        self.is_expired = datetime.strptime(use_by, '%Y-%m-%d').date() > today

    def __repr__(self) -> str:
        return f'<Ingredient {self.name}>'

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {
            'name' : self.name,
            'use_by' : str(self.use_by),
            'best_before' : str(self.best_before)
            }
