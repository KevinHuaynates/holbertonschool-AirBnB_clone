#!/usr/bin/python3
"""
Module contiene 'HBNBCommand' class, un comando interprete de AirBnB project.

"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User

HBNB_CMD = {
    "BaseModel": BaseModel,
    "User": User
}

class HBNBCommand(cmd.Cmd):
    """
    Esta class define el comando interprete
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """
        No hacer nada , pass.
        """
        pass

    def do_quit(self, arg):
        """
        Salir del comando para salir del programa.
        """
        return True

    def help_quit(self):
        """
        Mensaje de ayuda para salir del programa.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Maneja la señal EOF para salir del programa.
        """
        print()
        return True

    def help_EOF(self):
        """
        Mensaje de ayuda para la señal EOF.
        """
        print("EOF signal to exit the program")

    def do_create(self, arg):
        """
        Crear comando para crear una nueva instancia.

        Uso: crear <nombre de clase>
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
        Mostrar comando para la representación de cadena de una instancia.

        Uso: mostrar <nombre de clase> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in HBNB_CMD:
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
        Comando Destruir para eliminar una instancia.

        Uso: destruir <nombre de clase> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in HBNB_CMD:
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
        Comandos para mostrar todas las instancias.

        Uso: todos [nombre de clase]
        """
        objs = models.storage.all()
        if not arg:
            print("[{}]".format(', '.join(str(obj) for obj in objs.values())))
            return

        if arg not in HBNB_CMD:
            print("** class doesn't exist **")
            return

        print("[{}]".format(', '.join(str(obj) for key, obj in objs.items() if arg in key)))

    def do_update(self, arg):
        """
        Comando de actualización para modificar una instancia.

        Uso: actualizar <nombre de clase> <id> <nombre de atributo> <valor de atributo>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in HBNB_CMD:
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

        obj = models.storage.all()
        if not arg:
            print("[{}]".format(', '.join(str(obj) for obj in objs.values())))
            return

        if arg not in HBNB_CMD:
            print("** class doesn't exist **")
            return
        print("[{}]".format(', '.join(str(obj) for key, obj in objs.items() if arg in key)))
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()

