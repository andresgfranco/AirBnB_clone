#!/usr/bin/python3
""" Module to test cases """
import unittest


class TestBaseModel(unittest.TestCase):
    """ Unit test class for Base Model class """
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0)
