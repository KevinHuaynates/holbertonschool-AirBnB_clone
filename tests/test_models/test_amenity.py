# tests/test_models/test_amenity.py
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_create_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    # Agrega más pruebas según sea necesario

