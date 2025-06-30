from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.database import get_db 
from fastapi import Response
from ..repository import user

router = APIRouter(
    tags=["Users"],
    prefix="/user"
)



@router.post('',response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # hashed_password = pwd_context.hash(request.password)
    
    return user.create_user(request, db)



@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    
    return user.get_user_by_id(id, db)


 