from typing import List
from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient

def get_ingredient_by_recipe_id(db: Session, recipe_id: int) -> List[Ingredient]:
    return db.query(Ingredient).filter(Ingredient.recipe_id == recipe_id).all()

def get_ingredient_by_id(db: Session, id: int) -> Ingredient:
    return db.query(Ingredient).filter(Ingredient.id == id).first()

def get_ingredients(db: Session, skip: int = 0, limit: int = 100) -> List[Ingredient]:
    return db.query(Ingredient).offset(skip).limit(limit).all()
