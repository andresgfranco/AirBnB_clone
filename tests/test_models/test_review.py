#!/usr/bin/python3
""" Test for Review class """
import unittest
import json
import pep8
from models.review import Review


class TestReview(unittest.TestCase):
    """ Unittest for Review class """
    def test_pep8(self):
        """ Test pep8 style correct """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_city(self):
        """ Test pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)
        self.assertTrue(len(Review.__init__.__doc__) > 1)

    def test_str_format(self):
        """ Test if the strting representation is correct """
        my_obj = Review()
        str_format = "[Review] ({}) {}".format(my_obj.id, my_obj.__dict__)
        self.assertEqual(str_format, str(my_obj))

    def test_name_attr(self):
        """ Test Review instance has attribute text, and is empty """
        n = Review()
        self.assertTrue(hasattr(n, "text"))
        self.assertEqual(n.text, "")

    def test_place_id_attr(self):
        """ Test Review instance has attribute place_id, and is empty """
        n = Review()
        self.assertTrue(hasattr(n, "place_id"))
        self.assertEqual(n.place_id, "")

    def test_user_id_attr(self):
        """ Test Review instance has attribute user_id, and is empty """
        n = Review()
        self.assertTrue(hasattr(n, "user_id"))
        self.assertEqual(n.user_id, "")

    def test_regular_working(self):
        """ Test correct working """
        new = Review()
        self.assertEqual(type(new).__name__, "Review")

    def test_to_dict(self):
        """ Test to_dict method """
        n = Review()
        ndict = n.to_dict()
        self.assertEqual(type(ndict), dict)
        for attr in n.__dict__:
            self.assertTrue(attr in ndict)
        self.assertTrue("__class__" in ndict)
