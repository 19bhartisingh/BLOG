from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session  
from blog import models, schemas
from blog.database import get_db
from typing import List
from fastapi import APIRouter, Depends

router = APIRouter(
    tags=["Blogs"],
    prefix="/blog"
)


def get_all(db: Session = Depends(get_db)) -> List[schemas.ShowBlog]:
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No blogs found")
    return blogs

def create_blog(request: schemas.Blog, db: Session = Depends(get_db), user_id: int = 1) -> schemas.ShowBlog:
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=user_id  # Assuming user_id is provided
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    db.delete(blog)
    db.commit()
    return  "Blog deleted successfully"


def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return 'Updated'


def get_blog_by_id(id: int, response: Response, db: Session = Depends(get_db)) -> schemas.ShowBlog:
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    return blog