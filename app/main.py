from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.session import engine
from app.api.v1 import user


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)  # startup logic
    yield  # run app
    # (optional) teardown logic goes here


app = FastAPI(lifespan=lifespan)

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
