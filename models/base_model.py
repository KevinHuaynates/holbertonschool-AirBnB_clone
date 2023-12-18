#!/usr/bin/python3
"""
BaseModel module
"""
import uuid
from datetime import datetime
from models


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initializes an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Updates the updated_at attribute and saves to the storage engine"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts instance attributes to dictionary format"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
