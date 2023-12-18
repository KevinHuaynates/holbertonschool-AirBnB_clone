#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the console."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
