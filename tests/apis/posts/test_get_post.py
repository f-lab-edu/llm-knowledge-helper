from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session

from src.models.post import Post


# `GET /posts/{post_id}` API가 성공적으로 동작한다.
def test_get_post_successfully(client: TestClient, session: Session):
    # given
    # 서버 내에 Post 데이터가 저장되어 있다.
    post = Post(
        title="title",
        content="content",
    )
    session.add(post)
    session.commit()
    session.refresh(post)

    # when
    # `GET /posts/{post_id}` API를 호출한다.
    response = client.get(f"/posts/{post.id}")

    # then
    # 응답 상태 코드가 200이어야 한다.
    assert response.status_code == status.HTTP_200_OK

    # 응답 본문이 예상한 형식과 같아야 한다.
    data = response.json()
    assert data == {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "created_at": post.created_at.isoformat(),
    }


# `GET /posts/{post_id}` API가 존재하지 않는 Post ID에 대해서는 404를 응답한다.
def test_get_post_with_non_existing_post_id(client: TestClient):
    # given
    # 존재하지 않는 Post ID가 주어진다.
    post_id = 0

    # when
    # `GET /posts/{post_id}` API를 호출한다.
    response = client.get(f"/posts/{post_id}")

    # then
    # 응답 상태 코드가 404이어야 한다.
    assert response.status_code == status.HTTP_404_NOT_FOUND
