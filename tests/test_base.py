#!/usr/bin/python3
'''Unittest for basemodels
'''
import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Define unittests for class BaseModel"""

    def setUp(self):
        """sets up test methods"""
        pass

    def tearDown(self):
        """ Tears down test methods"""
        self.resetStorage()

    def resetStorage(self):
        """ Deletes storage file after every test"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """ tests to see that object is created when no args are passed"""
        test = BaseModel()
        self.assertIsInstance(test, BaseModel)
        self.assertTrue(test.id)
        self.assertTrue(test.updated_at)
        self.assertTrue(test.created_at)
        self.assertTrue(issubclass(type(test), BaseModel))

    def test_save(self):
        """ tests public instance method save"""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        with self.assertRaises(TypeError):
            b.save("see")  # takes no external arguments

    def test_to_dict(self):
        """ tests the public instance method to_dict """
        b = BaseModel()
        b.name = "Emma"
        b.age = 16
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["name"], b.name)
        self.assertEqual(d["age"], b.age)
        # test excess args
        with self.assertRaises(TypeError):
            BaseModel.to_dict(self, 98)

    def test_kwargs_instantiate(self):
        """ test instantiation with kwargs"""
        d = {"__class__": "BaseModel",
             "updated_at": datetime.now().isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "mooni",
             "int": 783}
        o = BaseModel(**d)
        self.assertEqual(o.to_dict(), d)

    if __name__ == '__main__':
        unittest.main()
