#!/usr/bin/python3
"""Test module for State class"""

import unittest
from models.base_model import BaseModel
from models.state import State
import datetime


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))

    def test_name_is_string(self):
        self.assertIsInstance(self.state.name, str)

    def test_inherits_from_base_model(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_str_representation(self):
        expected = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.state.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        new_updated_at = self.state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.state.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_updated_at_is_str(self):
        obj_dict = self.state.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_created_at_is_str(self):
        obj_dict = self.state.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)

    def test_to_dict_has_correct_class_name(self):
        obj_dict = self.state.to_dict()
        self.assertEqual(obj_dict['__class__'], 'State')

    def test_from_dict_creates_instance(self):
        obj_dict = self.state.to_dict()
        new_instance = State(**obj_dict)
        self.assertIsInstance(new_instance, State)

    def test_from_dict_attributes_match(self):
        obj_dict = self.state.to_dict()
        new_instance = State(**obj_dict)
        self.assertEqual(self.state.id, new_instance.id)
        self.assertEqual(self.state.created_at, new_instance.created_at)
        self.assertEqual(self.state.updated_at, new_instance.updated_at)
        self.assertEqual(self.state.name, new_instance.name)


if __name__ == '__main__':
    unittest.main()
