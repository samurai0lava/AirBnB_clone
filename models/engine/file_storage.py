#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This is the storage engine for AirBnB_clone project
    Class Methods:
        __init__: Initializes the FileStorage instance.
        all: Returns the object
        new: updates the dictionary
        save: Serializes, or converts Python objects into JSON strings
        reload: Deserializes, or converts JSON strings into Python objects.
    Class Attributes:
        classes (dict): A dictionary of all the classes.
    """

    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    self.__file_path = "file.json"
    self.__objects = {}

    def all(self):
        """Returns all objects"""
        return self.__objects

    def new(self, obj):
        """
        Sets key/value pair in dictionary __objects
        Key Format: <obj class name>.<id>
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save/serialize obj dictionaries to json file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize/convert obj dicts back to instances, if it exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.classes[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
