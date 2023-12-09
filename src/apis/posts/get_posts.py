from src.apis.posts.get_post import GetPostResponse
from src.global_vars import post_repository


def handler() -> list[GetPostResponse]:
    return sorted(
        [
            GetPostResponse(
                id=post.id,
                title=post.title,
                content=post.content,
                created_at=post.created_at,
            )
            for post in post_repository.get_all()
        ],
        key=lambda post: -post.id,
    )
