# tests/test_models/test_city.py
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_create_instance(self):
        city = City()
        self.assertIsInstance(city, City)

    # Agrega más pruebas según sea necesario

