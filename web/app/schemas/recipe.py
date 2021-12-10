from pydantic import BaseModel

class RecipeBase(BaseModel):
    title: str
    ingredients: list
