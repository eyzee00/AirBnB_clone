#!/usr/bin/python3
"""define a test class from the amenity object"""
import datetime
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """a test class to test the amenity class"""
    def test_default_values(self):
        """Test that the default values are as expected"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inherited_attributes(self):
        """test the attributes inherited from the BaseModel"""
        amenity = Amenity()
        # the object must have an id
        self.assertIsNotNone(amenity.id)
        # created_at and updated_at must be of type datetyime
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)

    def test_set_attributes(self):
        """Test setting attributes and check if they are set correctly"""
        amentity = Amenity()
        amentity.name = "Doe"

        self.assertEqual(amentity.name, "Doe")
