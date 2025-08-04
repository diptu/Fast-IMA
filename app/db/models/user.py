# app/db/model/user
from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False, unique=True)
    email: str = Field(index=True, nullable=False, unique=True)
    full_name: Optional[str] = Field(default=None)
    hashed_password: str = Field(nullable=False, min_length=60)
    is_active: bool = Field(default=True)
