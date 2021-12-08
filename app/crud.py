from sqlalchemy.orm import Session
from models import Ingredient, Recipe

def get_ingredient_by_id(db: Session, id: int) -> Ingredient:
    return db.query(Ingredient).filter(Ingredient.id == id).first()

def get_recipe_by_id(db: Session, id: int) -> Recipe:
    return db.query(Recipe).filter(Recipe.id == id).first()
