#!/usr/bin/python3
"""defines tests for the file storage model"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """class for testing file storage model"""

    def test_all_and_new_method(self):
        """test the all method"""
        self.assertIsInstance(storage.all(), dict)
        test_model = BaseModel()
        test_state = State()
        test_city = City()
        test_place = Place()
        test_user = User()
        test_amenity = Amenity()
        test_review = Review()
        storage.new(test_model)
        storage.new(test_state)
        storage.new(test_place)
        storage.new(test_city)
        storage.new(test_user)
        storage.new(test_amenity)
        storage.new(test_review)
        self.assertIn("BaseModel." + test_model.id, storage.all().keys())
        self.assertIn("User." + test_user.id, storage.all().keys())
        self.assertIn("State." + test_state.id, storage.all().keys())
        self.assertIn("City." + test_city.id, storage.all().keys())
        self.assertIn("Place." + test_place.id, storage.all().keys())
        self.assertIn("Amenity." + test_amenity.id, storage.all().keys())
        self.assertIn("Review." + test_review.id, storage.all().keys())

    def test_save_method(self):
        """test the save method"""
        test_model = BaseModel()
        test_state = State()
        test_city = City()
        test_place = Place()
        test_user = User()
        test_amenity = Amenity()
        test_review = Review()
        storage.new(test_model)
        storage.new(test_state)
        storage.new(test_place)
        storage.new(test_city)
        storage.new(test_user)
        storage.new(test_amenity)
        storage.new(test_review)
        storage.save()
        saved_json = " "
        with open("file.json", "r") as file:
            saved_json = file.read()
            self.assertIn("BaseModel." + test_model.id, saved_json)
            self.assertIn("User." + test_user.id, saved_json)
            self.assertIn("State." + test_state.id, saved_json)
            self.assertIn("City." + test_city.id, saved_json)
            self.assertIn("Place." + test_place.id, saved_json)
            self.assertIn("Amenity." + test_amenity.id, saved_json)
            self.assertIn("Review." + test_review.id, saved_json)

    def test_reload_method(self):
        """test the reload function"""
        test_model = BaseModel()
        test_state = State()
        test_city = City()
        test_place = Place()
        test_user = User()
        test_amenity = Amenity()
        test_review = Review()
        storage.new(test_state)
        storage.new(test_place)
        storage.new(test_city)
        storage.new(test_user)
        storage.new(test_amenity)
        storage.new(test_review)
        storage.new(test_model)
        storage.save()
        storage.reload()
        reloaded_dict = storage.all()
        self.assertIn("BaseModel." + test_model.id, reloaded_dict)
        self.assertIn("User." + test_user.id, reloaded_dict)
        self.assertIn("State." + test_state.id, reloaded_dict)
        self.assertIn("City." + test_city.id, reloaded_dict)
        self.assertIn("Place." + test_place.id, reloaded_dict)
        self.assertIn("Amenity." + test_amenity.id, reloaded_dict)
        self.assertIn("Review." + test_review.id, reloaded_dict)
