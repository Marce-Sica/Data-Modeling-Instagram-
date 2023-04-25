import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False)
    FirstName = Column(String(250), nullable=False)
    LastName = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)
    pass

class Post(Base):
    __tablename__ = 'Post'
    ID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('User.id'))
    pass

class Comment(Base):
    __tablename__ = 'Comment'
    ID = Column(Integer, primary_key=True)
    CommentText = Column(String(250), nullable=False)
    AuthorID = Column(Integer, ForeignKey('User.id'))
    PostID = Column(Integer, ForeignKey('Post.id'))
    pass

class Media(Base):
    __tablename__ = 'Media'
    ID = Column(Integer, primary_key=True)
    Type = Column(Enum, nullable=False)
    URL = Column(String(250), nullable=False)
    PostID = Column(Integer, ForeignKey('Post.id'))
    pass

class Follower(Base):
    __tablename__ = 'Follower'
    ID = Column(Integer, primary_key=True)
    UserFromID = Column(Integer, ForeignKey('User.id'))
    UserToID = Column(Integer, ForeignKey('User.id'))
    pass

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
