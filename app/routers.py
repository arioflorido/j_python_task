from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
from database import SessionLocal, engine
from schemas import IngredientBase, RecipeBase

models.Base.metadata.create_all(bind=engine)
router = APIRouter()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@router.get("/ingredient/{id}", response_model=IngredientBase)
def read_item(id: int, db: Session = Depends(get_session)):
    ingredient = crud.get_ingredient_by_id(db=db, id=id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient.serialize

@router.get("/ingredients/", response_model=List[IngredientBase])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    ingredients = crud.get_ingredients(db=db, skip=skip, limit=limit)
    return [i.serialize for i in ingredients]

@router.get("/recipe/{id}", response_model=RecipeBase)
def read_item(id: int, db: Session = Depends(get_session)):
    recipe = crud.get_recipe_by_id(db=db, id=id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe.serialize

@router.get("/recipes/", response_model=List[RecipeBase])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    recipes = crud.get_recipes(db=db, skip=skip, limit=limit)
    return [i.serialize for i in recipes]
