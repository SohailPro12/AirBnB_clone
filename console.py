#!/usr/bin/python3
""" Entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ A Class that inherits from cmd.CMD """
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ This method handles an empty line """
        pass

    def do_create(self, line):
        """
        creates a new instance of a specified class
        and prints its ID
        """
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name in HBNBCommand.classes:
            obj = HBNBCommand.classes[class_name]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)

        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)

        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def default(self, line):
        """handle <class name>.all()"""
        if '.' in line and 'all()' in line:
            arguments = line.split(".")
            Theclass_name = arguments[0]
            if Theclass_name in HBNBCommand.classes:
                self.do_all(Theclass_name)
        elif '.' in line and 'count()' in line:
            arguments = line.split(".")
            Theclass_name = arguments[0]
            if Theclass_name in HBNBCommand.classes:
                self.do_count(Theclass_name)

    def do_count(self, arg):
        """
        Counts the number of instances of a class.
        
        Args:
            arg: the name of the class.
        """
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == arg:
                count += 1
        print(count)

    def do_all(self, line):
        """
        Prints all string representation of instances
        """
        args = line.split()
        if not args:
            objs = [str(obj) for obj in storage.all().values()]
            if not objs:
                return
            else:
                print(objs)
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objs = [str(obj) for obj in storage.all().values()
                    if obj.__class__.__name__ == args[0]]
            print(objs)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)

        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        obj = storage.all()[key]

        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]

        if attr_name in ["id", "created_at", "updated_at"]:
            return

        try:
            the_attr = getattr(obj, attr_name, None)
        except Exception:
            pass

        value = str(value)
        value = value.strip('"')
        if the_attr is not None:
            if isinstance(the_attr, int):
                value = int(value)
            if isinstance(the_attr, float):
                value = float(value)
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
        setattr(obj, attr_name, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
