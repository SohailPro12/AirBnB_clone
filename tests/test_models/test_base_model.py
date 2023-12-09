#!/usr/bin/python3

"""
Tests for the BaseModel classs
"""

import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        initial_updated_at = self.base_model.updated_at
        with patch('models.storage.save') as mock_save:
            self.base_model.save()
            self.assertNotEqual(self.base_model.updated_at, initial_updated_at)
            mock_save.assert_called_once()

    def test_to_dict_method(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertCountEqual(model_dict.keys(), expected_keys)
        self.assertEqual(model_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
