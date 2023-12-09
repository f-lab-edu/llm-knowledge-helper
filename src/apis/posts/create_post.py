import datetime

from pydantic import BaseModel

from src.global_vars import post_repository
from src.models.post import Post


class CreatePostRequest(BaseModel):
    title: str
    content: str


class CreatePostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime.datetime


def handler(request: CreatePostRequest) -> CreatePostResponse:
    post_id = post_repository.get_next_id()
    post = Post(
        id=post_id,
        title=request.title,
        content=request.content,
    )
    post_repository.add(post)
    return CreatePostResponse(
        id=post.id, title=post.title, content=post.content, created_at=post.created_at
    )
