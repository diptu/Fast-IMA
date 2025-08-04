from sqlmodel import SQLModel
from typing import Optional


class UserBase(SQLModel):
    username: str
    email: str
    full_name: Optional[str] = None
    isActive: Optional[bool] = True


class UserCreate(UserBase):
    password: str  # plaintext input


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
