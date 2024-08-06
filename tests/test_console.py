#!/usr/bin/python3

"""Tests the Console Module"""
import unittest
import sys
import models
from console import HBNBCommand
import os
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Tests the functionality of the HBNB console."""
    @classmethod
    def setUpClass(cls):
        try:
            os.rename('file.json', 'tmp_file.json')
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove('file.json')
            os.rename('tmp_file.json', 'file.json')
        except IOError:
            pass
        del cls.HBNB
        if isinstance(models.storage, DBStorage):
            models.storage._DBStorage__session.close()

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    # @unittest.skipIf(type(models.storage) == DBStorage, 'Testing DBStorage')
    def test_create(self):
        """Tests the create function."""
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('create BaseModel')
            new_basemodel = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Amenity")
            new_amenity = test.getvalue().strip()


if __name__ == '__main__':
    unittest.main()
