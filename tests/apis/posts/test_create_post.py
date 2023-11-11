from starlette import status

from src.global_vars import post_repository
from src.models.post import Post


# `POST /posts/{post_id}` API가 성공적으로 동작한다.
def test_create_post_successfully(client):
    # when
    # `POST /posts/{post_id}` API를 호출한다.
    response = client.post(
        "/posts",
        json={
            "title": "title",
            "content": "content",
        },
    )

    # then
    # 응답 상태 코드가 201이어야 한다.
    assert response.status_code == status.HTTP_201_CREATED

    # 응답 본문이 예상한 형식과 같아야 한다.
    data = response.json()
    assert data == {
        "id": 0,
        "title": "title",
        "content": "content",
        "created_at": data["created_at"],
    }

    # 서버 내에 Post 데이터가 저장되어 있어야 한다.
    assert post_repository.get(post_id=0) == Post(
        id=0,
        title="title",
        content="content",
        created_at=data["created_at"],
    )
