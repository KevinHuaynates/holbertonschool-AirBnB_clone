#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_init(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))

    # Agrega más pruebas según sea necesario para los métodos de la clase Amenity


if __name__ == '__main__':
    unittest.main()
