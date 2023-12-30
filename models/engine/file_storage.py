#!/usr/bin/python3
"""File storage module"""
import json


class FileStorage:
    """File storage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        pass

    def new(self, obj):
        """Add a new object to __objects."""
        pass

    def save(self):
        """Save __objects to a JSON file."""
        pass

    def reload(self):
        """Reload objects from a JSON file."""
        pass
