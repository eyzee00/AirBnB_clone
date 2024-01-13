#!/usr/bin/python3
"""define a test class from the review object"""
import datetime
from models.review import Review
import unittest


class TestAmenity(unittest.TestCase):
    place_id = ""
    user_id = ""
    text = ""
    """a test class to test the review class"""
    def test_default_values(self):
        """Test that the default values are as expected"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inherited_attributes(self):
        """test the attributes inherited from the BaseModel"""
        review = Review()
        # the object must have an id
        self.assertIsNotNone(review.id)
        # created_at and updated_at must be of type datetyime
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertIsInstance(review.updated_at, datetime.datetime)

    def test_set_attributes(self):
        """Test setting attributes and check if they are set correctly"""
        review = Review()
        Review.place_id = "123"
        Review.user_id = "321"
        Review.text = "lurem apsum"

        self.assertEqual(Review.place_id, "123")
        self.assertEqual(Review.user_id, "321")
        self.assertEqual(Review.text, "lurem apsum")
