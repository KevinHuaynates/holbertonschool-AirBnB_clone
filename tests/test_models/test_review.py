#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_init(self):
        review = Review()
        self.assertIsNotNone(review.id)

    # Agrega más pruebas según sea necesario para los métodos de la clase Review


if __name__ == '__main__':
    unittest.main()
