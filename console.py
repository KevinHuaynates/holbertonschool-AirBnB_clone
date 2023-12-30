#!/usr/bin/python3
"""
AirBnB Clone Console Module

This module provides an interactive console for managing AirBnB objects.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = '(hbnb) '

    def do_help(self, arg):
        """Prints a list of available commands."""
        print("Available commands: help, quit")

    def do_quit(self, arg):
        """Exits the console."""
        return True

    # Agrega aquí la implementación de otros comandos según tus necesidades

if __name__ == '__main__':
    HBNBCommand().cmdloop()

