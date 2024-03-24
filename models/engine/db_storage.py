#!/usr/bin/python3
""" DBStorage Module """
from sqlalchemy import create_engine
import os

dialect = 'mysql'
driver = 'mysqldb'
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_ENV = os.getenv('HBNB_ENV')


class DBStorage:
    """ The city class, contains state ID and name
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(f"{dialect}+{driver}://\
            {HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@\
            {HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}", pool_pre_ping=True)
        if HBNB_ENV == 'test':
            """TODO: Drop all tables"""
            pass
