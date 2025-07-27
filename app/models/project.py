from sqlmodel import SQLModel, Field
from typing import Optional

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    created_by: Optional[int] = Field(foreign_key="user.id")
