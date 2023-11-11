from datetime import datetime

from pydantic import BaseModel

from src.config import config


class Post(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime = datetime.now(tz=config.zone_info)
