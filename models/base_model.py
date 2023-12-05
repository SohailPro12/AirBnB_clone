#!/usr/bin/python3

"""
BaseModel class that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """Parent class

    Args:
        id: a unique identifier
        created_at: when did we created it
        updated_at: when did we updated it
    """
    def __init__(self, *args, **kwargs):
        """initialize all attributes

        Args:
           *args: arguments (unused)
           **kwargs: key word arguments
        """
        ch = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                         ch)
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                         ch)
            for key, value in kwargs.items():
                if key != '__class':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Print the string documentation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        mydic = self.__dict__.copy()
        mydic["__class__ "] = self.__class__.__name__
        mydic["created_at"] = mydic["created_at"].isoformat()
        mydic["updated_at"] = mydic["updated_at"].isoformat()
        return mydic
