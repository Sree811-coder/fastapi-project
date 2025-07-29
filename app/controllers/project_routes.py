from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db import get_session
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.services import project_service
from app.middleware.rbac import get_current_user, require_admin

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/", response_model=ProjectRead)
def create(
    data: ProjectCreate,
    db: Session = Depends(get_session),
    admin=Depends(require_admin),
):
    return project_service.create_project(data, db)


@router.get("/", response_model=list[ProjectRead])
def get_all(db: Session = Depends(get_session), user=Depends(get_current_user)):
    return project_service.get_all_projects(db)


@router.get("/{project_id}", response_model=ProjectRead)
def get_one(
    project_id: int, db: Session = Depends(get_session), user=Depends(get_current_user)
):
    return project_service.get_project_by_id(project_id, db)


@router.put("/{project_id}", response_model=ProjectRead)
def update(
    project_id: int,
    data: ProjectUpdate,
    db: Session = Depends(get_session),
    admin=Depends(require_admin),
):
    return project_service.update_project(project_id, data, db)


@router.delete("/{project_id}")
def delete(
    project_id: int, db: Session = Depends(get_session), admin=Depends(require_admin)
):
    return project_service.delete_project(project_id, db)
