#!/usr/bin/python3
"""Defines a class BaseModel"""
from datetime import datetime
import json
import uuid


class BaseModel():
    """BaseModel: representation of the project's parent class"""
    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dicitionary containing all keys/values of the object"""
        target_dict = {key: value for key,
                value in self.__dict__.items()}
        target_dict['created_at'] = self.created_at.isoformat()
        target_dict['updated_at'] = self.updated_at.isoformat()
        target_dict['__class__'] = self.__class__.__name__
        return target_dict


if __name__ == "__main__":
    # create an instance of base model
    my_model = BaseModel()

    # add relative attributes to the instance
    my_model.name = "My_First_Model"
    my_model.my_number = 89

    # print the instance id
    print(my_model.id)

    # print the model string representation
    print(my_model)

    # print the type of the 'created_at' attribute
    print(type(my_model.created_at))
    print("--------------------")

    # get the dictionary representation of the instance
    my_model_json = my_model.to_dict()

    # print the dictionary representation of the instance
    print(my_model_json)

    # print the JSON representation of the instance
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    print("--------------------")

    # construct a new model based on a JSON representation
    my_new_model = BaseModel(**my_model_json)

    # print the id
    print(my_new_model.id)

    # print the new model's string representation
    print(my_new_model)

    # print the type of the 'created_at' attribute
    print(type(my_new_model.created_at))
    print("--------------------")

    # check if the new model is different from the previous one
    print(my_model is my_new_model)
