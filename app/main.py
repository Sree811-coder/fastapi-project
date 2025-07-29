from fastapi import FastAPI
from app.db import create_db_and_tables
from app.controllers import auth_routes, project_routes

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(auth_routes.router)
app.include_router(project_routes.router)


@app.get("/")
def read_root():
    return {"msg": "FastAPI + SQLModel + JWT RBAC is working!"}
