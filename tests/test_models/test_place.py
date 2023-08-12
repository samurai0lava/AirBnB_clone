#!/usr/bin/python3
"""Unit tests for the Place class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up for the test"""
        self.place = Place()

    def tearDown(self):
        """Clean up after the test"""
        del self.place

    def test_instance_creation(self):
        """Test Place instance creation"""
        self.assertIsInstance(self.place, Place)

    def test_attributes_initialization(self):
        """Test Place attributes initialization"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_types(self):
        """Test Place attribute types"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
