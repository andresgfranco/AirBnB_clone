#!/usr/bin/python3
""" Test for City class """
import unittest
import json
import pep8
from models.city import City


class TestCity(unittest.TestCase):
    """ Unittest for City class """
    def test_pep8(self):
        """ Test pep8 style correct """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_city(self):
        """ Test pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)
        self.assertTrue(len(City.__init__.__doc__) > 1)

    def test_str_format(self):
        """ Test if the strting representation is correct """
        my_obj = City()
        str_format = "[City] ({}) {}".format(my_obj.id, my_obj.__dict__)
        self.assertEqual(str_format, str(my_obj))

    def test_name_attr(self):
        """ Test City instance has attribute name, and is empty """
        n = City()
        self.assertTrue(hasattr(n, "name"))
        self.assertEqual(n.name, "")

    def test_regular_working(self):
        """ Test correct working """
        new = City()
        self.assertEqual(type(new).__name__, "City")

    def test_to_dict(self):
        """ Test to_dict method """
        n = City()
        ndict = n.to_dict()
        self.assertEqual(type(ndict), dict)
        for attr in n.__dict__:
            self.assertTrue(attr in ndict)
        self.assertTrue("__class__" in ndict)
