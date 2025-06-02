#!/usr/bin/python3
"""
serializes instances to a JSON file and deserializes
JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ serialize and deserialize json files to and from instances """
    __file_path = 'file.json'
    __objects = {}
    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = (type(obj)).__name__ + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        if FileStorage.__file_path == None or\
            len(FileStorage.__file_path) == 0:
            return
        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as file:
                dictionary = json.load(file)
        except FileNotFoundError:
            return
        new_dict = {}
        objs = {'BaseModel': BaseModel, 'User': User}
        for key, value in dictionary.items():
            bases = objs[key](**value)
            new_dict[key] = bases
        FileStorage.__objects = new_dict
