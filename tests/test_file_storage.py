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

    def test_new_method(self):
        """test the new method"""
        pass

    def test_save_method(self):
        """test the save method"""
        pass

    def test_reload_method(self):
        """test the reload function"""
        pass
