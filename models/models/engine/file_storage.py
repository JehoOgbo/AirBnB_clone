#!/usr/bin/python3
""" For serialization and deserialization """
import json


class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return the dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding='utf-8') as jsonfile:
            dictobject = {}
            for key, value in FileStorage.__objects.items():
                dictobject[key] = value.to_dict()
            json.dump(dictobject, jsonfile)

    def reload(self):
        """ deserializes JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as jfile:
                dictobject = json.loads(jfile.read())
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                for key, value in dictobject.items():
                    if value['__class__'] == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == "User":
                        FileStorage.__objects[key] = User(**value)
                    elif value['__class__'] == "State":
                        FileStorage.__objects[key] = State(**value)
                    elif value['__class__'] == "City":
                        FileStorage.__objects[key] = City(**value)
                    elif value['__class__'] == "Amenity":
                        FileStorage.__objects[key] = Amenity(**value)
                    elif value['__class__'] == "Place":
                        FileStorage.__objects[key] = Place(**value)
                    elif value['__class__'] == "Review":
                        FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
