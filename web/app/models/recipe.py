from sqlalchemy import Column, Integer, String
from app.database.session import Base

class Recipe(Base):
    """Defines the recipes model"""

    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __init__(self, title: str, ingredients: dict):
        self.title = title
        self.ingredients = ingredients

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
