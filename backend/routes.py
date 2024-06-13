from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
import orm

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/posts/")
def read_posts(db: Session = Depends(get_db)):
    return orm.get_all_posts(db)

@router.get("/posts/{post_id}")
def read_post(post_id: int, db: Session = Depends(get_db)):
    return orm.get_post(db, post_id)

@router.post("/posts/")
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return orm.create_post(db, post)