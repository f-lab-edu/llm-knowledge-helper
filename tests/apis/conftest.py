from fastapi.testclient import TestClient
from pytest import fixture
from sqlmodel import Session, SQLModel

from src.database import engine
from src.main import app


@fixture(scope="session")
def client() -> TestClient:
    with TestClient(app) as client:
        yield client


@fixture(scope="session")
def session() -> Session:
    with Session(engine) as session:
        yield session


@fixture(autouse=True)
def setup_and_teardown_db():
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)
