#!/usr/bin/python3
""" Entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ A Class that inherits from cmd.CMD """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ This method handles an empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
