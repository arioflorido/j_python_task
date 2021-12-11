from typing import List
from sqlalchemy.orm import Session
from app.models.recipe_ingredient import RecipeIngredient

def add_recipe_ingredient(db: Session, recipe_id: int, ingredient_id: int) -> RecipeIngredient:
    new_recipe_ingredient = db.query(RecipeIngredient).filter(RecipeIngredient.recipe_id == recipe_id and RecipeIngredient.ingredient_id == ingredient_id).first()
    if new_recipe_ingredient is None:
        new_recipe_ingredient = RecipeIngredient(recipe_id=recipe_id, ingredient_id=ingredient_id)
        db.add(new_recipe_ingredient)
        db.commit()
    return new_recipe_ingredient

