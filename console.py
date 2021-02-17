#!/usr/bin/python3
"""Module for entry point
of the command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand
    for command interpreter"""
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the cmd"""
        return True

    def do_quit(self, line):
        """quit command to exit the cmd"""
        return True

    def emptyline(self):
        """ Prints new line when press enter """
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id """
        args_list = args.split()

        if args == "":
            print("** class name missing **")
        elif args_list[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.__classes[args_list[0]]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        """ Prints the string representation of an instance
        based on the class name and id"""
        args_list = args.split()

        if self.__class_id_checker(args_list, len(args_list)) != 1:
            instance_id = args_list[0] + "." + args_list[1]
            existing_instances = models.storage.all()

            if instance_id in existing_instances.keys():
                print(existing_instances[instance_id])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        args_list = args.split()

        if self.__class_id_checker(args_list, len(args_list)) != 1:

            instance_id = args_list[0] + "." + args_list[1]
            existing_instances = models.storage.all()

            if instance_id in existing_instances.keys():
                del existing_instances[instance_id]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances
        based or not on the class name """
        args_list = args.split()
        if args == "" or args_list[0] in self.__classes:
            instances_id = models.storage.all()
            list_classes = []

            for key, value in instances_id.items():
                if args in key:
                    list_classes.append(value.__str__())

            print(list_classes)
        else:
            print("** class  doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""
        args_list = args.split()

        if self.__class_id_checker(args_list, len(args_list)) == 1:
            pass
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** value missing **")
        else:
            inst_id = args_list[0] + "." + args_list[1]
            dict_instances = models.storage.all()

            if inst_id in dict_instances.keys():
                if args_list[3]:
                    args_list[3] = args_list[3].replace('"', "")
                try:
                    args_list[3] = int(args_list[3])
                except ValueError:
                    try:
                        args_list[3] = float(args_list[3])
                    except ValueError:
                        args_list[3] = args_list[3]
                dict_instances[inst_id].__dict__[args_list[2]] = args_list[3]
                dict_instances[inst_id].save()
            else:
                print("** no instance found **")

    def __class_id_checker(self, args_list, len_args):
        """ Checks if class name and id exist """
        if len_args == 0:
            print("** class name missing **")
            return 1
        elif args_list[0] not in self.__classes:
            print("** class doesn't exist **")
            return 1
        elif len_args == 1:
            print("** instance id missing **")
            return 1

if __name__ == '__main__':
    HBNBCommand().cmdloop()
