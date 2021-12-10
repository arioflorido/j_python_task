from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_session
from app.schemas.ingredient import IngredientBase

router = APIRouter()

@router.get("/ingredient/{id}", response_model=IngredientBase)
def read_ingredient(id: int, db: Session = Depends(get_session)):
    ingredient = crud.get_ingredient_by_id(db=db, id=id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient.serialize

@router.get("/ingredients/", response_model=List[IngredientBase])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    ingredients = crud.get_ingredients(db=db, skip=skip, limit=limit)
    return [i.serialize for i in ingredients]
