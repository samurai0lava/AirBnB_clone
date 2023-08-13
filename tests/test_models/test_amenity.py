#!/usr/bin/python3
"""Test module for Amenity class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Unit tests for the Amenity class."""

    def setUp(self):
        """ Set up an instance of Amenity for testing."""
        self.amenity = Amenity()

    def test_attributes(self):
        """ Test if the Amenity instance has the expected attributes."""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_name_is_string(self):
        """ Test if the 'name' attribute of Amenity is of type string."""
        self.assertIsInstance(self.amenity.name, str)

    def test_inherits_from_base_model(self):
        """Test if Amenity class inherits from the BaseModel class."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_str_representation(self):
        """Test if string representation of Amenity is formatted correctly."""
        expected = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected)

    def test_created_at_is_datetime(self):
        """Test if 'created_at' attribute of Amenity is of type datetime."""
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if 'updated_at' attribute of Amenity is of type datetime."""
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test if 'save' method updates the 'updated_at' attribute of Amenity.
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        new_updated_at = self.amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        """ Test if the 'to_dict' method returns a dictionary."""
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_updated_at_is_str(self):
        """
        Test if 'updated_at' attribute in the dictionary
        returned by 'to_dict' is type str.
        """
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_created_at_is_str(self):
        """
        Test if 'created_at' attribute in the dictionary
        returned by 'to_dict' is of type str.
        """
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)

    def test_to_dict_has_correct_class_name(self):
        """
        Test if the '__class__' key in the dictionary
        returned by 'to_dict' matches 'Amenity'.
        """
        obj_dict = self.amenity.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Amenity')

    def test_from_dict_creates_instance(self):
        """
        Test if an instance of Amenity can be created using
        the dictionary returned by 'to_dict'.
        """
        obj_dict = self.amenity.to_dict()
        new_instance = Amenity(**obj_dict)
        self.assertIsInstance(new_instance, Amenity)

    def test_from_dict_attributes_match(self):
        """
        Test if the attributes of the newly created instance using 'from_dict'
        match the original Amenity instance.
        """
        obj_dict = self.amenity.to_dict()
        new_instance = Amenity(**obj_dict)
        self.assertEqual(self.amenity.id, new_instance.id)
        self.assertEqual(self.amenity.created_at, new_instance.created_at)
        self.assertEqual(self.amenity.updated_at, new_instance.updated_at)
        self.assertEqual(self.amenity.name, new_instance.name)


if __name__ == '__main__':
    unittest.main()
