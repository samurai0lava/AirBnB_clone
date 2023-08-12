#!/usr/bin/python3
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


if __name__ == '__main__':
    unittest.main()
