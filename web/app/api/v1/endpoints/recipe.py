from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_session
from app.schemas.recipe import RecipeBase

router = APIRouter()

@router.get("/recipe/{id}", response_model=RecipeBase)
def read_recipe(id: int, db: Session = Depends(get_session)):
    recipe = crud.get_recipe_by_id(db=db, id=id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    recipe.ingredients = get_recipe_ingredients(db, recipe)
    return recipe.serialize

@router.get("/recipes/", response_model=List[RecipeBase])
def read_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    recipes = crud.get_recipes(db=db, skip=skip, limit=limit)
    for recipe in recipes:
        recipe.ingredients  = get_recipe_ingredients(db, recipe)
    return [i.serialize for i in recipes]

def get_recipe_ingredients(db, recipe):
    return [ingredient.name for ingredient in crud.get_ingredient_by_recipe_id(db=db, recipe_id=recipe.id)]
