from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def register_user(user_data: UserCreate, db: Session) -> User:
    try:
        existing_user = db.exec(select(User).where(User.username == user_data.username)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        new_user = User(
            username=user_data.username,
            hashed_password=hash_password(user_data.password),
            role=user_data.role,
            project_id=user_data.project_id
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        print("🚨 Registration Error:", str(e))
        raise HTTPException(status_code=500, detail="Error: " + str(e))
