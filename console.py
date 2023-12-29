#!/usr/bin/python3
"""
This module contains the HBNBCommand class, a command interpreter for the AirBnB project.

It provides a custom prompt, handles quit and EOF commands to exit the console,
and includes a help command.
"""

import cmd
import models
from models.user import User
from models.base_model import BaseModel

HBNB_CMD = {
    "BaseModel": BaseModel,
    "User": User  # Add this line to include User
}

class HBNBCommand(cmd.Cmd):
    """
    This class defines the command interpreter.
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """
        Do nothing on an empty line + ENTER.
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

    def do_create(self, arg):
        """
        Create command to create a new instance of a model.

        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show command to display the string representation of an instance.

        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return

        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance.

        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return

        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """
        All command to display all instances.

        Usage: all [class name]
        """
        objs = models.storage.all()
        if not arg:
            print("[{}]".format(', '.join(str(obj) for obj in objs.values())))
            return

        if arg not in models.classes:
            print("** class doesn't exist **")
            return

        print("[{}]".format(', '.join(str(obj) for key, obj in objs.items() if arg in key)))

    def do_update(self, arg):
        """
        Update command to modify an instance.

        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = models.storage.all()[key]
        setattr(obj, args[2], args[3])
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

