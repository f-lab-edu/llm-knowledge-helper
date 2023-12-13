from sqlmodel import Session

from src.database import engine


def get_session() -> Session:
    with Session(engine) as session:
        yield session
