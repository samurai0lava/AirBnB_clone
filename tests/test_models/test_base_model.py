#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str_representation(self):
        expected = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_attributes(self):
        obj_dict = self.base_model.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def test_to_dict_updated_at_is_str(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_created_at_is_str(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)

    def test_to_dict_has_correct_class_name(self):
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_from_dict_creates_instance(self):
        obj_dict = self.base_model.to_dict()
        new_instance = BaseModel(**obj_dict)
        self.assertIsInstance(new_instance, BaseModel)

    def test_from_dict_attributes_match(self):
        obj_dict = self.base_model.to_dict()
        new_instance = BaseModel(**obj_dict)
        self.assertEqual(self.base_model.id, new_instance.id)
        self.assertEqual(self.base_model.created_at, new_instance.created_at)
        self.assertEqual(self.base_model.updated_at, new_instance.updated_at)


if __name__ == '__main__':
    unittest.main()
