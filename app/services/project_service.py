from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


def create_project(data: ProjectCreate, db: Session) -> Project:
    new_project = Project(name=data.name, description=data.description)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    print(new_project)
    return new_project


def get_all_projects(db: Session):
    return db.exec(select(Project)).all()


def get_project_by_id(project_id: int, db: Session) -> Project:
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    return project


def update_project(project_id: int, data: ProjectUpdate, db: Session) -> Project:
    project = get_project_by_id(project_id, db)
    for field, value in data.dict(exclude_unset=True).items():
        setattr(project, field, value)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def delete_project(project_id: int, db: Session):
    project = get_project_by_id(project_id, db)
    db.delete(project)
    db.commit()
    return {"detail": "Project deleted successfully"}
