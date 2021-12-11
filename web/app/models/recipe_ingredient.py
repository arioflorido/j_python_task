from sqlalchemy import Column, Integer, ForeignKey
from app.database.session import Base

class RecipeIngredient(Base):
    """Defines the association model of recipe_ingredient"""

    __tablename__ = 'recipe_ingredient'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    ingredient_id = Column(Integer, ForeignKey("recipe.id"))

    def __init__(self, id: int, recipe_id: int, ingredient_id: int):
        self.id = id
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id

    def __repr__(self) -> str:
        return f"<Recipe # {self.recipe_id}>"
