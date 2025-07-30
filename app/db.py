from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    from app.models.user import User
    from app.models.project import Project

    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
