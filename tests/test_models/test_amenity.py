import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_create_instance(self):
        """Test creating an instance of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
