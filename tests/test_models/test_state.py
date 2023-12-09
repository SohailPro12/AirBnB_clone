#!/usr/bin/python3

"""
Test for the state class
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.state, BaseModel)


if __name__ == '__main__':
    unittest.main()
