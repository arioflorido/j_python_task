# from logging import debug
from fastapi import FastAPI, APIRouter
from app.api.v1.api import api_router
import uvicorn

app = FastAPI()
root_router = APIRouter()
app.include_router(api_router)
app.include_router(root_router)

if __name__ == '__main__':
    uvicorn.run(app, port=8001, host='0.0.0.0', debug=True)
