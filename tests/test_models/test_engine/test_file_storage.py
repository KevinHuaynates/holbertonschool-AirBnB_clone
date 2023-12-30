# tests/test_engine/test_file_storage.py
import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_create_instance(self):
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)

    # Agrega más pruebas según sea necesario

