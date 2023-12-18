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
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj = eval(cls_name)(**val)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
