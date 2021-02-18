#!/usr/bin/python3
""" Test fo Amenity class """
import unittest
import json
import pep8
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Unittest for amenity Class"""
    def test_pep8(self):
        """ Test pep8 style correct """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_city(self):
        """ Test pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)

    def test_str_format(self):
        """ Test if the strting representation is correct """
        my_obj = Amenity()
        str_format = "[Amenity] ({}) {}".format(my_obj.id, my_obj.__dict__)
        self.assertEqual(str_format, str(my_obj))

    def test_name_attr(self):
        """ Test Amenity instance has attribute name, and is empty """
        n = Amenity()
        self.assertTrue(hasattr(n, "name"))
        self.assertEqual(n.name, "")

    def test_regular_working(self):
        """ Test correct working """
        new = Amenity()
        self.assertEqual(type(new).__name__, "Amenity")

    def test_to_dict(self):
        """ Test to_dict method """
        n = Amenity()
        ndict = n.to_dict()
        self.assertEqual(type(ndict), dict)
        for attr in n.__dict__:
            self.assertTrue(attr in ndict)
        self.assertTrue("__class__" in ndict)
