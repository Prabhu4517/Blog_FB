from fastapi import FastAPI
from routes import posts
app = FastAPI()

app.include_router(posts.router, prefix="/posts", tags=["posts"])
# app.include_router(categories.router, prefix="/categories", tags=["categories"])
