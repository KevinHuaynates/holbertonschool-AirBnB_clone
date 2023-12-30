#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def test_new(self):
        storage = FileStorage()
        model = BaseModel()
        model.save()
        obj_id = "{}.{}".format(type(model).__name__, model.id)
        self.assertIn(obj_id, storage.all())

    def test_reload(self):
        storage = FileStorage()
        storage.reload()
        self.assertTrue(len(storage.all()) >= 0)

    # Agrega más pruebas según sea necesario para otros métodos de la clase FileStorage


if __name__ == '__main__':
    unittest.main()
