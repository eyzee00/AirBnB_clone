#!/usr/bin/python3
"""defines a test class for the User class"""
import datetime
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """A class to test the User class"""
    def test_default_values(self):
        """Test that the default values are as expected"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inherited_attributes(self):
        """test the attributes inherited from the BaseModel"""
        model = User()
        # the object must have an id
        self.assertIsNotNone(model.id)
        # created_at and updated_at must be of type datetyime
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_set_attributes(self):
        """Test setting attributes and check if they are set correctly"""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
