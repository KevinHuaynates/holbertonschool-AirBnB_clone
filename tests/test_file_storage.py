# tests/test_file_storage.py

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__objects, {})

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

    def test_new(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage._FileStorage__objects)

    def test_save(self):
        # Your test code here

    def test_reload(self):
        # Your test code here

if __name__ == "__main__":
    unittest.main()

