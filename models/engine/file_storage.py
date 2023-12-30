#!/usr/bin/python3
""" File Storage
"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """ FileStorage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file
        """
        serial_dict = {}
        for key, value in FileStorage.__objects.items():
            serial_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(serial_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                deserial_dict = json.load(f)
            for key, value in deserial_dict.items():
                cls_name, obj_id = key.split('.')
                cls = BaseModel if cls_name == 'BaseModel' else None  # Update with other classes
                if cls:
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

