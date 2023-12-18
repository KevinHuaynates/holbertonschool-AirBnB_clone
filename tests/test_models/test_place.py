import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""
    def test_create_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)
