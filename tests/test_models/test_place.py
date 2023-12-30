#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_init(self):
        place = Place()
        self.assertIsNotNone(place.id)


if __name__ == '__main__':
    unittest.main()
