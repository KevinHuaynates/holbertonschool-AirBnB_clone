#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
import models


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
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = models.classes[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
