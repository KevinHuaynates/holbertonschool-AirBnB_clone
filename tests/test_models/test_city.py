#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_init(self):
        city = City()
        self.assertIsNotNone(city.id)

    # Agrega más pruebas según sea necesario para los métodos de la clase City


if __name__ == '__main__':
    unittest.main()
