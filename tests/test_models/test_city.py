#!/usr/bin/python3

"""
Test for the city class
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)


if __name__ == '__main__':
    unittest.main()
