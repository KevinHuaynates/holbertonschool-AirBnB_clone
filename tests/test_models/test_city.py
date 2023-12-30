import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    def test_init(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsNotNone(city.id)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
