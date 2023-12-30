#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_init(self):
        state = State()
        self.assertIsNotNone(state.id)

    # Agrega más pruebas según sea necesario para los métodos de la clase State


if __name__ == '__main__':
    unittest.main()
