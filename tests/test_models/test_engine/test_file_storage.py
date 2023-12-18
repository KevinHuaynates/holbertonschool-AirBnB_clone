import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_create_instance(self):
        """Test creating an instance of FileStorage."""
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)
