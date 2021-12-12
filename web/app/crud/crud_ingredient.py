from typing import List
from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient
from app.models.recipe_ingredient import RecipeIngredient

def get_ingredient_by_recipe_id(db: Session, recipe_id: int) -> List[Ingredient]:
    recipe_ingredients = db.query(RecipeIngredient).filter(RecipeIngredient.recipe_id == recipe_id).all()
    ingredients = [get_ingredient_by_id(db, item.ingredient_id) for item in recipe_ingredients]
    return ingredients

def get_ingredient_by_id(db: Session, id: int) -> Ingredient:
    return db.query(Ingredient).filter(Ingredient.id == id).first()

def get_ingredient_by_name(db: Session, name: str) -> Ingredient:
    return db.query(Ingredient).filter(Ingredient.name == name).first()

def get_ingredients(db: Session, skip: int = 0, limit: int = 100) -> List[Ingredient]:
    return db.query(Ingredient).offset(skip).limit(limit).all()

def upsert_ingredient(db: Session, ingredient_item: dict) -> Ingredient:
    existing_ingredient = db.query(Ingredient).filter(Ingredient.name == ingredient_item['name']).first()
    new_ingredient = Ingredient(**ingredient_item)
    if not existing_ingredient:
        db.add(new_ingredient)
        db.commit()
    else:
        # update if ingredient exist
        if (existing_ingredient.serialize != ingredient_item):
            existing_ingredient.best_before = new_ingredient.best_before
            existing_ingredient.best_before = new_ingredient.use_by
            existing_ingredient.is_expired = new_ingredient.is_expired
            db.commit()

    return new_ingredient

def upsert_ingredients(db: Session, ingredient_items: list) -> List[Ingredient]:
    #TODO: Implement transaction?
    return [upsert_ingredient(db, ingredient) for ingredient in ingredient_items]
