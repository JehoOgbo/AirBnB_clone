#!/usr/bin/python3
"""contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
import re


class HBNBCommand(cmd.Cmd):
    """ defines the command interpreter """
    prompt = '(hbnb) '

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
        elif arg != 'BaseModel':
            print("** class doesn't exist **")
            return
        new = BaseModel()
        new.save()
        print(new.id)

    def do_show(self, arg):
        """Print an instance based on class name and id"""
        args = arg.split()
        if arg is None or len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] != 'BaseModel':
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
        check = 0
        for key, value in new.items():
            if key == name:
                check = 1
                print(value)
                break
        if check == 0:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances based or not on class name"""
        if arg is None or len(arg) == 0:
            storage.reload()
            every = storage.all()
            for value in every.values():
                print(value)
        elif arg == 'BaseModel':
            storage.reload()
            every = storage.all()
            lister = []
            for key in every.keys():
                dey = key.split('.')
                if dey[0] == 'BaseModel':
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
        if result[0] != 'BaseModel':
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
        if args[0] != 'BaseModel':
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
