#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_init(self):
        user = User() 
        self.assertIsNotNone(user.id)
        

if __name__ == '__main__':
    unittest.main()
