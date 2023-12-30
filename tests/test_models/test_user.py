# tests/test_models/test_user.py
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_create_instance(self):
        user = User()
        self.assertIsInstance(user, User)

    # Agrega más pruebas según sea necesario

