from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
# from app.models.project import Project  # forward import-safe

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    role: str = Field(default="user")  # user or admin
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")

    project: Optional["Project"] = Relationship(back_populates="users")
