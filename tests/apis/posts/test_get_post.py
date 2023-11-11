from starlette import status

from src.global_vars import post_repository
from src.models.post import Post


# `GET /posts/{post_id}` API가 성공적으로 동작한다.
def test_get_post_successfully(client):
    # given
    # 서버 내에 Post 데이터가 저장되어 있다.
    post_repository.add(
        Post(
            id=0,
            title="title",
            content="content",
        )
    )

    # when
    # `GET /posts/{post_id}` API를 호출한다.
    response = client.get("/posts/0")

    # then
    # 응답 상태 코드가 200이어야 한다.
    assert response.status_code == status.HTTP_200_OK

    # 응답 본문이 예상한 형식과 같아야 한다.
    data = response.json()
    assert data == {
        "id": 0,
        "title": "title",
        "content": "content",
        "created_at": data["created_at"],
    }


# `GET /posts/{post_id}` API가 존재하지 않는 Post ID에 대해서는 404를 응답한다.
def test_get_post_with_non_existing_post_id(client):
    # given
    # 존재하지 않는 Post ID가 주어졌다.
    post_id = 0

    # when
    # `GET /posts/{post_id}` API를 호출한다.
    response = client.get(f"/posts/{post_id}")

    # then
    # 응답 상태 코드가 404이어야 한다.
    assert response.status_code == status.HTTP_404_NOT_FOUND
