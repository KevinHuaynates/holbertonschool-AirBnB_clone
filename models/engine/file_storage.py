#!/usr/bin/python3
"""This module defines a class FileStorage."""
import json
from os.path import isfile
from models.user import User
from ..models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            from ..models.base_model import BaseModel
            import models
            if isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                    serialized_objects = json.load(file)
                    for key, value in serialized_objects.items():
                        class_name = value['__class__']
                        cls = BaseModel
                        if class_name in models.classes:
                            cls = models.classes[class_name]
                        self.__objects[key] = cls(**value)
        except (FileNotFoundError, ImportError, KeyError):
            pass

    HBNB_MGMT = {
        "BaseModel": BaseModel,
        "User": User  # Add this line to include User
    }

