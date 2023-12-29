#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
"""This class defines the command interpreter"""

    prompt = '(hbnb) '

    def emptyline(self):
    """Do nothing on an empty line + ENTER.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handles the EOF signal to exit the program.
        """
        print()
        return True

    def help_EOF(self):
        """
        Help message for the EOF signal.
        """
        print("EOF signal to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

