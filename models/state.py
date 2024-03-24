#!/usr/bin/python3
""" State Module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModeli, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
