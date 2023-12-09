from src.models.post import Post


class PostRepository:
    def __init__(self) -> None:
        self.post_id = -1
        self.data: dict[int, Post] = {}

    def add(self, post: Post) -> None:
        self.data[post.id] = post

    def delete(self, post_id: int) -> None:
        del self.data[post_id]

    def get(self, post_id: int) -> Post | None:
        return self.data.get(post_id)

    def get_all(self) -> list[Post]:
        return list(self.data.values())

    def delete_all(self) -> None:
        self.data.pop: dict[int, Post] = {}

    def get_next_id(self) -> int:
        self.post_id += 1
        return self.post_id
