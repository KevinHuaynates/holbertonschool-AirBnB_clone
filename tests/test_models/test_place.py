# tests/test_models/test_place.py
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_create_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)

    # Agrega más pruebas según sea necesario

