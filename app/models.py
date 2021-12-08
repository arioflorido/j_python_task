from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base


class Ingredient(Base):
    """Defines the ingredients model"""

    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    best_before = Column(Date)
    use_by = Column(Date)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))

    def __init__(self, id: int, name: str, recipe_id: int):
        self.id = id
        self.name = name
        self.recipe_id = recipe_id

    def __repr__(self) -> str:
        return f"<Ingredient {self.name}>"

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {
            "name": self.name
            }


class Recipe(Base):
    """Defines the recipes model"""

    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __init__(self, id: int, title: str, ingredients: dict):
        self.id = id
        self.title = title
        self.ingredients = ingredients

    def __repr__(self) -> str:
        return f"<Recipe {self.title}>"

    @property
    def serialize(self):
        """
        Return recipe in serializeable format
        """
        return {
            "title": self.title,
            "ingredients": self.ingredients
            }
