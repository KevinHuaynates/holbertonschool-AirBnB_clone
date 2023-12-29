#!/usr/bin/python3
"""
This module contains the BaseModel class for the AirBnB project.
"""

import uuid
from datetime import datetime
from .engine.file_storage import FileStorage

class BaseModel:
    """
    This class defines the BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        If kwargs is not empty, updates the instance with the key/value pairs.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__.
        """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

