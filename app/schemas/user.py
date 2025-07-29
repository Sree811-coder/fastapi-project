from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[str] = "user"
    project_id: Optional[int] = None  # optional during registration

class UserRead(BaseModel):
    id: int
    username: str
    role: str
    project_id: Optional[int] = None
    
    model_config = {
        "from_attributes": True
    }