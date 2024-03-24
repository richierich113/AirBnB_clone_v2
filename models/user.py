'''
#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    # can't be null
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    # can be null
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    '''
#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        places: places associated with the User
        reviews: reviews the User has made
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place',
                          backref='user',
                          cascade='all, delete-orphan',
                          passive_deletes=True)
    reviews = relationship('Review',
                           backref='user',
                           cascade='all, delete-orphan',
                           passive_deletes=True)
