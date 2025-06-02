#!/usr/bin/python3
"""contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """ defines the command interpreter """
    prompt = '(hbnb) '
    objs = {'BaseModel': BaseModel, 'User': User,
            'Amenity': Amenity,
            'State': State,
            'Place': Place,
            'City': City,
            'Review': Review}

    def emptyline(self):
        """An empty line should not execute anything"""
        pass

    def do_EOF(self, arg):
        """Print newline and exit the interpreter"""
        print("")
        return True

    def do_quit(self, arg):
        """Print new_line and exit the interpreter"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and print the id"""
        if arg is None or len(arg) == 0:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.objs.keys():
            print("** class doesn't exist **")
            return
        new = HBNBCommand.objs[arg]()
        new.save()
        print(new.id)

    def do_show(self, arg):
        """Print an instance based on class name and id"""
        args = arg.split()
        if arg is None or len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.objs.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        new = storage.all()
        if new is None or len(new) == 0:
            print("** no instance found **")
            return
        name = args[0] + '.' + args[1]
        for key, value in new.items():
            if key == name:
                print(value)
                return
        print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances based or not on class name"""
        obj_list = ['BaseModel', 'User', 'State', 'Place', 'City',
                    'Amenity', 'Review']
        if arg is None or len(arg) == 0:
            storage.reload()
            every = storage.all()
            for value in every.values():
                print(value)
        elif arg in obj_list:
            index = obj_list.index(arg)
            storage.reload()
            every = storage.all()
            lister = []
            for key in every.keys():
                dey = key.split('.')
                if dey[0] == obj_list[index]:
                    lister.append(every[key].__str__())
            print(lister)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if arg is None or len(arg) == 0:
            print("** class name missing **")
            return
        result = re.split(r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)', arg)
        storage.reload()
        checker = storage.all()
        if result[0] not in HBNBCommand.objs.keys():
            print("** class doesn't exist **")
            return
        if len(result) < 2:
            print("** instance id missing **")
            return
        string = result[0] + '.' + result[1]
        if string not in checker.keys():
            print("** no instance found **")
            return
        if len(result) < 3:
            print("** attribute name missing **")
            return
        if len(result) < 4:
            print("** value missing **")
            return
        result[3] = (result[3]).strip('"')
        setattr(checker[string], result[2], result[3])
        storage.save()

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if arg is None or len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.objs.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        new = storage.all()
        for key in new.keys():
            if key == args[0] + '.' + args[1]:
                keep = new.pop(key)
                del keep
                storage.save()
                return
        print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
