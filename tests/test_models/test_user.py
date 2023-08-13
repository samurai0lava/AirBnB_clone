#!/bin/python3
"""Test module for User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_default_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_setting_attributes(self):
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_to_dict_method(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")

    def test_from_dict_method(self):
        user_dict = {
            "email": "test@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "__class__": "User",
            "id": "12345",
            "created_at": "2023-08-10T00:00:00.000000",
            "updated_at": "2023-08-10T12:00:00.000000"
        }
        new_user = User(**user_dict)
        self.assertEqual(new_user.email, "test@example.com")
        self.assertEqual(new_user.password, "password123")
        self.assertEqual(new_user.first_name, "John")
        self.assertEqual(new_user.last_name, "Doe")
        self.assertEqual(new_user.id, "12345")
        self.assertEqual(str(new_user.created_at), "2023-08-10 00:00:00")
        self.assertEqual(str(new_user.updated_at), "2023-08-10 12:00:00")


if __name__ == '__main__':
    unittest.main()
