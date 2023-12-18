#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
import os


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
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                class_obj = globals()[class_name]
                obj = class_obj(**value)
                self.__objects[key] = obj
