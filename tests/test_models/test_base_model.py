#!/usr/bin/python3
""" Module to test cases """
import unittest
import json
import models
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Unit test class for Base Model class """
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_base_model(self):
        """Test that tests/test_models/test_base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_uuid(self):
        """testing different uuid"""
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        """testing datetime base model"""
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_4.updated_at)
        self.assertNotEqual(model_4.created_at, model_3.updated_at)

    def test_file_save(self):
        """Test that info is saved to file"""
        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r') as f:
            self.assertIn(b3.id, f.read())

    def test_regular_behavior(self):
        """ Test if object was correctly created """
        my_obj = BaseModel()
        self.assertIs(type(my_obj), BaseModel)
        my_obj.name = "Holberton"
        my_obj.number = 89
        self.assertEqual(my_obj.name, "Holberton")
        self.assertEqual(my_obj.number, 89)

    def test_constructor_kwargs(self):
        """Test constructor that has kwargs as attributes values"""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        json_attributes = obj.to_dict()
        obj2 = BaseModel(**json_attributes)
        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)

    def test_to_dict(self):
        """ Test JSON serialization """
        my_obj = BaseModel()
        my_obj.name = "Holberton"
        my_obj.number = 89
        mdict = my_obj.to_dict()
        expec_attr = ["id", "created_at", "updated_at",
                      "name", "number", "__class__"]
        self.assertCountEqual(mdict.keys(), expec_attr)
        self.assertEqual(mdict['name'], "Holberton")
        self.assertEqual(mdict['number'], 89)
        self.assertEqual(mdict['__class__'], "BaseModel")

    def test_str_format(self):
        """ Test the string representation is correct """
        my_obj = BaseModel()
        str_format = "[BaseModel] ({}) {}".format(my_obj.id, my_obj.__dict__)
        self.assertEqual(str_format, str(my_obj))
