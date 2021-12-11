from typing import List
from sqlalchemy.orm import Session
from app.models.recipe import Recipe

def get_recipe_by_id(db: Session, id: int) -> Recipe:
    return db.query(Recipe).filter(Recipe.id == id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 100) -> List[Recipe]:
    return db.query(Recipe).offset(skip).limit(limit).all()

def add_recipe(db: Session, recipe_item: dict) -> Recipe:
    new_recipe = Recipe(**recipe_item)
    db.add(new_recipe)
    db.commit()
    return new_recipe

def add_recipes(db: Session, recipe_items: list) -> List[Recipe]:
    #TODO: Implement transaction?
    return [add_recipe(db, ingredient) for ingredient in recipe_items]
