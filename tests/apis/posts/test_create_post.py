import datetime

import pytest
from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.post import Post


# `POST /posts/{post_id}` API가 성공적으로 동작한다.
@pytest.mark.asyncio
async def test_create_post_successfully(client: AsyncClient, session: AsyncSession):
    # when
    # `POST /posts/{post_id}` API를 호출한다.
    response = await client.post(
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
        "id": 1,
        "title": "title",
        "content": "content",
        "created_at": data["created_at"],
    }

    # 서버 내에 Post 데이터가 저장되어 있어야 한다.
    post = await session.get(Post, 1)
    assert post.id == 1
    assert post.title == "title"
    assert post.content == "content"
    assert post.created_at == datetime.datetime.fromisoformat(data["created_at"])
