#!/usr/bin/python3
"""
Este módulo contiene la clase BaseModel para el proyecto AirBnB.
"""

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

class BaseModel:
    """
    Class define BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Inicia una nueva instancia de BaseModel.

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
            FileStorage.new(self)

    def __str__(self):
        """
        Return el string representacion del objeto.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update el attribute updated_at con la fecha y hora actual.
        """
        self.updated_at = datetime.now()
        FileStorage.new(self)

    def to_dict(self):
        """
        Returns el dictionary que contiene keys/values de __dict__.
        """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

