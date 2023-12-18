#!/usr/bin/python3
"""This module defines a class FileStorage to manage serialization and
deserialization of instances to JSON format.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This class manages serialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):

