#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    def test_base_model_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('__class__', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)


if __name__ == '__main__':
    unittest.main()
