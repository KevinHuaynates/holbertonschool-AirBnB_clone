#!/usr/bin/python3
"""This module defines the BaseModel class."""
import uuid
from datetime import datetime
import models

class BaseModel:
    """Defines all common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Initialize public instance attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            models.storage.new(self)

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        d = dict(self.__dict__)
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        d["__class__"] = self.__class__.__name__
        return d

    def save(self):
        """Update the updated_at attribute and save to the storage."""
        self.updated_at = datetime.now()
        models.storage.save()
