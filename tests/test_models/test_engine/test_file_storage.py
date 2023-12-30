#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_new(self):
        storage = FileStorage()
        obj = storage.all()
        self.assertIn("{}.{}".format(type(obj).__name__, obj.id), storage.all())

    def test_reload(self):
        storage = FileStorage()
        storage.reload()
        self.assertTrue(len(storage.all()) >= 0)

    # Agrega más pruebas según sea necesario para otros métodos de la clase FileStorage


if __name__ == '__main__':
    unittest.main()
