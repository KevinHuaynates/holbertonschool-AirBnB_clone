#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)

    def test_save(self):
        model = BaseModel()
        updated_at_before = model.updated_at
        model.save()
        updated_at_after = model.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)

    # Agrega más pruebas según sea necesario para otros métodos de la clase BaseModel


if __name__ == '__main__':
    unittest.main()
