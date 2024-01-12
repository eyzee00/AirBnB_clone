#!/usr/bin/python3
"""define the console of the program"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """main class for the console"""

    prompt = '(hbnb)'
    __supported_classes = [
            "BaseModel",
            "User",
            "Place",
            "Amenity",
            "State",
            "City",
            "Review"
            ]
    __supported_methods = [
            "all",
            "create",
            "count",
            "destroy"
            ]

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            class_name = args[0]

            try:
                cls = globals()[class_name]
                new_instance = cls()
                new_instance.save()
                print(new_instance.id)

            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance,
        based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            class_name = args[0]
            if class_name not in globals().keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                # the key in the dictionary is '<class_name>.<id>'
                search_key = "{}.{}".format(class_name, instance_id)
                # get the dictionary of all instances
                models.storage.reload()
                instance_dict = models.storage.all()
                if search_key not in instance_dict:
                    print("** no instance found **")
                else:
                    print(instance_dict[search_key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id,
        (save the change into the JSON file).
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            class_name = args[0]
            if class_name not in globals().keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                search_key = "{}.{}".format(class_name, instance_id)
                models.storage.reload()
                instance_dict = models.storage.all()
                if search_key not in instance_dict:
                    print("** no instance found **")
                else:
                    del instance_dict[search_key]
                    models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances,
        based or not on the class name
        """
        models.storage.reload()
        instance_dict = models.storage.all()
        if line != "" and line not in HBNBCommand.__supported_classes:
            print("** class doesn't exist **")
        elif line == "":
            str_list = [f"{value}"
                        for value in instance_dict.values()]
            print(str_list)
        else:
            args = line.split()
            class_name = args[0]
            if class_name not in globals().keys():
                print("** class doesn't exist **")
            else:
                re_match = r'^{}'.format(class_name)
                str_list = [f"{value}]"
                            for key, value in instance_dict.items()
                            if re.match(re_match, key)]
                print(str_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id,
        by adding or updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        # may need to recheck condintions in this fucntion
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            class_name = args[0]
            if class_name not in globals().keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance_id = args[1]
                search_key = f"{class_name}.{instance_id}"
                attr_name = args[2]
                attr_value = args[3].strip("\"")
                if attr_name not in ['id', 'created_at', 'updated_at']:
                    models.storage.reload()
                    instance_dict = dict(models.storage.all())
                    if search_key not in instance_dict.keys():
                        print("** no instance found **")
                    else:
                        instance = instance_dict[search_key]
                        setattr(instance, attr_name, attr_value)
                        instance.save()
                        print(instance)

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """(ctrl + D) exits the console"""
        return True

    def emptyline(self):
        """sets how the shell behaves on an empty line"""
        return False

    def count(self, class_name):
        """retrieve the number of instances of a class"""
        models.storage.reload()
        instance_dict = models.storage.all()
        re_match = r'^{}'.format(class_name)
        str_list = [f"{value}]"
                    for key, value in instance_dict.items()
                    if re.match(re_match, key)]
        return (len(str_list))

    def command_extracter(self, str):
        """ extract funciton and it's parameters"""
        fun, par = str.split('(')
        par = par[:-1]  # remove the closing parenthesis
        par = par.split(',')
        return fun, par

    def is_valid_command(self, command):
        """
        this fucntion compare the argument aganist a regex to
        only pass valid custom commands in the syntax class.function()
        """
        return bool(re.match(r'^\w+\.\w+\(.*\)$', command))

    def default(self, line):
        """
        used to implement the default behavior of the class
        modified it to handle the <class_name>.function()
        syntax
        """
        if not self.is_valid_command(line):
            print('*** Unknown syntax: command')
        else:
            class_name, method = line.split('.')
            func, par = self.command_extracter(method)

            if func == 'count':
                print(self.count(class_name))
            elif par == ['']:
                try:
                    getattr(self, 'do_' + func)(class_name)
                except AttributeError:
                    print("*** syntax error")
            else:
                full_command = class_name + " " + "".join(par)
                try:
                    getattr(self, 'do_' + func)(full_command)
                except AttributeError:
                    print("*** syntax error")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
