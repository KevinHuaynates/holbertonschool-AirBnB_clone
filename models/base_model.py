#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
            if "id" not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            if "created_at" not in kwargs:
                setattr(self, 'created_at', datetime.now())
            if "updated_at" not in kwargs:
                setattr(self, 'updated_at', datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        result = dict(self.__dict__)
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.__dict__))

