import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""
    
    def test_create_instance(self):
        """Test creating an instance of BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_attributes(self):
        """Test BaseModel attributes."""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        # Add more test cases as needed
