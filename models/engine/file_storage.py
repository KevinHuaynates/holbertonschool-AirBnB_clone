#!/usr/bin/python3
"""Module define a class FileStorage."""
import json
from os.path import isfile
from models.user import User
from ..models.base_model import BaseModel

class FileStorage:
    """Serializa instancias en un archivo JSON y deserializa el archivo JSON en instancias"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Establece en __objects el obj con la clave <nombre de clase de obj>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializa __objetos al archivo JSON (ruta: __file_path)."""
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializa JSON file a __objects."""
        try:
            from ..models.base_model import BaseModel
            import models
            if isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                    serialized_objects = json.load(file)
                    for key, value in serialized_objects.items():
                        class_name = value['__class__']
                        cls = BaseModel
                        if class_name in models.HBNB_MGMT:
                            cls = models.HBNB_MGMT[class_name]
                        self.__objects[key] = cls(**value)
        except (FileNotFoundError, ImportError, KeyError):
            pass

    HBNB_MGMT = {
        "BaseModel": BaseModel,
        "User": User
    }

