#!/usr/bin/python3
"""
This module contains the HBNBCommand class, a command interpreter for the AirBnB project.

It provides a custom prompt, handles quit and EOF commands to exit the console,
and includes commands to create, show, destroy, update, and list instances.
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage


classes = {"BaseModel": BaseModel}


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
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        if not arg or arg not in classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all().values() if isinstance(obj, classes[arg])])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    obj = storage.all()[key]
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

