from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from typing import Annotated, List

from app.db.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.db.session import get_session
from app.core.security import hash_password

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()


@router.post("/", response_model=UserRead)
def create_user(payload: UserCreate, session: SessionDep) -> UserRead:
    db_user = User(
        username=payload.username,
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=hash_password(payload.password),  # ✅ bcrypt hash
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/", response_model=List[UserRead])
def list_users(
    session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100
) -> List[UserRead]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, session: SessionDep) -> UserRead:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}
