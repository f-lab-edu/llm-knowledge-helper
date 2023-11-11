from fastapi import status


def test_health_successfully(client):
    # when
    response = client.get("/health")

    # then
    assert response.status_code == status.HTTP_200_OK
