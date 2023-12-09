from fastapi.testclient import TestClient
from starlette import status

from src.global_vars import post_repository
from src.models.post import Post


# `GET /posts` API가 성공적으로 동작한다.
def test_get_posts_successfully(client: TestClient):
    # given
    # 서버 내에 Post 데이터가 저장되어 있다.
    post_repository.add(
        Post(
            id=0,
            title="title 1",
            content="content 1",
        )
    )
    post_repository.add(
        Post(
            id=1,
            title="title 2",
            content="content 2",
        )
    )

    # when
    # `GET /posts` API를 호출한다.
    response = client.get("/posts")

    # then
    # 응답 상태 코드가 200이어야 한다.
    assert response.status_code == status.HTTP_200_OK

    # 응답 본문이 예상한 형식과 같아야 한다.
    data = response.json()
    assert data == [
        {
            "id": 1,
            "title": "title 2",
            "content": "content 2",
            "created_at": data[1]["created_at"],
        },
        {
            "id": 0,
            "title": "title 1",
            "content": "content 1",
            "created_at": data[0]["created_at"],
        },
    ]
