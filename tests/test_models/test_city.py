import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_create_instance(self):
        """Test creating an instance of City."""
        city = City()
        self.assertIsInstance(city, City)

    # Add more test cases as needed

