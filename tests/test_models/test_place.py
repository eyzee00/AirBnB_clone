#!/usr/bin/python3
"""define a test class from the place object"""
import datetime
from models.place import Place
import unittest


class TestAmenity(unittest.TestCase):
    """a test class to test the place class"""
    def test_default_values(self):
        """Test that the default values are as expected"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.altitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inherited_attributes(self):
        """test the attributes inherited from the BaseModel"""
        place = Place()
        # the object must have an id
        self.assertIsNotNone(place.id)
        # created_at and updated_at must be of type datetyime
        self.assertIsInstance(place.created_at, datetime.datetime)
        self.assertIsInstance(place.updated_at, datetime.datetime)

    def test_set_attributes(self):
        """Test setting attributes and check if they are set correctly"""
        place = Place()
        place.city_id = "001"
        place.user_id = "USER001"
        place.name = "place"
        place.description = "lorem apsum"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 200
        place.latitude = 23.57655
        place.altitude = 34.56835
        place.amenity_ids = ['A324', 'B234']

        self.assertEqual(place.city_id, "001")
        self.assertEqual(place.user_id, "USER001")
        self.assertEqual(place.name, "place")
        self.assertEqual(place.description, "lorem apsum")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 200)
        self.assertEqual(place.latitude, 23.57655)
        self.assertEqual(place.altitude, 34.56835)
        self.assertEqual(place.amenity_ids, ['A324', 'B234'])
