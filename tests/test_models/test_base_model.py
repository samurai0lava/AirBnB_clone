#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classe:
    TestBaseModel
"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_init_with_kwargs(self):
        """
        Test instantiation of BaseModel with keyword arguments.

        """
        d_f = '%Y-%m-%dT%H:%M:%S.%f'
        created_at = "2023-08-09T12:34:56.789012"
        updated_at = "2023-08-09T13:45:30.987654"
        obj_dict = {
            "id": "test-id",
            "created_at": created_at,
            "updated_at": updated_at
        }
        obj = BaseModel(**obj_dict)

        self.assertEqual(obj.id, "test-id")
        self.assertEqual(obj.created_at, datetime.strptime(created_at, d_f))
        self.assertEqual(obj.updated_at, datetime.strptime(updated_at, d_f))

    def test_init_without_kwargs(self):
        """
        Test instantiation of BaseModel without keyword arguments.

        """
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save(self):
        """
        Test the 'save' method of BaseModel.

        """
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(prev_updated_at, obj.updated_at)

    def test_to_dict(self):
        """
        Test the 'to_dict' method of BaseModel.

        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
