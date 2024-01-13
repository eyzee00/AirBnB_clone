#!/usr/bin/python3
"""define a test class from the state object"""
import datetime
from models.state import State
import unittest


class TestAmenity(unittest.TestCase):
    """a test class to test the state class"""
    def test_default_values(self):
        """Test that the default values are as expected"""
        state = State()
        self.assertEqual(state.name, "")

    def test_inherited_attributes(self):
        """test the attributes inherited from the BaseModel"""
        state = State()
        # the object must have an id
        self.assertIsNotNone(state.id)
        # created_at and updated_at must be of type datetyime
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)

    def test_set_attributes(self):
        """Test setting attributes and check if they are set correctly"""
        state = State()
        state.name = "Doe"

        self.assertEqual(state.name, "Doe")
