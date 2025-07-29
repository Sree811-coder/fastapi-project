from pydantic import BaseModel
from typing import Optional

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    model_config = {
        "from_attributes": True
    }

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None