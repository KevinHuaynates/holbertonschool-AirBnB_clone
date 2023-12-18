import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    def test_instance_creation(self):
        """Test creating an instance of User."""
        instance = User()
        self.assertIsInstance(instance, User)
