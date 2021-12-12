from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import false
from app.database.session import Base

class Recipe(Base):
    """Defines the recipes model"""

    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_available = Column(Boolean)
    is_fresh = Column(Boolean)
    ingredients = list()

    def __init__(self, title: str, is_fresh: bool, is_available: bool):
        self.title = title
        self.is_fresh = is_fresh
        self.is_available = is_available

    def __repr__(self) -> str:
        return f'<Recipe {self.title}>'

    @property
    def serialize(self):
        """
        Return recipe in serializeable format
        """
        return {
            'title': self.title,
            'is_fresh': self.is_fresh,
            'is_available': self.is_available,
            'ingredients': self.ingredients
            }

    def __bool__(self):
        if self.id is None:
            return False
        return True
