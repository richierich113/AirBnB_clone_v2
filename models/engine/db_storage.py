import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage """
        # Retrieve MySQL connection details from environment variables
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')

        # Create the engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, db),
                                      pool_pre_ping=True)

        # Drop all tables if environment is test
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects """
        from models import classes_dict
        obj_dict = {}

        if cls:
            query_result = self.__session.query(classes_dict[cls]).all()
        else:
            for cls in classes_dict.values():
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ Add object to current session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and create session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ Close session """
        self.__session.close()
Save to grepper
