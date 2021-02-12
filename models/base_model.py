#!/usr/bin/python3
""" Intializing module """
import uuid
from datetime import datetime


class BaseModel:
    """ base class """
    def __init__(self, *args, **kwargs):
        """ Initial state of an object """
        if kwargs:
            if "created_at" in kwargs:
                self.created_at = kwargs["created_at"]
            if "id" in kwargs:
                self.id = kwargs["id"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """ String representation of object """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Saves """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """ Returns a dictionary containing key/values of an instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
