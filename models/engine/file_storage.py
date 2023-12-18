#!/usr/bin/python3
"""File Storage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            from models import classes
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                serialized_objects = json.load(file)
                self.__objects = {key: classes[class_name](**value)
                                  for key, (class_name, value) in serialized_objects.items()}
        except FileNotFoundError:
            pass
