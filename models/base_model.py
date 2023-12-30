#!/usr/bin/python3
""" BaseModel
"""

from datetime import datetime
import uuid

class BaseModel:
    """ BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """ Constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def to_dict(self):
        """ Returns a dictionary representation
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def save(self):
        """ Updates the public instance attribute updated_at
        """
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """ Returns a string representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

