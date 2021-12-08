from pydantic import BaseModel

class IngredientBase(BaseModel):
    id: int
    name: str

class RecipeBase(BaseModel):
    id: int
    name: str
