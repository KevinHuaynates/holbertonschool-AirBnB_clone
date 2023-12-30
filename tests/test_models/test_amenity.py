import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    def test_init(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsNotNone(amenity.id)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
