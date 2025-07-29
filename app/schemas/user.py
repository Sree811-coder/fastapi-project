from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[str] = "user"
    project_id: Optional[int] = None


class UserRead(BaseModel):
    id: int
    username: str
    role: str
    project_id: Optional[int] = None

    model_config = {"from_attributes": True}


class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
