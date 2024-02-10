#!/usr/bin/python3
'''
Unittests for file Storage class
'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_File_storage(unittest.TestCase):
    """ Test cases for the FileStorage class."""

    def setUp(self):
        """sets up each test case"""
        pass

    def tearDown(self):
        """free up memory after each test"""
        pass

    def test_priv_attributes(self):
        """ test to see that file_path and objects are private attributes"""
        new = FileStorage()
        with self.assertRaises(AttributeError):
            print(new.__file_path)
        with self.assertRaises(AttributeError):
            return(new.__objects)

    def test_all(self):
        """test function that returns dictionary objects"""
        new = FileStorage()
        hello = new.all()
        self.assertEqual({}, hello)

    def test_new(self):
        """test module that updates the dict __objects"""
        b = BaseModel()
        files = FileStorage()
        files.new(b)
        self.assertTrue(FileStorage._FileStorage__objects)

    if __name__ == '__main__':
        unittest.main()
