#!/usr/bin/python3
"""Module: defines the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent a file based storage engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to JSON and save"""
        cls_dict = FileStorage.__objects
        tar_dict = {key: cls_dict[key].to_dict() for key in cls_dict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(tar_dict, file)

    def reload(self):
        """Deserialize the JSON file and save it to __objects"""
        try:
            with open(FileStorage.__file_path) as file:
                loaded_dict = json.load(file)
                for value in loaded_dict.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
