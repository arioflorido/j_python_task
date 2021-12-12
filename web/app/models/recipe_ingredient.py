from sqlalchemy import Column, Integer, ForeignKey
from app.database.session import Base

class RecipeIngredient(Base):
    """Defines the association model of recipe_ingredient"""

    __tablename__ = 'recipe_ingredient'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))

    def __init__(self, recipe_id: int, ingredient_id: int):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id

    def __repr__(self) -> str:
        return f"<RecipeIngredient {self.recipe_id}|{self.ingredient_id}>"

    def __bool__(self):
        if self.id is None:
            return False
        return True
