#!/usr/bin/python3
"""Test module for City class"""

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        """
        Set up for the test
        """
        self.city = City()

    def test_attributes(self):
        """
        Test City attributes initialization
        """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_state_id_is_string(self):
        """
        Test City attribute types
        """
        self.assertIsInstance(self.city.state_id, str)

    def test_name_is_string(self):
        """
        test name is string
        """
        self.assertIsInstance(self.city.name, str)

    def test_inherits_from_base_model(self):
        """
        Test City inheritance
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_str_representation(self):
        """
        Test City string representation
        """
        expected = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected)

    def test_created_at_is_datetime(self):
        """
        Test City created_at is datetime
        """
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test City updated_at is datetime
        """
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test City save method
        """
        old_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        """
        Test City to_dict method
        """
        obj_dict = self.city.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_attributes(self):
        """
        Test City dictionary contains correct attributes
        """
        obj_dict = self.city.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('state_id' in obj_dict)
        self.assertTrue('name' in obj_dict)

    def test_to_dict_updated_at_is_str(self):
        """
        Test City updated_at is string
        """
        obj_dict = self.city.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_created_at_is_str(self):
        """
        Test City created_at is string
        """
        obj_dict = self.city.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)

    def test_to_dict_has_correct_class_name(self):
        """
        Test City __class__ key in dictionary
        """
        obj_dict = self.city.to_dict()
        self.assertEqual(obj_dict['__class__'], 'City')

    def test_from_dict_creates_instance(self):
        """
        Test City from_dict method
        """
        obj_dict = self.city.to_dict()
        new_instance = City(**obj_dict)
        self.assertIsInstance(new_instance, City)

    def test_from_dict_attributes_match(self):
        """
        Test City from_dict method attributes match
        """
        obj_dict = self.city.to_dict()
        new_instance = City(**obj_dict)
        self.assertEqual(self.city.id, new_instance.id)
        self.assertEqual(self.city.created_at, new_instance.created_at)
        self.assertEqual(self.city.updated_at, new_instance.updated_at)
        self.assertEqual(self.city.state_id, new_instance.state_id)
        self.assertEqual(self.city.name, new_instance.name)


if __name__ == '__main__':
    unittest.main()
