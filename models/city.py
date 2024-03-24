'''
#!/usr/bin/python3
""" City Module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    '''
#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id",
                                 ondelete='CASCADE'),
                      nullable=False)
    places = relationship(
        'models.place.Place',
        backref='cities',
        cascade='all, delete-orphan')
