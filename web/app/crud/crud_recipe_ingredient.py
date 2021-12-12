from typing import List
from sqlalchemy.orm import Session
from app.models.recipe_ingredient import RecipeIngredient

def upsert_recipe_ingredient(db: Session, recipe_id: int, ingredient_id: int) -> RecipeIngredient:
    existing_recipe_ingredient = db.query(RecipeIngredient).filter(RecipeIngredient.recipe_id == recipe_id, RecipeIngredient.ingredient_id == ingredient_id).first()
    new_recipe_ingredient = RecipeIngredient(recipe_id=recipe_id, ingredient_id=ingredient_id)
    if not existing_recipe_ingredient:
        new_recipe_ingredient = RecipeIngredient(recipe_id=recipe_id, ingredient_id=ingredient_id)
        db.add(new_recipe_ingredient)
        db.commit()
    return new_recipe_ingredient

