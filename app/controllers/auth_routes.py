from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.user import UserCreate, UserRead
from app.services.auth_service import register_user
from app.db import get_session
from app.schemas.user import UserLogin, TokenResponse
from app.services.auth_service import login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_session)):
    print("🟡 Inside /register endpoint")
    return register_user(user, db)


@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin, db: Session = Depends(get_session)):
    token = login_user(data, db)
    return {"access_token": token}
