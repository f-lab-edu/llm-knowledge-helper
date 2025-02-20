from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel, pool

from src import config

engine = create_async_engine(
    url=config.db.async_url,
    echo=config.db.echo,
    poolclass=pool.StaticPool,
)


async def create_db_and_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def close_db() -> None:
    await engine.dispose()
