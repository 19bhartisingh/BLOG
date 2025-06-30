from .database import Base
from sqlalchemy import Column,String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Should be long enough for hashed passwords
    
    blogs = relationship("Blog", back_populates="creator")


class Blog(Base):

    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key to User table
    
    creator = relationship("User", back_populates="blogs")


    
    