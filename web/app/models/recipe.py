from sqlalchemy import Column, Integer, String, Boolean
from app.database.session import Base

class Recipe(Base):
    """Defines the recipes model"""

    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_available = Column(Boolean)

    def __init__(self, title: str):
        self.title = title
        self.is_available = False

    def __repr__(self) -> str:
        return f'<Recipe {self.title}>'

    @property
    def serialize(self):
        """
        Return recipe in serializeable format
        """
        return {
            'title': self.title,
            'ingredients': self.ingredients
            }
