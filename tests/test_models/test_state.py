import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    def test_init(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsNotNone(state.id)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
