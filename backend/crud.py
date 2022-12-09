from sqlalchemy.orm import Session
from . import models, schemas

def get_post(db: Session, post_id:int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, skip:int=0, limit:int=100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, content=post.content, author=post.author)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db:Session, post_id:int):
    post_to_remove = db.get(models.Post, post_id)
    db.delete(post_to_remove)
    db.commit()
    return f"Post with id:{post_id} has been deleted"