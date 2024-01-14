#!/usr/bin/python3
"""define a test class from the city object"""
import datetime
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """a test class to test the city class"""
    def test_default_values(self):
        """Test that the default values are as expected"""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_inherited_attributes(self):
        """test the attributes inherited from the BaseModel"""
        city = City()
        # the object must have an id
        self.assertIsNotNone(city.id)
        # created_at and updated_at must be of type datetyime
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertIsInstance(city.updated_at, datetime.datetime)

    def test_set_attributes(self):
        """Test setting attributes and check if they are set correctly"""
        city = City()
        city.name = "Doe"
        city.state_id = "123"

        self.assertEqual(city.name, "Doe")
        self.assertEqual(city.state_id, "123")
