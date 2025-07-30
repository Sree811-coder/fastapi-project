from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.user import UserCreate, UserRead
from app.services.auth_service import assign_project_to_user, register_user
from app.db import get_session
from app.schemas.user import UserLogin, TokenResponse
from app.services.auth_service import login_user
from app.middleware.rbac import get_current_user, require_admin

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_session)):
    print("🟡 Inside /register endpoint")
    return register_user(user, db)


@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin, db: Session = Depends(get_session)):
    token = login_user(data, db)
    return {"access_token": token}


@router.get("/user", response_model=UserRead)
def get_logged_in_user(user=Depends(get_current_user)):
    return user


@router.put("/assign-project/{user_id}")
def assign_project(
    user_id: int,
    project_id: int,
    db: Session = Depends(get_session),
    admin=Depends(require_admin),
):
    return assign_project_to_user(user_id, project_id, db)
