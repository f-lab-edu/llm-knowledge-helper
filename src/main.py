from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.apis.common import common_router
from src.apis.posts import post_router
from src.database import close_db, create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    await close_db()


app = FastAPI(lifespan=lifespan)
app.include_router(common_router)
app.include_router(post_router)


if __name__ == "__main__":
    uvicorn.run(app)
