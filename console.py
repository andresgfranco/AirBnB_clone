#!/usr/bin/python3
"""Module for entry point
of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand
    for command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the cmd"""
        return True
    def do_quit(self, line):
        """quit command to exit the cmd"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
