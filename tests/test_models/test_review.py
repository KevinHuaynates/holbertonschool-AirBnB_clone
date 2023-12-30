# tests/test_models/test_review.py
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_create_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)

    # Agrega más pruebas según sea necesario

