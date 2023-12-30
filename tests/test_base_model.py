import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_attributes(self):
        instance = BaseModel()
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))

    # Agrega más casos de prueba según sea necesario

