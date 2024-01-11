#!/usr/bin/python3
"""define the console of the program"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import re


class HBNBCommand(cmd.Cmd):
    """main class for the console"""

    prompt = '(hbnb)'
    __supported_classes = ["BaseModel"]

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
                search_key = "{}.{}".format(class_name, instance_id)
                attr_name = args[2]
                attr_value = args[3]
                if attr_name not in ['id', 'created_at', 'updated_at']:
                    models.storage.reload()
                    instance_dict = models.storage.all()
                    if search_key not in instance_dict:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
