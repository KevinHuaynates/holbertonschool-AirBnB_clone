import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def test_init(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
