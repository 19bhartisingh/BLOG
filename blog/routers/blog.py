from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import models, schemas,database
from blog.database import get_db 
from typing import List, Optional
from fastapi import Response
from ..repository import blog
from blog.oauth2 import get_current_user
from blog import oauth2


router = APIRouter(
    tags=["Blogs"],
    prefix="/blog"
)

@router.get('', response_model=List[schemas.ShowBlog] )
def get_all_blog(db: Session = Depends(get_db),get_current_user: schemas.User=Depends(oauth2.get_current_user)):
    
    return blog.get_all(db)


@router.post('',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), user_id: int = 1, get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db, user_id)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT )
def delete_blog(id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)


@router.put('/{id}',status_code=status.HTTP_200_OK )
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
   
   return blog.update_blog(id, request, db)


@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog )
def get_blog_by_id(id: int,response:Response, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    
    return blog.get_blog_by_id(id, response, db)
