from fastapi import FastAPI
from app.API.routes import router

app = FastAPI()

app.include_router(router)