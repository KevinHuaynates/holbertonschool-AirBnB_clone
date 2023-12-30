# tests/test_models/test_state.py
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_create_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    # Agrega más pruebas según sea necesario

