#!/usr/bin/python3
"""Define a class"""

from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    A class that serializes instances to a JSON file
    and deserializes a JSON file to instances

    args:
        __file_path: string
        __objects: dictionary
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

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
