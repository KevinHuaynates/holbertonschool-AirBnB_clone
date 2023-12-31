#!/usr/bin/python3
"""This module defines the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                obj_dict = storage.all()
                key = args[0] + "." + args[1]
                print(str(obj_dict[key]))
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                obj_dict = storage.all()
                key = args[0] + "." + args[1]
                del obj_dict[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of instances"""
        args = arg.split()
        obj_dict = storage.all()
        if not args:
            print([str(obj) for obj in obj_dict.values()])
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in obj_dict.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            try:
                obj_dict = storage.all()
                key = args[0] + "." + args[1]
                obj = obj_dict[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, eval(attr_value))
                obj.save()
            except KeyError:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

