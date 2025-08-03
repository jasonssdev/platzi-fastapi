from typing import Annotated
from contextlib import asynccontextmanager
from sqlmodel import Session, create_engine, SQLModel
from fastapi import Depends, FastAPI

sqlite_name = "db.sqlite3"
sqlite_path = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_path)


@asynccontextmanager
async def create_tables(app: FastAPI):
    """Create database tables on startup."""
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
