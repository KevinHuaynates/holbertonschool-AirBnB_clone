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
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                obj_dict = storage.all()
                key = args[0] + "." + args[1]
                print(obj_dict[key])
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                obj_dict = storage.all()
                key = args[0] + "." + args[1]
                del obj_dict[key]
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        obj_dict = storage.all()
        if not args:
            print([str(obj) for key, obj in obj_dict.items()])
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in obj_dict.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj_dict.keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = obj_dict[key]
            setattr(instance, args[2], eval(args[3]))
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

