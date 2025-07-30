from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.project import Project
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.core.security import verify_password
from app.schemas.user import UserLogin
from app.core.jwt_handler import create_access_token


def register_user(user_data: UserCreate, db: Session) -> User:
    try:
        existing_user = db.exec(
            select(User).where(User.username == user_data.username)
        ).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        new_user = User(
            username=user_data.username,
            hashed_password=hash_password(user_data.password),
            role=user_data.role,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        print("🚨 Registration Error:", str(e))
        raise HTTPException(status_code=500, detail="Error: " + str(e))


def login_user(data: UserLogin, db: Session) -> str:
    user = db.exec(select(User).where(User.username == data.username)).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token_data = {"sub": str(user.id), "role": user.role}
    access_token = create_access_token(token_data)
    return access_token


def assign_project_to_user(user_id: int, project_id: int, db: Session):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    user.project_id = project_id
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"detail": f"Assigned project {project.name} to user {user.username}"}
