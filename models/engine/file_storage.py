#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_dict = {}
        for key, value in self.__objects.items():
            serialized_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        else:
            return
