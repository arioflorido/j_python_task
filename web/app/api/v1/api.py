from fastapi import APIRouter
from app.api.v1.endpoints import recipe, ingredient

api_router = APIRouter()
api_router.include_router(recipe.router)
api_router.include_router(ingredient.router)
