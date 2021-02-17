#!/usr/bin/python3
""" Test for Place class """
import unittest
import json
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Unittest fot Place class """
    def test_pep8(self):
        """ Test pep8 style correct """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_city(self):
        """ Test pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Place.__init__.__doc__
        self.assertGreater(len(doc), 1)
        self.assertTrue(len(Place.__init__.__doc__) > 1)

    def test_str_format(self):
        """ Test if the strting representation is correct """
        my_obj = Place()
        str_format = "[Place] ({}) {}".format(my_obj.id, my_obj.__dict__)
        self.assertEqual(str_format, str(my_obj))

    def test_city_id_attr(self):
        """ Test Place instance has attribute city_id, and is empty """
        n = Place()
        self.assertTrue(hasattr(n, "city_id"))
        self.assertEqual(n.city_id, "")

    def test_user_id_attr(self):
        """ Test Place instance has attribute user_id, and is empty """
        n = Place()
        self.assertTrue(hasattr(n, "user_id"))
        self.assertEqual(n.user_id, "")

    def test_name_attr(self):
        """ Test Place instance has attribute name, and is empty """
        n = Place()
        self.assertTrue(hasattr(n, "name"))
        self.assertEqual(n.name, "")

    def test_description_attr(self):
        """ Test Place instance has attribute description, and is empty """
        n = Place()
        self.assertTrue(hasattr(n, "description"))
        self.assertEqual(n.description, "")

    def test_number_rooms_attr(self):
        """ Test Place instance has attribute number_rooms, and is 0 """
        n = Place()
        self.assertTrue(hasattr(n, "number_rooms"))
        self.assertEqual(n.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """ Test Place instance has attribute number_bathrooms, and is 0 """
        n = Place()
        self.assertTrue(hasattr(n, "number_bathrooms"))
        self.assertEqual(n.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """ Test Place instance has attribute max_guest, and is 0 """
        n = Place()
        self.assertTrue(hasattr(n, "max_guest"))
        self.assertEqual(n.max_guest, 0)

    def test_price_by_night_attr(self):
        """ Test Place instance has attribute price_by_night, and is 0 """
        n = Place()
        self.assertTrue(hasattr(n, "price_by_night"))
        self.assertEqual(n.price_by_night, 0)

    def test_latitude_attr(self):
        """ Test Place instance has attribute latitude, and is 0.0 """
        n = Place()
        self.assertTrue(hasattr(n, "latitude"))
        self.assertEqual(n.latitude, 0.0)

    def test_longitude_attr(self):
        """ Test Place instance has attribute longitude, and is 0.0 """
        n = Place()
        self.assertTrue(hasattr(n, "longitude"))
        self.assertEqual(n.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """ Test Place instance has attribute amenity_ids, and is empty """
        n = Place()
        self.assertTrue(hasattr(n, "amenity_ids"))
        self.assertEqual(n.amenity_ids, [])

    def test_regular_working(self):
        """ Test correct working """
        new = Place()
        self.assertEqual(type(new).__name__, "Place")

    def test_to_dict(self):
        """ Test to_dict method """
        n = Place()
        ndict = n.to_dict()
        self.assertEqual(type(ndict), dict)
        for attr in n.__dict__:
            self.assertTrue(attr in ndict)
        self.assertTrue("__class__" in ndict)
