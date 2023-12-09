from fastapi.testclient import TestClient
from pytest import fixture

from src.main import app


# 테스트 클라이언트를 생성한다.
@fixture(scope="session")
def client() -> TestClient:
    with TestClient(app) as client:
        yield client
