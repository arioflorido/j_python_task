from typing import List
from sqlalchemy.orm import Session
from app.models.models.ingredient import Ingredient
from app.models.models.recipe import Recipe

def get_ingredient_by_recipe_id(db: Session, recipe_id: int) -> List[Ingredient]:
    return db.query(Ingredient).filter(Ingredient.recipe_id == recipe_id).all()

def get_ingredient_by_id(db: Session, id: int) -> Ingredient:
    return db.query(Ingredient).filter(Ingredient.id == id).first()

def get_ingredients(db: Session, skip: int = 0, limit: int = 100) -> List[Ingredient]:
    return db.query(Ingredient).offset(skip).limit(limit).all()

def get_recipe_by_id(db: Session, id: int) -> Recipe:
    return db.query(Recipe).filter(Recipe.id == id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 100) -> List[Recipe]:
    return db.query(Recipe).offset(skip).limit(limit).all()
