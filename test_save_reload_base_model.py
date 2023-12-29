#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
import os
import unittest

class TestSaveReloadBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)

    def test_type_file_path(self):
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_type_objects(self):
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_type_objects(self):
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        b = BaseModel()
        storage.new(b)
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIn(key, storage.all())

    def test_save(self):
        b = BaseModel()
        storage.new(b)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            content = f.read()
        self.assertIsInstance(content, str)

    def test_reload(self):
        b = BaseModel()
        storage.new(b)

