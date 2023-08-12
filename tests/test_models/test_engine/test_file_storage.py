#!/usr/bin/python3
"""Unittest for FileStorage class"""


import unittest
import os
import json
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """

    def setUp(self):
        """
        Set up the environment and objects for testing.
        """
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.obj1 = BaseModel()
#        self.obj2 = User()

    def tearDown(self):
        """
        Clean up after testing.

        This method removes temporary files or objects created during testing.
        """
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Test the 'all' method of FileStorage.

        test ensures that the 'all' method returns a dictionary
        containing all stored objects.
        """
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIs(all_objs, self.storage._FileStorage__objects)

    def test_new(self):
        """
        Test the 'new' method of FileStorage.

        test verifies that the 'new' method adds a new object to the storage.
        """
        self.storage.new(self.obj1)
        obj_key = "{}.{}".format(self.obj1.__class__.__name__, self.obj1.id)
        self.assertIn(obj_key, self.storage._FileStorage__objects)

    def test_save(self):
        """
        Test the 'save' method of FileStorage.

        checks if the 'save' method correctly stores objects in file storage.
        """
        self.storage.new(self.obj1)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            file_content = json.load(f)
        obj_key = "{}.{}".format(self.obj1.__class__.__name__, self.obj1.id)
        self.assertIn(obj_key, file_content)

    def test_reload(self):
        """
        Test the 'reload' method of FileStorage.

        verifies that 'reload' method restores objects from the file storage.
        """
        self.storage.new(self.obj1)
        self.storage.save()
        self.storage.reload()
        obj_key = "{}.{}".format(self.obj1.__class__.__name__, self.obj1.id)
        self.assertIn(obj_key, self.storage._FileStorage__objects)

    def test_reload_nonexistent_file(self):
        """
        Test reloading when the file does not exist.

        ensures that 'reload' method handles when file does not exist case.
        """
        self.storage.reload()


if __name__ == '__main__':
    unittest.main()
