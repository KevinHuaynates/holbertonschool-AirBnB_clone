import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_create_instance(self):
        """Test creating an instance of State."""
        state = State()
        self.assertIsInstance(state, State)
