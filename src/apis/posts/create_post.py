import datetime
from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel
from sqlmodel import Session

from src.apis.dependencies import get_session
from src.models.post import Post


class CreatePostRequest(BaseModel):
    title: str
    content: str


class CreatePostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime.datetime


def handler(
    request: CreatePostRequest, session: Annotated[Session, Depends(get_session)]
) -> CreatePostResponse:
    post = Post(
        title=request.title,
        content=request.content,
    )
    session.add(post)
    session.commit()
    session.refresh(post)
    return CreatePostResponse(
        id=post.id, title=post.title, content=post.content, created_at=post.created_at
    )
