import datetime

from fastapi import HTTPException
from pydantic import BaseModel
from starlette import status

from src.global_vars import post_repository


class GetPostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime.datetime


def handler(post_id: int) -> GetPostResponse:
    post = post_repository.get(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return GetPostResponse(
        id=post.id,
        title=post.title,
        content=post.content,
        created_at=post.created_at,
    )
