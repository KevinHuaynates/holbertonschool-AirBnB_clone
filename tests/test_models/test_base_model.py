#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))

    def test_save(self):
        model = BaseModel()
        model.save()
        self.assertIsNotNone(model.updated_at)


if __name__ == '__main__':
    unittest.main()
