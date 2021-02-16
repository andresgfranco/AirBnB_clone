#!/usr/bin/python3
""" Intializing module """
import uuid
import models
from datetime import datetime


class BaseModel():
    """ Base class model that will define all common
    attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ Initial state of an object """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation of object """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Saves the objects """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing key/values of an instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict.update({"updated_at": self.updated_at.isoformat()})
        new_dict.update({"created_at": self.created_at.isoformat()})
        return new_dict
