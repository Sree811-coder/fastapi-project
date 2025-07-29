from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.user import UserCreate, UserRead
from app.services.auth_service import register_user
from app.db import get_session

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_session)):
    print("🟡 Inside /register endpoint")  # Add this line
    return register_user(user, db)
