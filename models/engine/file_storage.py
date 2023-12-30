#!/usr/bin/python3
"""
File Storage Module

This module defines the FileStorage class for serializing and deserializing instances to/from a JSON file.
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """FileStorage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = BaseModel if cls_name == "BaseModel" else None  # Add other class names as needed
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

