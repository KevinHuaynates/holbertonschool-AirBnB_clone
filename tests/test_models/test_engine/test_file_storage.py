import unittest
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    def test_all(self):
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        storage = FileStorage()
        storage.new(object)
        all_objects = storage.all()
        self.assertIn("{}.{}".format(type(object).__name__, object.id),
                      all_objects)

    def test_save(self):
        storage = FileStorage()
        storage.new(object)
        storage.save()
        filename = storage._FileStorage__file_path
        self.assertTrue(os.path.exists(filename))

    def test_reload(self):
        storage = FileStorage()
        storage.new(object)
        storage.save()
        storage.reload()
        all_objects = storage.all()
        self.assertIn("{}.{}".format(type(object).__name__, object.id),
                      all_objects)


if __name__ == '__main__':
    unittest.main()
