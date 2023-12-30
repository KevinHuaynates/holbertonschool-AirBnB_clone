#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_init(self):
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)


if __name__ == '__main__':
    unittest.main()
