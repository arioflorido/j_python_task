from typing import List
from sqlalchemy.orm import Session
from app.models.recipe import Recipe

def get_recipe_by_id(db: Session, id: int) -> Recipe:
    return db.query(Recipe).filter(Recipe.id == id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 100) -> List[Recipe]:
    return db.query(Recipe).offset(skip).limit(limit).all()

def add_recipe(db: Session, recipe_item: dict) -> Recipe:
    existing_recipe = db.query(Recipe).filter(Recipe.title == recipe_item['title']).first()
    new_recipe = Recipe(**recipe_item)
    if not existing_recipe:
        db.add(new_recipe)
        db.commit()
    else:
        if new_recipe.serialize != existing_recipe.serialize:
            existing_recipe.title = new_recipe.title
            existing_recipe.is_available = new_recipe.is_available
            db.commit()
    return new_recipe

def add_recipes(db: Session, recipe_items: list) -> List[Recipe]:
    #TODO: Implement transaction?
    return [add_recipe(db, ingredient) for ingredient in recipe_items]
