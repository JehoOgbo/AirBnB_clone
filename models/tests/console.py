#!/usr/bin/python3
'''
this module contains the entry point of the command interpreter
'''
import cmd
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage
import json
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ''' Command interpreter for Airbnb clone.'''
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place']
    classes.append('Review')

    def strip(self, arg):
        """strip input of leading '"' characters"""
        count = 0
        for item in arg:
            if item[0] in ['"', "'"] and item[-1] in ['"', "'"]:
                print("Iwork")
                item = item[1:-1]
                print(item)
                arg[count] = item
            count = count + 1
        return arg

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """return true. Needed to exit the program"""
        print("")
        return True

    def help_quit(self):
        """print help text for quit command"""
        print('\n' + 'Quit command to exit the program')

    def emptyline(self):
        pass

    def do_create(self, classname):
        """Create a new instance of baseModel, save it and print its id"""
        if not classname:
            print("** class name missing **")
            return
        if classname not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if classname == 'BaseModel':
            new = BaseModel()
        elif classname == 'User':
            new = User()
        elif classname == 'State':
            new = State()
        elif classname == 'City':
            new = City()
        elif classname == 'Amenity':
            new = Amenity()
        elif classname == 'Place':
            new = Place()
        elif classname == 'Review':
            new = Review()
        new.save()
        print(new.id)

    def do_show(self, classinfo):
        """Print the string representation of an instance"""
        if not classinfo:
            print("** class name missing **")
            return
        liste = classinfo.split()
        if liste[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(liste) < 2:
            print("** instance id missing **")
            return
        try:
            with open(FileStorage._FileStorage__file_path, 'r') as jfile:
                dictobject = json.load(jfile)
                for key, value in dictobject.items():
                    val = '__class__'
                    if value['id'] == liste[1] and value[val] == liste[0]:
                        print(liste[0])
                        if liste[0] == 'BaseModel':
                            new = BaseModel(**value)
                        elif liste[0] == 'User':
                            new = User(**value)
                        elif liste[0] == 'State':
                            new = State(**value)
                        elif liste[0] == 'City':
                            new = City(**value)
                        elif liste[0] == 'Amenity':
                            new = Amenity(**value)
                        elif liste[0] == 'Place':
                            new = Place(**value)
                        elif liste[0] == 'Review':
                            new = Review(**value)
                        print(new)
                        return
                print("** no instance found **")
        except FileNotFoundError:
            print("** no instance found **")

    def help_show(self):
        """print help info for command show"""
        print('\n' + 'Print the string representation of an instance' +
              'based on the class name and id.' + '\n' +
              'Usage: show <class_name> <id>')

    def do_destroy(self, classinfo):
        """Deletes an instance based on the class name and id"""
        if not classinfo:
            print("** class name missing **")
            return
        liste = classinfo.split()
        if liste[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(liste) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        new_str = liste[0] + '.' + liste[1]
        if new_str not in obj_dict.keys():
            print("** no instance found **")
            return
        del obj_dict[new_str]
        storage.save()

    def do_all(self, class_name):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all <class_name> or all
        Prints a list of strings
        """
        if class_name and class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        # work for only basemodel
        num = -1
        if class_name:
            length = len(HBNBCommand.classes)
            for num in range(0, length):
                if class_name == HBNBCommand.classes[num]:
                    break
        obj_dict = storage.all()
        lister = []
        for key, value in obj_dict.items():
            new_str = str(value)
            if num != -1:
                newer = key.split('.')
                if newer[0] == HBNBCommand.classes[num]:
                    lister.append(new_str)
            else:
                lister.append(new_str)
        print(lister)

    def do_update(self, info):
        '''Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value"'''
        if not info:
            print("** class name missing **")
            return
        words = info.split()
        obj_dict = storage.all()
        if words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print('** instance id missing **')
            return
        if len(words) > 1:
            new_str = words[0] + '.' + words[1]
            if new_str not in obj_dict.keys():
                print("** no instance found **")
                return
        if len(words) == 2:
            print('** attribute name missing **')
        elif len(words) == 3:
            print('** value missing **')
        else:
            words = self.strip(words)
            new_str = words[0] + '.' + words[1]
            obj = obj_dict[new_str]
            if words[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[words[2]])
                obj.__dict__[words[2]] = valtype(words[3])
            else:
                obj.__dict__[words[2]] = words[3]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
