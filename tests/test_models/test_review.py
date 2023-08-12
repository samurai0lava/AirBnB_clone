#!/usr/bin/python3
"""Test module for Review class"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_place_id_is_string(self):
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_is_string(self):
        self.assertIsInstance(self.review.user_id, str)

    def test_text_is_string(self):
        self.assertIsInstance(self.review.text, str)

    def test_inherits_from_base_model(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_str_representation(self):
        expected = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.review.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_updated_at_is_str(self):
        obj_dict = self.review.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_created_at_is_str(self):
        obj_dict = self.review.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)

    def test_to_dict_has_correct_class_name(self):
        obj_dict = self.review.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Review')

    def test_from_dict_creates_instance(self):
        obj_dict = self.review.to_dict()
        new_instance = Review(**obj_dict)
        self.assertIsInstance(new_instance, Review)

    def test_from_dict_attributes_match(self):
        obj_dict = self.review.to_dict()
        new_instance = Review(**obj_dict)
        self.assertEqual(self.review.id, new_instance.id)
        self.assertEqual(self.review.created_at, new_instance.created_at)
        self.assertEqual(self.review.updated_at, new_instance.updated_at)
        self.assertEqual(self.review.place_id, new_instance.place_id)
        self.assertEqual(self.review.user_id, new_instance.user_id)
        self.assertEqual(self.review.text, new_instance.text)


if __name__ == '__main__':
    unittest.main()
