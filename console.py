#!/usr/bin/python3
"""contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ defines the command interpreter """
    prompt = '(hbnb) '

    def emptyline(self):
        """An empty line should not execute anything"""
        pass

    def do_EOF(self, arg):
        """Print newline and exit the interpreter"""
        return True

    def do_quit(self, arg):
        """Print new_line and exit the interpreter"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
