#!/usr/bin/python3
"""defines tests for the file storage model"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """class for testing file storage model"""

    def test_all_method(self):
        """test the all method"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)
        test_model = BaseModel()
        storage.new(test_model)
        self.assertIn("BaseModel." + test_model.id, storage.all().keys())

    def test_new_method(self):
        """test the new method"""
        storage = FileStorage()
        test_model = BaseModel()
        storage.new(test_model)
        self.assertIn("BaseModel." + test_model.id, storage.all().keys())

    def test_save_method(self):
        """test the save method"""
        storage = FileStorage()
        test_model = BaseModel()
        storage.new(test_model)
        storage.save()
        saved_json = " "
        with open("file.json", "r") as file:
            saved_json = file.read()
            self.assertIn("BaseModel." + test_model.id, saved_json)

    def test_reload_method(self):
        """test the reload function"""
        storage = FileStorage()
        test_model = BaseModel()
        storage.new(test_model)
        storage.save()
        storage.reload()
        reloaded_dict = storage.all()
        self.assertIn("BaseModel." + test_model.id, reloaded_dict)
