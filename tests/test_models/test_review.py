import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def test_init(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsNotNone(review.id)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
