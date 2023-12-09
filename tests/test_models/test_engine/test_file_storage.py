#!/usr/bin/python3

"""
Test for the FileStorage class
"""

from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import unittest


class TestCodeUnderTest(unittest.TestCase):

    def test_base_model_instance(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.password)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)

    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsNotNone(state.name)


if __name__ == '__main__':
    unittest.main()
