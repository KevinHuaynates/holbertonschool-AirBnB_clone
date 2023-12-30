# tests/test_models/test_base_model.py
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_str_method(self):
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(
            obj_dict['created_at'], obj.created_at.isoformat()
        )
        self.assertEqual(
            obj_dict['updated_at'], obj.updated_at.isoformat()
        )

    def test_to_dict_with_additional_attribute(self):
        obj = BaseModel()
        obj.name = "Test"
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['name'], "Test")

    def test_to_dict_with_datetime_objects(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_with_non_datetime_objects(self):
        obj = BaseModel()
        obj.some_data = [1, 2, 3]
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['some_data'], [1, 2, 3])

    def test_create_instance_with_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.created_at, obj.created_at)
        self.assertEqual(new_obj.updated_at, obj.updated_at)

    def test_create_instance_with_dict_additional_attribute(self):
        obj = BaseModel()
        obj.name = "Test"
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(new_obj.name, "Test")

    def test_create_instance_with_dict_datetime_objects(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)

    def test_create_instance_with_dict_non_datetime_objects(self):
        obj = BaseModel()
        obj.some_data = [1, 2, 3]
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(new_obj.some_data, [1, 2, 3])

