from fastapi import APIRouter
from app.api.v1.endpoints import recipe, ingredient

API_VERSION = "/api/v1"

api_router = APIRouter()
api_router.include_router(recipe.router, prefix=API_VERSION)
api_router.include_router(ingredient.router, prefix=API_VERSION)
