from pydantic import BaseModel
from .database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import Optional, List


class Blog(BaseModel):
    title: str
    body: str
    # user_id: int  # Assuming user_id is required to associate the blog with a user
    
    class Config:
        orm_mode = True

        
        
class User(BaseModel):
    username: str
    email: str
    password: str
    
    class Config:
        orm_mode = True
    
    
class ShowUser(BaseModel):
    id: int
    username: str
    email: str
    blogs: list[Blog] =[] # List of blogs associated with the user

    class Config:
        orm_mode = True
        
        
    
class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: Optional[ShowUser] = None  # Optional field for the creator of the blog

    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
        
        

class Token(BaseModel):
    access_token: str
    token_type: str
    
    class Config:
        orm_mode = True


class TokenData(BaseModel):
    username: Optional[str] | None = None
    
    class Config:
        orm_mode = True