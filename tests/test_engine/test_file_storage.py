#!/usr/bin/python3
"""Module for testing FileStorage class"""
import unittest


class TestFileStorage(unittest.Testcase):
    """Class for testing FileStorage class"""
    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)
