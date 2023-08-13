#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classe :
    TestBaseModel
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.

    This module contains test cases
    that cover various aspects of the BaseModel class.
    """

    def setUp(self):
        """
        Set up an instance of BaseModel for testing.
        """
        self.base_model = BaseModel()

    def test_instance_attributes(self):
        """
        Test if the BaseModel instance has the expected attributes.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        """
        Test if the 'id' attribute of BaseModel is of type string.
        """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test if the 'created_at' attribute of BaseModel
        is of type datetime.datetime.
        """
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if the 'updated_at' attribute of BaseModel
        is of type datetime.datetime.
        """
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str_representation(self):
        """
        Test if the string representation
        of BaseModel is formatted correctly.
        """
        expected = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected)

    def test_save_updates_updated_at(self):
        """
        Test if the 'save' method updates
        the 'updated_at' attribute of BaseModel.
        """
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        """
        Test if the 'to_dict' method returns a dictionary.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_attributes(self):
        """
        Test if the dictionary returned by 'to_dict'
        contains required attributes.
        """
        obj_dict = self.base_model.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def test_to_dict_updated_at_is_str(self):
        """
        Test if the 'updated_at' attribute in the dictionary
        returned by 'to_dict' is of type str.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_created_at_is_str(self):
        """
        Test if the 'created_at' attribute in the dictionary
        returned by 'to_dict' is of type str.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)

    def test_to_dict_has_correct_class_name(self):
        """
        Test if the '__class__' key in the dictionary returned by 'to_dict'
        matches 'BaseModel'.
        """
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_from_dict_creates_instance(self):
        """
        Test if an instance of BaseModel can be created using the dictionary
        returned by 'to_dict'.
        """
        obj_dict = self.base_model.to_dict()
        new_instance = BaseModel(**obj_dict)
        self.assertIsInstance(new_instance, BaseModel)

    def test_from_dict_attributes_match(self):
        """
        Test if the attributes of the newly created instance using 'from_dict'
        match the original BaseModel instance.
        """
        obj_dict = self.base_model.to_dict()
        new_instance = BaseModel(**obj_dict)
        self.assertEqual(self.base_model.id, new_instance.id)
        self.assertEqual(self.base_model.created_at, new_instance.created_at)
        self.assertEqual(self.base_model.updated_at, new_instance.updated_at)


if __name__ == '__main__':
    unittest.main()
