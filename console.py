#!/usr/bin/python4
"""Module for the entry point of the command interpreter."""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models import storage
import shlex
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file), and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel":
                new_instance = BaseModel()
            elif arg == "User":
                new_instance = User()
            elif arg == "Place":
                new_instance = Place()
            elif arg == "State":
                new_instance = State()
            elif arg == "City":
                new_instance = City()
            elif arg == "Amenity":
                new_instance = Amenity()
            elif arg == "Review":
                new_instance = Review()

            new_instance.save()
            print(new_instance.id)

     def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if obj_key in all_objects:
                print(all_objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if obj_key in all_objects:
                del all_objects[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def precmd(self, line):

        comd = ['create', 'show', 'update', 'all', 'destroy', 'count']

        if '.' in line and '(' in line and ')' in line:
            clas = line.split('.')
            meth = clas[1].split('(')
            args = meth[1].split(')')
            if clas[0] in self.classes and meth[0] in comd:
                line = meth[0] + ' ' + clas[0] + ' ' + args[0]
        return line

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = shlex.split(arg)
        all_objects = storage.all()
        if not args:
            print([str(obj) for obj in all_objects.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objects.items() if key.startswith(args[0])])

    def do_count(self, arg):
        """Prints the number of instances of a class."""

        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            class_count = sum(1 for obj in storage.all().values() if isinstance(obj, self.classes[class_name]))
            print(class_count)

    def do_update(self, arg):
        """
        Updates an instance based on the c
        lass name and id by adding or updating an attribute.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            #obj = all_objects[obj_key]
            if obj_key in all_objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    obj = all_objects[obj_key]
                    if hasattr(obj, attr_name):
                        attr_type = type(obj.__class__.__dict__[attr_name])
                        try:
                            setattr(obj, attr_name, attr_type(attr_value))
                            storage.save()
                        except ValueError:
                            print("** value must be a valid **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

