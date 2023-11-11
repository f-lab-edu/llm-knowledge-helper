import uvicorn
from fastapi import FastAPI

from src.apis.common import common_router
from src.apis.posts import post_router

app = FastAPI()
app.include_router(common_router)
app.include_router(post_router)

if __name__ == "__main__":
    uvicorn.run(app)
