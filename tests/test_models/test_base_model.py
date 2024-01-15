#!/usr/bin/python3
"""defines a class for testing the basemdoule module"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases"""
    def test_instaance_creation(self):
        """test actions related to instance creation"""
        model = BaseModel()
        # the object must have an id
        self.assertIsNotNone(model.id)
        # created_at and updated_at must be of type datetyime
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_kwargs_instance_creation(self):
        """test the passed object through kwargs"""
        # an object with id and a custom attribute
        data = {'id': '123',
                'crated_at': '2017-09-28T21:07:25.047372',
                'updated_at': '2017-09-28T21:07:25.047372',
                'custom_attr': 'value'}
        model = BaseModel(**data)
        self.assertAlmostEqual(model.id, '123')
        self.assertEqual(model.custom_attr, 'value')
        # test the type convertion to datetime
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

        # an object with no id passed
        data2 = {'custom_attr': 'value'}
        model2 = BaseModel(**data2)
        self.assertIsNotNone(model2.id)
        self.assertAlmostEqual(model2.custom_attr, 'value')
        self.assertIsInstance(model2.created_at, datetime.datetime)
        self.assertIsInstance(model2.updated_at, datetime.datetime)

    def test_save_method(self):
        """test if the save funciton update the update_at value"""
        model = BaseModel()
        intial_update_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, intial_update_at)

    def test_to_dict_method(self):
        """test if to_dict return the expected dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_str_method(self):
        """test the string representation of the model"""
        model = BaseModel()
        str_rep = str(model)
        self.assertIn('BaseModel', str_rep)
        self.assertIn(model.id, str_rep)
