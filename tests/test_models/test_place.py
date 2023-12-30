import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    def test_init(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsNotNone(place.id)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
