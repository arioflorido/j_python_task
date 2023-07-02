from fastapi import FastAPI
from app.api.v1.api import api_router
import uvicorn

app = FastAPI()
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, port=8001, host='0.0.0.0')
