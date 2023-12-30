import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    # Agrega más pruebas según sea necesario

