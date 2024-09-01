from fastapi import FastAPI
from . import models
from .database import engine
from .routers import items
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router, prefix=settings.API_V1_STR + "/items", tags=["items"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI template!"}
