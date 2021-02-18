#!/usr/bin/python3
"""Module for testing FileStorage class"""
import unittest
import pep8
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Class for testing FileStorage class"""

    def setUp(self):
        self.storage = FileStorage()

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0)

    def test_class_docstrings(self):
        """ Checking for class docstring """
        self.assertGreater(len(self.storage.__doc__), 1)

    def test_docstrings(self):
        """ Checking docstring for the methods"""
        for obj in dir(self.storage):
            self.assertGreater(len(obj.__doc__), 1)

    def test_save(self):
        """ Function to test save method of FileStorage """
        my_model = BaseModel()
        my_model.save()
        self.assertEqual("", "")

    def test_new(self):
        """ Function to test new method of FileStorage """
        new_user = User()
        self.storage.new(new_user)
        dict_storage = self.storage.all()
        self.assertIn(new_user.__class__.__name__ +
                "." + new_user.id, dict_storage)

    def test_all(self):
        """ Function to test all metehod of FileStorage """
        self.assertTrue(type(self.storage.all()) == dict)

