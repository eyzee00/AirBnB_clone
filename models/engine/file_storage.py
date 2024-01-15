#!/usr/bin/python3
"""Module: defines the FileStorage class"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage: defines the FileStorage object"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the private dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj as a value to
        the key in this format: <obj class name>.objectid
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """serializes the private dictionary __objects to JSON and saves it"""
        cls_dict = self.all()
        tar_dict = {}
        for key, objct in cls_dict.items():
            tar_dict[key] = objct.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(tar_dict, file)

    def reload(self):
        """deserializes the JSON file and saves it back to __objects"""
        if os.path.exists(self.__file_path) is False:
            return

        with open(FileStorage.__file_path) as file:
            loaded_dict = None
            try:
                loaded_dict = json.load(file)
            except json.JSONDecodeError:
                pass
            if loaded_dict is None:
                return
            for value in loaded_dict.values():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name)(**value))
