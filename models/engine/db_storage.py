#!/usr/bin/python3
""" DATABASE STORAGE """

from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

classes = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

class DBStorage:
    """ DATABASE STORAGE """
    __engine = None
    __session = None
  

    def __init__(self):
        """ INIT """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ ALL """
        new_dict = {}
        if cls is None:
            for class_name in classes:
                for instance in self.__session.query(classes[class_name]):
                    key = instance.__class__.__name__ + '.' + instance.id
                    new_dict[key] = instance
        else:
            for instance in self.__session.query(cls):
                key = instance.__class__.__name__ + '.' + instance.id
                new_dict[key] = instance
        return new_dict
    
    def new(self, obj):
        """ NEW """
        self.__session.add(obj)
    
    def save(self):
        """ SAVE """
        self.__session.commit()
    
    def delete(self, obj=None):
        """ DELETE """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """ RELOAD """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

                                                    