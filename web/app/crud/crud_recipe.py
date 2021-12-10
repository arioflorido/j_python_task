from typing import List
from sqlalchemy.orm import Session
from app.models.recipe import Recipe

def get_recipe_by_id(db: Session, id: int) -> Recipe:
    return db.query(Recipe).filter(Recipe.id == id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 100) -> List[Recipe]:
    return db.query(Recipe).offset(skip).limit(limit).all()
