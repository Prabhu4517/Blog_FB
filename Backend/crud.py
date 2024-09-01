from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Post
from schemas import PostCreate

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: PostCreate):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def del_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first() 
    if db_post is None:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    db.delete(db_post)
    db.commit()
    return db_post

# def get_category(db: Session, category_id: int):
#     return db.query(Category).filter(Category.id == category_id).first()

# def get_categories(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Category).offset(skip).limit(limit).all()

# def create_category(db: Session, category: CategoryCreate):
#     db_category = Category(**category.dict())
#     db.add(db_category)
#     db.commit()
#     db.refresh(db_category)
#     return db_category
