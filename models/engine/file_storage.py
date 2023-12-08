#!/usr/bin/python3
"""Define a class"""

from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    FileStorage class for serializing and deserializing instances to/from
    a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def all(self):
        """./
        Returns the dictionary with all objects of a specific class.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w') as file:
            json_objects = {k: v.to_dict()
                            for k, v in FileStorage.__objects.items()}
            json.dump(json_objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                objs = json.load(file)
            for obj in objs.values():
                cls = obj.pop('class', None)
                if cls:
                    FileStorage.__objects["{}.{}".format(cls,
                                          obj['id'])] = eval(cls)(**obj)
