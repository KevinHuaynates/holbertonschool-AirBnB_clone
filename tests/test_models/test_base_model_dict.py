# tests/test_models/test_base_model_dict.py
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModelDict(unittest.TestCase):
    def test_create_instance_with_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel.from_dict(obj_dict)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.created_at, obj.created_at)
        self.assertEqual(new_obj.updated_at, obj.updated_at)

    def test_create_instance_with_dict_additional_attribute(self):
        obj = BaseModel()
        obj.name = "Test"
        obj_dict = obj.to_dict()
        new_obj = BaseModel.from_dict(obj_dict)
        self.assertEqual(new_obj.name, "Test")

    def test_create_instance_with_dict_datetime_objects(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel.from_dict(obj_dict)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)

    def test_create_instance_with_dict_non_datetime_objects(self):
        obj = BaseModel()
        obj.some_data = [1, 2, 3]
        obj_dict = obj.to_dict()
        new_obj = BaseModel.from_dict(obj_dict)
        self.assertEqual(new_obj.some_data, [1, 2, 3])

