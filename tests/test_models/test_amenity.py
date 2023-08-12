#!/usr/bin/python3
"""Test module for Amenity class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_name_is_string(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_inherits_from_base_model(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_str_representation(self):
        expected = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        new_updated_at = self.amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict, dict)


    def test_to_dict_updated_at_is_str(self):
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_created_at_is_str(self):
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)

    def test_to_dict_has_correct_class_name(self):
        obj_dict = self.amenity.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Amenity')

    def test_from_dict_creates_instance(self):
        obj_dict = self.amenity.to_dict()
        new_instance = Amenity(**obj_dict)
        self.assertIsInstance(new_instance, Amenity)

    def test_from_dict_attributes_match(self):
        obj_dict = self.amenity.to_dict()
        new_instance = Amenity(**obj_dict)
        self.assertEqual(self.amenity.id, new_instance.id)
        self.assertEqual(self.amenity.created_at, new_instance.created_at)
        self.assertEqual(self.amenity.updated_at, new_instance.updated_at)
        self.assertEqual(self.amenity.name, new_instance.name)


if __name__ == '__main__':
    unittest.main()
