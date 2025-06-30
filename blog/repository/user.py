from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session  
from blog import models, schemas ,database, hashing
from blog.hashing import Hash
from blog.database import get_db
from typing import List
from fastapi import APIRouter, Depends
from passlib.context import CryptContext

router = APIRouter(
    tags=["Blogs"],
    prefix="/user"
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)) -> schemas.ShowUser:
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=Hash().bcrypt(request.password)  # Assuming Hash.bcrypt is a method to hash passwords
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user 


@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user_by_id(id: int, db: Session = Depends(get_db)) -> schemas.ShowUser:
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user