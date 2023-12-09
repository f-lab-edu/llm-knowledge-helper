from fastapi import status
from fastapi.testclient import TestClient


def test_health_successfully(client: TestClient):
    # when
    response = client.get("/health")

    # then
    assert response.status_code == status.HTTP_200_OK
