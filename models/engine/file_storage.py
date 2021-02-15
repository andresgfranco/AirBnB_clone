#!/usr/bin/python3
""" Initializes module """
import json
from models.base_model import BaseModel


class FileStorage():
    """ Storage class of objects """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __object to the JSON file """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as save_file:
            json.dump(my_dict, save_file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path) as my_file:
                json_rep = json.load(my_file)
                for key, value in json_rep.items():
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
