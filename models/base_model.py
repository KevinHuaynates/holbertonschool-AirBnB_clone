#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                setattr(self, "id", str(uuid.uuid4()))
            time_now = datetime.utcnow()
            if "created_at" not in kwargs:
                setattr(self, "created_at", time_now)
            if "updated_at" not in kwargs:
                setattr(self, "updated_at", time_now)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def reload(self):
        storage.reload()

