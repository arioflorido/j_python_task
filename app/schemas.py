from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str

class RecipeBase(BaseModel):
    title: str
    ingredients: list
