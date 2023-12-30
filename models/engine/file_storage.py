#!/usr/bin/python3
"""Module for FileStorage class."""
from models.base_model import BaseModel
import json


class FileStorage:
    """Class for managing storage of instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objs_dict = json.load(f)
                self.__objects = {k: BaseModel(**v) for k, v in objs_dict.items()}
        except FileNotFoundError:
            pass

