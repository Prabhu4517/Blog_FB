from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import Post, PostCreate, DeleteResponse
from crud import get_post, get_posts, create_post, del_post
from dbs import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Post)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db=db, post=post)

@router.get("/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_posts(db=db, skip=skip, limit=limit)

@router.get("/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = get_post(db=db, post_id=post_id)
    print(db_post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.delete("/{post_id}", response_model=DeleteResponse)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = del_post(db=db, post_id=post_id)
    return {"message" : " Post Deleted Succesfully"}