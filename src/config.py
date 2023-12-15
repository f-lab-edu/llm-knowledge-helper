from pydantic import Field
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    url: str = Field(default="sqlite+aiosqlite:///./db.sqlite3", alias="DATABASE_URL")
    echo: bool = Field(default=True, alias="DATABASE_ECHO")


db = DatabaseConfig()
